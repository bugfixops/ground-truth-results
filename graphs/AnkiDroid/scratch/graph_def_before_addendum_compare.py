# AnkiDroid 2.6beta6 (package com.ichi2.anki; source final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java,
# flavor not stated in DATASET.txt, src/main only) trigger graph definition, schema 2.
# Written by hand from the app sources after the schema-1 draft (graphs/AnkiDroid/generated_draft_graph_def.py.txt,
# inventory only). Direct app-to-app calls come from the bytecode extractor (USE_AUTO, auto_calls.json). This file holds
# the entry points (AndroidManifest.xml), one page per screen class, the lifecycle chains and the gate texts. The
# GUI, intent, result and framework-callback edges are added in the label parts (graphs/AnkiDroid/parts/).

TITLE = 'AnkiDroid 2.6beta6 trigger graph'
USE_AUTO = True
STRICT = False

ENV_KINDS_OF, STATE_KINDS_OF = {}, {}


def env_text(text, kinds):
    ENV_KINDS_OF[text] = list(kinds)
    return text


def state_text(text, kinds):
    STATE_KINDS_OF[text] = list(kinds)
    return text


def gui(src, dst, text, kind='GUI', **kw):
    e(src, dst, kind, text, gui=[text], **kw)


def sup(*pairs):
    for p in pairs:
        SUPPRESS.add(p)


# Lifecycle order for the edges that start at a constructor (X.<init>) and for the callbacks after it (AnyMemo style).
LC_RANK = {'onAttach': 0, 'onCreate': 1, 'onCreateDialog': 2, 'onCreateView': 2, 'onStart': 3, 'onResume': 4,
           'onPause': 5, 'onStop': 6, 'onDestroyView': 7}
LC_NO_TRIGGER = ('onDestroy', 'onDetach', 'onConfigurationChanged', 'onOptionsItemSelected')


def lc_chain(cls, cbs):
    has = tuple(cbs)
    first = 'onAttach' if 'onAttach' in has else ('onCreate' if 'onCreate' in has else None)
    out = []
    for cb in has:
        if cb in LC_NO_TRIGGER:
            continue
        if cb == first or first is None:
            s = cls + '.<init>'
        elif cb in LC_RANK:
            below = [x for x in has if x in LC_RANK and LC_RANK[x] < LC_RANK[cb]]
            s = (cls + '.' + max(below, key=lambda x: LC_RANK[x])) if below else (cls + '.<init>')
        else:
            s = (cls + '.onCreate') if 'onCreate' in has else (cls + '.<init>')
        out.append((cb, s))
    return out


# ================================================================== A. pages (one per screen class)

SCREENS = {
    'S_ENTRY': 'Outside the app: launcher, another app or adb (VIEW .apkg, SEND, CREATE_FLASHCARD, DO_SYNC), a ContentProvider call, a system broadcast, a widget update, the test harness',
    'S_DECKPICKER': 'DeckPicker: the main deck list (launcher home screen of the app)',
    'S_STUDYOPTIONS': 'StudyOptionsActivity: study options for the selected deck',
    'S_STUDYOPTIONS_FRAG': 'StudyOptionsFragment: the fragment shown inside StudyOptionsActivity',
    'S_CARDBROWSER': 'CardBrowser: the card list browser',
    'S_REVIEWER': 'Reviewer: the study screen (questions and answers, grading buttons)',
    'S_PREVIEWER': 'Previewer: card preview',
    'S_VIDEOPLAYER': 'VideoPlayer: video playback of a media file',
    'S_MYACCOUNT': 'MyAccount: AnkiWeb account login and registration',
    'S_PREFERENCES': 'Preferences: the settings screen',
    'S_DECKOPTIONS': 'DeckOptions: the options of one deck (preference screen)',
    'S_FILTEREDDECKOPTIONS': 'FilteredDeckOptions: the options of a filtered deck',
    'S_INFO': 'Info: the about / information screen',
    'S_NOTEEDITOR': 'NoteEditor: add or edit a note (also opened from other apps: CREATE_FLASHCARD, SEND)',
    'S_CRASH_REPORT': 'AnkiDroidCrashReportDialog: the crash report activity',
    'S_STATISTICS': 'Statistics: the statistics screen',
    'S_MODELBROWSER': 'ModelBrowser: note type list',
    'S_MODELFIELDEDITOR': 'ModelFieldEditor: edit the fields of a note type',
    'S_CARDTEMPLATEEDITOR': 'CardTemplateEditor: edit the card templates of a note type',
    'S_MULTIMEDIA_EDIT_FIELD': 'MultimediaEditFieldActivity: edit one multimedia field (image, sound, text)',
    'S_TRANSLATION': 'TranslationActivity: translation lookup for a field',
    'S_LOAD_PRONOUNCIATION': 'LoadPronounciationActivity: pronunciation lookup for a field',
    'S_DLG_CARDBROWSER_CONTEXT': 'CardBrowserContextMenu: long-press menu of a card row',
    'S_DLG_CARDBROWSER_SEARCHES': 'CardBrowserMySearchesDialog: saved searches',
    'S_DLG_CARDBROWSER_ORDER': 'CardBrowserOrderDialog: sort order of the card list',
    'S_DLG_CONFIRMATION': 'ConfirmationDialog: generic yes/no confirmation',
    'S_DLG_CUSTOM_STUDY': 'CustomStudyDialog: custom study options',
    'S_DLG_DATABASE_ERROR': 'DatabaseErrorDialog: the collection could not be opened or repaired',
    'S_DLG_DECKPICKER_BACKUP_NO_SPACE': 'DeckPickerBackupNoSpaceLeftDialog: backup could not be made, no space left',
    'S_DLG_DECKPICKER_DELETE_DECK': 'DeckPickerConfirmDeleteDeckDialog: confirm deleting a deck',
    'S_DLG_DECKPICKER_CONTEXT': 'DeckPickerContextMenu: long-press menu of a deck row',
    'S_DLG_DECKPICKER_EXPORT_DONE': 'DeckPickerExportCompleteDialog: export finished',
    'S_DLG_DECKPICKER_NO_SPACE': 'DeckPickerNoSpaceLeftDialog: no space left on the device',
    'S_DLG_EXPORT': 'ExportDialog: export options',
    'S_DLG_IMPORT': 'ImportDialog: import options',
    'S_DLG_MEDIA_CHECK': 'MediaCheckDialog: media check result',
    'S_DLG_MODELBROWSER_CONTEXT': 'ModelBrowserContextMenu: long-press menu of a note type row',
    'S_DLG_MODELEDITOR_CONTEXT': 'ModelEditorContextMenu: long-press menu of a field or template row',
    'S_DLG_RESCHEDULE_CARD': 'NoteEditorRescheduleCard: reschedule the current card',
    'S_DLG_SIMPLE_MESSAGE': 'SimpleMessageDialog: a message with OK',
    'S_DLG_SYNC_ERROR': 'SyncErrorDialog: sync error with actions',
    'S_DLG_TAGS': 'TagsDialog: tag selection',
    'S_DLG_PICK_STRING': 'PickStringDialogFragment: pick one string value (multimedia field editing)',
}

# ================================================================== B. gate texts (predefined; helpers use these only)

ENV_OTHER_APP_INTENT = env_text(
    'outside package: another app (or adb) sends an intent to this exported component (VIEW of an .apkg, SEND of text, '
    'org.openintents.action.CREATE_FLASHCARD, com.ichi2.anki.DO_SYNC), see AndroidManifest.xml', ('other_app',))
ENV_PROVIDER_CALL = env_text(
    'outside package: another app calls ContentResolver on the exported CardContentProvider (manifest exported=true, '
    'permission com.ichi2.anki.permission.READ_WRITE_DATABASE)', ('other_app', 'permission'))
ENV_SDCARD_EVENT = env_text(
    'system event: the system broadcasts MEDIA_MOUNTED or MEDIA_EJECT for a file:// volume (SdCardReceiver, manifest exported=true)',
    ('system_event',))
ENV_WIDGET = env_text(
    'outside package: the user adds the AnkiDroid widget to the home screen, or the AppWidget host sends APPWIDGET_UPDATE',
    ('other_app', 'system_event'))
ENV_NETWORK = env_text('network: the AnkiWeb sync server is reachable (sync, login, media sync)', ('network',))
ENV_STORAGE = env_text('hardware: external storage (SD card or emulated storage) is mounted and writable', ('hardware',))
ENV_PERM_STORAGE = env_text('permission: android.permission.WRITE_EXTERNAL_STORAGE granted at runtime', ('permission',))
ENV_PERM_RECORD = env_text('permission: android.permission.RECORD_AUDIO granted at runtime', ('permission',))
ENV_TTS = env_text('other: a text-to-speech engine is installed and ready (android.speech.tts)', ('other',))
ENV_BROWSER = env_text('other_app: an external browser opens a URL (ACTION_VIEW to a web page)', ('other_app',))
ENV_CONFIG_CHANGE = env_text('system event: the device configuration changes while the app runs (rotation, locale, screen size)', ('system_event',))

STATE_DECK = state_text('data: a deck exists in the collection (the user created or imported one)', ('data',))
STATE_CARDS = state_text('data: the deck has cards to study (new, learning or due)', ('data',))
STATE_NOTE = state_text('data: at least one note exists in the collection', ('data',))
STATE_COLLECTION = state_text('file: a collection file (collection.anki2) exists in the AnkiDroid folder', ('file', 'data'))
STATE_APKG = state_text('file: the .apkg file is available to import (the intent carries its content URI)', ('file',))
STATE_ACCOUNT = state_text('account: an AnkiWeb account is logged in (hkey stored)', ('account',))
STATE_SETTINGS = state_text('settings: the preference is set to the value the route needs', ('settings',))
STATE_SESSION = state_text('session: the app has already run in this process (a second visit, not a cold start)', ('session',))

# ================================================================== C. entry points (manifest)

e('S_ENTRY', 'IntentHandler.onCreate', 'ENTRY', 'launcher (MAIN, LAUNCHER, MULTIWINDOW_LAUNCHER)',
  evidence='SRC AndroidManifest.xml:81-89')
e('S_ENTRY', 'IntentHandler.onCreate', 'ENTRY', 'VIEW of an .apkg / content URI, or the DO_SYNC action, from another app',
  env=ENV_OTHER_APP_INTENT, evidence='SRC AndroidManifest.xml:91-130')
e('S_ENTRY', 'AnkiDroidApp.onCreate', 'ENTRY', 'process start: the system creates the Application (manifest android:name)',
  evidence='SRC AndroidManifest.xml:74; SRC com/ichi2/anki/AnkiDroidApp.java:146; INFERRED the system calls Application.onCreate at process start (framework source not read)')
e('S_ENTRY', 'CardContentProvider.onCreate', 'ENTRY', 'process start: the system creates the exported provider before Application.onCreate',
  evidence='SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:151; INFERRED the system calls ContentProvider.onCreate at process start (framework source not read)')
e('S_ENTRY', 'NoteEditor.<init>', 'ENTRY', 'another app starts NoteEditor (CREATE_FLASHCARD, SEND text/plain)',
  env=ENV_OTHER_APP_INTENT, evidence='SRC AndroidManifest.xml:214-228')
e('S_ENTRY', 'SdCardReceiver.onReceive', 'ENTRY', 'MEDIA_MOUNTED or MEDIA_EJECT broadcast for a file volume',
  env=ENV_SDCARD_EVENT, evidence='SRC AndroidManifest.xml:268-282; SRC com/ichi2/anki/receiver/SdCardReceiver.java:42')
e('S_ENTRY', 'AnkiDroidWidgetSmall.onUpdate', 'ENTRY', 'the AppWidget host sends APPWIDGET_UPDATE for the installed widget',
  env=ENV_WIDGET, evidence='SRC AndroidManifest.xml:253-263; SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:45')
e('S_ENTRY', 'AnkiDroidWidgetSmall.onReceive', 'ENTRY', 'a broadcast to the widget receiver (manifest intent-filter APPWIDGET_UPDATE)',
  env=ENV_WIDGET, evidence='SRC AndroidManifest.xml:253-263; SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:70')

# ================================================================== D. lifecycle chains (generated from the declarations; decl lines in each evidence)

for cb, lsrc in lc_chain('AbstractFlashcardViewer', ('onCreate', 'onResume', 'onPause', 'onDestroy')):
    e(lsrc, 'AbstractFlashcardViewer.' + cb, 'LIFECYCLE', 'lifecycle callback of AbstractFlashcardViewer (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/AbstractFlashcardViewer.java:849, com/ichi2/anki/AbstractFlashcardViewer.java:936, com/ichi2/anki/AbstractFlashcardViewer.java:918, com/ichi2/anki/AbstractFlashcardViewer.java:949')

for cb, lsrc in lc_chain('AnkiActivity', ('onCreate', 'onStart', 'onResume', 'onStop')):
    e(lsrc, 'AnkiActivity.' + cb, 'LIFECYCLE', 'lifecycle callback of AnkiActivity (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/AnkiActivity.java:55, com/ichi2/anki/AnkiActivity.java:65, com/ichi2/anki/AnkiActivity.java:78, com/ichi2/anki/AnkiActivity.java:71')

for cb, lsrc in lc_chain('AnkiDroidApp', ('onCreate',)):
    e(lsrc, 'AnkiDroidApp.' + cb, 'LIFECYCLE', 'lifecycle callback of AnkiDroidApp (Application)', evidence='INFERRED system calls this callback in order (framework source not read for this component); SRC com/ichi2/anki/AnkiDroidApp.java:146')

for cb, lsrc in lc_chain('CardBrowser', ('onCreate', 'onResume', 'onStop', 'onDestroy')):
    e(lsrc, 'CardBrowser.' + cb, 'LIFECYCLE', 'lifecycle callback of CardBrowser (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/CardBrowser.java:343, com/ichi2/anki/CardBrowser.java:564, com/ichi2/anki/CardBrowser.java:525, com/ichi2/anki/CardBrowser.java:539')

for cb, lsrc in lc_chain('CardTemplateEditor', ('onCreate',)):
    e(lsrc, 'CardTemplateEditor.' + cb, 'LIFECYCLE', 'lifecycle callback of CardTemplateEditor (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/CardTemplateEditor.java:127')

for cb, lsrc in lc_chain('DeckOptions', ('onCreate', 'onDestroy')):
    e(lsrc, 'DeckOptions.' + cb, 'LIFECYCLE', 'lifecycle callback of DeckOptions (PreferenceActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/DeckOptions.java:499, com/ichi2/anki/DeckOptions.java:601')

for cb, lsrc in lc_chain('DeckPicker', ('onCreate', 'onResume', 'onPause', 'onStop', 'onDestroy')):
    e(lsrc, 'DeckPicker.' + cb, 'LIFECYCLE', 'lifecycle callback of DeckPicker (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/DeckPicker.java:353, com/ichi2/anki/DeckPicker.java:700, com/ichi2/anki/DeckPicker.java:730, com/ichi2/anki/DeckPicker.java:738, com/ichi2/anki/DeckPicker.java:749')

for cb, lsrc in lc_chain('FilteredDeckOptions', ('onCreate', 'onDestroy')):
    e(lsrc, 'FilteredDeckOptions.' + cb, 'LIFECYCLE', 'lifecycle callback of FilteredDeckOptions (PreferenceActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/FilteredDeckOptions.java:351, com/ichi2/anki/FilteredDeckOptions.java:442')

for cb, lsrc in lc_chain('Info', ('onCreate',)):
    e(lsrc, 'Info.' + cb, 'LIFECYCLE', 'lifecycle callback of Info (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/Info.java:59')

for cb, lsrc in lc_chain('IntentHandler', ('onCreate',)):
    e(lsrc, 'IntentHandler.' + cb, 'LIFECYCLE', 'lifecycle callback of IntentHandler (Activity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/IntentHandler.java:38')

for cb, lsrc in lc_chain('ModelBrowser', ('onCreate', 'onResume', 'onStop')):
    e(lsrc, 'ModelBrowser.' + cb, 'LIFECYCLE', 'lifecycle callback of ModelBrowser (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/ModelBrowser.java:182, com/ichi2/anki/ModelBrowser.java:196, com/ichi2/anki/ModelBrowser.java:224')

for cb, lsrc in lc_chain('ModelFieldEditor', ('onCreate', 'onStop')):
    e(lsrc, 'ModelFieldEditor.' + cb, 'LIFECYCLE', 'lifecycle callback of ModelFieldEditor (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/ModelFieldEditor.java:72, com/ichi2/anki/ModelFieldEditor.java:93')

for cb, lsrc in lc_chain('MyAccount', ('onCreate',)):
    e(lsrc, 'MyAccount.' + cb, 'LIFECYCLE', 'lifecycle callback of MyAccount (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/MyAccount.java:85')

for cb, lsrc in lc_chain('NoteEditor', ('onCreate', 'onStop', 'onDestroy')):
    e(lsrc, 'NoteEditor.' + cb, 'LIFECYCLE', 'lifecycle callback of NoteEditor (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/NoteEditor.java:287, com/ichi2/anki/NoteEditor.java:541, com/ichi2/anki/NoteEditor.java:792')

for cb, lsrc in lc_chain('Preferences', ('onCreate', 'onResume', 'onPause')):
    e(lsrc, 'Preferences.' + cb, 'LIFECYCLE', 'lifecycle callback of Preferences (PreferenceActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/Preferences.java:109, com/ichi2/anki/Preferences.java:201, com/ichi2/anki/Preferences.java:175, com/ichi2/anki/Preferences.java:164')

for cb, lsrc in lc_chain('Previewer', ('onCreate',)):
    e(lsrc, 'Previewer.' + cb, 'LIFECYCLE', 'lifecycle callback of Previewer (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/Previewer.java:32')

for cb, lsrc in lc_chain('Reviewer', ('onStop',)):
    e(lsrc, 'Reviewer.' + cb, 'LIFECYCLE', 'lifecycle callback of Reviewer (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/Reviewer.java:423')

for cb, lsrc in lc_chain('Statistics', ('onCreate', 'onResume')):
    e(lsrc, 'Statistics.' + cb, 'LIFECYCLE', 'lifecycle callback of Statistics (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/Statistics.java:81, com/ichi2/anki/Statistics.java:163')

for cb, lsrc in lc_chain('StudyOptionsActivity', ('onCreate', 'onResume', 'onStop')):
    e(lsrc, 'StudyOptionsActivity.' + cb, 'LIFECYCLE', 'lifecycle callback of StudyOptionsActivity (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/StudyOptionsActivity.java:36, com/ichi2/anki/StudyOptionsActivity.java:129, com/ichi2/anki/StudyOptionsActivity.java:119')

for cb, lsrc in lc_chain('StudyOptionsFragment', ('onAttach', 'onCreateView', 'onResume', 'onDestroy')):
    e(lsrc, 'StudyOptionsFragment.' + cb, 'LIFECYCLE', 'lifecycle callback of StudyOptionsFragment (Fragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/StudyOptionsFragment.java:107, com/ichi2/anki/StudyOptionsFragment.java:173, com/ichi2/anki/StudyOptionsFragment.java:206, com/ichi2/anki/StudyOptionsFragment.java:196')

for cb, lsrc in lc_chain('VideoPlayer', ('onCreate', 'onStop')):
    e(lsrc, 'VideoPlayer.' + cb, 'LIFECYCLE', 'lifecycle callback of VideoPlayer (Activity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/VideoPlayer.java:37, com/ichi2/anki/VideoPlayer.java:78')

for cb, lsrc in lc_chain('CardBrowserContextMenu', ('onCreateDialog',)):
    e(lsrc, 'CardBrowserContextMenu.' + cb, 'LIFECYCLE', 'lifecycle callback of CardBrowserContextMenu (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/CardBrowserContextMenu.java:39')

for cb, lsrc in lc_chain('CardBrowserMySearchesDialog', ('onCreateDialog',)):
    e(lsrc, 'CardBrowserMySearchesDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of CardBrowserMySearchesDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:57')

for cb, lsrc in lc_chain('CardBrowserOrderDialog', ('onCreateDialog',)):
    e(lsrc, 'CardBrowserOrderDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of CardBrowserOrderDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/CardBrowserOrderDialog.java:31')

for cb, lsrc in lc_chain('ConfirmationDialog', ('onCreateDialog',)):
    e(lsrc, 'ConfirmationDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of ConfirmationDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:31')

for cb, lsrc in lc_chain('CustomStudyDialog', ('onCreateDialog',)):
    e(lsrc, 'CustomStudyDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of CustomStudyDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:94')

for cb, lsrc in lc_chain('DatabaseErrorDialog', ('onCreateDialog',)):
    e(lsrc, 'DatabaseErrorDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of DatabaseErrorDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:57')

for cb, lsrc in lc_chain('DeckPickerBackupNoSpaceLeftDialog', ('onCreateDialog',)):
    e(lsrc, 'DeckPickerBackupNoSpaceLeftDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of DeckPickerBackupNoSpaceLeftDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/DeckPickerBackupNoSpaceLeftDialog.java:22')

for cb, lsrc in lc_chain('DeckPickerConfirmDeleteDeckDialog', ('onCreateDialog',)):
    e(lsrc, 'DeckPickerConfirmDeleteDeckDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of DeckPickerConfirmDeleteDeckDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/DeckPickerConfirmDeleteDeckDialog.java:24')

for cb, lsrc in lc_chain('DeckPickerContextMenu', ('onCreateDialog',)):
    e(lsrc, 'DeckPickerContextMenu.' + cb, 'LIFECYCLE', 'lifecycle callback of DeckPickerContextMenu (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:61')

for cb, lsrc in lc_chain('DeckPickerExportCompleteDialog', ('onCreateDialog',)):
    e(lsrc, 'DeckPickerExportCompleteDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of DeckPickerExportCompleteDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/DeckPickerExportCompleteDialog.java:23')

for cb, lsrc in lc_chain('DeckPickerNoSpaceLeftDialog', ('onCreateDialog',)):
    e(lsrc, 'DeckPickerNoSpaceLeftDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of DeckPickerNoSpaceLeftDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/DeckPickerNoSpaceLeftDialog.java:20')

for cb, lsrc in lc_chain('ExportDialog', ('onCreateDialog',)):
    e(lsrc, 'ExportDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of ExportDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/ExportDialog.java:53')

for cb, lsrc in lc_chain('ImportDialog', ('onCreateDialog',)):
    e(lsrc, 'ImportDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of ImportDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/ImportDialog.java:59')

for cb, lsrc in lc_chain('MediaCheckDialog', ('onCreateDialog',)):
    e(lsrc, 'MediaCheckDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of MediaCheckDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:56')

for cb, lsrc in lc_chain('ModelBrowserContextMenu', ('onCreateDialog',)):
    e(lsrc, 'ModelBrowserContextMenu.' + cb, 'LIFECYCLE', 'lifecycle callback of ModelBrowserContextMenu (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/ModelBrowserContextMenu.java:28')

for cb, lsrc in lc_chain('ModelEditorContextMenu', ('onCreateDialog',)):
    e(lsrc, 'ModelEditorContextMenu.' + cb, 'LIFECYCLE', 'lifecycle callback of ModelEditorContextMenu (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/ModelEditorContextMenu.java:31')

for cb, lsrc in lc_chain('NoteEditorRescheduleCard', ('onCreateDialog',)):
    e(lsrc, 'NoteEditorRescheduleCard.' + cb, 'LIFECYCLE', 'lifecycle callback of NoteEditorRescheduleCard (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/NoteEditorRescheduleCard.java:19')

for cb, lsrc in lc_chain('SimpleMessageDialog', ('onCreateDialog',)):
    e(lsrc, 'SimpleMessageDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of SimpleMessageDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/SimpleMessageDialog.java:34')

for cb, lsrc in lc_chain('SyncErrorDialog', ('onCreateDialog',)):
    e(lsrc, 'SyncErrorDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of SyncErrorDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:65')

for cb, lsrc in lc_chain('TagsDialog', ('onCreate', 'onCreateDialog')):
    e(lsrc, 'TagsDialog.' + cb, 'LIFECYCLE', 'lifecycle callback of TagsDialog (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/dialogs/TagsDialog.java:89, com/ichi2/anki/dialogs/TagsDialog.java:112')

for cb, lsrc in lc_chain('LoadPronounciationActivity', ('onCreate', 'onPause')):
    e(lsrc, 'LoadPronounciationActivity.' + cb, 'LIFECYCLE', 'lifecycle callback of LoadPronounciationActivity (Activity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:91, com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:483')

for cb, lsrc in lc_chain('MultimediaEditFieldActivity', ('onCreate', 'onDestroy')):
    e(lsrc, 'MultimediaEditFieldActivity.' + cb, 'LIFECYCLE', 'lifecycle callback of MultimediaEditFieldActivity (AppCompatActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:74, com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:336')

for cb, lsrc in lc_chain('PickStringDialogFragment', ('onCreateDialog',)):
    e(lsrc, 'PickStringDialogFragment.' + cb, 'LIFECYCLE', 'lifecycle callback of PickStringDialogFragment (DialogFragment)', evidence='INFERRED androidx Fragment/DialogFragment lifecycle order (androidx source not read); SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:41')

for cb, lsrc in lc_chain('TranslationActivity', ('onCreate', 'onPause')):
    e(lsrc, 'TranslationActivity.' + cb, 'LIFECYCLE', 'lifecycle callback of TranslationActivity (FragmentActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:91, com/ichi2/anki/multimediacard/activity/TranslationActivity.java:411')

for cb, lsrc in lc_chain('CardContentProvider', ('onCreate',)):
    e(lsrc, 'CardContentProvider.' + cb, 'LIFECYCLE', 'lifecycle callback of CardContentProvider (ContentProvider)', evidence='INFERRED system calls this callback in order (framework source not read for this component); SRC com/ichi2/anki/provider/CardContentProvider.java:151')

for cb, lsrc in lc_chain('NotificationService', ('onCreate',)):
    e(lsrc, 'NotificationService.' + cb, 'LIFECYCLE', 'lifecycle callback of NotificationService (Service)', evidence='FW-SRC core/java/android/app/Service.java:343 (onCreate), 515 (onDestroy); SRC com/ichi2/anki/services/NotificationService.java:47')

for cb, lsrc in lc_chain('AppCompatPreferenceActivity', ('onCreate', 'onStop', 'onDestroy')):
    e(lsrc, 'AppCompatPreferenceActivity.' + cb, 'LIFECYCLE', 'lifecycle callback of AppCompatPreferenceActivity (PreferenceActivity)', evidence='FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1239 (onStart), 1311 (onResume), 1673 (onPause), 1858 (onStop), 1909 (onDestroy); SRC com/ichi2/ui/AppCompatPreferenceActivity.java:43, com/ichi2/ui/AppCompatPreferenceActivity.java:107, com/ichi2/ui/AppCompatPreferenceActivity.java:113')

# ---- part 001 (2026-10-27)
# AnkiDroid batch 001 (LABEL helper). Writes the S_ENTRY edges whose destination is a method in this
# batch, plus one edge between two methods of this batch: IntentHandler$1.<init> -> IntentHandler$1.onPositive
# (FRAMEWORK, as directed by the coordinator). Other edges between methods of this batch are not written here:
# the route into each method passes through nodes owned by other batches
# (see graphs/AnkiDroid/scratch/conflicts_001.md).
# ENV_CONFIG_CHANGE is the constant requested by the coordinator; it is added at merge.

e('S_ENTRY', 'AnkiDroidApp.<init>', 'FRAMEWORK',
  'process start: the framework creates the Application object',
  env=None,
  note='Default constructor of AnkiDroidApp. The S_ENTRY to AnkiDroidApp.onCreate edge already exists in graph_def.py (line 142).',
  evidence='FW-SRC core/java/android/app/LoadedApk.java:983-984; FW-SRC core/java/android/app/Instrumentation.java:1099-1102; SRC com/ichi2/anki/AnkiDroidApp.java:111')

e('S_ENTRY', 'IntentHandler.<init>', 'FRAMEWORK',
  'launcher, VIEW .apkg, or DO_SYNC intent starts the IntentHandler activity',
  env=None,
  note='Default constructor of the IntentHandler activity. The S_ENTRY to IntentHandler.onCreate edges already exist in graph_def.py (lines 138-140).',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2669-2670; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; SRC com/ichi2/anki/IntentHandler.java:36; SRC AndroidManifest.xml:85-89')

e('S_ENTRY', 'AnkiDroidApp.onConfigurationChanged', 'SYSTEM',
  'system configuration change (rotation or locale) delivered to the Application',
  env=ENV_CONFIG_CHANGE,
  note='NEW CONST ENV_CONFIG_CHANGE',
  evidence='SRC com/ichi2/anki/AnkiDroidApp.java:204-209; FW-SRC core/java/android/app/ActivityThread.java:5040')

e('IntentHandler$1.<init>', 'IntentHandler$1.onPositive', 'FRAMEWORK',
  'the user taps the positive button of the dialog that IntentHandler.onCreate builds with the callback IntentHandler$1 (registered in its constructor)',
  env=None,
  note='Written as FRAMEWORK, not REGISTER: the builder does not follow REGISTER edges for reachability, so REGISTER would leave onPositive unreachable. IntentHandler$1.<init> is the anonymous ButtonCallback creation at IntentHandler.java:118; its batch owner is unknown (see conflicts_001.md).',
  evidence='SRC com/ichi2/anki/IntentHandler.java:118; SRC com/ichi2/anki/IntentHandler.java:120')

UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.createTag'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.e(String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.e(Throwable,String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.formatString'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.i(String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.i(Throwable,String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.w(String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.w(Throwable,String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')

# ---- part 004 (2026-10-27)
# Batch 004 (DeckPicker anonymous classes).
# Names used (graph_def.py): gui (line 25), ENV_NETWORK (120), ENV_STORAGE (121), STATE_CARDS (128), STATE_ACCOUNT (132).
# UNREACHABLE is a local dict for this part (not a graph_def name). Its keys are the 7 UNREACHABLE rows in label_004.md.
# REACHABLE rows are only in label_004.md. AsyncTask/Connection dispatch edges are owned by the DeckPicker part that calls execute() (not written here).
# Routes owned by other batches (DeckTask, Connection, SdCardReceiver, IntentHandler, dialog callers) are in graphs/AnkiDroid/scratch/conflicts_004.md.


UNREACHABLE['DeckPicker$13.onCancelled'] = (
    'no_trigger_in_app',
    "The undo task is never cancelled in the app. DeckTask.cancelTask(int) cancels only when the type matches (DeckTask.java:181-185), and its only callers are CardBrowser for SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). TaskOperations.stopTaskGracefully is called only by LoadPronounciationActivity and TranslationActivity, not by DeckTask. AsyncTask runs onCancelled only after cancel() (FW-SRC core/java/android/os/AsyncTask.java:479-480,525-527).",
    'SRC com/ichi2/anki/DeckPicker.java:1001-1003',
    'SOURCE')

UNREACHABLE['DeckPicker$14.onCancelled'] = (
    'no_trigger_in_app',
    "The repair task type is never cancelled (DeckTask.cancelTask(int) callers are CardBrowser only, see $13.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1139-1141',
    'SOURCE')

UNREACHABLE['DeckPicker$14.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundRepairDeck (DeckTask.java:687-694) calls no publishProgress. The publishProgress calls in DeckTask.java are at 380, 420, 422, 457, 565, 601, 633, 659, 809 and 859, none inside this method. ProgressCallback is used only by the importer (DeckTask.java:750). AsyncTask dispatches onProgressUpdate only from publishProgress (FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1134-1135',
    'SOURCE')

UNREACHABLE['DeckPicker$15.onCancelled'] = (
    'no_trigger_in_app',
    "The check-database task type is never cancelled (see $13.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1183-1184',
    'SOURCE')

UNREACHABLE['DeckPicker$15.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundCheckDatabase (DeckTask.java:667-684) calls no publishProgress (see $14.onProgressUpdate for the full check). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1178-1179',
    'SOURCE')

UNREACHABLE['DeckPicker$16.onCancelled'] = (
    'no_trigger_in_app',
    "The check-media task type is never cancelled (see $13.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1220-1221',
    'SOURCE')

UNREACHABLE['DeckPicker$16.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundCheckMedia (DeckTask.java:1015-1021) calls no publishProgress. The only progress path outside DeckTask is ProgressCallback, which is used only by the importer (DeckTask.java:750). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1215-1216',
    'SOURCE')

gui('S_DECKPICKER', 'DeckPicker$10.onClick',
    'tap the + button, then the add-shared-deck button in the add menu',
    evidence='SRC com/ichi2/anki/DeckPicker.java:488-494; SRC res/layout-v14/floating_add_button.xml:27')

gui('S_DECKPICKER', 'DeckPicker$11.onClick',
    'tap the + button, then the add-note button in the add menu',
    evidence='SRC com/ichi2/anki/DeckPicker.java:495-500; SRC res/layout-v14/floating_add_button.xml:36')

gui('S_DECKPICKER', 'DeckPicker$12.onPositive',
    'options menu: New filtered deck, then Create in the name dialog (menu item enabled only with SD card mounted)',
    env=ENV_STORAGE,
    evidence='SRC com/ichi2/anki/DeckPicker.java:527,566-590')

gui('S_DECKPICKER', 'DeckPicker$17$1.onKey',
    'press Back while a sync progress dialog is showing (cancel the running sync)',
    env=ENV_NETWORK, needs_state=STATE_ACCOUNT,
    evidence='SRC com/ichi2/anki/DeckPicker.java:1328-1340')

gui('S_DECKPICKER', 'DeckPicker$17$1$1.onPositive',
    'during sync, press Back after 2 s, then OK in the cancel-sync confirmation',
    env=ENV_NETWORK, needs_state=STATE_ACCOUNT,
    evidence='SRC com/ichi2/anki/DeckPicker.java:1350-1354')

gui('S_DECKPICKER', 'DeckPicker$19.onClick',
    'select a deck whose daily study limit is reached (new or review cards still waiting), then the Study more snackbar button',
    needs_state=STATE_CARDS,
    evidence='SRC com/ichi2/anki/DeckPicker.java:1744-1752')

# ---- suppressed auto dispatch edges (2026-10-27): DeckTask dispatches to a listener per task type; the DeckPicker listeners
# below are never cancelled (cancelTask callers are CardBrowser only) and their doInBackground publishes no progress
sup(('DeckTask.onCancelled', 'DeckPicker$13.onCancelled'),
    ('DeckTask.onCancelled', 'DeckPicker$14.onCancelled'),
    ('DeckTask.onCancelled', 'DeckPicker$15.onCancelled'),
    ('DeckTask.onCancelled', 'DeckPicker$16.onCancelled'),
    ('DeckTask$TaskListener.onProgressUpdate', 'DeckPicker$14.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@DeckPicker$14', 'DeckPicker$14.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate', 'DeckPicker$15.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@DeckPicker$15', 'DeckPicker$15.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate', 'DeckPicker$16.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@DeckPicker$16', 'DeckPicker$16.onProgressUpdate'))

# ---- part 003 (2026-10-27)
# AnkiDroid batch 003 (LABEL helper). DeckPicker lifecycle, options menu, undo, sync, dialog entry points.
# Edges written here have a source method in batch 003, or a page source (S_DECKPICKER) whose destination is in batch 003
# (coordinator rule 1). Routes through other batches' nodes are cited in graphs/AnkiDroid/parts/label_003.md.
# No UNREACHABLE entries: all 40 batch methods have a route from S_ENTRY.
# Missing gates are notes only (MISSING GATE ...); env and needs_state are unset on those edges.
# Lifecycle edges (DeckPicker.onResume/onPause/onStop) come from the lc_chain in graph_def.py line 176 and are not repeated here.

e('S_DECKPICKER', 'DeckPicker.onPrepareOptionsMenu', 'GUI',
  'the user opens the options menu of the deck list',
  gui=['the user opens the options menu of the deck list'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:505; FW-SRC core/java/android/app/Activity.java:3404-3406',
  note='Page edge; the destination is in batch 003, so this part writes it. The framework calls onPrepareOptionsMenu through onPreparePanel.')

e('S_DECKPICKER', 'DeckPicker.openCardBrowser', 'GUI',
  'the user taps Browse in the navigation drawer',
  gui=['the user taps Browse in the navigation drawer'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1708; SRC com/ichi2/anki/NavigationDrawerActivity.java:262-263',
  note='NavigationDrawerActivity (batch_036) also reaches this override by virtual dispatch at line 263; this page edge is the DeckPicker route.')

e('S_DECKPICKER', 'DeckPicker.openReviewer', 'GUI',
  'the user taps a deck that has cards to study',
  gui=['the user taps a deck that has cards to study'],
  needs_state=STATE_CARDS,
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2128, 1739',
  note='handleDeckSelection (batch_002) calls openReviewer at line 1739 for a deck with cards.')

e('S_DECKPICKER', 'DeckPicker.openStudyOptions', 'GUI',
  'the user taps a deck without cards to study',
  gui=['the user taps a deck without cards to study'],
  needs_state=STATE_DECK,
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1695, 1736',
  note='handleDeckSelection (batch_002) calls openStudyOptions(false) at lines 1736, 1743, 1768, 1780 and 1796.')

e('S_DECKPICKER', 'DeckPicker.undo', 'GUI',
  'the user taps Undo in the options menu',
  gui=['the user taps Undo in the options menu'],
  evidence='SRC com/ichi2/anki/DeckPicker.java:996, 511, 551-553',
  note='MISSING GATE MG2: undo available. The Undo item is visible only when getCol().undoAvailable() is true (DeckPicker.java:511-517). env and needs_state unset.')

e('S_DECKPICKER', 'DeckPicker.sync()', 'GUI',
  'the user taps Sync in the options menu',
  gui=['the user taps Sync in the options menu'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1266, 556-558',
  note='No gate is needed to reach sync(); the offline case changes only the outcome (MISSING GATE MG4 is noted on the sync(String) ASYNC edge).')

e('S_DECKPICKER', 'DeckPicker.showImportDialog(int)', 'GUI',
  'the user taps Import in the options menu',
  gui=['the user taps Import in the options menu'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1088, 561-563',
  note='showImportDialog(int) delegates to showImportDialog(int,String) at line 1089.')

e('S_DECKPICKER', 'DeckPicker.showMediaCheckDialog(int)', 'GUI',
  'the user taps Check media in the options menu',
  gui=['the user taps Check media in the options menu'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1033, 600-602',
  note='Options menu action_check_media case (DeckPicker.java:600-602).')

e('S_DECKPICKER', 'DeckPicker$1.onClick', 'GUI',
  'the user taps the expander arrow next to a deck',
  gui=['the user taps the expander arrow next to a deck'],
  evidence='SRC com/ichi2/anki/DeckPicker.java:183-187',
  note='MISSING GATE (unnumbered): deck has subdecks. The listener only acts when children exist (DeckPicker.java:185). env and needs_state unset.')

e('DeckPicker.onPause', 'DeckPicker.onSaveInstanceState', 'FRAMEWORK',
  'the framework saves the activity state after onPause and before onStop',
  evidence='SRC com/ichi2/anki/DeckPicker.java:716; FW-SRC core/java/android/app/ActivityThread.java:4023-4025',
  note='MISSING GATE (unnumbered): activity not finishing (ActivityThread saves only when !mFinished and saveState). env and needs_state unset.')

e('DeckPicker.updateDeckList', 'DeckPicker$22.onPostExecute', 'ASYNC',
  'the deck-count load task finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1823, 1834',
  note='Listener DeckPicker$22 is in batch_005. onPostExecute calls scrollDecklistToDeck at DeckPicker.java:1868.')

e('DeckPicker.undo', 'DeckPicker$13.onPostExecute', 'ASYNC',
  'the undo task finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:999, 1011-1014',
  note='Listener DeckPicker$13 is in batch_004. The route into undo carries MG2 (see the S_DECKPICKER -> DeckPicker.undo edge).')

e('DeckPicker.sync(String)', 'DeckPicker$17.onPostExecute', 'ASYNC',
  'the sync task finishes and calls its listener',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1284, 1291, 1404',
  note='MISSING GATE MG4: offline. The onDisconnected branch (DeckPicker.java:1299) shows the offline message. env and needs_state unset.')

e('DeckPicker$1.<init>', 'DeckPicker$1.onClick', 'REGISTER',
  'the expander click listener is registered with the deck list',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:181, 183',
  note='The builder does not follow REGISTER for reachability (see label_001.py note); the route to onClick is the S_DECKPICKER -> DeckPicker$1.onClick edge.')

e('DeckPicker$10.<init>', 'DeckPicker$10.onClick', 'REGISTER',
  'the add-shared FAB click listener is registered',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:488, 492',
  note='onClick is in batch_004. The builder does not follow REGISTER for reachability.')

# ---- part 001b (2026-10-27)
# IntentHandler.onCreate is not in any batch file: it was already REACHABLE from the S_ENTRY edge at build 001, so the
# batch plan (UNRESOLVED methods only) skipped it. This part is the only writer of its edges to DeckPicker.<init>.
# DeckPicker is started from three branches of onCreate; each start site is its own edge because the outside-intent
# condition (env) differs by site. IntentHandler.<init> and IntentHandler$1.onPositive start no activity.

e('IntentHandler.onCreate', 'DeckPicker.<init>', 'INTENT',
  'the user opens AnkiDroid from the launcher (ACTION_MAIN with CATEGORY_LAUNCHER); IntentHandler.onCreate starts DeckPicker with startActivityIfNeeded',
  guard='action is neither Intent.ACTION_VIEW (line 46) nor com.ichi2.anki.DO_SYNC (line 126), so the else branch at lines 132-138 runs; DeckPicker starts only if no other task exists, otherwise the previous task is shown (comment lines 133-134)',
  env=None,
  note='Launcher start site (1 of 3 in IntentHandler.onCreate that start DeckPicker). No outside intent is needed, so env is None.',
  evidence='SRC com/ichi2/anki/IntentHandler.java:43; SRC com/ichi2/anki/IntentHandler.java:132-138; SRC AndroidManifest.xml:85-89')

e('IntentHandler.onCreate', 'DeckPicker.<init>', 'INTENT',
  'another app (or adb) sends a VIEW intent for an .apkg file or content URI; IntentHandler.onCreate starts DeckPicker after the import dialog message is stored',
  guard='action equals Intent.ACTION_VIEW (line 46) and successful is true (lines 105-108): content scheme with a name ending .apkg (lines 79-82; the dummy name unknown_filename.apkg at lines 68-71 when the MIME type is application/apkg or the data is a valid zip) and copyFileToCache succeeded (line 85), or file scheme with a path ending .apkg (lines 93-99)',
  env=ENV_OTHER_APP_INTENT,
  note='VIEW start site (2 of 3). The start depends on an outside intent, so env is ENV_OTHER_APP_INTENT.',
  evidence='SRC com/ichi2/anki/IntentHandler.java:46; SRC com/ichi2/anki/IntentHandler.java:43; SRC com/ichi2/anki/IntentHandler.java:85; SRC com/ichi2/anki/IntentHandler.java:93-108')

e('IntentHandler.onCreate', 'DeckPicker.<init>', 'INTENT',
  'another app (or adb) sends the com.ichi2.anki.DO_SYNC action; IntentHandler.onCreate stores MSG_DO_SYNC and starts DeckPicker',
  guard='action is not Intent.ACTION_VIEW (line 46) and equals com.ichi2.anki.DO_SYNC (line 126); sendDoSyncMsg (line 127) stores MSG_DO_SYNC, then startActivity at line 130',
  env=ENV_OTHER_APP_INTENT,
  note='DO_SYNC start site (3 of 3). The start depends on an outside intent, so env is ENV_OTHER_APP_INTENT.',
  evidence='SRC com/ichi2/anki/IntentHandler.java:126-130; SRC com/ichi2/anki/IntentHandler.java:172-177')
# ---- part 006 (2026-10-27)
# AnkiDroid batch 006 (LABEL helper). DeckPicker anonymous listeners: $5 (onPreExecute, onProgressUpdate),
# $6 (all five methods), $7 (all five), $8 (both), $9 (both), $9$1 (both). 18 methods; the full row list is in
# graphs/AnkiDroid/parts/label_006.md.
#
# Route ownership: the launchers importAdd (DeckPicker.java:1579-1582), importReplace (1587-1589) and exportApkg (1593-1623)
# belong to batch_002 (no label_002.py yet). Their ASYNC edges to the listener callbacks are NOT written here; the launcher's
# part writes them (see graphs/AnkiDroid/scratch/conflicts_006.md). Those callbacks are REACHABLE rows in the .md with
# "confirmed_by INFERRED" in the reason.
# The fallback FAB branch ($8) is closed on the standard API 27 config (closed_by_api_level).
# UNREACHABLE entries are assigned one key at a time.
# No env or needs_state gate is set on the GUI edges below: the screen is already open with the collection loaded.

e('DeckPicker$9.<init>', 'DeckPicker$9.onClick', 'REGISTER',
  'the add-deck listener is registered on the New deck button of the add menu',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:461-463',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_DECKPICKER -> DeckPicker$9.onClick GUI edge below.')

e('S_DECKPICKER', 'DeckPicker$9.onClick', 'GUI',
  'tap the + button, then New deck in the add menu',
  gui=['tap the + button, then New deck in the add menu'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:391-393, 463-467; SRC res/layout-v14/floating_add_button.xml:7, 18',
  note='Page edge; the destination is in this part. The guard at line 464 passes on the standard API 27 path because mActionsMenu is set at line 391 and configureFloatingActionsMenu runs at line 393.')

e('DeckPicker$9$1.<init>', 'DeckPicker$9$1.onPositive', 'REGISTER',
  'the new-deck dialog callback is registered in the MaterialDialog builder',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:471-475',
  note='onPositive is in this part. The builder does not follow REGISTER for reachability; the route is the S_DECKPICKER -> DeckPicker$9$1.onPositive GUI edge below.')

e('S_DECKPICKER', 'DeckPicker$9$1.onPositive', 'GUI',
  'tap the + button, tap New deck in the add menu, then OK in the new-deck name dialog',
  gui=['tap the + button, tap New deck in the add menu, then OK in the new-deck name dialog'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:463-485',
  note='Page edge. The dialog is built only by DeckPicker$9.onClick (lines 471-485), so the route goes through the add-deck click. No env or needs_state gate is set.')

UNREACHABLE['DeckPicker$6.onCancelled'] = (
    'no_trigger_in_app',
    "The import-replace task type is never cancelled. DeckTask.cancelTask(int) cancels only when the type matches (DeckTask.java:181-185), and its callers are CardBrowser only (CardBrowser.java:528-529, 796-797, 1155). The no-argument DeckTask.cancelTask() (DeckTask.java:168-178) has no caller except cancelTask(int) (DeckTask.java:184). TaskOperations.stopTaskGracefully is called only with the activities' own task fields (LoadPronounciationActivity.java:471-479, TranslationActivity.java:404-405). DeckPicker.java:1340 and 1354 call Connection.cancel(), which cancels the sync Connection task (Connection.java:541), not DeckTask. AsyncTask runs onCancelled only after cancel() (FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:307-309; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$7.onCancelled'] = (
    'no_trigger_in_app',
    "The export task type is never cancelled. The reasons are the same as for DeckPicker$6.onCancelled: DeckTask.cancelTask(int) (DeckTask.java:181-185) has only CardBrowser callers (CardBrowser.java:528-529, 796-797, 1155); the no-argument cancelTask() (DeckTask.java:168-178) is called only from cancelTask(int); TaskOperations.stopTaskGracefully is called only with the activities' own task fields (LoadPronounciationActivity.java:471-479, TranslationActivity.java:404-405); Connection.cancel() (DeckPicker.java:1340, 1354) cancels the sync Connection task, not DeckTask. AsyncTask runs onCancelled only after cancel() (FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:340-342; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$7.onProgressUpdate'] = (
    'framework_never_calls',
    "The export task never publishes progress. doInBackgroundExportApkg (DeckTask.java:881-909) calls exporter.exportInto (line 895) and contains no publishProgress. The publishProgress calls in DeckTask.java are at 380, 420, 422, 457, 565, 601, 633, 659, 809 and 859, none inside 881-909. Across the app's java tree, publishProgress, ProgressCallback and doProgress occur only in DeckTask, Connection, the importers and the syncers; AnkiPackageExporter has none. AsyncTask dispatches onProgressUpdate only from publishProgress (FW-SRC core/java/android/os/AsyncTask.java:684-689, 714-716). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:335-337; SRC com/ichi2/async/DeckTask.java:881-909; FW-SRC core/java/android/os/AsyncTask.java:684-689',
    'SOURCE')

UNREACHABLE['DeckPicker$8.<init>'] = (
    'closed_by_api_level',
    "Created only in the fallback else branch (DeckPicker.java:394-405), which runs only when findViewById(R.id.add_content_menu) returns null (line 391). On the standard API 27 config the layout-v14 variant of floating_add_button.xml is selected (res/layout/deck_picker.xml:36 includes @layout/floating_add_button, and the v14 variant declares add_content_menu at line 7; the base layout has only add_note_action), so mActionsMenu is non-null and configureFloatingActionsMenu runs (line 393). minSdkVersion is 10 (build.gradle), so the branch is reachable only on API 10 to 13. The auto CALL edge DeckPicker.onCreate -> DeckPicker$8.<init> (line 399) is an over-approximation; see conflicts_006.md.",
    'SRC com/ichi2/anki/DeckPicker.java:391-405; SRC res/layout-v14/floating_add_button.xml:7; SRC res/layout/deck_picker.xml:36',
    'SOURCE')

UNREACHABLE['DeckPicker$8.onClick'] = (
    'closed_by_api_level',
    "Its only creator is the fallback else branch at DeckPicker.java:399-404, which is closed on the standard API 27 config for the same reason as DeckPicker$8.<init> (layout-v14 declares add_content_menu, line 391 is non-null, the else branch never runs). Reachable only on API 10 to 13 (minSdkVersion 10).",
    'SRC com/ichi2/anki/DeckPicker.java:391-405; SRC res/layout-v14/floating_add_button.xml:7',
    'SOURCE')

# ---- suppressed auto edges (2026-10-27): DeckPicker$6 and $7 are never cancelled and the export task publishes no progress; $8 is closed on API 27 because layout-v14 declares add_content_menu
sup(('DeckTask.onCancelled', 'DeckPicker$6.onCancelled'),
    ('DeckTask.onCancelled', 'DeckPicker$7.onCancelled'),
    ('DeckTask$TaskListener.onProgressUpdate', 'DeckPicker$7.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@DeckPicker$7', 'DeckPicker$7.onProgressUpdate'),
    ('DeckPicker.onCreate', 'DeckPicker$8.<init>'))
# ---- part 005 (2026-10-27)
# AnkiDroid batch 005 (LABEL helper). DeckPicker listeners and callbacks: deck tap, counts tap, long-press, empty-deck
# and custom-study snackbars, rename, delete, rebuild and empty filtered decks, find empty cards, import.
# ASYNC edges belong to the part that starts the task (batch 002 or 003) and are not written here.

gui('S_DECKPICKER', 'DeckPicker$2.onClick',
    'tap a deck in the deck list (the deck row, not the counts area)',
    needs_state=STATE_DECK,
    evidence='SRC com/ichi2/anki/DeckPicker.java:195-207,384')

gui('S_DECKPICKER', 'DeckPicker$3.onClick',
    'tap the due counts of a deck in the deck list',
    needs_state=STATE_DECK,
    evidence='SRC com/ichi2/anki/DeckPicker.java:212-224,385; SRC com/ichi2/anki/DeckPicker.java:1735')

gui('S_DECKPICKER', 'DeckPicker$4.onLongClick',
    'long-press a deck in the deck list (opens the deck context menu)',
    needs_state=STATE_DECK,
    evidence='SRC com/ichi2/anki/DeckPicker.java:229-235,387')

gui('S_DECKPICKER', 'DeckPicker$20.onClick',
    'select an empty deck (no cards, no subdecks, not filtered), then tap Help in the snackbar',
    evidence='SRC com/ichi2/anki/DeckPicker.java:1769-1778')

gui('S_DECKPICKER', 'DeckPicker$21.onClick',
    'select a deck with subdecks or cards but nothing due, then tap Custom study in the snackbar',
    evidence='SRC com/ichi2/anki/DeckPicker.java:1784-1794')

e('DeckPicker$3.<init>', 'DeckPicker$3.onClick', 'REGISTER',
  'the counts listener is set on the deck adapter',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:210,385',
  note='The builder does not follow REGISTER for reachability; the route to onClick is the S_DECKPICKER -> DeckPicker$3.onClick edge.')

e('DeckPicker$4.<init>', 'DeckPicker$4.onLongClick', 'REGISTER',
  'the long-click listener is set on the deck adapter',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:227,387',
  note='The builder does not follow REGISTER for reachability; the route to onLongClick is the S_DECKPICKER -> DeckPicker$4.onLongClick edge.')

e('DeckPicker$20.<init>', 'DeckPicker$20.onClick', 'REGISTER',
  'the Help action listener is passed to UIUtils.showSnackbar',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1773-1778; SRC com/ichi2/anki/UIUtils.java:56-58',
  note='The builder does not follow REGISTER for reachability; the route to onClick is the S_DECKPICKER -> DeckPicker$20.onClick edge.')

e('DeckPicker$21.<init>', 'DeckPicker$21.onClick', 'REGISTER',
  'the Custom study action listener is passed to UIUtils.showSnackbar',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1786-1794; SRC com/ichi2/anki/UIUtils.java:56-58',
  note='The builder does not follow REGISTER for reachability; the route to onClick is the S_DECKPICKER -> DeckPicker$21.onClick edge.')

e('DeckPicker$26.<init>', 'DeckPicker$26.onDismissed', 'REGISTER',
  'the show/hide callback is passed to every snackbar that handleDeckSelection shows',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1754,1778,1794,2151; SRC com/ichi2/anki/UIUtils.java:56-58',
  note='Snackbar.Callback dispatch is library code with no source in the dataset; onDismissed is INFERRED in label_005.md.')

e('DeckPicker$26.<init>', 'DeckPicker$26.onShown', 'REGISTER',
  'the show/hide callback is passed to every snackbar that handleDeckSelection shows',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1754,1778,1794,2151; SRC com/ichi2/anki/UIUtils.java:56-58',
  note='Snackbar.Callback dispatch is library code with no source in the dataset; onShown is INFERRED in label_005.md.')

e('DeckPicker$23.<init>', 'DeckPicker$23.onPositive', 'FRAMEWORK',
  'the rename dialog calls onPositive when its positive button is tapped (MaterialDialog.ButtonCallback)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1921-1925,1938-1956',
  note='Library dispatch (no source in the dataset). The dialog is shown only after $23.<init> is constructed in renameDeckDialog(long).')

e('DeckPicker$23.<init>', 'DeckPicker$23.onNegative', 'FRAMEWORK',
  'the rename dialog calls onNegative when its negative button is tapped (MaterialDialog.ButtonCallback)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1921-1925,1958-1961',
  note='Library dispatch (no source in the dataset). Same dialog as onPositive.')

e('DeckPicker$27$1.<init>', 'DeckPicker$27$1.confirm', 'FRAMEWORK',
  'the confirmation dialog calls confirm() when its positive button is tapped',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2188-2195; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43',
  note='Library dispatch (no source in the dataset). The dialog is shown only from DeckPicker$27.onPostExecute when the count is non-zero.')

UNREACHABLE['DeckPicker$5.onCancelled'] = (
    'no_trigger_in_app',
    "The import task is never cancelled in the app. DeckTask.cancelTask(int) cancels only when the task type matches (DeckTask.java:181-186), and its only callers are CardBrowser for SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). TaskOperations.stopTaskGracefully is called only with the caller's own task (TranslationActivity.java:405). AsyncTask runs onCancelled only after cancel() (FW-SRC core/java/android/os/AsyncTask.java:525-527,691-698). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:265-267; SRC com/ichi2/async/DeckTask.java:181-186; SRC com/ichi2/anki/CardBrowser.java:528-529; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405',
    'SOURCE')

UNREACHABLE['DeckPicker$22.onCancelled'] = (
    'no_trigger_in_app',
    "The deck-count load task is never cancelled in the app (DeckTask.cancelTask(int) callers are CardBrowser only, see $5.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1881-1882; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$22.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundLoadDeckCounts (DeckTask.java:480-491) calls no publishProgress, so AsyncTask never dispatches onProgressUpdate for this task type. AsyncTask dispatches onProgressUpdate only from publishProgress (FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1877-1878; SRC com/ichi2/async/DeckTask.java:480-491; FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716',
    'SOURCE')

UNREACHABLE['DeckPicker$24.onCancelled'] = (
    'no_trigger_in_app',
    "The delete-deck task is never cancelled in the app (DeckTask.cancelTask(int) callers are CardBrowser only, see $5.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2065-2066; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$24.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundDeleteDeck (DeckTask.java:719-725) calls no publishProgress, so AsyncTask never dispatches onProgressUpdate for this task type (see $22.onProgressUpdate). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2060-2061; SRC com/ichi2/async/DeckTask.java:719-725; FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716',
    'SOURCE')

UNREACHABLE['DeckPicker$25.onCancelled'] = (
    'no_trigger_in_app',
    "The rebuild and empty filtered-deck tasks are never cancelled in the app (DeckTask.cancelTask(int) callers are CardBrowser only, see $5.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2096-2097; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$25.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundRebuildCram (DeckTask.java:728-733) and doInBackgroundEmptyCram (DeckTask.java:736-741) call no publishProgress, so AsyncTask never dispatches onProgressUpdate for these task types (see $22.onProgressUpdate). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2091-2092; SRC com/ichi2/async/DeckTask.java:728-741; FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716',
    'SOURCE')

UNREACHABLE['DeckPicker$27.onCancelled'] = (
    'no_trigger_in_app',
    "The find-empty-cards task is never cancelled in the app (DeckTask.cancelTask(int) callers are CardBrowser only, see $5.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2209-2211; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$27.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackGroundFindEmptyCards (DeckTask.java:1228-1232) calls no publishProgress, so AsyncTask never dispatches onProgressUpdate for this task type (see $22.onProgressUpdate). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2204-2206; SRC com/ichi2/async/DeckTask.java:1228-1232; FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716',
    'SOURCE')

# ---- suppressed auto edges (2026-10-27, batch 005): IMPORT, LOAD_DECK_COUNTS, DELETE_DECK, REBUILD/EMPTY_CRAM and FIND_EMPTY_CARDS are never cancelled and publish no progress
sup(('DeckTask.onCancelled', 'DeckPicker$5.onCancelled'),
    ('DeckTask.onCancelled', 'DeckPicker$22.onCancelled'),
    ('DeckTask.onCancelled', 'DeckPicker$24.onCancelled'),
    ('DeckTask.onCancelled', 'DeckPicker$25.onCancelled'),
    ('DeckTask.onCancelled', 'DeckPicker$27.onCancelled'),
    ('DeckTask$TaskListener.onProgressUpdate', 'DeckPicker$22.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@DeckPicker$22', 'DeckPicker$22.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate', 'DeckPicker$24.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@DeckPicker$24', 'DeckPicker$24.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate', 'DeckPicker$25.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@DeckPicker$25', 'DeckPicker$25.onProgressUpdate'),
    ('DeckTask.onProgressUpdate', 'DeckPicker$27.onProgressUpdate'))

# ---- part 002 (2026-10-28)
# AnkiDroid batch 002 (LABEL helper): DeckPicker methods. Items and routes are in label_002.md.
# Edges written here:
#   - edges whose source is a batch-002 method: FRAMEWORK, ENTERS, REGISTER, ASYNC;
#   - page -> batch-002 method edges (RESULT, GUI), written here because the destination is in this batch
#     (ownership rule: page-sourced edges are written by the part that holds the destination);
#   - UNREACHABLE for DeckPicker.hasErrorFiles.
# Edges whose source is outside batch 002 are not written here (see graphs/AnkiDroid/scratch/conflicts_002.md).
# Constants used (defined in graph_def.py): ENV_STORAGE, ENV_PERM_STORAGE, STATE_COLLECTION, STATE_DECK.
# MISSING GATE notes (MG1, MG4, MG5, MG6) are text only: no env or needs_state is set for them.

# ---- FRAMEWORK (5) ----

e('DeckPicker.onCreate', 'DeckPicker.onRestoreInstanceState', 'FRAMEWORK',
  'the framework restores saved instance state into the recreated activity',
  env=None,
  note='Written here because onCreate is the batch-002 source. Batch 003 REACHABLE rows depend on this edge (see conflicts_002.md). Only when saved state exists (ActivityThread 2746-2751).',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2747-2751; SRC com/ichi2/anki/DeckPicker.java:723-726')

e('DeckPicker.firstCollectionOpen', 'DeckPicker.onRequestPermissionsResult', 'FRAMEWORK',
  'the storage permission result from the request made in firstCollectionOpen is dispatched back to the activity',
  env=None,
  note='firstCollectionOpen calls ActivityCompat.requestPermissions (DeckPicker.java:450-451). Framework start at Activity.java 4382-4383; dispatch at 7267-7270 and 7412-7419. Batch 003 REACHABLE rows depend on this edge.',
  evidence='FW-SRC core/java/android/app/Activity.java:4382-4383, 7267-7270, 7412-7419; SRC com/ichi2/anki/DeckPicker.java:442-455, 680-682')

e('DeckPicker.onCreate', 'DeckPicker.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the activity',
  env=None,
  note='Activity.onCreatePanelMenu calls onCreateOptionsMenu. The exact time the panel is prepared is not modelled; the edge starts at onCreate, the batch-002 source on the route.',
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388; SRC com/ichi2/anki/DeckPicker.java:523-524')

e('DeckPicker.onCreate', 'DeckPicker.onAttachedToWindow', 'FRAMEWORK',
  'the decor view attaches to the window and the framework calls onAttachedToWindow',
  env=None,
  note='APPROXIMATION: the framework attaches the window after onResume (batch 003 owns onResume). The edge starts at onCreate because onCreate is the batch-002 source. See conflicts_002.md.',
  evidence='FW-SRC core/java/com/android/internal/policy/DecorView.java:1585-1590; FW-SRC core/java/android/app/Activity.java:3169; SRC com/ichi2/anki/DeckPicker.java:2113-2119')

e('DeckPicker.finishWithAnimation', 'DeckPicker.onDestroy', 'FRAMEWORK',
  'the activity finishes and the framework performs destroy, which calls onDestroy',
  env=None,
  note='finishWithAnimation -> AnkiActivity.finishWithAnimation -> Activity.finish -> performDestroy -> onDestroy.',
  evidence='FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208; SRC com/ichi2/anki/AnkiActivity.java:206-209; SRC com/ichi2/anki/DeckPicker.java:749-750')

# ---- ENTERS (17): method -> page, condition in the trigger text ----

e('DeckPicker.onCreate', 'S_DECKPICKER', 'ENTERS',
  'the collection is open (colOpen true) so the deck list is shown',
  env=ENV_PERM_STORAGE, needs_state=STATE_COLLECTION,
  note='firstCollectionOpen (line 357) then startup screens when colOpen is true (lines 415-417). Storage permission is the ENV_PERM_STORAGE gate.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:357; SRC com/ichi2/anki/DeckPicker.java:415-417')

e('DeckPicker.onCreate', 'S_PREFERENCES', 'ENTERS',
  'the collection is not open and the AnkiDroid directory is inaccessible: the advanced preferences open to update the path',
  env=ENV_STORAGE,
  note='OPEN DECISION: ENV_STORAGE is used for the directory-inaccessible branch (see conflicts_002.md). The branch runs only when the SD card is mounted.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:418-428')

e('DeckPicker.onCreate', 'S_DLG_DATABASE_ERROR', 'ENTERS',
  'the collection is not open and the storage checks pass: the cursor-size dialog (id 9) or the load-failed dialog (id 0) is shown',
  env=None,
  note='MISSING GATE MG1: no STATE exists for an unopenable collection. The gate is not modelled here; env and needs_state are unset.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:418, 430-433; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:27-36')

e('DeckPicker.addNote', 'S_NOTEEDITOR', 'ENTERS',
  'the add-note floating button is tapped and the note editor opens for a new note',
  env=None,
  note='The editor returns through RESULT to onActivityResult (written below).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:840-844')

e('DeckPicker.loginToSyncServer', 'S_MYACCOUNT', 'ENTERS',
  'a login for sync is needed, so the MyAccount activity opens for login',
  env=None,
  note='The caller of this method is the sync-error dialog (gui edge below, MG4).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1570-1573')

e('DeckPicker.onOptionsItemSelected', 'S_DLG_IMPORT', 'ENTERS',
  'the import menu item is tapped and the import dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:561-563')

e('DeckPicker.onOptionsItemSelected', 'S_DLG_DATABASE_ERROR', 'ENTERS',
  'the check-database or restore-backup menu item is tapped and the database dialog opens (ids 6 and 7)',
  env=None,
  note='User-initiated, so no MG. The dialog is shown through the showDatabaseErrorDialog helper (DeckPicker.java:1026-1028).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:595-598, 616-619, 1026-1028')

e('DeckPicker.onOptionsItemSelected', 'S_DLG_MEDIA_CHECK', 'ENTERS',
  'the check-media menu item is tapped and the media check dialog opens',
  env=None,
  note='The dialog is shown through the showMediaCheckDialog helper.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:600-603')

e('DeckPicker.onOptionsItemSelected', 'S_DLG_EXPORT', 'ENTERS',
  'the export menu item is tapped and the export dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:621-625')

e('DeckPicker.onOptionsItemSelected', 'S_MODELBROWSER', 'ENTERS',
  'the model browser menu item is tapped and the model browser opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:610-614')

e('DeckPicker.exportDeck', 'S_DLG_EXPORT', 'ENTERS',
  'a deck export is requested and the export dialog opens for that deck',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1909-1916')

e('DeckPicker.confirmDeckDeletion(long)', 'S_DLG_DECKPICKER_DELETE_DECK', 'ENTERS',
  'a deck other than the default deck (did != 1) that has cards (cnt != 0) is to be deleted: the delete-confirmation dialog opens',
  env=None, needs_state=STATE_DECK,
  note='Guard: did != 1 (line 1977) and cnt != 0 (line 1994). When cnt is 0, deleteDeck is called directly (line 1995).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1972-1978, 1991-1995, 2008')

e('DeckPicker.handleDbError', 'S_DLG_DATABASE_ERROR', 'ENTERS',
  'a database error result is reported and the load-failed dialog opens',
  env=None,
  note='MISSING GATE MG1: no STATE for an unopenable collection or load failure. The gate is not modelled here.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1243-1245')

e('DeckPicker.onCollectionLoadError', 'S_DLG_DATABASE_ERROR', 'ENTERS',
  'the collection load error is reported and the load-failed dialog opens through DialogHandler (indirect)',
  env=None,
  note='MISSING GATE MG1 (indirect through the DialogHandler message path).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:835-837; SRC com/ichi2/anki/dialogs/DialogHandler.java:58-60')

e('DeckPicker.deleteUnused', 'S_DLG_SIMPLE_MESSAGE', 'ENTERS',
  'unused media is deleted and a simple message reports the result (indirect through showSimpleMessageDialog)',
  env=None,
  note='MISSING GATE MG6: no STATE for unused media. The gate is not modelled here.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1227-1233')

e('DeckPicker.loadStudyOptionsFragment', 'S_STUDYOPTIONS_FRAG', 'ENTERS',
  'the device uses the fragmented (tablet) layout and the study options fragment is loaded',
  env=None,
  note='Only when mFragmented is true (DeckPicker.java:829 under mFragmented; check at 1650-1655).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:829, 1650-1655')

e('DeckPicker.onFinishedStartup', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the mod-schema change needs confirmation (ConfirmModSchemaException) and the force-full-sync confirmation dialog opens through DialogHandler (indirect)',
  env=None,
  note='MISSING GATE MG5: the ConfirmModSchemaException path (catch at line 814) is not modelled. The gate is not modelled here.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:805-832; SRC com/ichi2/anki/dialogs/DialogHandler.java:88-90')

# ---- RESULT (8): page -> DeckPicker.onActivityResult ----

e('S_NOTEEDITOR', 'DeckPicker.onActivityResult', 'RESULT',
  'the note editor finishes and returns a result to the deck picker',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:634-641, 840-844')

e('S_MYACCOUNT', 'DeckPicker.onActivityResult', 'RESULT',
  'the MyAccount login activity finishes and returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:634-641, 1570-1573')

e('S_PREFERENCES', 'DeckPicker.onActivityResult', 'RESULT',
  'the preferences activity opened for the path update (REQUEST_PATH_UPDATE) returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:428, 634-641')

e('S_INFO', 'DeckPicker.onActivityResult', 'RESULT',
  'the Info page opened for a new version returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:938-947')

e('S_STUDYOPTIONS', 'DeckPicker.onActivityResult', 'RESULT',
  'the study options activity finishes and returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1695-1703')

e('S_CARDBROWSER', 'DeckPicker.onActivityResult', 'RESULT',
  'the card browser finishes and returns a result (REQUEST_BROWSE_CARDS)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1708-1713')

e('S_REVIEWER', 'DeckPicker.onActivityResult', 'RESULT',
  'the reviewer finishes and returns a result (REQUEST_REVIEW)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2128-2130')

e('S_MODELBROWSER', 'DeckPicker.onActivityResult', 'RESULT',
  'the model browser finishes and returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:610-614')

# ---- GUI (19): page -> method, via gui() ----

gui('S_DECKPICKER', 'DeckPicker.onBackPressed',
    'back key pressed on the deck list with the navigation drawer closed',
    evidence='SRC com/ichi2/anki/DeckPicker.java:773-786')

gui('S_DECKPICKER', 'DeckPicker.onOptionsItemSelected',
    'an options menu item is tapped on the deck list',
    evidence='SRC com/ichi2/anki/DeckPicker.java:544-549')

gui('S_DLG_DECKPICKER_CONTEXT', 'DeckPicker.confirmDeckDeletion()',
    'the delete item of the deck context menu is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:122-124')

gui('S_DLG_DECKPICKER_CONTEXT', 'DeckPicker.emptyFiltered',
    'the empty-filtered-deck item of the deck context menu is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:164-166')

gui('S_DLG_DECKPICKER_DELETE_DECK', 'DeckPicker.deleteContextMenuDeck',
    'the confirm button of the delete-deck dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DeckPickerConfirmDeleteDeckDialog.java:36-37')

gui('S_STUDYOPTIONS_FRAG', 'DeckPicker.confirmDeckDeletion(long)',
    'the delete item in the study options fragment is tapped (fragmented layout only)',
    evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:331-332')

gui('S_STUDYOPTIONS_FRAG', 'DeckPicker.exportDeck',
    'the export item in the study options fragment is tapped (fragmented layout only)',
    evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:334-335')

gui('S_DLG_EXPORT', 'DeckPicker.exportApkg',
    'the positive button of the export dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:98-100')

gui('S_DLG_IMPORT', 'DeckPicker.importAdd',
    'the add button of the import dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:133-134')

gui('S_DLG_IMPORT', 'DeckPicker.importReplace',
    'the replace button of the import dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:147-148')

gui('S_DLG_DATABASE_ERROR', 'DeckPicker.integrityCheck',
    'the positive button of the database-check confirmation is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:294-302')

gui('S_DLG_DATABASE_ERROR', 'DeckPicker.exit',
    'the negative button of the load-failed dialog is tapped',
    note='MISSING GATE MG1: the page is reached only through the unopenable-collection path (no STATE). The gate is not modelled here.',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:89-92')

gui('S_DLG_MEDIA_CHECK', 'DeckPicker.mediaCheck',
    'the positive button of the media check dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:69-70')

gui('S_DLG_MEDIA_CHECK', 'DeckPicker.deleteUnused',
    'the delete-unused button of the media check dialog is tapped',
    note='MISSING GATE MG6: unused-media state is not modelled. The gate is not modelled here.',
    evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:126-128')

gui('S_DLG_DECKPICKER_EXPORT_DONE', 'DeckPicker.emailFile',
    'the email button of the export-complete dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DeckPickerExportCompleteDialog.java:34-36')

gui('S_DLG_SYNC_ERROR', 'DeckPicker.loginToSyncServer',
    'the login button of the sync-error dialog is tapped',
    note='MISSING GATE MG4: the failed-sync state is not modelled. S_DLG_SYNC_ERROR has no ENTERS owner yet (see conflicts_002.md).',
    evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:80-81')

gui('S_DLG_SYNC_ERROR', 'DeckPicker.mediaCheck',
    'the media check button of the sync-error dialog is tapped',
    note='MISSING GATE MG4: the failed-sync state is not modelled. S_DLG_SYNC_ERROR has no ENTERS owner yet.',
    evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:209-210')

gui('S_DLG_CUSTOM_STUDY', 'DeckPicker.onCreateCustomStudySession',
    'the positive button of the custom study dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:467')

gui('S_DLG_CUSTOM_STUDY', 'DeckPicker.onExtendStudyLimits',
    'the extend-limits button of the custom study dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:482-488')

# ---- REGISTER (3): listener registration in configureFloatingActionsMenu ----

e('DeckPicker.configureFloatingActionsMenu', 'DeckPicker$9.onClick', 'REGISTER',
  'the add-deck floating button listener is registered',
  env=None,
  note='REGISTER is not followed for reachability. The node DeckPicker$9.onClick belongs to batch 006.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:461-463')

e('DeckPicker.configureFloatingActionsMenu', 'DeckPicker$10.onClick', 'REGISTER',
  'the add-shared-deck floating button listener is registered',
  env=None,
  note='REGISTER is not followed for reachability. The node DeckPicker$10.onClick belongs to batch 004.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:488-492')

e('DeckPicker.configureFloatingActionsMenu', 'DeckPicker$11.onClick', 'REGISTER',
  'the add-note floating button listener is registered',
  env=None,
  note='REGISTER is not followed for reachability. The node DeckPicker$11.onClick belongs to batch 004.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:495-499')

# ---- ASYNC (8): method -> listener onPostExecute ----

e('DeckPicker.integrityCheck', 'DeckPicker$15.onPostExecute', 'ASYNC',
  'the integrity check runs as a background task and its result is posted to onPostExecute',
  env=None,
  note='DeckPicker$15.onPostExecute (batch 004) calls handleDbError on failure (line 1172).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1146-1147')

e('DeckPicker.mediaCheck', 'DeckPicker$16.onPostExecute', 'ASYNC',
  'the media check runs as a background task and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1190-1191')

e('DeckPicker.importAdd', 'DeckPicker$5.onPostExecute', 'ASYNC',
  'the add-import runs as a background task and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1579-1581')

e('DeckPicker.importReplace', 'DeckPicker$6.onPostExecute', 'ASYNC',
  'the replace-import runs as a background task and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1587-1588')

e('DeckPicker.exportApkg', 'DeckPicker$7.onPostExecute', 'ASYNC',
  'the apkg export runs as a background task and its result is posted to onPostExecute',
  env=None,
  note='DeckPicker$7.onPostExecute (batch 006) shows DeckPickerExportCompleteDialog at line 328, which is the route to emailFile.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1622-1623')

e('DeckPicker.deleteDeck', 'DeckPicker$24.onPostExecute', 'ASYNC',
  'the delete-deck task runs in the background and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2016-2017')

e('DeckPicker.emptyFiltered', 'DeckPicker$25.onPostExecute', 'ASYNC',
  'the empty-cram task runs in the background (TASK_TYPE_EMPTY_CRAM) and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2106-2109')

e('DeckPicker.handleEmptyCards', 'DeckPicker$27.onPostExecute', 'ASYNC',
  'the empty-cards task runs in the background and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2171-2172')

# ---- UNREACHABLE (1) ----

UNREACHABLE['DeckPicker.hasErrorFiles'] = ('no_trigger_in_app', 'the only caller is DatabaseErrorDialog.java:126, inside case DIALOG_DB_ERROR (id 1); no code passes or sends id 1, so the case never runs and hasErrorFiles is never called', 'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:28; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:96-126; SRC com/ichi2/anki/dialogs/DialogHandler.java:87', 'SOURCE')

# ---- suppressed: bytecode edges from dead branches (2026-10-28) ----

sup(('DatabaseErrorDialog.onCreateDialog', 'DeckPicker.hasErrorFiles'),
    ('AnkiDroidApp$ProductionCrashReportingTree.e(String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.createTag'),
    ('AnkiDroidApp$ProductionCrashReportingTree.e(Throwable,String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.createTag'),
    ('AnkiDroidApp$ProductionCrashReportingTree.w(String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.createTag'),
    ('AnkiDroidApp$ProductionCrashReportingTree.w(Throwable,String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.createTag'),
    ('AnkiDroidApp$ProductionCrashReportingTree.e(String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.formatString'),
    ('AnkiDroidApp$ProductionCrashReportingTree.e(Throwable,String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.formatString'),
    ('AnkiDroidApp$ProductionCrashReportingTree.w(String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.formatString'),
    ('AnkiDroidApp$ProductionCrashReportingTree.w(Throwable,String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.formatString'),
    ('AnkiDroidApp$ProductionCrashReportingTree.i(String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.formatString'),
    ('AnkiDroidApp$ProductionCrashReportingTree.i(Throwable,String,Object[])', 'AnkiDroidApp$ProductionCrashReportingTree.formatString'))

# ---- part 007 (2026-10-28) ----

# AnkiDroid batch 007 (LABEL helper): the 14 StudyOptionsActivity methods. The full row list is in
# graphs/AnkiDroid/parts/label_007.md.
#
# Ownership: an edge is written in the part that holds its source method. Page-sourced edges into batch-007
# methods are written here (GUI, RESULT). Written here: ENTERS from onCreate and loadStudyOptionsFragment (source
# is in this batch); GUI from S_STUDYOPTIONS and S_DLG_CUSTOM_STUDY; RESULT from the five result pages.
# Not written here: DeckPicker.openStudyOptions -> StudyOptionsActivity.<init> (INTENT, batch 003); the page edges
# from S_STUDYOPTIONS_FRAG (DeckOptions, FilteredDeckOptions, custom study dialog; batch 038); the page edges from the
# navigation drawer (Statistics, Preferences, CardBrowser; batch 036); the suppression of the unguarded bytecode CALL
# StudyOptionsFragment$3.onPostExecute -> StudyOptionsActivity.onRequireDeckListUpdate (batch 038, sup()).
#
# UNREACHABLE entries: StudyOptionsActivity.onOptionsItemSelected and StudyOptionsActivity.onRequireDeckListUpdate.
# Constants: none. Missing gates are text only (note='MISSING GATE MGn: ...', MG14 to MG16); no env or needs_state gate.

# ---- ENTERS (2): method -> page ----

e('StudyOptionsActivity.onCreate', 'S_STUDYOPTIONS', 'ENTERS',
  'the study options screen is shown: studyoptions.xml is inflated and the navigation drawer is set up',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsActivity.java:36-48; SRC res/layout/studyoptions.xml:16-18',
  note='onCreate is in this part. The start edge (DeckPicker.openStudyOptions -> StudyOptionsActivity.<init>, INTENT) is batch 003. Phone layout only: DeckPicker.java:365-367 sets mFragmented false when studyoptions_fragment is absent (it exists only in res/layout-xlarge/homescreen.xml:19).')

e('StudyOptionsActivity.loadStudyOptionsFragment', 'S_STUDYOPTIONS_FRAG', 'ENTERS',
  'the study options fragment is committed into the studyoptions_frame container of the activity',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsActivity.java:45-57; SRC res/layout/studyoptions.xml:16',
  note='Runs from onCreate only when savedInstanceState is null (StudyOptionsActivity.java:45-46). The withDeckOptions extra is set by DeckPicker.openStudyOptions (DeckPicker.java:1700-1701, batch 003).')

# ---- GUI (3): page -> method, via gui() ----

gui('S_STUDYOPTIONS', 'StudyOptionsActivity.onBackPressed',
    'press the Back key while the navigation drawer is closed',
    env=None,
    evidence='SRC com/ichi2/anki/StudyOptionsActivity.java:107-115; SRC com/ichi2/anki/NavigationDrawerActivity.java:240-247; FW-SRC core/java/android/app/Activity.java:2975-2981, 3272; FW-SRC core/java/android/view/KeyEvent.java:2715',
    note='MISSING GATE MG16: the drawer must be closed. With the drawer open the Back key closes the drawer instead (NavigationDrawerActivity.java:241-243; StudyOptionsActivity.java:109). Not modelled as a gate.')

gui('S_DLG_CUSTOM_STUDY', 'StudyOptionsActivity.onCreateCustomStudySession',
    'choose a Forgotten, Ahead, Random or Preview option in the custom study menu, then confirm; the custom study deck is built and the listener is called',
    env=None,
    evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:272-276, 304-307, 346-349; SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:184-185, 258-279, 415, 424-430, 467',
    note='MISSING GATE MG14: createCustomStudySession returns early (CustomStudyDialog.java:424-430) when a deck with the custom study name exists and its type flag is not 1; the standard fixture is assumed to have no such deck. MISSING GATE MG15: the custom study menu item is hidden for filtered decks (StudyOptionsFragment.java:346-349); the page edge from S_STUDYOPTIONS_FRAG is batch 038. A second route, through the tags dialog (CustomStudyDialog.java:145-176), reaches the same callback from another page; that page edge is not written here.')

gui('S_DLG_CUSTOM_STUDY', 'StudyOptionsActivity.onExtendStudyLimits',
    'choose the new-card limit or the review limit in the custom study menu and confirm',
    env=None,
    evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:272-276; SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:78-79, 184-185, 234-253, 482-488',
    note='MISSING GATE MG15: the custom study menu item is hidden for filtered decks (StudyOptionsFragment.java:346-349). jumpToReviewer is false on this path (the two-argument newInstance at CustomStudyDialog.java:78-79 is used at StudyOptionsFragment.java:273-274), so onLimitsExtended calls the listener (CustomStudyDialog.java:488).')

# ---- RESULT (5): page -> StudyOptionsActivity.onActivityResult ----

e('S_DECKOPTIONS', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the deck options screen started from the study options fragment returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:294-301; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='The fragment starts DeckOptions with getActivity().startActivityForResult (StudyOptionsFragment.java:300), so the result goes to this activity. The page edge from S_STUDYOPTIONS_FRAG is batch 038 and is not written here.')

e('S_FILTEREDDECKOPTIONS', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the filtered deck options screen started from the study options fragment returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:138-139, 149-152, 296-297; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='openFilteredDeckOptions (StudyOptionsFragment.java:149-152) is reached from the deck options item for a filtered deck (lines 296-297). The page edge from S_STUDYOPTIONS_FRAG is batch 038 and is not written here.')

e('S_STATISTICS', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the statistics screen started from the navigation drawer returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:265-268; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='nav_stats branch of the navigation drawer (line 265) starts Statistics with REQUEST_STATISTICS (line 268). The drawer is batch 036; its page edge is not written here.')

e('S_PREFERENCES', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the preferences screen started from the navigation drawer returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:273-277; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='nav_settings branch of the navigation drawer (line 273) starts Preferences with REQUEST_PREFERENCES_UPDATE (line 277). The drawer is batch 036; its page edge is not written here.')

e('S_CARDBROWSER', 'StudyOptionsActivity.onActivityResult', 'RESULT',
  'the card browser started from the navigation drawer returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:262-264, 295-298; FW-SRC core/java/android/app/Activity.java:748, 4486-4493, 7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='nav_browser branch (line 262) calls openCardBrowser (line 263), which starts CardBrowser with REQUEST_BROWSE_CARDS (line 298). The drawer is batch 036; its page edge is not written here.')

# ---- UNREACHABLE (2) ----

UNREACHABLE['StudyOptionsActivity.onOptionsItemSelected'] = (
    'framework_never_calls',
    "The framework calls this method from Activity.onMenuItemSelected for the options panel (Activity.java:3450). The panel is built in Activity.onCreatePanelMenu (Activity.java:3386-3390) from onCreateOptionsMenu and from the fragment manager's options-menu dispatch. StudyOptionsActivity, NavigationDrawerActivity and AnkiActivity do not override onCreateOptionsMenu, and StudyOptionsFragment never calls setHasOptionsMenu (grep of the app tree), so the activity has no options-panel item to select. The fragment's own toolbar menu (StudyOptionsFragment.java:186) sends its clicks to the fragment listener (StudyOptionsFragment.java:343), not to this activity. The home button is the only other source: its click listener is the Toolbar navigation listener (NavigationDrawerActivity.java:77-86), which opens the drawer because mNavButtonGoesBack stays false here (it is set only by showBackIcon, NavigationDrawerActivity.java:308, and showBackIcon is called only from Previewer.java:40 and 50). Toolbar and AppCompat dispatch is not in the dataset, so this claim is INFERRED. The body (StudyOptionsActivity.java:66-79) is therefore not reached.",
    'SRC com/ichi2/anki/StudyOptionsActivity.java:66-79; SRC com/ichi2/anki/StudyOptionsFragment.java:186, 343; SRC com/ichi2/anki/NavigationDrawerActivity.java:71-86, 301-309; FW-SRC core/java/android/app/Activity.java:3386-3390, 3439-3452',
    'INFERRED')

UNREACHABLE['StudyOptionsActivity.onRequireDeckListUpdate'] = (
    'branch_never_taken',
    "Two app call sites exist. StudyOptionsFragment.java:657-658 calls the listener only when mFragmented && refreshDecklist holds, and mFragmented is set at line 180 to getActivity().getClass() != StudyOptionsActivity.class, so it is false in this activity and the call is never made here. DeckPickerContextMenu.java:154 is the other call site; its only host is DeckPicker (DeckPicker.java:233 is the only DeckPickerContextMenu.newInstance call in the app tree), so the cast there is to DeckPicker and this method is not called on this activity. The bytecode extractor adds an unguarded CALL edge StudyOptionsFragment$3.onPostExecute -> StudyOptionsActivity.onRequireDeckListUpdate (auto_calls.json, line 11373, source StudyOptionsFragment.java:658); it ignores the guard at line 657 and must be suppressed by batch 038 with sup(). The body (StudyOptionsActivity.java:137) is not reached.",
    'SRC com/ichi2/anki/StudyOptionsFragment.java:180, 657-658; SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:154; SRC com/ichi2/anki/DeckPicker.java:233, 2123; SRC com/ichi2/anki/StudyOptionsActivity.java:136-138',
    'SOURCE')

sup(('StudyOptionsFragment$3.onPostExecute', 'StudyOptionsActivity.onRequireDeckListUpdate'),
    ('DeckPickerContextMenu$1.onSelection', 'StudyOptionsActivity.onRequireDeckListUpdate'))

# ---- DeckPicker INTENT addendum (orchestrator, 2026-10-28): launches missing from parts 002 and 003 ----

e('DeckPicker.onCreate', 'Preferences.<init>', 'INTENT',
  'the AnkiDroid directory cannot be accessed, so the user is sent to the Advanced preferences subscreen to change the path',
  guard='storage permission is granted and the SD card is mounted (DeckPicker.java:420-422), and the directory check at line 425 fails',
  env=None,
  note='The intent is built in CompatV10 and CompatV11 getPreferenceSubscreenIntent, and both create new Intent(context, Preferences.class). Written here, at the DeckPicker call site, by the orchestrator.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:420-428; SRC com/ichi2/compat/CompatV10.java:183-186; SRC com/ichi2/compat/CompatV11.java:41-48')

e('DeckPicker.onOptionsItemSelected', 'ModelBrowser.<init>', 'INTENT',
  'the user selects the options menu item action_model_browser_open, and the note type browser opens',
  env=None,
  note='Written here by the orchestrator (part 002 omitted it).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:610-613')

e('DeckPicker.addNote', 'NoteEditor.<init>', 'INTENT',
  'the add note action opens the note editor with the DeckPicker caller',
  env=None,
  note='Written here by the orchestrator (part 002 omitted it).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:840-843')

e('DeckPicker.loginToSyncServer', 'MyAccount.<init>', 'INTENT',
  'the sign-in screen for sync opens with notLoggedIn set',
  env=None,
  note='Written here by the orchestrator (part 002 omitted it).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1570-1573')

e('DeckPicker.openStudyOptions', 'StudyOptionsActivity.<init>', 'INTENT',
  'the study options screen opens as its own activity, with withDeckOptions set',
  guard='phone layout: mFragmented is false (DeckPicker.java:365-367), so the else branch at line 1699 runs',
  env=None,
  note='MISSING GATE MG54: phone layout only. With the studyoptions_fragment container (res/layout-xlarge), openStudyOptions loads the fragment instead (DeckPicker.java:1696-1698). Not modelled as a gate. Written here by the orchestrator (part 003 omitted it).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:365-367, 1695-1703; SRC res/layout-xlarge/homescreen.xml:19')

e('DeckPicker.openCardBrowser', 'CardBrowser.<init>', 'INTENT',
  'the card browser opens with the selected deck and the last browser deck as extras',
  env=None,
  note='Written here by the orchestrator (part 003 omitted it).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1708-1713')

e('DeckPicker.showContextMenuDeckOptions', 'FilteredDeckOptions.<init>', 'INTENT',
  'the options screen for a filtered deck opens from the deck context menu',
  guard='the deck with id mContextMenuDid is a filtered deck (getCol().getDecks().isDyn, DeckPicker.java:1891)',
  env=None,
  note='Written here by the orchestrator (part 003 omitted it).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1889-1895')

e('DeckPicker.showContextMenuDeckOptions', 'DeckOptions.<init>', 'INTENT',
  'the deck options screen for a normal deck opens from the deck context menu',
  guard='the deck is not a filtered deck (else branch, DeckPicker.java:1896-1898)',
  env=None,
  note='Written here by the orchestrator (part 003 omitted it).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1889-1900')

e('DeckPicker.openReviewer', 'Reviewer.<init>', 'INTENT',
  'the reviewer opens with REQUEST_REVIEW, and the collection timebox starts',
  env=None,
  note='Batch 008 wrote the page shortcut S_DECKPICKER -> Reviewer.<init> (needs STATE_CARDS, label_008.py:12). This method-level edge is the route through openReviewer. Written here by the orchestrator (part 003 omitted it).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:2128-2131')

# ---- part 008 (2026-10-28) ----

# AnkiDroid batch 008 (LABEL helper). Reviewer activity: lifecycle, options menu, whiteboard, bury/suspend submenus, activity results.
# Edges written here have a source method in batch 008, or a page source (S_DECKPICKER, S_REVIEWER, S_NOTEEDITOR, S_CARDBROWSER,
# S_DECKOPTIONS, S_STATISTICS) whose destination is in batch 008 (coordinator rule 1). Routes through other batches' nodes are cited in
# graphs/AnkiDroid/parts/label_008.md.
# No UNREACHABLE entries: all 34 batch methods have a route. Some routes need a setting (customButtonAddCard, customButtonBury,
# customButtonSuspend) or a note state; those are set on the edge.
# Missing gates (notes only, env and needs_state unset): MG24 per-deck whiteboard state (MetaDB), MG25 note with two or more cards,
# MG26 filtered deck hides the deck options item.
# ActionProvider callbacks (hasSubMenu, onCreateActionView, onPrepareSubMenu, onMenuItemClick) come from the support library, which is
# not in fw_src; their routes are confirmed_by INFERRED.

e('S_DECKPICKER', 'Reviewer.<init>', 'INTENT',
  'the user taps a deck that has cards to study, and the Reviewer opens',
  needs_state=STATE_CARDS,
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2128-2131; SRC com/ichi2/anki/Reviewer.java:56',
  note='Page edge; the destination is in batch 008, so this part writes it. Shortcut: the route passes DeckPicker.openReviewer (batch_003), whose INTENT edge DeckPicker.openReviewer -> Reviewer.<init> is not in label_003.py. batch_003 should add that edge; both routes end at the same method, so there is no conflict.')

e('Reviewer.onOptionsItemSelected', 'DeckOptions.<init>', 'INTENT',
  'the user taps Deck options in the Reviewer menu',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:208-211; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1759',
  note='MISSING GATE MG26: the item is hidden for a filtered deck (Reviewer.java:302-304, Decks.isDyn), and no STATE models a filtered deck, so needs_state is unset. customButtonDeckOptions defaults to 0, which shows the item in the menu, so no setting gate applies.')

e('Reviewer.addNote', 'NoteEditor.<init>', 'INTENT',
  'the user taps Add note in the Reviewer menu, when the item is shown',
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:230-234, 237-244; SRC com/ichi2/anki/AbstractFlashcardViewer.java:173, 1754',
  note='customButtonAddCard defaults to 3 (MENU_DISABLED, AbstractFlashcardViewer.java:173). setCustomButtons hides action_add_note_reviewer when the value is 3 (Reviewer.java:239-244), so the route needs the preference set to 0, 1 or 2. The intent carries EXTRA_CALLER = CALLER_REVIEWER_ADD (Reviewer.java:232).')

e('Reviewer.openCardBrowser', 'CardBrowser.<init>', 'INTENT',
  'the user taps Browse cards in the navigation drawer while studying',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:508-517; SRC com/ichi2/anki/NavigationDrawerActivity.java:262-263',
  note='The CALL edge NavigationDrawerActivity.onNavigationItemSelected -> Reviewer.openCardBrowser is owned by batch_036 (NavigationDrawerActivity.java:262-263). The request code is REQUEST_BROWSE_CARDS (Reviewer.java:517).')

e('S_NOTEEDITOR', 'Reviewer.onActivityResult', 'RESULT',
  'the note editor, opened from the Reviewer to add a note, returns',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:960-963; SRC com/ichi2/anki/Reviewer.java:61, 232-233, 533-547',
  note='Page edge; the destination is in batch 008. The request code is ADD_NOTE (Reviewer.java:61, 233). Other NoteEditor callers return to their own activities (not this batch).')

e('S_CARDBROWSER', 'Reviewer.onActivityResult', 'RESULT',
  'the card browser, opened from the Reviewer, returns',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1132; SRC com/ichi2/anki/Reviewer.java:517, 533-547',
  note='Page edge; the destination is in batch 008. The request code is REQUEST_BROWSE_CARDS (Reviewer.java:534). The result data carries allDecksSelected and originalDeck, which Reviewer.onActivityResult reads (Reviewer.java:536-544).')

e('S_DECKOPTIONS', 'Reviewer.onActivityResult', 'RESULT',
  'the deck options screen, opened from the Reviewer menu, returns',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:590-593; SRC com/ichi2/anki/Reviewer.java:208-211, 533-547',
  note='Page edge; the destination is in batch 008. The request code is DECK_OPTIONS (Reviewer.java:210). Reviewer.onActivityResult passes it to super (546), which handles the request code (AbstractFlashcardViewer.java:1080-1088).')

e('S_STATISTICS', 'Reviewer.onActivityResult', 'RESULT',
  'the statistics screen, opened from the navigation drawer while studying, returns',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:708; SRC com/ichi2/anki/NavigationDrawerActivity.java:265-268; SRC com/ichi2/anki/Reviewer.java:533-547',
  note='Page edge; the destination is in batch 008. The request code is REQUEST_STATISTICS (NavigationDrawerActivity.java:265-268). Reviewer.onActivityResult stores the selected deck and restores originalDeck (Reviewer.java:534-544).')

e('S_REVIEWER', 'Reviewer.onCreateOptionsMenu', 'FRAMEWORK',
  'the Reviewer shows its options menu, and again after each invalidateOptionsMenu (each new question)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388; FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631; SRC com/ichi2/anki/Reviewer.java:251-255',
  note='The framework calls onCreatePanelMenu, which calls onCreateOptionsMenu. Reviewer.java:252 says it runs on every new question. The menu build also creates the Suspend and Bury providers (Reviewer.java:310-311).')

e('S_REVIEWER', 'Reviewer.onWindowFocusChanged', 'FRAMEWORK',
  'the Reviewer window gains or loses focus (a dialog, system UI, or returning to the app)',
  env=None,
  evidence='FW-SRC core/java/com/android/internal/policy/DecorView.java:1559-1571; FW-SRC core/java/android/app/Activity.java:3157-3159, 6938; SRC com/ichi2/anki/Reviewer.java:522-530',
  note='DecorView calls the window callback (DecorView.java:1571), which is the Activity (Activity.attach sets the callback at Activity.java:6938). Activity.onWindowFocusChanged runs first, then this override.')

e('S_REVIEWER', 'Reviewer$BuryProvider.hasSubMenu', 'FRAMEWORK',
  'the Bury item is shown or tapped, and the support library asks whether it has a dropdown',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:159-165, 629-631 (in-app call at 161)',
  note='INFERRED: ActionProvider is a support-library class and is not in fw_src. The in-app call at Reviewer.java:161 is a virtual call on the ActionProvider type and is not in auto_calls.json, so this page edge carries the route. hasSubMenu returns dismissNoteAvailable(BURY_NOTE) (Reviewer.java:630).')

e('S_REVIEWER', 'Reviewer$SuspendProvider.hasSubMenu', 'FRAMEWORK',
  'the Suspend item is shown or tapped, and the support library asks whether it has a dropdown',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:167-173, 587-589 (in-app call at 169)',
  note='INFERRED: same reason as the Bury edge (support-library ActionProvider, not in fw_src). hasSubMenu returns dismissNoteAvailable(SUSPEND_NOTE) (Reviewer.java:588).')

e('S_REVIEWER', 'Reviewer$BuryProvider.onCreateActionView', 'FRAMEWORK',
  'the Bury item is shown as an action-bar button (customButtonBury is 1 or 2)',
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:624-626; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1760; SRC com/ichi2/anki/Reviewer.java:237-246',
  note='INFERRED: the support library creates the action view. customButtonBury defaults to 0 (never shown as an action, AbstractFlashcardViewer.java:1760), so the route needs the preference set to 1 or 2. The method returns null (Reviewer.java:625).')

e('S_REVIEWER', 'Reviewer$SuspendProvider.onCreateActionView', 'FRAMEWORK',
  'the Suspend item is shown as an action-bar button (customButtonSuspend is 1 or 2)',
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:582-584; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1761; SRC com/ichi2/anki/Reviewer.java:237-246',
  note='INFERRED: same reason as the Bury edge. customButtonSuspend defaults to 0 (never shown as an action, AbstractFlashcardViewer.java:1761), so the route needs the preference set to 1 or 2.')

e('S_REVIEWER', 'Reviewer.onOptionsItemSelected', 'GUI',
  'the user taps an item in the Reviewer action bar or overflow menu',
  gui=['the user taps an item in the Reviewer action bar or overflow menu'],
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3440-3450; SRC com/ichi2/anki/Reviewer.java:125-127',
  note='Page edge; the destination is in batch 008. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). The default case calls AnkiActivity.onOptionsItemSelected (Reviewer.java:224).')

e('S_REVIEWER', 'Reviewer.onKeyUp', 'GUI',
  'the user releases a key while the Reviewer is on screen',
  gui=['the user releases a key while the Reviewer is on screen'],
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:2975; SRC com/ichi2/anki/Reviewer.java:331-333, 391',
  note='Page edge. The body acts only when the answer field exists and is not focused (Reviewer.java:333); other keys fall through to super (391). No ENV models keyboard input, so env is unset.')

e('S_REVIEWER', 'Reviewer$1.onTouch', 'GUI',
  'the user touches the whiteboard area while it is on screen',
  gui=['the user touches the whiteboard area while it is on screen'],
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:461-471',
  note='MISSING GATE MG24: the whiteboard is on per deck (MetaDB state, Reviewer.java:103 and 446). No STATE models it, so needs_state is unset. The listener is registered in createWhiteboard (Reviewer.java:461), which runs when the whiteboard is enabled (448).')

e('S_REVIEWER', 'Reviewer$BuryProvider.onPrepareSubMenu', 'GUI',
  'the user taps Bury in the Reviewer menu and the bury dropdown opens',
  gui=['the user taps Bury in the Reviewer menu and the bury dropdown opens'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:159-161, 630, 634-640',
  note='INFERRED: the support library calls onPrepareSubMenu after hasSubMenu returns true. MISSING GATE MG25: the dropdown needs a note with two or more cards (Reviewer.java:556 and 559-568). No STATE models the sibling count, so only STATE_NOTE is set.')

e('S_REVIEWER', 'Reviewer$BuryProvider.onMenuItemClick', 'GUI',
  'the user taps Bury card or Bury note in the bury dropdown',
  gui=['the user taps Bury card or Bury note in the bury dropdown'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:636-639, 643-654',
  note='Page edge. The entries are added and registered by onPrepareSubMenu (REGISTER edge below), and REGISTER is not followed for reachability, so this page edge carries the route. MISSING GATE MG25 as on the Bury onPrepareSubMenu edge.')

e('S_REVIEWER', 'Reviewer$SuspendProvider.onPrepareSubMenu', 'GUI',
  'the user taps Suspend in the Reviewer menu and the suspend dropdown opens',
  gui=['the user taps Suspend in the Reviewer menu and the suspend dropdown opens'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:167-169, 588, 592-598',
  note='INFERRED: the support library calls onPrepareSubMenu after hasSubMenu returns true. MISSING GATE MG25: the dropdown needs a note with two or more cards (Reviewer.java:556 and 559-564). No STATE models the sibling count, so only STATE_NOTE is set.')

e('S_REVIEWER', 'Reviewer$SuspendProvider.onMenuItemClick', 'GUI',
  'the user taps Suspend card or Suspend note in the suspend dropdown',
  gui=['the user taps Suspend card or Suspend note in the suspend dropdown'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:594-597, 601-612',
  note='Page edge. The entries are added and registered by onPrepareSubMenu (REGISTER edge below). MISSING GATE MG25 as on the Suspend onPrepareSubMenu edge.')

e('Reviewer$1.<init>', 'Reviewer$1.onTouch', 'REGISTER',
  'the whiteboard touch listener is set on the whiteboard view',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:461-471',
  note='Same convention as label_003.py line 93 (DeckPicker$1.<init> -> DeckPicker$1.onClick). Not followed for reachability.')

e('Reviewer$BuryProvider.onPrepareSubMenu', 'Reviewer$BuryProvider.onMenuItemClick', 'REGISTER',
  'each bury dropdown entry is given this provider as its click listener',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:636-639',
  note='Registration only (setOnMenuItemClickListener). Not followed for reachability; the GUI page edge above carries the route.')

e('Reviewer$SuspendProvider.onPrepareSubMenu', 'Reviewer$SuspendProvider.onMenuItemClick', 'REGISTER',
  'each suspend dropdown entry is given this provider as its click listener',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:594-597',
  note='Registration only (setOnMenuItemClickListener). Not followed for reachability; the GUI page edge above carries the route.')

# ---- part 009 (2026-10-28) ----

# AnkiDroid batch 009 (LABEL helper). CardBrowser part 1: 40 methods, all REACHABLE, so there are no UNREACHABLE entries.
# The rows and reasons are in graphs/AnkiDroid/parts/label_009.md.
#
# Route notes:
# - The entry S_DECKPICKER -> CardBrowser.<clinit> (INTENT) skips the DeckPicker.openCardBrowser node (batch 003).
# - DeckDropDownAdapter.getView belongs to another batch. The edge into it is written here because its source is in batch 009.
# - No env or needs_state gate is set. The card browser is opened from the deck picker with the collection loaded.
# - The closeCardBrowser(int) route (RESULT_DB_ERROR) always throws NullPointerException (bug finding; no MG number assigned).

e('S_DECKPICKER', 'CardBrowser.<clinit>', 'INTENT',
  'open the card browser from the deck picker',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1708-1713; FW-SRC core/java/android/app/Instrumentation.java:1170-1174',
  note='Entry edge into batch 009. It skips the DeckPicker.openCardBrowser node (batch 003), which has no INTENT edge into CardBrowser in its part.')

e('CardBrowser.<clinit>', 'CardBrowser.<init>', 'FRAMEWORK',
  'newInstance constructs the instance after the class is initialized',
  env=None,
  evidence='FW-SRC core/java/android/app/Instrumentation.java:1170-1174; SRC com/ichi2/anki/CardBrowser.java:121, 134-135',
  note='Java class initialization runs before the first constructor call (not cited).')

e('S_CARDBROWSER', 'CardBrowser.onOptionsItemSelected', 'GUI',
  'tap a menu item in the card browser action bar',
  gui=['tap a menu item in the card browser action bar'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:624-628',
  note='Page edge. lc_chain skips onOptionsItemSelected (graph_def.py LC_NO_TRIGGER), so this edge is the route in.')

e('CardBrowser.onCreate', 'CardBrowser.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu after onCreate (onCreatePanelMenu calls onCreateOptionsMenu)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388; SRC com/ichi2/anki/CardBrowser.java:572-573',
  note='Follows the label_002.py precedent (DeckPicker.onCreate -> onCreateOptionsMenu). The timing of the panel build is not modelled.')

e('CardBrowser.onCreate', 'CardBrowser.onCollectionLoaded', 'ASYNC',
  'the collection loader delivers onLoadFinished after startLoadingCollection',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:348; SRC com/ichi2/anki/AnkiActivity.java:255-262, 282-290',
  note='The loader is restarted in AnkiActivity.startLoadingCollection (261) and the result reaches onCollectionLoaded through AnkiActivity.onLoadFinished (286). The library delivery step is not in the tree.')

e('CardBrowser.onCollectionLoaded', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the spinner draws its rows with the adapter set in onCollectionLoaded',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:367, 373; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:90',
  note='Cross-batch: DeckDropDownAdapter.getView belongs to another batch. The getView -> getSubtitleText edge is automatic (CHA, DeckDropDownAdapter.java:90).')

e('S_CARDBROWSER', 'CardBrowser.onBackPressed', 'GUI',
  'press the back key with the navigation drawer closed',
  gui=['press the back key with the navigation drawer closed'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:548-561; FW-SRC core/java/android/app/Activity.java:3001',
  note='Page edge. The framework calls onBackPressed on the back key (not cited).')

e('S_CARDBROWSER', 'CardBrowser$10.onQueryTextChange', 'GUI',
  'type in the search view',
  gui=['type in the search view'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:597-602',
  note='Page edge. The SearchView dispatch is library behaviour (not cited).')

e('CardBrowser.onOptionsItemSelected', 'S_NOTEEDITOR', 'ENTERS',
  'the add-card menu item starts the note editor (ADD_NOTE)',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:630-634',
  note='ENTERS edge: method to page. The result returns through the RESULT edge S_NOTEEDITOR -> CardBrowser.onActivityResult.')

e('S_CARDBROWSER', 'CardBrowser$10.onQueryTextSubmit', 'GUI',
  'submit a query in the search view',
  gui=['submit a query in the search view'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:605-610',
  note='Page edge. The SearchView dispatch is library behaviour (not cited).')

e('S_CARDBROWSER', 'CardBrowser$11.onClick', 'GUI',
  'tap the search view (search click)',
  gui=['tap the search view (search click)'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:612-617',
  note='Page edge. The View click dispatch is library behaviour (not cited).')

e('S_DLG_CARDBROWSER_CONTEXT', 'CardBrowser$1.onSelection', 'GUI',
  'tap an item in the card context menu',
  gui=['tap an item in the card context menu'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:159-161; SRC com/ichi2/anki/dialogs/CardBrowserContextMenu.java:58-62',
  note='Page edge. The MaterialDialog list dispatch is library behaviour (not cited).')

e('S_NOTEEDITOR', 'CardBrowser.onActivityResult', 'RESULT',
  'the note editor returns to the card browser (ADD_NOTE or EDIT_CARD result, or RESULT_DB_ERROR)',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:686-693; SRC com/ichi2/anki/NoteEditor.java:271, 1021-1022',
  note='RESULT edge: page to method. The framework delivers the result (not cited). The RESULT_DB_ERROR branch leads to the closeCardBrowser NullPointerException (bug finding).')

e('S_DLG_CARDBROWSER_CONTEXT', 'CardBrowser$1$1.onClick', 'GUI',
  'tap DELETE in the context menu, then OK in the delete confirmation',
  gui=['tap DELETE in the context menu, then OK in the delete confirmation'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:185-197',
  note='Page edge. The delete confirmation is built in CardBrowser$1.onSelection (187-203). The MaterialDialog button dispatch is library behaviour (not cited).')

e('S_DLG_TAGS', 'CardBrowser$12.onPositive', 'GUI',
  'pick tags in the tag dialog and confirm',
  gui=['pick tags in the tag dialog and confirm'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:732-734; SRC com/ichi2/anki/dialogs/TagsDialog.java:162-167',
  note='Page edge. Also an automatic CHA CALL edge from TagsDialog$2.onPositive (TagsDialog.java:166).')

e('CardBrowser.onCreate', 'S_CARDBROWSER', 'ENTERS',
  'the card browser screen is shown after onCreate sets the content view',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:343-349',
  note='ENTERS edge: method to page.')

e('CardBrowser.showTagsDialog', 'S_DLG_TAGS', 'ENTERS',
  'showTagsDialog shows the TagsDialog fragment',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:729-731, 768',
  note='ENTERS edge: method to page.')

e('CardBrowser.onOptionsItemSelected', 'S_DLG_CARDBROWSER_SEARCHES', 'ENTERS',
  'the save-search and list-my-searches items show CardBrowserMySearchesDialog',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:636-640, 642-654',
  note='ENTERS edge: method to page.')

e('CardBrowser.onOptionsItemSelected', 'S_DLG_CARDBROWSER_ORDER', 'ENTERS',
  'the sort item shows CardBrowserOrderDialog',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:655-658',
  note='ENTERS edge: method to page.')

e('CardBrowser.closeCardBrowser(int,Intent)', 'CardBrowser.onDestroy', 'FRAMEWORK',
  'finishWithAnimation leads the framework to destroy the activity',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1124-1134; SRC com/ichi2/anki/AnkiActivity.java:206-209; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='Follows the label_002.py precedent (finishWithAnimation -> onDestroy). Only the non-null Intent route (back key) reaches it; the closeCardBrowser(int) route throws first (bug finding).')

# ---- part 010 (2026-10-28)
# AnkiDroid batch 010 (LABEL helper). CardBrowser anonymous listeners and callbacks: $2, $3, $4, $5,
# $13 to $17 (DeckTask TaskListeners) and $18 (runtime BroadcastReceiver). 40 methods; the full row list is in
# graphs/AnkiDroid/parts/label_010.md.
#
# Route ownership: CardBrowser.<init>, onCollectionLoaded, onActivityResult, searchCards, onStop, onDestroy,
# registerExternalStorageListener and the context-menu listener CardBrowser$1.onSelection belong to batch_009.
# CardBrowser$7.onItemClick, RenderOnScroll.onScroll, onScrollStateChanged and CardBrowser$6 belong to batch_011.
# SdCardReceiver (the manifest receiver) belongs to batch_017. The ASYNC edges from those launchers to the
# DeckTask callbacks here are NOT written in this part; the launcher's part writes them. Those callbacks are
# REACHABLE rows in the .md with "confirmed_by INFERRED" in the reason.
# CardBrowser$6 has no method in this batch (batch_011 owns its two callbacks).
# REGISTER edges from an <init> are written here with a note: the builder does not follow REGISTER for
# reachability, so the route is the GUI or FRAMEWORK edge from the page or the framework node.
# The saved-search dialog edges carry needs_state=STATE_SETTINGS: saved searches live in col.conf 'savedFilters'
# and there is no saved-search STATE kind (MG note).

# --- sort-order dialog listener ($2). Set in CardBrowserOrderDialog.newInstance (CardBrowser.java:657).
e('CardBrowser$2.<init>', 'CardBrowser$2.onSelection', 'REGISTER',
  'the sort-order listener is passed to the order dialog and stored in its static field',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:216-217, 657; SRC com/ichi2/anki/dialogs/CardBrowserOrderDialog.java:15, 24, 50',
  note='onSelection is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_CARDBROWSER_ORDER -> CardBrowser$2.onSelection GUI edge below.')

e('S_DLG_CARDBROWSER_ORDER', 'CardBrowser$2.onSelection', 'GUI',
  'open the sort dialog from the card browser menu, then tap a sort order',
  gui=['open the sort dialog from the card browser menu, then tap a sort order'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:655-658, 219-254; SRC com/ichi2/anki/dialogs/CardBrowserOrderDialog.java:50',
  note='Page edge; the destination is in this part. The MaterialDialog callback dispatch is library code not in the dataset: INFERRED. No env or needs_state gate.')

# --- saved-searches dialog listener ($3). Set in CardBrowserMySearchesDialog.newInstance (CardBrowser.java:638, 652).
e('CardBrowser$3.<init>', 'CardBrowser$3.OnSelection', 'REGISTER',
  'the saved-searches listener is passed to the dialog and stored in its static field',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:259-260, 638, 652; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:37, 46',
  note='OnSelection is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_CARDBROWSER_SEARCHES -> CardBrowser$3.OnSelection GUI edge below.')

e('CardBrowser$3.<init>', 'CardBrowser$3.OnRemoveSearch', 'REGISTER',
  'the saved-searches listener is passed to the dialog and stored in its static field',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:259-260, 638, 652; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:37, 46',
  note='OnRemoveSearch is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_CARDBROWSER_SEARCHES -> CardBrowser$3.OnRemoveSearch GUI edge below.')

e('CardBrowser$3.<init>', 'CardBrowser$3.OnSaveSearch', 'REGISTER',
  'the saved-searches listener is passed to the dialog and stored in its static field',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:259-260, 638, 652; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:37, 46',
  note='OnSaveSearch is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_CARDBROWSER_SEARCHES -> CardBrowser$3.OnSaveSearch GUI edge below.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowser$3.OnSelection', 'GUI',
  'open My searches from the card browser menu, then tap a saved search',
  gui=['open My searches from the card browser menu, then tap a saved search'],
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:642-654, 262-270; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:73',
  note='Page edge. Needs at least one saved search in col.conf savedFilters (CardBrowser.java:263), modelled as STATE_SETTINGS (MG note). The dialog item click is library-backed: INFERRED.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowser$3.OnRemoveSearch', 'GUI',
  'open My searches from the card browser menu, tap the remove button of a saved search, then OK',
  gui=['open My searches from the card browser menu, tap the remove button of a saved search, then OK'],
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:109-112, 161-166; SRC com/ichi2/anki/CardBrowser.java:273-288',
  note='Page edge. Needs at least one saved search (STATE_SETTINGS, MG note). The confirm callback is library-backed: INFERRED.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowser$3.OnSaveSearch', 'GUI',
  'open the save-search dialog from the card browser menu, enter a name, then save',
  gui=['open the save-search dialog from the card browser menu, enter a name, then save'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:636-640, 291-296; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:85',
  note='Page edge. No gate: the empty-name case returns at CardBrowser.java:292-296 and the non-empty name reaches the method. The dialog callback is library-backed: INFERRED.')

# --- toolbar deck spinner ($4). Created in onCollectionLoaded (CardBrowser.java:373-374).
e('CardBrowser$4.<init>', 'CardBrowser$4.onItemSelected', 'REGISTER',
  'the toolbar spinner listener is registered on the deck spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:373-374',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the routes are the S_CARDBROWSER edges below.')

e('CardBrowser$4.<init>', 'CardBrowser$4.onNothingSelected', 'REGISTER',
  'the toolbar spinner listener is registered on the deck spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:373-374',
  note='onNothingSelected is in this part (UNREACHABLE below). The builder does not follow REGISTER for reachability.')

e('S_CARDBROWSER', 'CardBrowser$4.onItemSelected', 'FRAMEWORK',
  'the card browser opens: the framework lays out the deck spinner and selects position 0 (the default deck), which fires onItemSelected',
  env=None,
  evidence='FW-SRC core/java/android/widget/AdapterView.java:1034-1085, 937-947, 1103-1110; FW-SRC core/java/android/widget/Spinner.java:637-648, 681; SRC com/ichi2/anki/CardBrowser.java:373-378',
  note='Page edge. The default selection (position 0 after setAdapter) is set in AbsSpinner, which is not in fw_src: INFERRED for that step. The GUI edge below is the alternative route.')

e('S_CARDBROWSER', 'CardBrowser$4.onItemSelected', 'GUI',
  'pick another deck in the toolbar drop-down of the card browser',
  gui=['pick another deck in the toolbar drop-down of the card browser'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:376-378, 772-792; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:19',
  note='Page edge. Needs two or more decks in the drop-down (no STATE kind written: the default deck always exists, see the UNREACHABLE note on onNothingSelected).')

# --- first-column spinner ($5). Created in onCollectionLoaded (CardBrowser.java:415-417).
e('CardBrowser$5.<init>', 'CardBrowser$5.onItemSelected', 'REGISTER',
  'the first-column spinner listener is registered on the column spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:415-417',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the routes are the S_CARDBROWSER edges below.')

e('CardBrowser$5.<init>', 'CardBrowser$5.onNothingSelected', 'REGISTER',
  'the first-column spinner listener is registered on the column spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:415-417',
  note='onNothingSelected is in this part (UNREACHABLE below). The builder does not follow REGISTER for reachability.')

e('S_CARDBROWSER', 'CardBrowser$5.onItemSelected', 'FRAMEWORK',
  'the card browser opens: the framework lays out the first-column spinner and selects position 0, which fires onItemSelected (the body changes nothing when the position is unchanged)',
  env=None,
  evidence='FW-SRC core/java/android/widget/AdapterView.java:1034-1085, 937-947, 1103-1110; FW-SRC core/java/android/widget/Spinner.java:637-648, 681; SRC com/ichi2/anki/CardBrowser.java:419-427',
  note='Page edge. The default selection is set in AbsSpinner, which is not in fw_src: INFERRED for that step. The GUI edge below is the alternative route.')

e('S_CARDBROWSER', 'CardBrowser$5.onItemSelected', 'GUI',
  'pick another first column in the card browser column spinner',
  gui=['pick another first column in the card browser column spinner'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:419-427; SRC res/layout/card_browser.xml:25-30',
  note='Page edge. The spinner has no visibility gate in the layout (card_browser.xml:25-30).')

# --- SD-card receiver ($18). Registered in registerExternalStorageListener (CardBrowser.java:1320-1330).
e('CardBrowser$18.<init>', 'CardBrowser$18.onReceive', 'REGISTER',
  'the MEDIA_EJECT receiver is registered while the card browser is open',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1318-1330',
  note='onReceive is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$18.onReceive SYSTEM edge below.')

e('S_CARDBROWSER', 'CardBrowser$18.onReceive', 'SYSTEM',
  'the SD card is ejected while the card browser is open (ACTION_MEDIA_EJECT, delivered to SdCardReceiver, which re-broadcasts MEDIA_EJECT)',
  env=ENV_SDCARD_EVENT,
  evidence='SRC AndroidManifest.xml:268-282; SRC com/ichi2/anki/receiver/SdCardReceiver.java:42-47; SRC com/ichi2/anki/CardBrowser.java:1322-1326; FW-SRC core/java/android/content/Intent.java:2701',
  note='Page edge; the destination is in this part. The first hop (system delivery of ACTION_MEDIA_EJECT to a manifest receiver on API 27) is not verifiable from fw_src: INFERRED. SdCardReceiver is batch_017; the edge is written here, not in that part.')

# --- UNREACHABLE entries.
UNREACHABLE['CardBrowser$13.onCancelled'] = (
    'no_trigger_in_app',
    "The update-note task (TASK_TYPE_UPDATE_FACT) is never cancelled. DeckTask.cancelTask(int) cancels only when the type matches (DeckTask.java:181-186), and its only callers are CardBrowser SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). The no-argument DeckTask.cancelTask() (DeckTask.java:168-178) is reached only from cancelTask(int) (DeckTask.java:184). The only direct cancel(true) on a DeckTask is sLatestInstance inside cancelTask() (DeckTask.java:172); TaskOperations.stopTaskGracefully cancels only the activities' own BackgroundPost and DownloadFileTask fields (LoadPronounciationActivity.java:474-478, TranslationActivity.java:405). AsyncTask runs onCancelled only after cancel() (AsyncTask.java:525-528, 691-698). Body is empty (CardBrowser.java:924-925).",
    'SRC com/ichi2/async/DeckTask.java:168-186; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 924-925, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-35; SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405; FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698',
    'SOURCE')

UNREACHABLE['CardBrowser$14.onCancelled'] = (
    'no_trigger_in_app',
    "The suspend task (TASK_TYPE_DISMISS, suspend) is never cancelled. The reasons are the same as for CardBrowser$13.onCancelled: DeckTask.cancelTask(int) has only the SEARCH_CARDS and RENDER_BROWSER_QA callers (CardBrowser.java:528-529, 796-797, 1155), and the no-argument cancelTask() is reached only from cancelTask(int) (DeckTask.java:184). Body is empty (CardBrowser.java:1024-1025).",
    'SRC com/ichi2/async/DeckTask.java:168-186; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1024-1025, 1155; FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698',
    'SOURCE')

UNREACHABLE['CardBrowser$15.onCancelled'] = (
    'no_trigger_in_app',
    "The delete-note task (TASK_TYPE_DISMISS, delete) is never cancelled. The reasons are the same as for CardBrowser$13.onCancelled: DeckTask.cancelTask(int) has only the SEARCH_CARDS and RENDER_BROWSER_QA callers (CardBrowser.java:528-529, 796-797, 1155), and the no-argument cancelTask() is reached only from cancelTask(int) (DeckTask.java:184). Body is empty (CardBrowser.java:1047-1048).",
    'SRC com/ichi2/async/DeckTask.java:168-186; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1047-1048, 1155; FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698',
    'SOURCE')

UNREACHABLE['CardBrowser$4.onNothingSelected'] = (
    'framework_never_calls',
    "The toolbar deck spinner is filled from the deck list (DeckDropDownAdapter over mDropDownDecks = allSorted(), CardBrowser.java:366-373). AdapterView fires onNothingSelected only when the selected position is negative (fireOnSelected, AdapterView.java:937-947), and handleDataChanged leaves nothing selected only when the adapter has no selectable item (AdapterView.java:1038, 1057-1085). The deck list is never empty because the default deck (id 1) cannot be deleted (Decks.java:285-287), so the adapter always has a selectable item (DeckDropDownAdapter.java:19, BaseAdapter.java:68). The claim that the default deck always exists in the collection is INFERRED. Body is '// do nothing' (CardBrowser.java:381-383).",
    'SRC com/ichi2/anki/CardBrowser.java:366-373, 381-383; SRC com/ichi2/libanki/Decks.java:285-287; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:19; FW-SRC core/java/android/widget/AdapterView.java:937-947, 1038, 1057-1085; FW-SRC core/java/android/widget/BaseAdapter.java:68',
    'INFERRED')

UNREACHABLE['CardBrowser$5.onNothingSelected'] = (
    'framework_never_calls',
    "The first-column spinner is filled from ArrayAdapter.createFromResource over R.array.browser_column1_headings (CardBrowser.java:412-415), a static array of two items (res/values/02-strings.xml:56-59). The array is never empty and its items are enabled (ArrayAdapter has no isEnabled override; BaseAdapter.isEnabled defaults to true, BaseAdapter.java:68), so handleDataChanged always finds a selectable position (AdapterView.java:1038, 1057-1085) and fireOnSelected never receives a negative position (AdapterView.java:937-947). Body is '// Do Nothing' (CardBrowser.java:432-434).",
    'SRC com/ichi2/anki/CardBrowser.java:412-415, 432-434; SRC res/values/02-strings.xml:56-59; FW-SRC core/java/android/widget/ArrayAdapter.java:73, 506; FW-SRC core/java/android/widget/BaseAdapter.java:68; FW-SRC core/java/android/widget/AdapterView.java:937-947, 1038, 1057-1085',
    'SOURCE')

# DeckTask dispatch to CardBrowser onCancelled listeners that are never cancelled (see handoff decisions 2026-10-28)
sup(('DeckTask.onCancelled', 'CardBrowser$13.onCancelled'),
    ('DeckTask.onCancelled', 'CardBrowser$14.onCancelled'),
    ('DeckTask.onCancelled', 'CardBrowser$15.onCancelled'))

# ---- part 014 (2026-10-28)
# AnkiDroid batch 014 (LABEL helper). NoteEditor note type listeners and the JSON name comparator:
# NoteEditor$SetNoteTypeListener (add mode), NoteEditor$EditNoteTypeListener (edit mode) and
# NoteEditor$JSONNameComparator. 8 methods; the full row list is in graphs/AnkiDroid/parts/label_014.md.
#
# Route ownership: NoteEditor.onCollectionLoaded (NoteEditor.java:331) belongs to batch_012. Its CALL edges to the
# three <init> methods come from auto_calls.json (NoteEditor.java:453, 500, 521) and are not written here.
# The edge NoteEditor.onCollectionLoaded -> NoteEditor$JSONNameComparator.compare (via java.util.Collections.sort,
# which is not in the dataset) is NOT written here; the part that holds onCollectionLoaded (batch_012) writes it.
# The edit-mode entries into NoteEditor.<init> are batch_011 (CardBrowser$7.onItemClick) and batch_019
# (AbstractFlashcardViewer.editCard); they are not written here.
# REGISTER edges from an <init> are written here with a note: the builder does not follow REGISTER for reachability,
# so the route is the S_NOTEEDITOR FRAMEWORK or GUI edge below.
# Gates: MG85 (add mode), MG86 (two or more note types or entries), MG87 (edit mode). env and needs_state are unset
# on the MG edges.

# --- SetNoteTypeListener (add mode). Set in onCollectionLoaded inside the mAddNote branch (NoteEditor.java:499-500).
e('NoteEditor$SetNoteTypeListener.<init>', 'NoteEditor$SetNoteTypeListener.onItemSelected', 'REGISTER',
  'the add-mode note type listener is set on the note type spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:499-500',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR FRAMEWORK edge below.')

e('NoteEditor$SetNoteTypeListener.<init>', 'NoteEditor$SetNoteTypeListener.onNothingSelected', 'REGISTER',
  'the add-mode note type listener is set on the note type spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:499-500',
  note='onNothingSelected is in this part (UNREACHABLE below). The builder does not follow REGISTER for reachability.')

e('S_NOTEEDITOR', 'NoteEditor$SetNoteTypeListener.onItemSelected', 'FRAMEWORK',
  'the add-mode note editor opens: the framework lays out the note type spinner and fires onItemSelected for the selected note type',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:364-384, 434, 497-500; FW-SRC core/java/android/widget/Spinner.java:619-623, 681; FW-SRC core/java/android/widget/AdapterView.java:194, 204, 903-930, 932-935, 937-949, 1103-1108',
  note='MISSING GATE MG85: the note editor is in add mode (mAddNote is true; callers STUDYOPTIONS, DECKPICKER, REVIEWER_ADD, CARDBROWSER_ADD, CARDEDITOR and CARDEDITOR_INTENT_ADD, NoteEditor.java:380-415). No predefined ENV or STATE kind covers the caller mode. env and needs_state unset.')

e('S_NOTEEDITOR', 'NoteEditor$SetNoteTypeListener.onItemSelected', 'GUI',
  'pick another note type in the note type drop-down of the add-mode note editor',
  gui=['pick another note type in the note type drop-down of the add-mode note editor'],
  evidence='SRC com/ichi2/anki/NoteEditor.java:497-500, 1542-1554; FW-SRC core/java/android/widget/Spinner.java:1183-1190',
  note='MISSING GATE MG86: needs two or more note types in the collection (a pick that changes the selection needs a second item). Also the add-mode gate MG85 (see the FRAMEWORK edge above). env and needs_state unset.')

# --- EditNoteTypeListener (edit mode). Set in onCollectionLoaded in the else branch (NoteEditor.java:520-521).
e('NoteEditor$EditNoteTypeListener.<init>', 'NoteEditor$EditNoteTypeListener.onItemSelected', 'REGISTER',
  'the edit-mode note type listener is set on the note type spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:520-521',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR FRAMEWORK edge below.')

e('NoteEditor$EditNoteTypeListener.<init>', 'NoteEditor$EditNoteTypeListener.onNothingSelected', 'REGISTER',
  'the edit-mode note type listener is set on the note type spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:520-521',
  note='onNothingSelected is in this part (UNREACHABLE below). The builder does not follow REGISTER for reachability.')

e('S_NOTEEDITOR', 'NoteEditor$EditNoteTypeListener.onItemSelected', 'FRAMEWORK',
  'the edit-mode note editor opens for an existing note: the framework lays out the note type spinner and fires onItemSelected for the note type of that note',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:370-394, 434, 497, 520-521, 1592-1594; FW-SRC core/java/android/widget/Spinner.java:619-623, 681; FW-SRC core/java/android/widget/AdapterView.java:194, 204, 903-930, 932-935, 937-949, 1103-1108',
  note='MISSING GATE MG87: the note editor is in edit mode (mAddNote is false; callers REVIEWER and CARDBROWSER_EDIT, NoteEditor.java:370-378 and 386-394). No predefined ENV or STATE kind covers the caller mode, and the open card is also required (the editor finishes when it is missing, NoteEditor.java:372-374 and 388-390), which no predefined STATE covers. env and needs_state unset.')

e('S_NOTEEDITOR', 'NoteEditor$EditNoteTypeListener.onItemSelected', 'GUI',
  'pick another note type in the note type drop-down of the edit-mode note editor',
  gui=['pick another note type in the note type drop-down of the edit-mode note editor'],
  evidence='SRC com/ichi2/anki/NoteEditor.java:520-521, 1592-1605; FW-SRC core/java/android/widget/Spinner.java:1183-1190',
  note='MISSING GATE MG86: needs two or more note types in the collection (a pick that changes the selection needs a second item). Also the edit-mode gate MG87 (see the FRAMEWORK edge above). env and needs_state unset.')

# --- onNothingSelected of both listeners (body '// Do Nothing').
UNREACHABLE['NoteEditor$SetNoteTypeListener.onNothingSelected'] = (
    'framework_never_calls',
    "The note type spinner gets its adapter once (NoteEditor.java:434) and its selection once (NoteEditor.java:497); the only other read is getSelectedItemPosition (NoteEditor.java:1447). AdapterView calls onNothingSelected only when the selected position is negative at a dispatch (fireOnSelected, AdapterView.java:937-949). A dispatch runs only when the selection changed (checkSelectionChanged, AdapterView.java:1103-1108). The selection starts at INVALID_POSITION (AdapterView.java:194, 204), so an empty adapter gives no dispatch (Spinner.java:637-645, and handleDataChanged leaves INVALID_POSITION equal to the old value at AdapterView.java:1086-1094). A non-empty adapter always gets a selectable position (handleDataChanged, AdapterView.java:1043-1085), so the position is never negative at a dispatch. The body is '// Do Nothing' (NoteEditor.java:1585-1588). The AbsSpinner setAdapter and setSelection steps are not in fw_src, so this is INFERRED.",
    'SRC com/ichi2/anki/NoteEditor.java:434, 497, 1447, 1585-1588; FW-SRC core/java/android/widget/AdapterView.java:194, 204, 937-949, 1043-1085, 1086-1094, 1103-1108; FW-SRC core/java/android/widget/Spinner.java:637-645',
    'INFERRED')

UNREACHABLE['NoteEditor$EditNoteTypeListener.onNothingSelected'] = (
    'framework_never_calls',
    "The same spinner serves edit mode: the adapter is set once (NoteEditor.java:434), the selection is set once (NoteEditor.java:497), the edit-mode listener is attached in the else branch (NoteEditor.java:520-521), and the only other read is getSelectedItemPosition (NoteEditor.java:1447). The framework argument is the same as for the add-mode listener: onNothingSelected needs a negative selected position at a dispatch (AdapterView.java:937-949), and a dispatch needs a change of the selection (AdapterView.java:1103-1108). An empty adapter leaves the selection at INVALID_POSITION with no change (AdapterView.java:194, 204, 1086-1094; Spinner.java:637-645), and a non-empty adapter always gets a selectable position (AdapterView.java:1043-1085). The body is '// Do Nothing' (NoteEditor.java:1645-1648). The AbsSpinner setAdapter and setSelection steps are not in fw_src, so this is INFERRED.",
    'SRC com/ichi2/anki/NoteEditor.java:434, 497, 520-521, 1447, 1645-1648; FW-SRC core/java/android/widget/AdapterView.java:194, 204, 937-949, 1043-1085, 1086-1094, 1103-1108; FW-SRC core/java/android/widget/Spinner.java:637-645',
    'INFERRED')

# ---- part 011 (2026-10-28)
# AnkiDroid batch 011 (LABEL helper). CardBrowser part 3: the second-column spinner listener CardBrowser$6, the card-row
# click and long-click listeners CardBrowser$7 and $8, the search expand/collapse listener CardBrowser$9, the list adapter
# CardBrowser$MultiColumnListAdapter and the scroll listener CardBrowser$RenderOnScroll. 22 methods; the full row list is
# in graphs/AnkiDroid/parts/label_011.md.
#
# Ownership: an edge is written in the part that holds its source method. Written here: the REGISTER edges from the
# <init>s of $7, $8, $9 and RenderOnScroll; the page edges into the batch-011 methods (GUI, FRAMEWORK); INTENT and ENTERS
# from CardBrowser$7.onItemClick; ENTERS from CardBrowser$8.onItemLongClick; ASYNC from RenderOnScroll.onScroll and
# onScrollStateChanged to the CardBrowser$17 callbacks (those callbacks are batch 010 rows and are not labelled here).
# Not written here: CardBrowser$6.<init> (listed in batch_010.txt, not in batch_011; see the report); the auto CALL edges
# from CardBrowser.onCollectionLoaded to the <init>s and from CardBrowser.onCreateOptionsMenu to $9.<init> (batch 009
# methods); the auto CALL edges inside the adapter and from the scroll listeners to DeckTask (auto_calls.json); the
# NoteEditor.<init> label (NoteEditor batch); the CardBrowser$17 callbacks (batch 010); the cancelTask calls in
# CardBrowser.onStop and onDestroy (batch 009).
#
# UNREACHABLE entries: CardBrowser$6.onNothingSelected (framework_never_calls) and
# CardBrowser$MultiColumnListAdapter.getItem (no_trigger_in_app). Constants: none.
# Missing gates are text only, in note= (MG55 to MG57); env and needs_state are not set on those edges.

# ---- CardBrowser$6: second-column spinner (set up in CardBrowser.onCollectionLoaded, CardBrowser.java:439-462) ----

e('S_CARDBROWSER', 'CardBrowser$6.onItemSelected', 'FRAMEWORK',
  'the card browser opens: the framework lays out the second-column spinner and selects position 0, which fires onItemSelected',
  env=None,
  evidence='FW-SRC core/java/android/widget/AdapterView.java:1034-1085, 937-947, 1103-1110; FW-SRC core/java/android/widget/Spinner.java:637-648, 681; SRC com/ichi2/anki/CardBrowser.java:437-457, 482',
  note='Page edge. The default selection (position 0) is set in AbsSpinner, which is not in fw_src: INFERRED for that step. The listener is attached after setAdapter (CardBrowser.java:443, 445). The saved index is read at line 437 and applied with setSelection at line 482, after the listener is attached and before the first layout, so the first callback should report the saved index and not overwrite it (not tested). The GUI edge below is the other route.')

e('S_CARDBROWSER', 'CardBrowser$6.onItemSelected', 'GUI',
  'pick another second column in the card browser column spinner',
  gui=['pick another second column in the card browser column spinner'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:445-457; SRC res/layout/card_browser.xml:32-37',
  note='Page edge. The spinner has no visibility gate: the layout sets none (card_browser.xml:32-37) and the code looks the spinner up only at CardBrowser.java:439.')

UNREACHABLE['CardBrowser$6.onNothingSelected'] = (
    'framework_never_calls',
    "The second-column spinner is filled from ArrayAdapter.createFromResource over R.array.browser_column2_headings (CardBrowser.java:440-443), a static array of six items (res/values/02-strings.xml:60-66). ArrayAdapter does not override isEnabled, so BaseAdapter.isEnabled (BaseAdapter.java:68) makes every item selectable. AdapterView.handleDataChanged pins the position into range and selects a selectable one (AdapterView.java:1040-1085), so the selection is not cleared while the six items stay. fireOnSelected calls onNothingSelected only for a negative selection (AdapterView.java:937-947). Not read: AbsSpinner (not in fw_src), and the other places that set the selection to INVALID_POSITION (not searched), so confirmed_by is INFERRED. Body is '// Do Nothing' (CardBrowser.java:460-462). Same reasoning as CardBrowser$5.onNothingSelected in label_010.py.",
    'SRC com/ichi2/anki/CardBrowser.java:440-443, 460-462; SRC res/values/02-strings.xml:60-66; FW-SRC core/java/android/widget/ArrayAdapter.java:73, 506; FW-SRC core/java/android/widget/BaseAdapter.java:68; FW-SRC core/java/android/widget/AdapterView.java:937-947, 1040-1085',
    'INFERRED')

UNREACHABLE['CardBrowser$MultiColumnListAdapter.getItem'] = (
    'no_trigger_in_app',
    "The card list gets its row data through getView and bindView, which read the card list directly, not through getItem. The framework reaches ListAdapter.getItem only from AdapterView.getSelectedItem (AdapterView.java:590-594) and AdapterView.getItemAtPosition (AdapterView.java:796-798). A search of the widget and view packages of fw_src finds no caller of either method (only their definitions), and CardBrowser.java has no call to getItem on this adapter (the only getItem( in the file is the definition at line 1295). No code in the app or the framework asks this list for an item, so no route reaches the method.",
    'SRC com/ichi2/anki/CardBrowser.java:477, 1295-1297; FW-SRC core/java/android/widget/AdapterView.java:590-594, 796-798',
    'SOURCE')

# ---- CardBrowser$7: card-row click (listener set in CardBrowser.onCollectionLoaded, CardBrowser.java:485-497) ----

e('CardBrowser$7.<init>', 'CardBrowser$7.onItemClick', 'REGISTER',
  'the card-row click listener is set on the card list',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:485-486',
  note='onItemClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$7.onItemClick GUI edge below. The <init> is called from CardBrowser.onCollectionLoaded (auto CALL, CardBrowser.java:485).')

e('S_CARDBROWSER', 'CardBrowser$7.onItemClick', 'GUI',
  'tap a card row in the card browser list',
  gui=['tap a card row in the card browser list'],
  needs_state=STATE_CARDS,
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:408, 485-497; FW-SRC core/java/android/widget/AdapterView.java:314-318',
  note='Page edge. The list needs at least one row (STATE_CARDS). The framework calls the listener from AdapterView.performItemClick (line 318).')

e('CardBrowser$7.onItemClick', 'NoteEditor.<init>', 'INTENT',
  'start the note editor for the tapped card: explicit Intent to NoteEditor with the caller and the card id as extras',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:493-496',
  note='INTENT edge (explicit component, app to app; no framework gate). NoteEditor.<init> is labelled in the NoteEditor batch. The result returns through the RESULT edge S_NOTEEDITOR -> CardBrowser.onActivityResult (graph_def.py:1566).')

e('CardBrowser$7.onItemClick', 'S_NOTEEDITOR', 'ENTERS',
  'the note editor screen is shown for the tapped card',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:493-496',
  note='ENTERS edge: method to page, the same pattern as CardBrowser.onOptionsItemSelected -> S_NOTEEDITOR (graph_def.py:1539).')

# ---- CardBrowser$8: card-row long-click (listener set in CardBrowser.onCollectionLoaded, CardBrowser.java:499-512) ----

e('CardBrowser$8.<init>', 'CardBrowser$8.onItemLongClick', 'REGISTER',
  'the card-row long-click listener is set on the card list',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:499-500',
  note='onItemLongClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$8.onItemLongClick GUI edge below. The <init> is called from CardBrowser.onCollectionLoaded (auto CALL, CardBrowser.java:499).')

e('S_CARDBROWSER', 'CardBrowser$8.onItemLongClick', 'GUI',
  'long-press a card row in the card browser list',
  gui=['long-press a card row in the card browser list'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:499-511, 1087-1091; FW-SRC core/java/android/widget/AbsListView.java:3223-3237',
  note='Page edge. MISSING GATE MG55: the Q&A render task of the card list (DeckTask.TASK_TYPE_RENDER_BROWSER_QA) is said to block the long-click callback while it runs (comment at CardBrowser.java:1088-1089); no gate kind expresses a running background task. A row must exist.')

e('CardBrowser$8.onItemLongClick', 'S_DLG_CARDBROWSER_CONTEXT', 'ENTERS',
  'the card menu dialog is shown for the long-pressed card',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:501-511',
  note='ENTERS edge: method to page. The dialog listener CardBrowser$1.onSelection is batch 009 (its GUI edge is graph_def.py:1559).')

# ---- CardBrowser$9: search expand and collapse (listener set in CardBrowser.onCreateOptionsMenu, CardBrowser.java:579-594) ----

e('CardBrowser$9.<init>', 'CardBrowser$9.onMenuItemActionExpand', 'REGISTER',
  'the search expand and collapse listener is set on the search menu item',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:579-580',
  note='onMenuItemActionExpand is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$9.onMenuItemActionExpand GUI edge below. The <init> is called from CardBrowser.onCreateOptionsMenu (auto CALL, CardBrowser.java:580; batch 009).')

e('CardBrowser$9.<init>', 'CardBrowser$9.onMenuItemActionCollapse', 'REGISTER',
  'the search expand and collapse listener is set on the search menu item',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:579-580',
  note='onMenuItemActionCollapse is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$9.onMenuItemActionCollapse GUI edge below. The <init> is called from CardBrowser.onCreateOptionsMenu (auto CALL, CardBrowser.java:580; batch 009).')

e('S_CARDBROWSER', 'CardBrowser$9.onMenuItemActionExpand', 'GUI',
  'tap the search icon in the card browser action bar (the search view expands)',
  gui=['tap the search icon in the card browser action bar (the search view expands)'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:579-584; SRC res/menu/card_browser.xml:9-14; FW-SRC core/java/com/android/internal/view/menu/MenuItemImpl.java:749-758',
  note='Page edge. MenuItemImpl.expandActionView calls the listener (lines 754-755) before it expands the view. The step from the tap to expandActionView is INFERRED (the ActionBar and support-library code is not in the dataset).')

e('S_CARDBROWSER', 'CardBrowser$9.onMenuItemActionCollapse', 'GUI',
  'close the expanded search view of the card browser (the search view collapses)',
  gui=['close the expanded search view of the card browser (the search view collapses)'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:587-594; FW-SRC core/java/com/android/internal/view/menu/MenuItemImpl.java:763-773',
  note='Page edge. MenuItemImpl.collapseActionView calls the listener (lines 772-773). Which control calls collapseActionView (the SearchView close control in the support library) is INFERRED. The listener calls searchCards (auto CALL, CardBrowser.java:592; batch 009).')

# ---- CardBrowser$RenderOnScroll: scroll listener (set in CardBrowser.onCollectionLoaded, CardBrowser.java:479) ----

e('CardBrowser$RenderOnScroll.<init>', 'CardBrowser$RenderOnScroll.onScroll', 'REGISTER',
  'the render-on-scroll listener is set on the card list',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:479',
  note='onScroll is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$RenderOnScroll.onScroll GUI edge below. The <init> is called from CardBrowser.onCollectionLoaded (auto CALL, CardBrowser.java:479).')

e('CardBrowser$RenderOnScroll.<init>', 'CardBrowser$RenderOnScroll.onScrollStateChanged', 'REGISTER',
  'the render-on-scroll listener is set on the card list',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:479',
  note='onScrollStateChanged is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$RenderOnScroll.onScrollStateChanged GUI edge below. The <init> is called from CardBrowser.onCollectionLoaded (auto CALL, CardBrowser.java:479).')

e('S_CARDBROWSER', 'CardBrowser$RenderOnScroll.onScroll', 'GUI',
  'scroll the card list: rows whose question and answer are not rendered yet get them rendered',
  gui=['scroll the card list: rows whose question and answer are not rendered yet get them rendered'],
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:1471-1477; SRC com/ichi2/anki/CardBrowser.java:1141-1161',
  note='Page edge. MISSING GATE MG56: the render branch needs a visible row whose answer is empty and a list longer than its last visible row (CardBrowser.java:1145-1149; a data state with no kind). MISSING GATE MG57: the render starts only when 300 ms have passed since the last render, or the last visible row is the last row (CardBrowser.java:1153; timing, no kind).')

e('S_CARDBROWSER', 'CardBrowser$RenderOnScroll.onScrollStateChanged', 'GUI',
  'scroll the card list and let it come to rest (the scroll state becomes idle)',
  gui=['scroll the card list and let it come to rest (the scroll state becomes idle)'],
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:4548-4555; SRC com/ichi2/anki/CardBrowser.java:1164-1173',
  note='Page edge. The framework reports the idle state through AbsListView.reportScrollStateChange (4548-4555) when a drag or fling ends. Only SCROLL_STATE_IDLE (CardBrowser.java:1167) starts a render; there is no other gate.')

# ASYNC edges from the two launchers to the CardBrowser$17 callbacks (batch 010 rows).

e('CardBrowser$RenderOnScroll.onScroll', 'CardBrowser$17.onPreExecute', 'ASYNC',
  'the render task starts on the UI thread: DeckTask.launchDeckTask executes it',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1155-1157, 1095-1098; SRC com/ichi2/async/DeckTask.java:129-134, 344-346',
  note='Launch at CardBrowser.java:1156-1157, reached only when MG56 and MG57 hold. The target callback is a batch 010 row (CardBrowser$17.onPreExecute).')

e('CardBrowser$RenderOnScroll.onScroll', 'CardBrowser$17.onProgressUpdate', 'ASYNC',
  'a card is rendered and the progress update reaches the render listener, which redraws the list',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:654-660, 352-354; SRC com/ichi2/anki/CardBrowser.java:1087-1091',
  note='DeckTask publishes progress only for a card it renders (DeckTask.java:659), so the loop must find an empty answer in the requested range. The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScroll', 'CardBrowser$17.onPostExecute', 'ASYNC',
  'the render task finishes without cancellation: the list is redrawn and the progress bar is hidden',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:129-134, 360-362, 639-669; SRC com/ichi2/anki/CardBrowser.java:1101-1110; FW-SRC core/java/android/os/AsyncTask.java:691-696',
  note='The task ends with a non-null TaskData (DeckTask.java:639-669), so the success branch runs. The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScroll', 'CardBrowser$17.onCancelled', 'ASYNC',
  'the render task started before this scroll is cancelled when the user scrolls again',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1155; SRC com/ichi2/async/DeckTask.java:168-175, 181-186, 368-370; FW-SRC core/java/android/os/AsyncTask.java:525-527, 691-696',
  note='The cancel at CardBrowser.java:1155 cancels the latest DeckTask only when its type is RENDER_BROWSER_QA (DeckTask.java:181-186): it cancels the task launched earlier, not the one this call launches. AsyncTask.finish calls onCancelled instead of onPostExecute (AsyncTask.java:692-695). The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScrollStateChanged', 'CardBrowser$17.onPreExecute', 'ASYNC',
  'the idle-state render task starts on the UI thread',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1167-1171, 1095-1098; SRC com/ichi2/async/DeckTask.java:129-134, 344-346',
  note='Launch at CardBrowser.java:1170, always under SCROLL_STATE_IDLE. Its cancel is in a later onScroll (edge above), so no onCancelled edge is written from this method. The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScrollStateChanged', 'CardBrowser$17.onProgressUpdate', 'ASYNC',
  'a card is rendered and the progress update reaches the render listener, which redraws the list',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:654-660, 352-354; SRC com/ichi2/anki/CardBrowser.java:1087-1091',
  note='DeckTask publishes progress only for a card it renders (DeckTask.java:659). The target is a batch 010 row.')

e('CardBrowser$RenderOnScroll.onScrollStateChanged', 'CardBrowser$17.onPostExecute', 'ASYNC',
  'the idle-state render task finishes without cancellation: the list is redrawn and the progress bar is hidden',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:129-134, 360-362, 639-669; SRC com/ichi2/anki/CardBrowser.java:1101-1110; FW-SRC core/java/android/os/AsyncTask.java:691-696',
  note='The task ends with a non-null TaskData (DeckTask.java:639-669), so the success branch runs. The target is a batch 010 row.')

# ---- CardBrowser$MultiColumnListAdapter: edges into the adapter from the page (framework calls) ----
# The other adapter methods (bindView, getColor, setFont, setFromMapping, getFromMapping) are reached through auto CALL
# edges from app methods (auto_calls.json) and have no entry here.

e('S_CARDBROWSER', 'CardBrowser$MultiColumnListAdapter.getView', 'FRAMEWORK',
  'the framework draws the card rows: the list asks the adapter for the view of each visible row',
  needs_state=STATE_CARDS,
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2335-2365; SRC com/ichi2/anki/CardBrowser.java:1201-1215',
  note='Page edge. The framework calls getView from AbsListView.obtainView (lines 2348 and 2365). No row is drawn for an empty list (STATE_CARDS). getView calls bindView (auto CALL, CardBrowser.java:1215).')

e('S_CARDBROWSER', 'CardBrowser$MultiColumnListAdapter.getCount', 'FRAMEWORK',
  'the framework reads the row count when the card list is set up and measured',
  env=None,
  evidence='FW-SRC core/java/android/widget/ListView.java:552-575, 1269-1282; SRC com/ichi2/anki/CardBrowser.java:477, 1288-1291',
  note='Page edge. ListView.setAdapter (line 575, called at CardBrowser.java:477) and onMeasure (line 1282) read the count. The count is 0 for an empty list, so there is no state gate.')

e('S_CARDBROWSER', 'CardBrowser$MultiColumnListAdapter.getItemId', 'FRAMEWORK',
  'the framework reads the id of a row when the user taps it or long-presses it',
  needs_state=STATE_CARDS,
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3108-3128, 3133-3149; FW-SRC core/java/android/widget/BaseAdapter.java:35-37; SRC com/ichi2/anki/CardBrowser.java:1300-1303',
  note='Page edge. PerformClick.run calls adapter.getItemId for the tapped row (AbsListView.java:3127) and CheckForLongPress.run for the long-pressed row (AbsListView.java:3149). The body returns the position. Needs at least one row (STATE_CARDS). AbsListView.setItemViewLayoutParams (AbsListView.java:2413-2414) also calls getItemId, but only when the adapter has stable ids; MultiColumnListAdapter inherits hasStableIds() = false (BaseAdapter.java:35-37), so that path is not a route here.')

# ---- CardBrowser INTENT and REGISTER addendum (orchestrator, 2026-10-28): launches in batch 009 methods and the $6 REGISTER edges that no part wrote
e('CardBrowser$1.onSelection', 'Previewer.<init>', 'INTENT',
  'open the card preview from the card context menu (Details)',
  guard='the Details item of the card browser context menu (CardBrowser.java:206-210)',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:206-210; SRC com/ichi2/anki/Previewer.java:28-34',
  note='The card id goes to Previewer as the currentCardId extra (CardBrowser.java:208-209).')

e('CardBrowser.onOptionsItemSelected', 'NoteEditor.<init>', 'INTENT',
  'add a note from the card browser action bar',
  guard='the action_add_card_from_card_browser menu item (CardBrowser.java:628-633)',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:628-633',
  note='The add-note launch sets NoteEditor.CALLER_CARDBROWSER_ADD (CardBrowser.java:632). The ENTERS edge to S_NOTEEDITOR is in part 009.')

e('CardBrowser$6.<init>', 'CardBrowser$6.onItemSelected', 'REGISTER',
  'the second-column listener is set on the column spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:445-447',
  note='onItemSelected is in part 011; its routes are the S_CARDBROWSER edges there. The builder does not follow REGISTER for reachability. Written here because the part 010 header says CardBrowser$6 has no method in that batch, but batch_010.txt lists CardBrowser$6.<init>.')

e('CardBrowser$6.<init>', 'CardBrowser$6.onNothingSelected', 'REGISTER',
  'the second-column listener is set on the column spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:445-447',
  note='onNothingSelected is in part 011 (UNREACHABLE there). The builder does not follow REGISTER for reachability. Written here for the same reason as the onItemSelected edge.')

# ---- part 012 (2026-10-28)
# AnkiDroid batch 012 (LABEL helper): NoteEditor part 1, 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_012.md.
#
# Result: all 40 methods are REACHABLE, so this part has no UNREACHABLE entries.
# Edges written here (15): INTENT 3 (the launches in this batch), RESULT 3, FRAMEWORK 4, GUI 2, ASYNC 3.
# INTENT check, done for each launch: the Intent names an explicit component, so no framework gate applies.
# Missing gates are notes only (MISSING GATE MGn). MG65 to MG72 are used here.
# Route ownership: NoteEditor$1 (the DeckTask TaskListener), NoteEditor$2, $4, $5, $6, $8, $9, $11, $13, the
# SetNoteTypeListener and EditNoteTypeListener classes belong to other batches; their auto CALL edges are not
# written here. The NoteEditorRescheduleCard$1.onInput listener belongs to the dialog batch. The
# AnkiActivity.onLoadFinished -> NoteEditor.onCollectionLoaded edge belongs to the AnkiActivity part.
# The ASYNC edges from saveNote are written here (launcher convention, as in label_002 and label_010).
# No page edge is written from S_NOTEEDITOR to showCardTemplateEditor: its route is the cards-line listener
# NoteEditor$2.onClick (another batch), whose auto CALL edge reaches it.

# --- INTENT: launches from this batch (explicit components; INTENT check done for each) ---

e('NoteEditor.onOptionsItemSelected', 'NoteEditor.<init>', 'INTENT',
  'copy card or add card from card editor (edit mode): explicit Intent to NoteEditor with EXTRA_CALLER set to CALLER_CARDEDITOR; the copy adds the current field text, then startActivityForResultWithAnimation with REQUEST_ADD',
  env=None,
  needs_state=STATE_NOTE,
  evidence='SRC com/ichi2/anki/NoteEditor.java:839-848',
  note='MISSING GATE MG66: the copy, add-card, reset and reschedule items are shown only in edit mode (NoteEditor.java:804-809). Edit mode is not a STATE. STATE_NOTE is a necessary condition (an edited note exists), not the full gate. INTENT check: explicit component, no framework gate. The result returns through the RESULT edge S_NOTEEDITOR -> NoteEditor.onActivityResult below. confirmed_by SOURCE.')

e('NoteEditor.showCardTemplateEditor', 'CardTemplateEditor.<init>', 'INTENT',
  'open the card template editor from the cards line of the note editor: explicit Intent to CardTemplateEditor with modelId, and noteId when editing',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1001-1013; SRC res/layout/note_editor.xml:117-125',
  note='INTENT check: explicit component, no framework gate. The tap route is the click listener NoteEditor$2.onClick (NoteEditor.java:353-357, another batch), whose auto CALL edge reaches this method. The result returns through the RESULT edge S_CARDTEMPLATEEDITOR -> NoteEditor.onActivityResult below. confirmed_by SOURCE.')

e('NoteEditor.startMultimediaFieldEditor', 'MultimediaEditFieldActivity.<init>', 'INTENT',
  'edit one multimedia field: explicit Intent to MultimediaEditFieldActivity, then startActivityForResultWithoutAnimation with REQUEST_MULTIMEDIA_EDIT',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1235-1240',
  note='INTENT check: explicit component, no framework gate. The media-button routes (NoteEditor$11.onClick at NoteEditor.java:1141 and the popup items at 1159, 1165, 1172) belong to another batch. The result returns through the RESULT edge S_MULTIMEDIA_EDIT_FIELD -> NoteEditor.onActivityResult below. confirmed_by SOURCE.')

# --- RESULT: child editors return to NoteEditor.onActivityResult (framework dispatch, Activity.java:7265-7266) ---

e('S_NOTEEDITOR', 'NoteEditor.onActivityResult', 'RESULT',
  'a copy-card or add-card editor (another NoteEditor instance) finishes; REQUEST_ADD sets mChanged in the parent',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1018-1029, 848, 937-951; FW-SRC core/java/android/app/Activity.java:7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='Page edge; S_NOTEEDITOR is the child editor. The child returns RESULT_OK only when its mChanged is set (NoteEditor.java:937-951). confirmed_by SOURCE.')

e('S_CARDTEMPLATEEDITOR', 'NoteEditor.onActivityResult', 'RESULT',
  'the card template editor returns after the user edits the templates (REQUEST_TEMPLATE_EDIT); the parent reloads its cards',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1059-1063, 1001-1013; FW-SRC core/java/android/app/Activity.java:7265-7266',
  note='Page edge; S_CARDTEMPLATEEDITOR is the child. Launched by showCardTemplateEditor (INTENT edge above). The result handler sets mReloadRequired and calls updateCards (NoteEditor.java:1063). confirmed_by SOURCE.')

e('S_MULTIMEDIA_EDIT_FIELD', 'NoteEditor.onActivityResult', 'RESULT',
  'the multimedia field editor returns (REQUEST_MULTIMEDIA_EDIT); the field text or media is updated and saved',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1031-1057, 1235-1240; FW-SRC core/java/android/app/Activity.java:7265-7266',
  note='Page edge; S_MULTIMEDIA_EDIT_FIELD is the child. Launched by startMultimediaFieldEditor (INTENT edge above). env unset here; the gates of the child page belong to its own batch. confirmed_by SOURCE.')

# --- FRAMEWORK: callbacks the framework makes (no app caller) ---

e('S_NOTEEDITOR', 'NoteEditor.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework asks the editor for its options menu (Activity.onCreatePanelMenu calls onCreateOptionsMenu)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3390; SRC com/ichi2/anki/NoteEditor.java:801-802',
  note='Page edge; the framework is the caller. The edit-mode items are hidden or shown inside the method (NoteEditor.java:804-809); see MG66 on the menu edge. Precedent: DeckPicker.onCreate -> onCreateOptionsMenu. confirmed_by SOURCE.')

e('S_NOTEEDITOR', 'NoteEditor.onSaveInstanceState', 'FRAMEWORK',
  'the framework saves the editor state when the activity is stopped and not finishing (ActivityThread: not mFinished and saveState)',
  env=None,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:4023-4025; SRC com/ichi2/anki/NoteEditor.java:313-326',
  note='Page edge. MISSING GATE MG72: the not-finishing and saveState conditions are framework state with no STATE kind, so env and needs_state are unset. Precedent: DeckPicker.onPause -> onSaveInstanceState. confirmed_by SOURCE.')

e('NoteEditor.closeNoteEditor(int,Intent)', 'NoteEditor.onDestroy', 'FRAMEWORK',
  'the editor finishes (finishWithAnimation calls finish); the framework then destroys it and calls onDestroy (performDestroy)',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:960-969; SRC com/ichi2/anki/AnkiActivity.java:206-209; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='Framework edge. onDestroy is skipped by lc_chain (LC_NO_TRIGGER), so this edge and the one from onCollectionLoaded are its inbound routes. Precedent: DeckPicker.finishWithAnimation -> onDestroy. The hop from finish to performDestroy goes through ActivityThread and is INFERRED. confirmed_by SOURCE for the written edge.')

e('NoteEditor.onCollectionLoaded', 'NoteEditor.onDestroy', 'FRAMEWORK',
  'the editor finishes without animation inside onCollectionLoaded (CALLER_NOCALLER, an intent without source text, or an Aedict note added); the framework then destroys it and calls onDestroy',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:364-367, 405-411; SRC com/ichi2/anki/AnkiActivity.java:200-203; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='Framework edge; second inbound route for onDestroy. The finish calls are finishWithoutAnimation (AnkiActivity.java:200-203), which does not run closeNoteEditor. The hop from finish to performDestroy is INFERRED, as on the edge above. confirmed_by SOURCE for the written edge.')

# --- GUI: user input on the editor page (menu, Back key) ---

e('S_NOTEEDITOR', 'NoteEditor.onBackPressed', 'GUI',
  'press the Back key in the note editor (unsaved-changes check, then close)',
  gui=['press the Back key in the note editor'],
  env=None,
  evidence='FW-SRC core/java/android/view/KeyEvent.java:2715; FW-SRC core/java/android/app/Activity.java:2975-2981; SRC com/ichi2/anki/NoteEditor.java:786-789',
  note='Page edge. KeyEvent dispatch calls Activity.onKeyUp, which calls onBackPressed (Activity.java:2980). No env or needs_state gate. Precedent: S_CARDBROWSER -> CardBrowser.onBackPressed. confirmed_by SOURCE.')

e('S_NOTEEDITOR', 'NoteEditor.onOptionsItemSelected', 'GUI',
  'tap an action-bar item in the note editor: Save, the Up arrow, Copy card, Add card from card editor, Reset card progress or Reschedule card',
  gui=['tap an action-bar item in the note editor: Save, the Up arrow, Copy card, Add card from card editor, Reset card progress or Reschedule card'],
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3439-3452; SRC com/ichi2/anki/NoteEditor.java:826-880',
  note='Page edge. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). MISSING GATE MG66: Copy card, Add card, Reset card progress and Reschedule card appear only in edit mode (NoteEditor.java:804-809); no STATE models edit mode, so needs_state is unset here. onOptionsItemSelected is skipped by lc_chain (LC_NO_TRIGGER), so this is its only inbound route. confirmed_by SOURCE.')

# --- ASYNC: saveNote launches the add-note DeckTask; the callbacks are NoteEditor$1 (another batch) ---

e('NoteEditor.saveNote', 'NoteEditor$1.onPreExecute', 'ASYNC',
  'the add-note task starts: DeckTask.onPreExecute calls the TaskListener (NoteEditor$1)',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:662, 681; SRC com/ichi2/async/DeckTask.java:129-134, 344-347; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='MISSING GATE MG65: the task is launched only in add mode (mAddNote, NoteEditor.java:662 and 681). No STATE kind models a new note being added, so needs_state is unset. The listener belongs to another batch; this launcher writes the ASYNC edge. confirmed_by SOURCE.')

e('NoteEditor.saveNote', 'NoteEditor$1.onProgressUpdate', 'ASYNC',
  'the add-note task publishes the new note (progress count greater than zero); DeckTask.onProgressUpdate calls the TaskListener',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:198-204; SRC com/ichi2/async/DeckTask.java:352-355, 372-380; FW-SRC core/java/android/os/AsyncTask.java:714-715',
  note='MISSING GATE MG65 as on the onPreExecute edge (add mode only). The listener calls setNote() on success (NoteEditor.java:204). confirmed_by SOURCE.')

e('NoteEditor.saveNote', 'NoteEditor$1.onPostExecute', 'ASYNC',
  'the add-note task ends: on success the editor closes with the new note; on failure it closes with RESULT_DB_ERROR',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:250-271; SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='MISSING GATE MG65 as on the onPreExecute edge (add mode only). MISSING GATE MG67: the failure branch (closeNoteEditor(DeckPicker.RESULT_DB_ERROR), NoteEditor.java:271) needs a failed insert; no STATE models a database error, so needs_state is unset. confirmed_by SOURCE.')


# ---- part 012 addendum (orchestrator, 2026-10-28): the comparator sorts in NoteEditor.onCollectionLoaded (batch 012 did not write this edge)
e('NoteEditor.onCollectionLoaded', 'NoteEditor$JSONNameComparator.compare', 'CALL',
  'sort the note types (NoteEditor.java:423) and the decks (NoteEditor.java:453) by name during the editor setup',
  env=None,
  cls='non_standard',
  via='java.util.Collections.sort (library, not in the dataset)',
  evidence='SRC com/ichi2/anki/NoteEditor.java:421-424, 451-454, 1514-1516',
  note='MISSING GATE MG86: compare runs only when the sorted list has two or more entries (two or more note types, or two or more decks). Written here because the sort is a library call the bytecode extractor does not follow.')

# ---- part 013 (2026-10-28)
# AnkiDroid batch 013 (LABEL helper). NoteEditor part 2, 40 methods: NoteEditor.updateCards, updateDeckPosition,
# updateField, updateFieldsFromMap, updateTags; the anonymous listeners and callbacks NoteEditor$1 (DeckTask
# TaskListener), $2 to $4, $5 to $7 (ConfirmationDialog), $8 (SD card receiver), $9 and $10 (dialog callbacks),
# $11 and $11$1 (media button and popup), $12 and $12$1 (remap button and popup) and $13 (TextWatcher).
# The full row list is in graphs/AnkiDroid/parts/label_013.md.
#
# Route ownership: setNote(Note), setNote(), onCollectionLoaded, populateEditFields, initFieldEditText,
# setMMButtonListener, setRemapButtonListener, saveNote (the TASK_TYPE_ADD_FACT launch at NoteEditor.java:681),
# showTagsDialog, showCardTemplateEditor, startMultimediaFieldEditor, onOptionsItemSelected, onActivityResult,
# registerExternalStorageListener, closeCardEditorWithCheck, showDiscardChangesDialog's caller chain,
# changeNoteTypeWithErrorHandling and duplicateCheck belong to batch_012. The edit-type and set-type listeners
# (NoteEditor$EditNoteTypeListener, NoteEditor$SetNoteTypeListener), which reach updateFieldsFromMap, updateCards,
# updateDeckPosition and updateTags, belong to batch_014.
# The ASYNC edges from the saveNote launch to NoteEditor$1 are written by batch_012, not here. The edges from
# batch_012 methods into the S_DLG_CONFIRMATION and S_DLG_TAGS pages are written by batch_012.
# REGISTER edges from an <init> are written here with a note: the builder does not follow REGISTER for
# reachability, so the route is the page GUI or FRAMEWORK edge from S_NOTEEDITOR, S_DLG_CONFIRMATION or S_DLG_TAGS.
# No method in this batch launches an app activity directly: showCardTemplateEditor, showTagsDialog and
# startMultimediaFieldEditor (the Intent launches) are batch_012 methods, so no INTENT edge is written here.
# Gates: MG75 to MG81 (no predefined ENV or STATE kind covers the edit mode, the note type change, the remap gate,
# the unsaved-changes check, the deck count or the typing gate).
# NoteEditor$1.onCancelled is UNREACHABLE. If the DeckTask onCancelled dispatch draws an auto CALL edge to it, the
# builder warns (as for CardBrowser$13 to $15, build_018); the orchestrator's sup() handles that, not this part.

# --- Cards button listener ($2). Set in onCollectionLoaded (NoteEditor.java:353-359).
e('NoteEditor$2.<init>', 'NoteEditor$2.onClick', 'REGISTER',
  'the Cards button listener is set on the card templates text view',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:353-359',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$2.onClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$2.onClick', 'GUI',
  'tap the card templates text (Cards) in the note editor, which opens the card template editor',
  gui=['tap the card templates text (Cards) in the note editor, which opens the card template editor'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:353-359, 1001-1002; SRC res/layout/note_editor.xml:116-122',
  note='Page edge. No gate: the text view has no visibility attribute (note_editor.xml:116-122). The launch of CardTemplateEditor is in showCardTemplateEditor (batch_012), not here.')

# --- Deck spinner listener ($3). Set in onCollectionLoaded (NoteEditor.java:471-482).
e('NoteEditor$3.<init>', 'NoteEditor$3.onItemSelected', 'REGISTER',
  'the deck spinner listener is set on the note deck spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:471-482',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the routes are the S_NOTEEDITOR FRAMEWORK and GUI edges below.')

e('S_NOTEEDITOR', 'NoteEditor$3.onItemSelected', 'FRAMEWORK',
  'the note editor opens: the framework lays out the deck spinner and selects position 0, which fires onItemSelected',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:452-469, 471-476; FW-SRC core/java/android/widget/AdapterView.java:937-947, 1103-1108; FW-SRC core/java/android/widget/Spinner.java:637-648, 681',
  note='Page edge. The default selection after setAdapter (NoteEditor.java:469) is set in AbsSpinner, which is not in fw_src: INFERRED for that step. The GUI edge below is the alternative route.')

e('S_NOTEEDITOR', 'NoteEditor$3.onItemSelected', 'GUI',
  'pick another deck in the deck drop-down of the note editor',
  gui=['pick another deck in the deck drop-down of the note editor'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:452-462, 471-476',
  note='Page edge. MISSING GATE MG80: needs two or more entries in the deck list (NoteEditor.java:452-462); no predefined STATE kind is a count of decks. The deck list keeps every non-filtered deck (dyn 0), and the current deck in edit mode.')

# --- Tags button listener ($4). Set in onCollectionLoaded (NoteEditor.java:526-532).
e('NoteEditor$4.<init>', 'NoteEditor$4.onClick', 'REGISTER',
  'the Tags button listener is set on the tags button',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:526-532',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$4.onClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$4.onClick', 'GUI',
  'tap the Tags button in the note editor, which opens the tags dialog',
  gui=['tap the Tags button in the note editor, which opens the tags dialog'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:526-531, 983-999; SRC res/layout/note_editor.xml:85-90',
  note='Page edge. No gate: the tags button has no visibility attribute (note_editor.xml:85-90). showTagsDialog is batch_012.')

# --- Confirmation dialogs ($5, $6, $7). Each anonymous ConfirmationDialog is the dialog object itself; its OK
# calls confirm() (ConfirmationDialog.java:40-43). No REGISTER edge is needed for these three.
e('S_DLG_CONFIRMATION', 'NoteEditor$5.confirm', 'GUI',
  'change the note type of an edited note when the mapping would lose cards, then tap OK',
  gui=['change the note type of an edited note when the mapping would lose cards, then tap OK'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:684-698; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43',
  note='Page edge; the route into S_DLG_CONFIRMATION is saveNote (NoteEditor.java:688-698, batch_012). MISSING GATE MG76: the change needs an edited note in change-note-type mode, and no predefined STATE kind covers the note type change. The MaterialDialog OK dispatch to ConfirmationDialog is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'NoteEditor$6.confirm', 'GUI',
  'change the note type of an edited note when libanki needs the user to confirm a full sync, then tap OK',
  gui=['change the note type of an edited note when libanki needs the user to confirm a full sync, then tap OK'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:745-767; SRC com/ichi2/libanki/Collection.java:364-371; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43',
  note='Page edge; the route into S_DLG_CONFIRMATION is changeNoteTypeWithErrorHandling (batch_012). MISSING GATE MG76 plus the libanki check: modSchema(true) throws ConfirmModSchemaException only when the schema is not yet marked changed (Collection.java:364-371), which is a collection state with no predefined kind. The MaterialDialog OK dispatch is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'NoteEditor$7.confirm', 'GUI',
  'open the note editor on an existing note, tap the reset card progress item in the menu, then tap OK',
  gui=['open the note editor on an existing note, tap the reset card progress item in the menu, then tap OK'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:800-810, 851-869; SRC res/menu/note_editor.xml:17-20; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43',
  note='Page edge. MISSING GATE MG75: the reset item is hidden in add mode (NoteEditor.java:803-809; the XML sets visible false at note_editor menu 17-20). STATE_NOTE is the closest predefined kind (an edited note exists). The route into S_DLG_CONFIRMATION is onOptionsItemSelected (batch_012). The MaterialDialog OK dispatch is library code: INFERRED.')

# --- SD card receiver ($8). Registered in registerExternalStorageListener (NoteEditor.java:890-902), which
# onCollectionLoaded calls at NoteEditor.java:340 (batch_012).
e('NoteEditor$8.<init>', 'NoteEditor$8.onReceive', 'REGISTER',
  'the MEDIA_EJECT receiver is registered while the note editor is open',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:890-902, 340',
  note='onReceive is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$8.onReceive SYSTEM edge below.')

e('S_NOTEEDITOR', 'NoteEditor$8.onReceive', 'SYSTEM',
  'the SD card is ejected while the note editor is open (ACTION_MEDIA_EJECT, delivered to SdCardReceiver, which re-broadcasts MEDIA_EJECT)',
  env=ENV_SDCARD_EVENT,
  evidence='SRC com/ichi2/anki/NoteEditor.java:892-902; SRC com/ichi2/anki/receiver/SdCardReceiver.java:42-47',
  note='Page edge; the destination is in this part. The first hop (system delivery of ACTION_MEDIA_EJECT to the dynamically registered receiver) is not verifiable from fw_src: INFERRED. The receiver calls finishWithoutAnimation (NoteEditor.java:895-896), not the save path.')

# --- Discard-changes dialog callback ($9). Built in showDiscardChangesDialog (NoteEditor.java:917-928).
e('NoteEditor$9.<init>', 'NoteEditor$9.onPositive', 'REGISTER',
  'the discard-changes dialog callback is set when the dialog is built',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:917-928',
  note='onPositive is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$9.onPositive GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$9.onPositive', 'GUI',
  'use the close action of the note editor while there are unsaved changes, then tap OK on the discard-changes dialog',
  gui=['use the close action of the note editor while there are unsaved changes, then tap OK on the discard-changes dialog'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:625-627, 907-911, 916-928',
  note='Page edge. MISSING GATE MG79: showDiscardChangesDialog runs only when hasUnsavedChanges() is true (NoteEditor.java:907-909). The close action is closeCardEditorWithCheck (batch_012). The MaterialDialog callback is library code: INFERRED.')

# --- Tags dialog listener ($10). Set in showTagsDialog (NoteEditor.java:989-997, batch_012 method).
e('NoteEditor$10.<init>', 'NoteEditor$10.onPositive', 'REGISTER',
  'the tags dialog listener is set on the dialog in showTagsDialog',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:989-997; SRC com/ichi2/anki/dialogs/TagsDialog.java:162-167',
  note='onPositive is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_TAGS -> NoteEditor$10.onPositive GUI edge below.')

e('S_DLG_TAGS', 'NoteEditor$10.onPositive', 'GUI',
  'in the tags dialog, select tags and tap OK',
  gui=['in the tags dialog, select tags and tap OK'],
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:162-167; SRC com/ichi2/anki/NoteEditor.java:983-999',
  note='Page edge. The route into S_DLG_TAGS is showTagsDialog (batch_012). TagsDialog.java:164-166 calls the listener from app code; the MaterialDialog OK callback that reaches it is library code: INFERRED.')

# --- Media button ($11) and its popup ($11$1). setMMButtonListener is called only when editModelMode is false
# (NoteEditor.java:1116-1122), so both edges carry MG77.
e('NoteEditor$11.<init>', 'NoteEditor$11.onClick', 'REGISTER',
  'the media button listener is set on the media button of each field when not in change-note-type mode',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1116-1122, 1129-1131',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$11.onClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$11.onClick', 'GUI',
  'tap the media button next to a field in the note editor (not in change-note-type mode)',
  gui=['tap the media button next to a field in the note editor (not in change-note-type mode)'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1108-1122, 1129-1146',
  note='Page edge. MISSING GATE MG77: setMMButtonListener runs only when editModelMode is false (NoteEditor.java:1116-1122). A non-empty field starts the field editor (startMultimediaFieldEditor, batch_012); an empty field shows the popup.')

e('NoteEditor$11$1.<init>', 'NoteEditor$11$1.onMenuItemClick', 'REGISTER',
  'the popup menu listener is set on the media popup of an empty field',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1142-1148',
  note='onMenuItemClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$11$1.onMenuItemClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$11$1.onMenuItemClick', 'GUI',
  'tap the media button of an empty field, then choose audio, image or text in the popup menu',
  gui=['tap the media button of an empty field, then choose audio, image or text in the popup menu'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1142-1160',
  note='Page edge. MISSING GATE MG77 applies (the field is empty and the editor is not in change-note-type mode). The PopupMenu item dispatch is framework and library code: INFERRED.')

# --- Remap button ($12) and its popup ($12$1). Both need editModelMode and more than two fields (MG78).
e('NoteEditor$12.<init>', 'NoteEditor$12.onClick', 'REGISTER',
  'the remap button listener is set on the media button of a new field in change-note-type mode',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1112-1115, 1186-1189',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$12.onClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$12.onClick', 'GUI',
  'change the note type of an existing note to one with more than two fields, then tap the remap button of a new field',
  gui=['change the note type of an existing note to one with more than two fields, then tap the remap button of a new field'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1112-1115, 1186-1198, 1505-1508',
  note='Page edge. MISSING GATE MG78: editModelMode and allowFieldRemapping() (mEditorNote.items().length > 2, NoteEditor.java:1507). editModelMode is the argument of populateEditFields(fields, boolean) and is true only through updateFieldsFromMap (NoteEditor.java:1497), which the change-note-type listener calls (NoteEditor$EditNoteTypeListener, batch_014, line 1625). The PopupMenu dispatch is library code: INFERRED.')

e('NoteEditor$12$1.<init>', 'NoteEditor$12$1.onMenuItemClick', 'REGISTER',
  'the remap popup listener is set on the old-field popup',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1192-1199',
  note='onMenuItemClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$12$1.onMenuItemClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$12$1.onMenuItemClick', 'GUI',
  'after a remap button tap, pick an old field (or None) in the popup menu',
  gui=['after a remap button tap, pick an old field (or None) in the popup menu'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1186-1229',
  note='Page edge. MISSING GATE MG78 applies. The choice updates mModelChangeFieldMap and reloads the fields through updateFieldsFromMap (NoteEditor.java:1225). The popup dispatch is library code: INFERRED.')

# --- Field TextWatcher ($13). Added in initFieldEditText after editText.init (NoteEditor.java:1247, then 1253).
e('NoteEditor$13.<init>', 'NoteEditor$13.afterTextChanged', 'REGISTER',
  'the text watcher is added to each field EditText in initFieldEditText',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1247, 1253-1271',
  note='afterTextChanged is in this part. The builder does not follow REGISTER for reachability; the routes are the S_NOTEEDITOR FRAMEWORK edges below.')

e('NoteEditor$13.<init>', 'NoteEditor$13.beforeTextChanged', 'REGISTER',
  'the text watcher is added to each field EditText in initFieldEditText',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1247, 1253-1271',
  note='beforeTextChanged is in this part (empty body). The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR FRAMEWORK edge below.')

e('NoteEditor$13.<init>', 'NoteEditor$13.onTextChanged', 'REGISTER',
  'the text watcher is added to each field EditText in initFieldEditText',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1247, 1253-1271',
  note='onTextChanged is in this part (empty body). The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR FRAMEWORK edge below.')

e('S_NOTEEDITOR', 'NoteEditor$13.afterTextChanged', 'FRAMEWORK',
  'type or delete text in a field of the note editor; the TextView dispatches the change to the watcher',
  env=None,
  evidence='FW-SRC core/java/android/widget/TextView.java:9375-9380; SRC com/ichi2/anki/NoteEditor.java:1253-1260',
  note='Page edge. MISSING GATE MG81: the field is enabled only when editModelMode is false (initFieldEditText enabled = !editModelMode, NoteEditor.java:1102, 1272). The watcher is added after init (1247, then 1253), so the cold-start init does not fire it: typing is the route.')

e('S_NOTEEDITOR', 'NoteEditor$13.beforeTextChanged', 'FRAMEWORK',
  'type or delete text in a field of the note editor; the TextView dispatches the change to the watcher',
  env=None,
  evidence='FW-SRC core/java/android/widget/TextView.java:9309-9314; SRC com/ichi2/anki/NoteEditor.java:1264-1265',
  note='Page edge. MISSING GATE MG81 applies (enabled field, typing). The body is empty, so the edge has no effect on state.')

e('S_NOTEEDITOR', 'NoteEditor$13.onTextChanged', 'FRAMEWORK',
  'type or delete text in a field of the note editor; the TextView dispatches the change to the watcher',
  env=None,
  evidence='FW-SRC core/java/android/widget/TextView.java:9359-9364; SRC com/ichi2/anki/NoteEditor.java:1269-1270',
  note='Page edge. MISSING GATE MG81 applies (enabled field, typing). The body is empty, so the edge has no effect on state.')

# --- UNREACHABLE entries.
UNREACHABLE['NoteEditor$1.onCancelled'] = (
    'no_trigger_in_app',
    "The add-note task (TASK_TYPE_ADD_FACT, launched by saveNote at NoteEditor.java:681) is never cancelled. The only cancel of a DeckTask is sLatestInstance inside the no-argument cancelTask() (DeckTask.java:172). That method is reached only from cancelTask(int) when the type matches (DeckTask.java:181-186), and the only callers of cancelTask(int) are CardBrowser SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). The ADD_FACT case is at DeckTask.java:243-244. AsyncTask runs onCancelled only after cancel() (AsyncTask.java:525-528, 691-698). The body is empty (NoteEditor.java:276-278).",
    'SRC com/ichi2/async/DeckTask.java:172, 181-186, 243-244; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/NoteEditor.java:276-278, 681; FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698',
    'SOURCE')

UNREACHABLE['NoteEditor$3.onNothingSelected'] = (
    'framework_never_calls',
    "The deck spinner adapter is built once from a static deck list and set once; nothing else sets an adapter or calls notifyDataSetChanged on it (NoteEditor.java:468-469). Both selection calls are guarded by a valid index (updateDeckPosition at NoteEditor.java:1385-1387; the edit-type listener at 1632-1634). AdapterView fires onNothingSelected only when the selected position is negative (fireOnSelected, AdapterView.java:941-947), and the position changes only through checkSelectionChanged (AdapterView.java:1103-1108). This path never moves the selection to a negative position. The framework dispatch is read from source, not run: INFERRED. The body is a comment only (NoteEditor.java:479-481).",
    'SRC com/ichi2/anki/NoteEditor.java:468-469, 479-481, 1385-1387; FW-SRC core/java/android/widget/AdapterView.java:941-947, 1103-1108',
    'INFERRED')


# DeckTask dispatch to the NoteEditor add-note listener, which is never cancelled (batch 013; see handoff decisions 2026-10-28 02:37 EDT)
sup(('DeckTask.onCancelled', 'NoteEditor$1.onCancelled'))

# ---- part 016 (2026-10-28)
# AnkiDroid batch 016 (LABEL helper). Preferences part 2: the advanced-screen click listener Preferences$8 (force full
# sync, set in Preferences.initSubscreen, case advanced) and the settings fragment Preferences$SettingsFragment (<init>,
# onCreate, onResume, onPause, onSharedPreferenceChanged). 7 methods; the full row list is in
# graphs/AnkiDroid/parts/label_016.md.
#
# Ownership: an edge is written in the part that holds its source method. Written here: the REGISTER edges from
# Preferences$8.<init> and SettingsFragment.onResume (the builder does not follow REGISTER for reachability, so the
# routes are the S_PREFERENCES GUI and FRAMEWORK edges below); the LIFECYCLE edges inside SettingsFragment; and the
# page edges S_PREFERENCES -> my methods (the part holding the destination writes page-source edges).
# Not written here (leads, not my edges): the CALL edges from Preferences.initSubscreen to Preferences$8.<init>
# (batch_015); from SettingsFragment.onCreate to Preferences.initSubscreen and Preferences.initAllPreferences
# (Preferences.java:788-789); from SettingsFragment.onResume and onSharedPreferenceChanged to
# Preferences.updatePreference (Preferences.java:801, 812); and from Preferences$8.onPreferenceClick to
# Collection.modSchemaNoCheck and Collection.setMod (Preferences.java:350-351, other batches). These CALL edges come
# from auto_calls.json (USE_AUTO) and are not written by hand here.
#
# INTENT check: none of the 7 methods starts an app-class activity. The subscreen intent (CompatV11.java:41-48, started by
# DeckPicker.java:427) has its INTENT edge in graph_def.py (DeckPicker.onCreate -> Preferences.<init>).
#
# UNREACHABLE entries: none. All 7 methods have a route.
# Gates: MG105 is text only (note=) on the subscreen route. Predefined constants used: ENV_STORAGE on the force-full-sync
# click; STATE_SETTINGS on the onSharedPreferenceChanged GUI edge. Only MG105 is needed; MG106 to MG111 are not used.

# ---- Preferences$8: force_full_sync click listener (set in Preferences.initSubscreen, case advanced, Preferences.java:347-355) ----

e('Preferences$8.<init>', 'Preferences$8.onPreferenceClick', 'REGISTER',
  'the force-full-sync click listener is set on the force_full_sync preference',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:347-355',
  note='REGISTER. The builder does not follow REGISTER for reachability; the route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$8.onPreferenceClick', 'GUI',
  'tap Force full sync on the Advanced settings screen',
  gui=['tap Force full sync on the Advanced settings screen'],
  env=ENV_STORAGE,
  evidence='SRC com/ichi2/anki/Preferences.java:347-355; SRC res/xml/preferences_advanced.xml:34-37; FW-SRC core/java/android/preference/PreferenceScreen.java:240-250; FW-SRC core/java/android/preference/Preference.java:1129-1139',
  note='Page edge. The row is a plain Preference in the advanced screen (preferences_advanced.xml:28, 34-37): no category, no enabled or hidden attribute. Preference.performClick returns early when disabled (Preference.java:1131), which does not apply here. The handler needs the collection: getCol (Preferences.java:350) opens it (CollectionHelper.java:85-101) and returns null only when the AnkiDroid directory cannot be initialised (CollectionHelper.java:90-96); line 350 then throws a NullPointerException. So env is ENV_STORAGE. needs_state unset: getCol opens the collection itself, and the route does not check its file state.')

# ---- Preferences$SettingsFragment (Preferences.java:782-814): lifecycle chain and listener registration ----

e('Preferences$SettingsFragment.<init>', 'Preferences$SettingsFragment.onCreate', 'LIFECYCLE',
  'lifecycle callback of Preferences$SettingsFragment (PreferenceFragment): onCreate follows the constructor',
  env=None,
  evidence='FW-SRC core/java/android/app/Fragment.java:2483-2490; FW-SRC core/java/android/app/FragmentManager.java:1237; SRC com/ichi2/anki/Preferences.java:782-790',
  note='The fragment is constructed by Fragment.instantiate (PreferenceActivity.java:1254). Its onCreate runs from FragmentManager.moveToState (FragmentManager.java:1237), which calls performCreate (Fragment.java:2489).')

e('Preferences$SettingsFragment.onCreate', 'Preferences$SettingsFragment.onResume', 'LIFECYCLE',
  'lifecycle callback of Preferences$SettingsFragment: onResume follows onCreate',
  env=None,
  evidence='FW-SRC core/java/android/app/Fragment.java:2547-2554; FW-SRC core/java/android/app/FragmentManager.java:1322; SRC com/ichi2/anki/Preferences.java:792-796',
  note='FragmentManager.java:1322 calls performResume, which calls onResume (Fragment.java:2554). The fragment is resumed while the settings screen is on top.')

e('Preferences$SettingsFragment.onResume', 'Preferences$SettingsFragment.onPause', 'LIFECYCLE',
  'lifecycle callback of Preferences$SettingsFragment: onPause follows onResume',
  env=None,
  evidence='FW-SRC core/java/android/app/Fragment.java:2703-2709; FW-SRC core/java/android/app/FragmentManager.java:1334; SRC com/ichi2/anki/Preferences.java:804-808',
  note='FragmentManager.java:1334 calls performPause, which calls onPause (Fragment.java:2709). The framework pauses the fragment when it leaves the resumed state (the activity pauses, or the fragment is removed or replaced by a header switch at PreferenceActivity.java:1259-1260).')

e('Preferences$SettingsFragment.onResume', 'Preferences$SettingsFragment.onSharedPreferenceChanged', 'REGISTER',
  'the settings fragment registers as the SharedPreferences listener on resume',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:796, 806',
  note='REGISTER at Preferences.java:796; the listener is removed in onPause (Preferences.java:806). The builder does not follow REGISTER for reachability; the route is the S_PREFERENCES GUI edge below.')

# ---- page edges into the SettingsFragment methods: the Advanced subscreen (intent) and the headers list (tap) ----

e('S_PREFERENCES', 'Preferences$SettingsFragment.<init>', 'FRAMEWORK',
  'the settings screen opens straight on the Advanced subscreen: the activity is started with the subscreen extras',
  env=None,
  evidence='SRC com/ichi2/compat/CompatV11.java:41-48; SRC com/ichi2/anki/DeckPicker.java:353, 415-428; FW-SRC core/java/android/preference/PreferenceActivity.java:582, 605-611, 1246-1256; SRC com/ichi2/anki/Preferences.java:146-148; FW-SRC core/java/android/app/Fragment.java:508-524',
  note='MISSING GATE MG105: the AnkiDroid directory is not accessible and no collection is open (the subscreen intent is started only in that branch of DeckPicker.onCreate, DeckPicker.java:415-427). No predefined ENV or STATE kind covers this. env and needs_state unset. The route: CompatV11.java:41-48 puts EXTRA_SHOW_FRAGMENT (the SettingsFragment name), the subscreen argument and EXTRA_NO_HEADERS; PreferenceActivity.onCreate skips the header build when headers are hidden (PreferenceActivity.java:606) and calls switchToHeader(initialFragment, initialArguments) (610-611); isValidFragment accepts this class name (Preferences.java:146-148); Fragment.instantiate creates the fragment (PreferenceActivity.java:1254).')

e('S_PREFERENCES', 'Preferences$SettingsFragment.<init>', 'GUI',
  'tap the Advanced row in the settings headers list',
  gui=['tap the Advanced row in the settings headers list'],
  env=None,
  evidence='SRC res/xml/preference_headers.xml:64-73; FW-SRC core/java/android/preference/PreferenceActivity.java:1079-1089, 1100-1106, 1295-1307, 1246-1256; FW-SRC core/java/android/app/Fragment.java:508-524',
  note='Page edge. The Advanced header names this fragment and carries the subscreen argument (preference_headers.xml:64-73). The tap runs onListItemClick and onHeaderClick (PreferenceActivity.java:1079-1089, 1100-1106); switchToHeader(Header) (1305) then creates the fragment. The headers are built by Preferences.onBuildHeaders (batch_015, a lead). The single-pane headers list on a phone is INFERRED: onIsMultiPane reads a resource that is not in fw_src.')

e('S_PREFERENCES', 'Preferences$SettingsFragment.onSharedPreferenceChanged', 'GUI',
  'change a preference value on the settings screen (a checkbox, a text field or a list choice)',
  gui=['change a preference value on the settings screen (a checkbox, a text field or a list choice)'],
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/Preferences.java:796, 806, 810-813; FW-SRC core/java/android/app/SharedPreferencesImpl.java:448, 491-500, 551-573; FW-SRC core/java/android/preference/Preference.java:1587, 1609',
  note='Page edge. The listener runs while the fragment is resumed (registered at Preferences.java:796, removed at 806), which the open settings page implies. The framework notifies it from SharedPreferencesImpl.notifyListeners (SharedPreferencesImpl.java:561) only for a key whose value changed; an equal value is skipped (SharedPreferencesImpl.java:497-500). needs_state=STATE_SETTINGS: the new value must differ from the stored one. The widgets that make the change (for example CheckBoxPreference) are framework classes outside this part. Other writers of the default preferences reach the same method while the fragment is resumed: leads for the batches that hold those writers.')


# ---- part 018 (2026-10-28)
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

# Guarded replacements for the unguarded auto CALLs from the mount receiver (auto_calls.json, line 118).
e('AnkiDroidWidgetSmall$UpdateService$1.onReceive', 'WidgetStatus.update', 'CALL',
  'the second media-mounted broadcast refreshes the small widget and unregisters the mount receiver',
  guard='the static remounted flag is already set: the first MEDIA_MOUNTED only sets it (AnkiDroidWidgetSmall.java:117-124)',
  env=None,
  evidence='SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:117-124',
  note='Replaces the unguarded auto CALL (auto_calls.json, line 118). The mount receiver itself is entered by the SYSTEM edge above, which carries MG123 and the predefined gates.')

e('AnkiDroidWidgetSmall$UpdateService$1.onReceive', 'WidgetStatus.<clinit>', 'CALL',
  'the second media-mounted broadcast triggers the first use of WidgetStatus in this process',
  guard='the same as the WidgetStatus.update edge above: the second MEDIA_MOUNTED broadcast (AnkiDroidWidgetSmall.java:117-124)',
  env=None,
  evidence='SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:117-118',
  note='Replaces the unguarded auto CALL (auto_calls.json, line 118). The class initialisation step is not in fw_src: INFERRED.')

# ---- part 015 (2026-10-28)
# AnkiDroid batch 015 (LABEL helper). Preferences part 1: the Preferences activity methods, the class initialiser,
# and the subscreen listeners Preferences$1 to Preferences$7. Preferences$8 and Preferences$SettingsFragment are batch 016.
# 40 methods; the full row list is in graphs/AnkiDroid/parts/label_015.md.
#
# Ownership: an edge is written in the part that holds its source method. For a page source (S_PREFERENCES) it is written
# in the part that holds the destination method, so the page edges into this part are written here.
# Written here: the page edges S_PREFERENCES -> (FRAMEWORK,
# GUI) into this part; the REGISTER edges from the <init>s of Preferences$2 to $7; the INTENT edges from $3, $6 and $7 into
# Preferences.<init>; the entry Preferences.<clinit> -> Preferences.<init>.
# Not written here: the bytecode CALL edges inside Preferences and from Preferences$SettingsFragment (auto_calls.json, batch 016);
# the lifecycle chain of graph_def.py line 200 (orchestrator; onCreateDialog was removed from it); the DeckPicker.onCreate ->
# Preferences.<init> INTENT edge (graph_def.py:1240, orchestrator); NavigationDrawerActivity.java:277 -> Preferences.<init>
# (batch 036).
#
# Gates (Missing gates are text only, in note=; env and needs_state are not set on those edges):
#   MG95 the Reviewing screen is open (its header was tapped; batch 016 starts it through SettingsFragment.onCreate)
#   MG96 the Advanced screen is open (its header was tapped)
#   MG97 the Custom buttons screen is open (it is started by the Custom buttons link, see Preferences$3)
#   MG98 the settings activity is started fresh (no saved state) and its start intent has no EXTRA_NO_HEADERS
#
# UNREACHABLE entries: Preferences.onCreateDialog, Preferences$1.<init>, Preferences$1.onPositive (closed_by_api_level: the
# only showDialog call sits in the fixHebrewText case, which needs a checked checkbox, and that checkbox is removed on SDK >= 16);
# Preferences.onSharedPreferenceChanged (closed_by_api_level: the activity is registered only in the isHoneycomb-false branch).
# Constants: none.

# ---- Page edges from the settings screen (S_PREFERENCES) into this part.
e('S_PREFERENCES', 'Preferences.onBuildHeaders', 'FRAMEWORK',
  'the framework builds the header list when the settings screen opens without EXTRA_NO_HEADERS',
  evidence='FW-SRC core/java/android/preference/PreferenceActivity.java:588, 605-607, 772-774; SRC com/ichi2/anki/Preferences.java:140-142',
  note='MISSING GATE MG98: the activity is started fresh (PreferenceActivity.java:588 is the saved-state test, the else branch at 605) and its start intent has no EXTRA_NO_HEADERS (PreferenceActivity.java:772-774). The navigation drawer start (NavigationDrawerActivity.java:277, batch 036) is a plain intent and reaches this edge; the CompatV11 subscreen intents set EXTRA_NO_HEADERS (CompatV11.java:47) and do not. env and needs_state unset.')

e('S_PREFERENCES', 'Preferences.isValidFragment', 'FRAMEWORK',
  'the framework checks the fragment name when the user opens a header, or when the activity starts with EXTRA_SHOW_FRAGMENT',
  evidence='FW-SRC core/java/android/preference/PreferenceActivity.java:610-611, 1246-1249, 1277-1286, 1295-1305, 968-973; SRC com/ichi2/anki/Preferences.java:146-148',
  note='The check is PreferenceActivity.java:1249 (switchToHeaderInner), reached from a header tap (switchToHeader(Header) at 1295-1305) or from the initial fragment at 610-611. The name in res/xml/preference_headers.xml is com.ichi2.anki.Preferences$SettingsFragment, so the method returns true. The subscreen intents of Preferences$3, $6 and $7 carry the same EXTRA_SHOW_FRAGMENT name. No gate: the check runs on every header tap or fragment start.')

e('S_PREFERENCES', 'Preferences.onKeyDown', 'GUI',
  'press the Back key on a settings screen',
  gui=['press the Back key on a settings screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:191-197; FW-SRC core/java/android/app/Activity.java:3255-3274',
  note='Preferences.onKeyDown handles Back only when event.getRepeatCount() is 0 (Preferences.java:192) and then calls closePreferences (auto CALL, Preferences.java:194). The step from Activity.dispatchKeyEvent (Activity.java:3272-3273, event.dispatch) to onKeyDown is inside KeyEvent, which is not printed (INFERRED). No ENV gate.')

e('S_PREFERENCES', 'Preferences.onOptionsItemSelected', 'GUI',
  'tap the Up (home) arrow in the action bar of a settings screen',
  gui=['tap the Up (home) arrow in the action bar of a settings screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:128-129, 152-158; SRC com/ichi2/ui/AppCompatPreferenceActivity.java:43; FW-SRC core/java/android/app/Activity.java:3439-3450',
  note='The home arrow is enabled at Preferences.java:128-129. The base class com/ichi2/ui/AppCompatPreferenceActivity.java overrides onCreate only (no onOptionsItemSelected or onKeyDown). The step from the AppCompat home button to Activity.onMenuItemSelected is INFERRED. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). The only menu case is android.R.id.home, which calls finish (Preferences.java:154-155).')

# ---- Subscreen listeners of initSubscreen. REGISTER from each <init> (the builder does not follow REGISTER for reachability;
# the route is the GUI edge from the page).
e('Preferences$2.<init>', 'Preferences$2.onPreferenceChange', 'REGISTER',
  'the reviewing screen sets the full-screen mode change listener on the fullscreenMode preference',
  evidence='SRC com/ichi2/anki/Preferences.java:242-248',
  note='onPreferenceChange is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$2.onPreferenceChange', 'GUI',
  'change the Full screen mode in the Reviewing screen',
  gui=['change the Full screen mode in the Reviewing screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:248-259; FW-SRC core/java/android/preference/Preference.java:1079-1081',
  note='MISSING GATE MG95: the Reviewing screen is open (its header was tapped). Preference.callChangeListener (Preference.java:1079-1081) calls the listener. The ListPreference change path that reaches callChangeListener is not printed (INFERRED). The value 2 with gestures off returns false and shows a toast (Preferences.java:251-256). env and needs_state unset.')

e('Preferences$3.<init>', 'Preferences$3.onPreferenceClick', 'REGISTER',
  'the reviewing screen sets the click listener on the custom_buttons_link preference',
  evidence='SRC com/ichi2/anki/Preferences.java:262-263',
  note='onPreferenceClick is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$3.onPreferenceClick', 'GUI',
  'tap Custom buttons in the Reviewing screen',
  gui=['tap Custom buttons in the Reviewing screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:262-270; FW-SRC core/java/android/preference/Preference.java:1129-1140',
  note='MISSING GATE MG95: the Reviewing screen is open. Preference.performClick calls onClick and then the listener (Preference.java:1137).')

e('Preferences$3.onPreferenceClick', 'Preferences.<init>', 'INTENT',
  'the custom buttons screen opens in a new settings activity (CompatV11 subscreen intent)',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:264-266; SRC com/ichi2/compat/CompatV11.java:41-49; SRC com/ichi2/compat/CompatHelper.java:35-36; SRC com/ichi2/compat/CompatV21.java:13; SRC com/ichi2/compat/CompatV19.java:21; SRC com/ichi2/compat/CompatV17.java:11; SRC com/ichi2/compat/CompatV16.java:27; SRC com/ichi2/compat/CompatV15.java:11; SRC com/ichi2/compat/CompatV12.java:10',
  note='On API 27 the Compat object is CompatV21 (CompatHelper.java:35-36). CompatV21 -> CompatV19 -> CompatV17 -> CompatV16 -> CompatV15 -> CompatV12 -> CompatV11 is the class chain, and getPreferenceSubscreenIntent is declared only in CompatV11 (line 41) and CompatV10 (line 183), so the CompatV11 version is inherited. The intent names Preferences and sets EXTRA_NO_HEADERS (CompatV11.java:47). MISSING GATE MG95 (the tap) applies. Preferences is android:exported="false" (AndroidManifest.xml:192-196), so only AnkiDroid starts it.')

e('Preferences$4.<init>', 'Preferences$4.onPreferenceClick', 'REGISTER',
  'the custom buttons screen sets the click listener on reset_custom_buttons',
  evidence='SRC com/ichi2/anki/Preferences.java:279-285; SRC res/xml/preferences_custom_buttons.xml:27-28',
  note='onPreferenceClick is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$4.onPreferenceClick', 'GUI',
  'tap Reset custom buttons in the Custom buttons screen',
  gui=['tap Reset custom buttons in the Custom buttons screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:285-305; SRC res/xml/preferences_custom_buttons.xml:27-28',
  note='MISSING GATE MG97: the Custom buttons screen is open. It is entered only through the INTENT edge Preferences$3.onPreferenceClick -> Preferences.<init> (MG95 for the tap there). env and needs_state unset.')

e('Preferences$5.<init>', 'Preferences$5.onPreferenceChange', 'REGISTER',
  'the advanced screen sets the change listener on the deckPath preference',
  evidence='SRC com/ichi2/anki/Preferences.java:311-312',
  note='onPreferenceChange is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$5.onPreferenceChange', 'GUI',
  'change the collection path (deckPath) in the Advanced screen',
  gui=['change the collection path (deckPath) in the Advanced screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:311-324; SRC res/xml/preferences_advanced.xml:31',
  note='MISSING GATE MG96: the Advanced screen is open. CollectionHelper.initializeAnkiDroidDirectory (auto CALL, Preferences.java:316) is in another batch and is not read here; it either returns or throws StorageAccessException (line 318, toast and false). env and needs_state unset.')

e('Preferences$6.<init>', 'Preferences$6.onPreferenceClick', 'REGISTER',
  'the advanced screen sets the click listener on custom_sync_server_link',
  evidence='SRC com/ichi2/anki/Preferences.java:326-327; SRC res/xml/preferences_advanced.xml:39',
  note='onPreferenceClick is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$6.onPreferenceClick', 'GUI',
  'tap Custom sync server in the Advanced screen',
  gui=['tap Custom sync server in the Advanced screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:326-334; SRC res/xml/preferences_advanced.xml:39; FW-SRC core/java/android/preference/Preference.java:1129-1140',
  note='MISSING GATE MG96: the Advanced screen is open (its header was tapped). env and needs_state unset.')

e('Preferences$6.onPreferenceClick', 'Preferences.<init>', 'INTENT',
  'the custom sync server screen opens in a new settings activity (CompatV11 subscreen intent)',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:329-331; SRC com/ichi2/compat/CompatV11.java:41-49',
  note='The intent is built by CompatV11.getPreferenceSubscreenIntent, inherited on API 27 (see the Preferences$3 INTENT edge). MISSING GATE MG96 (the tap in the Advanced screen) applies.')

e('Preferences$7.<init>', 'Preferences$7.onPreferenceClick', 'REGISTER',
  'the advanced screen sets the click listener on advanced_statistics_link',
  evidence='SRC com/ichi2/anki/Preferences.java:336-337; SRC res/xml/preferences_advanced.xml:132',
  note='onPreferenceClick is in this part. The route is the S_PREFERENCES GUI edge below.')

e('S_PREFERENCES', 'Preferences$7.onPreferenceClick', 'GUI',
  'tap Advanced statistics in the Advanced screen',
  gui=['tap Advanced statistics in the Advanced screen'],
  evidence='SRC com/ichi2/anki/Preferences.java:336-344; SRC res/xml/preferences_advanced.xml:132; FW-SRC core/java/android/preference/Preference.java:1129-1140',
  note='MISSING GATE MG96: the Advanced screen is open (its header was tapped). env and needs_state unset.')

e('Preferences$7.onPreferenceClick', 'Preferences.<init>', 'INTENT',
  'the advanced statistics screen opens in a new settings activity (CompatV11 subscreen intent)',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:339-341; SRC com/ichi2/compat/CompatV11.java:41-49',
  note='The intent is built by CompatV11.getPreferenceSubscreenIntent, inherited on API 27. MISSING GATE MG96 (the tap in the Advanced screen) applies.')

# ---- Class initialiser. The static array sCollectionPreferences makes Preferences.<clinit> a real method.
e('Preferences.<clinit>', 'Preferences.<init>', 'FRAMEWORK',
  'the instance is constructed after the class is initialised',
  env=None,
  evidence='SRC com/ichi2/anki/Preferences.java:99-100, 788, 799, 812',
  note='The entries into Preferences.<clinit> are the bytecode CALL edges from Preferences$SettingsFragment.onCreate (788), onResume (799) and onSharedPreferenceChanged (812), and from Preferences$8.onPreferenceClick (350), all in auto_calls.json and batch 016. The JVM class-initialiser rule is not in the dataset: INFERRED. The DeckPicker INTENT edge (graph_def.py:1240) goes straight to Preferences.<init> and skips this node.')

# ---- UNREACHABLE: closed on API 27.
UNREACHABLE['Preferences.onCreateDialog'] = (
    'closed_by_api_level',
    "The only showDialog call is Preferences.java:479, in the fixHebrewText case of updatePreference, and that case runs only when the checkbox is checked (Preferences.java:476-478). On API 27 the checkbox cannot be checked: removeUnnecessaryAdvancedPrefs removes fixHebrewText from category_workarounds for SDK >= 16 (Preferences.java:723-724), and CompatHelper.removeHiddenPreferences removes the fixHebrewText key for SDK >= 16 (CompatHelper.java:133-134). The framework reaches onCreateDialog(int) through Activity.createDialog only from showDialog or from restoreManagedDialogs, and restoreManagedDialogs rebuilds only a dialog that was shown before (Activity.java:1154-1157, 1167-1168, 3971-3978). So there is no route. The lc_chain list at graph_def.py:200 no longer names onCreateDialog, because the framework never calls it as a lifecycle step.",
    'SRC com/ichi2/anki/Preferences.java:201, 476-479, 707-709, 723-724; SRC com/ichi2/compat/CompatHelper.java:133-134; FW-SRC core/java/android/app/Activity.java:1154-1157, 1167-1168, 3971-3978',
    'SOURCE')

UNREACHABLE['Preferences$1.<init>'] = (
    'closed_by_api_level',
    "The only caller in auto_calls.json is onCreateDialog (Preferences.java:209). onCreateDialog is closed on API 27 (see Preferences.onCreateDialog), so the constructor never runs.",
    'SRC com/ichi2/anki/Preferences.java:201, 209, 479, 723-724',
    'SOURCE')

UNREACHABLE['Preferences$1.onPositive'] = (
    'closed_by_api_level',
    "The positive button callback of the Hebrew font dialog (Preferences.java:209-216). The dialog is built only in onCreateDialog, which is closed on API 27 (see Preferences.onCreateDialog), so no dialog exists and the callback never runs. Its body would start the VIEW intent for the Hebrew font link (lines 212-214).",
    'SRC com/ichi2/anki/Preferences.java:201, 209-216, 479, 723-724',
    'SOURCE')

UNREACHABLE['Preferences.onSharedPreferenceChanged'] = (
    'closed_by_api_level',
    "The activity is registered as an OnSharedPreferenceChangeListener only in the legacy onResume branch (Preferences.java:178-180), which runs only when CompatHelper.isHoneycomb() is false (CompatHelper.java:61-62). On API 27 the activity is never registered, so SharedPreferences does not call this method. Its only other caller would be the settings fragment, which registers itself (Preferences.java:796) and calls Preferences.updatePreference from its own onSharedPreferenceChanged (Preferences.java:811-812), not this method. The other registrations in the app (DeckOptions.java:521, FilteredDeckOptions.java:376) are in other classes.",
    'SRC com/ichi2/anki/Preferences.java:178-180, 224-225, 796, 811-812; SRC com/ichi2/compat/CompatHelper.java:61-62; SRC com/ichi2/anki/DeckOptions.java:521; SRC com/ichi2/anki/FilteredDeckOptions.java:376',
    'SOURCE')

# ---- part 015 sup (orchestrator, 2026-10-28): the legacy auto CALLs are dead on API 27, because the branches at
# Preferences.java:116 and 177 run only when CompatHelper.isHoneycomb() is false (CompatHelper.java:61-62, SDK_INT >= 11).
# initSubscreen, initAllPreferences and updatePreference stay reachable through Preferences$SettingsFragment (batch 016).
sup(('Preferences.onCreate', 'Preferences.initSubscreen'),
    ('Preferences.onCreate', 'Preferences.initAllPreferences'),
    ('Preferences.onResume', 'Preferences.updatePreference'))

# ---- part 015 sup 2 (orchestrator, 2026-10-28): Preferences.onCreateDialog is closed on API 27 (part 015 UNREACHABLE entry),
# so its auto CALL to the Hebrew dialog listener constructor never runs.
sup(('Preferences.onCreateDialog', 'Preferences$1.<init>'))

# ---- part 017 (2026-10-28)
# AnkiDroid batch 017 (LABEL helper). CardContentProvider (32 methods, with onCreate) and SdCardReceiver (<init> and onReceive).
# The 34 route rows (REACHABLE or UNREACHABLE, with route, kind, reason and source) are in graphs/AnkiDroid/parts/label_017.md.
#
# Route ownership: every CardContentProvider method in batch_017 is in this part, so the CALL edges between them come from
# auto_calls.json and are not written here. CardContentProvider.onCreate and SdCardReceiver.onReceive are not in
# batch_017.txt; the coordinator added their rows to this part (34 method rows). Their S_ENTRY edges are in graph_def.py:145
# and graph_def.py:149-150 and are not written here; the LIFECYCLE edge <init> -> onCreate is in graph_def.py:293.
# The broadcast edge SdCardReceiver.onReceive -> DeckPicker$18.onReceive was not in graph_def.py, so it is written below.
#
# Page edges from S_ENTRY are written here, because their destination method is in this part:
#   S_ENTRY -> CardContentProvider.<clinit>          process start (no env)
#   S_ENTRY -> query, insert, update, delete, bulkInsert, getType   another app calls ContentResolver (ENV_PROVIDER_CALL)
#   S_ENTRY -> SdCardReceiver.<init>                 MEDIA_MOUNTED or MEDIA_EJECT broadcast (ENV_SDCARD_EVENT)
#
# Gates: numbers only, in the note text (no constants added). Meanings used in the rows:
#   MG112 the caller holds com.ichi2.anki.permission.READ_WRITE_DATABASE (hasReadWritePermission true). Without it, on
#         API 27, the security check throws SecurityException (query 209-210, update 417-418, delete 674-675,
#         bulkInsert 711-712, insert 813-814). getType has no check (159-195).
#   MG113 the URI type case of the switch that the route names (query 222-, update 429-, delete 683-, insert 825-).
#   MG114 bulkInsert: match == NOTES (718) and the deckId query parameter parses as a long (719-727).
#   MG115 update SCHEDULE: cardOrd and noteID were set from the values (633-634) and getCard returns a card (635-636).
#   MG116 query SCHEDULE: the selection has deckID=... and selectDeckWithCheck returns true (326-334).
#   MG117 update DECK_SELECTED: the values have a DECK_ID key (651-657).
#   MG118 SDK_INT below 23 (CompatHelper.isMarshmallow false). Only path to knownRogueClient; not on API 27.
#   MG119 CollectionHelper.getCol returns a collection (else IllegalStateException at 214-215 for query; 420, 677, 816, 740 for the others).
#   MG120 SDK_INT >= 19 (KITKAT) in getCallingPackageSafe (1327-1329). The other branch (1330-1334) needs SDK_INT below 19.
#   MG121 query DECKS_ID: a due-tree node has the requested deck id (384-389).
#
# Judgement calls (also in label_017.md):
#   - No STATE gate on the entry edges. CollectionHelper.getCol (CollectionHelper.java:85-) opens or creates the collection,
#     so collection.anki2 need not exist before the call; a failed directory setup returns null (MG119).
#   - ENV_PROVIDER_CALL is used for getType too. Its permission text does not apply to getType, which has no check.
#   - knownRogueClient is closed_by_api_level (its only callers are behind an SDK check that holds on API 27), not
#     branch_never_taken. On API 22 and lower (minSdkVersion 10 in build.gradle:12) it is reachable.
#   - The binder hop from another process to ContentProvider.Transport is INFERRED: ContentProviderNative is not in fw_src.
#   - The ASYNC broadcast edge to DeckPicker$18.onReceive has no env; its registration condition is MISSING GATE MG112 in the note.

# --- Page entry edges (destination methods are in this batch).

e('S_ENTRY', 'CardContentProvider.<clinit>', 'ENTRY',
  'process start: the framework installs the manifest provider in the app process and loads its class',
  env=None,
  evidence='SRC com/ichi2/anki/provider/CardContentProvider.java:109-112, 139, 142; FW-SRC core/java/android/app/ActivityThread.java:5722, 6227-6228; SRC AndroidManifest.xml:324-330; INFERRED the process start that reaches installContentProviders (FW-SRC core/java/android/app/ActivityThread.java:5722) is not read in full',
  note='The static blocks (112, 142) and the FlashCardsContract.Note.<clinit> call (139) run here. Same process-start entry as CardContentProvider.onCreate in graph_def.py:145. No permission gate on the process start.')

e('CardContentProvider.<clinit>', 'CardContentProvider.<init>', 'FRAMEWORK',
  'the framework creates the provider instance after the class is initialized (Class.newInstance)',
  env=None,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:6227-6228; INFERRED Class.newInstance runs class initialization before the constructor (JVM behaviour, not in fw_src)',
  note='CardContentProvider has no explicit constructor (class at CardContentProvider.java:89), so <init> is the default constructor. The LIFECYCLE edge <init> -> onCreate is in graph_def.py:293.')

e('S_ENTRY', 'CardContentProvider.query', 'ENTRY',
  'another app calls ContentResolver.query on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:209-240, 581, 605; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:208; INFERRED the cross-process hop into Transport.query (ContentProviderNative.onTransact) is not in fw_src',
  note='No readPermission is declared in the manifest, so the framework allows the call (ContentProvider.java:581, 605). Both branches of Transport.query call ContentProvider.this.query (lines 228 and 240). The body needs MG112 (query 209-210).')

e('S_ENTRY', 'CardContentProvider.insert', 'ENTRY',
  'another app calls ContentResolver.insert on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:256-265, 663, 687; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:812; INFERRED the cross-process hop into Transport.insert is not in fw_src',
  note='No writePermission is declared, so the framework allows the call (ContentProvider.java:663, 687). The body needs MG112 (insert 813-814). bulkInsert reaches insert too, through super.bulkInsert (CardContentProvider.java:730).')

e('S_ENTRY', 'CardContentProvider.update', 'ENTRY',
  'another app calls ContentResolver.update on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:348-357, 663, 687; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:416; INFERRED the cross-process hop into Transport.update is not in fw_src',
  note='No writePermission is declared, so the framework allows the call (ContentProvider.java:663, 687). The body needs MG112 (update 417-418).')

e('S_ENTRY', 'CardContentProvider.delete', 'ENTRY',
  'another app calls ContentResolver.delete on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:333-341, 663, 687; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:673; INFERRED the cross-process hop into Transport.delete is not in fw_src',
  note='No writePermission is declared, so the framework allows the call (ContentProvider.java:663, 687). The body needs MG112 (delete 674-675).')

e('S_ENTRY', 'CardContentProvider.bulkInsert', 'ENTRY',
  'another app calls ContentResolver.bulkInsert on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:272-280, 663, 687; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:710; INFERRED the cross-process hop into Transport.bulkInsert is not in fw_src',
  note='No writePermission is declared, so the framework allows the call (ContentProvider.java:663, 687). The body needs MG112 (bulkInsert 711-712).')

e('S_ENTRY', 'CardContentProvider.getType', 'ENTRY',
  'another app calls ContentResolver.getType on the exported provider',
  env=ENV_PROVIDER_CALL,
  evidence='FW-SRC core/java/android/content/ContentProvider.java:249-252; SRC AndroidManifest.xml:324-330; SRC com/ichi2/anki/provider/CardContentProvider.java:159; INFERRED the cross-process hop into Transport.getType is not in fw_src',
  note='Transport.getType calls ContentProvider.this.getType directly (line 252), with no permission check. getType (159-195) has no permission check either, so MG112 does not apply here.')

e('S_ENTRY', 'SdCardReceiver.<init>', 'ENTRY',
  'system broadcast MEDIA_MOUNTED or MEDIA_EJECT for a file volume: the framework instantiates the manifest receiver',
  env=ENV_SDCARD_EVENT,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3141-3166; SRC AndroidManifest.xml:268-282; SRC com/ichi2/anki/receiver/SdCardReceiver.java:35; INFERRED the system delivers the broadcast to the manifest receiver (not in fw_src)',
  note='SdCardReceiver has no explicit constructor (class at SdCardReceiver.java:35), so <init> is the default constructor. The framework creates a new receiver for each broadcast (handleReceiver, newInstance at ActivityThread.java:3166). onReceive is entered by its own edge (graph_def.py:149), not through <init>.')

# --- Broadcast edge out of SdCardReceiver.onReceive (source method is in this batch, so this part writes it).

e('SdCardReceiver.onReceive', 'DeckPicker$18.onReceive', 'ASYNC',
  'the receiver re-broadcasts MEDIA_EJECT (line 47) or MEDIA_MOUNT (line 56); the runtime receiver DeckPicker$18.onReceive handles it (MEDIA_EJECT: onSdCardNotMounted; MEDIA_MOUNT: restartActivity)',
  env=None,
  evidence='SRC com/ichi2/anki/receiver/SdCardReceiver.java:42-47, 52-56; SRC com/ichi2/anki/DeckPicker.java:369, 751, 1674-1680; FW-SRC core/java/android/app/ContextImpl.java:965; FW-SRC core/java/android/content/BroadcastReceiver.java:327; INFERRED the ActivityManager delivers the broadcast to the runtime-registered receiver (not in fw_src)',
  note='DeckPicker$18 is batch_004, and no edge in graph_def.py names it yet. The receiver exists only while DeckPicker is alive: DeckPicker.onCreate registers it (369) and onDestroy unregisters it (751). MISSING GATE MG112: the DeckPicker activity is alive (it registered the receiver, DeckPicker.java:369, and has not unregistered it, DeckPicker.java:751). env and needs_state unset. Also absent from graph_def.py and owned by batch_004: the registration edge DeckPicker.registerExternalStorageListener -> DeckPicker$18.<init>.')

# --- UNREACHABLE entry (the one method in this batch with no route).

UNREACHABLE['CardContentProvider.knownRogueClient'] = (
    'closed_by_api_level',
    "knownRogueClient is called from shouldEnforceQueryOrInsertSecurity (CardContentProvider.java:199) and shouldEnforceUpdateSecurity (204), and only when CompatHelper.isMarshmallow() returns false (it is the first operand of ||). isMarshmallow is getSdkVersion() >= M, and getSdkVersion returns Build.VERSION.SDK_INT. On API 27 the first operand is true, so knownRogueClient is never evaluated. It runs only on devices below API 23 (MG118), which is not the API 27 target in handoff/SCHEMA_V2.md. On those older devices (minSdkVersion 10 in build.gradle:12) the method is reachable, so the label is for the API 27 target and the method is not dead code.",
    'SRC com/ichi2/anki/provider/CardContentProvider.java:199, 204; SRC com/ichi2/compat/CompatHelper.java:55-57, 69-71',
    'SOURCE')

# ---- part 017 addendum (orchestrator, 2026-10-28): the REGISTER edge that batch_004 did not write (registerExternalStorageListener,
# DeckPicker.java:1670-1680). REGISTER is documentation only; the route is the ASYNC edge above.
e('DeckPicker.registerExternalStorageListener', 'DeckPicker$18.<init>', 'REGISTER',
  'the activity registers the unmount receiver for MEDIA_EJECT and MEDIA_MOUNT in registerExternalStorageListener, called from onCreate',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:369, 751, 1670-1680',
  note='MISSING GATE MG112: the activity is alive (registered in onCreate, unregistered in onDestroy). env and needs_state unset.')

# ---- part 017 sup (orchestrator, 2026-10-28): shouldEnforceQueryOrInsertSecurity and shouldEnforceUpdateSecurity test
# CompatHelper.isMarshmallow() first (CardContentProvider.java:199, 204), so knownRogueClient is never evaluated on API 27.
sup(('CardContentProvider.shouldEnforceQueryOrInsertSecurity', 'CardContentProvider.knownRogueClient'),
    ('CardContentProvider.shouldEnforceUpdateSecurity', 'CardContentProvider.knownRogueClient'))

# ---- part 019 (2026-10-28)
# AnkiDroid batch 019 (LABEL helper). AbstractFlashcardViewer, part 1: 40 methods (scratch/batches/batch_019.txt).
# One row per method, judgment calls and spot checks: graphs/AnkiDroid/parts/label_019.md.
#
# Ownership: an edge belongs to the part that contains its source. The edges here have their source in this batch:
# editCard (the edit path into NoteEditor) and the DeckTask launch sites answerCard and dismiss. Their listeners
# (AbstractFlashcardViewer$8, declared at AbstractFlashcardViewer.java:484; AbstractFlashcardViewer$10, declared at
# AbstractFlashcardViewer.java:578) are in another part and are only named here.
# Auto CALL edges (graphs/AnkiDroid/auto_calls.json) are not re-added.
# Gate: STATE_CARDS on these edges (the study screen shows a card only when the deck has cards to study).
# MG132 to MG135 are missing gates. They are written in the .md rows only (env and needs_state unset there).

# --- editCard -> NoteEditor.<init> (edit mode). Required edge. Explicit intent, app to app: no framework gate.
e('AbstractFlashcardViewer.editCard', 'NoteEditor.<init>', 'INTENT',
  'the study screen opens the note editor in edit mode for the card on screen',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1183-1187',
  note='Edit mode: EXTRA_CALLER is CALLER_REVIEWER (AbstractFlashcardViewer.java:1185) and the card is kept in sEditorCard (AbstractFlashcardViewer.java:1186). NoteEditor reads it at NoteEditor.java:370-378 and finishes when it is null. The result returns through the EDIT_CURRENT_CARD branch of onActivityResult (AbstractFlashcardViewer.java:1081-1084), which is in another part. NoteEditor.<init> is labelled in the NoteEditor part.')

# --- answerCard launches DeckTask ANSWER_CARD with mAnswerCardHandler (AbstractFlashcardViewer$10).
e('AbstractFlashcardViewer.answerCard', 'AbstractFlashcardViewer$10.onPreExecute', 'ASYNC',
  'the answer task starts and calls the listener before its background work',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1320-1321, 578-585',
  note='The listener is declared at AbstractFlashcardViewer.java:578 in another part. onPreExecute calls blockControls (AbstractFlashcardViewer.java:584; auto CALL edge). The dispatch of the listener by the task is not read in this part: INFERRED.')

e('AbstractFlashcardViewer.answerCard', 'AbstractFlashcardViewer$10.onProgressUpdate', 'ASYNC',
  'the answer task publishes the next card and calls the listener',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1320-1321, 598-607; SRC com/ichi2/async/DeckTask.java:437, 457',
  note='DeckTask.doInBackgroundAnswerCard publishes the next card (DeckTask.java:457). The listener calls updateTypeAnswerInfo (AbstractFlashcardViewer.java:604) and displayCardQuestion (AbstractFlashcardViewer.java:607), both auto CALL edges. A null card means no more cards (AbstractFlashcardViewer.java:599-601).')

e('AbstractFlashcardViewer.answerCard', 'AbstractFlashcardViewer$10.onPostExecute', 'ASYNC',
  'the answer task finishes and calls the listener',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1320-1321, 631-641',
  note='onPostExecute closes the reviewer on failure (AbstractFlashcardViewer.java:634) and when no more cards are left (AbstractFlashcardViewer.java:640). Both calls are auto CALL edges to closeReviewer.')

# --- dismiss launches DeckTask DISMISS with mDismissCardHandler (AbstractFlashcardViewer$8).
e('AbstractFlashcardViewer.dismiss', 'AbstractFlashcardViewer$8.onPostExecute', 'ASYNC',
  'the dismiss task finishes and calls its listener',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2825, 484, 497-502',
  note='The listener mDismissCardHandler is declared at AbstractFlashcardViewer.java:484 and is in another part. onPostExecute calls closeReviewer on failure (AbstractFlashcardViewer.java:499; auto CALL edge) and forwards the result to mAnswerCardHandler.onPostExecute (AbstractFlashcardViewer.java:501).')

# --- finishNoStorageAvailable: its only caller is onActivityResult for result code 202 (DeckPicker.RESULT_MEDIA_EJECTED).
UNREACHABLE['AbstractFlashcardViewer.finishNoStorageAvailable'] = (
    'no_trigger_in_app',
    "The only caller is onActivityResult, when resultCode equals DeckPicker.RESULT_MEDIA_EJECTED (202; AbstractFlashcardViewer.java:1067-1068). "
    "In the app's Java sources the constant is referenced at AbstractFlashcardViewer.java:1067 (the guard) and 1178 (the setResult inside this method, the only setter), "
    "at StudyOptionsFragment.java:401 and DeckPicker.java:637 (readers only), and at its definition DeckPicker.java:119. "
    "The literal 202 appears nowhere else, and finishNoStorageAvailable has no other caller. "
    "So this activity can receive 202 only from a child activity that already returns 202, and the only code that produces 202 is this method. "
    "The chain has no first step in the app. The framework passes a child's result code to the parent and does not create codes. confirmed_by SOURCE.",
    'SRC com/ichi2/anki/AbstractFlashcardViewer.java:1067-1068, 1177-1180; com/ichi2/anki/DeckPicker.java:119, 637; com/ichi2/anki/StudyOptionsFragment.java:401',
    'SOURCE')

# --- calculateDynamicFontSize: the only call is under if (mCurrentCard == null) in updateCard. Both callers of updateCard
# dereference or guard mCurrentCard before the call, so the branch is never taken.
UNREACHABLE['AbstractFlashcardViewer.calculateDynamicFontSize'] = (
    'branch_never_taken',
    "The only call is in updateCard under if (mCurrentCard == null) (AbstractFlashcardViewer.java:2063-2064). "
    "updateCard has two callers. displayCardQuestion dereferences mCurrentCard (AbstractFlashcardViewer.java:1922) before it calls updateCard (L1943). "
    "displayCardAnswer returns when mCurrentCard is null (L1995-1997) before it calls updateCard (L2028). "
    "So a null card would throw before updateCard runs, and the branch is never taken. "
    "The Reviewer and Previewer variants run the same inherited code. confirmed_by SOURCE.",
    'SRC com/ichi2/anki/AbstractFlashcardViewer.java:1922, 1943, 1995-1997, 2028, 2063-2064',
    'SOURCE')

# ---- part 019 sup (orchestrator, 2026-10-28): both methods are closed on this path (see part 019 UNREACHABLE entries).
sup(('AbstractFlashcardViewer.onActivityResult', 'AbstractFlashcardViewer.finishNoStorageAvailable'),
    ('AbstractFlashcardViewer.onActivityResult@Previewer', 'AbstractFlashcardViewer.finishNoStorageAvailable'),
    ('AbstractFlashcardViewer.onActivityResult@Reviewer', 'AbstractFlashcardViewer.finishNoStorageAvailable'),
    ('AbstractFlashcardViewer.updateCard', 'AbstractFlashcardViewer.calculateDynamicFontSize'),
    ('AbstractFlashcardViewer.updateCard@Previewer', 'AbstractFlashcardViewer.calculateDynamicFontSize'),
    ('AbstractFlashcardViewer.updateCard@Reviewer', 'AbstractFlashcardViewer.calculateDynamicFontSize'))

# ---- part 021 (2026-10-28)
# AnkiDroid batch 021 (LABEL helper). AbstractFlashcardViewer part 3: $1.handleMessage, $2 to $6, $7.<init>, and $10 to $21
# (40 methods in graphs/AnkiDroid/scratch/batches/batch_021.txt). The full row list is in graphs/AnkiDroid/parts/label_021.md.
#
# Ownership: AbstractFlashcardViewer$1.<init> is batch_020; $7.onLongClick, $8, $9 and the MyGestureDetector callbacks are
# batch_022; initLayout, initControls, initTimer, createWebView, answerCard, displayCardQuestion, displayCardAnswer and
# delayedHide are batch_019; onActivityResult, registerExternalStorageListener, showDeleteNoteDialog and undo are batch_020.
# Edges written here all have a source method of batch 021. Edges from other batches into these methods are leads in
# label_021.md.
#
# Auto CALL edges (the <init> edges of the anonymous classes, and callee calls such as answerCard, displayCardAnswer,
# displayCardQuestion, executeCommand, setFullScreen) come from auto_calls.json and are not written here.
#
# REGISTER edges go from $N.<init> to each callback. The builder does not follow REGISTER for reachability, so each
# callback's route is written by the part that calls it (see the leads in label_021.md).
#
# Gates: MG152 to MG156 are used on the edges below. Gates whose only condition is a predefined ENV_ or STATE_ kind are not
# used here. env and needs_state are unset on every MG edge.

# --- REGISTER edges from the anonymous-class constructors to their callbacks.
e('AbstractFlashcardViewer$2.<init>', 'AbstractFlashcardViewer$2.run', 'REGISTER',
  'the long-click test runnable is a field of AbstractFlashcardViewer and is created with the viewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:359-372',
  note='The builder does not follow REGISTER for reachability. The route into run is AbstractFlashcardViewer$6.onTouch -> $2.run (FRAMEWORK, below).')

e('AbstractFlashcardViewer$3.<init>', 'AbstractFlashcardViewer$3.run', 'REGISTER',
  'the start-long-click runnable is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:373-378',
  note='The builder does not follow REGISTER for reachability. The route into run is AbstractFlashcardViewer$2.run -> $3.run (FRAMEWORK, below).')

e('AbstractFlashcardViewer$4.<init>', 'AbstractFlashcardViewer$4.onClick', 'REGISTER',
  'the show-answer listener is set on the flip-card layout in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:382-395, 1384',
  note='The builder does not follow REGISTER. The registration is at line 1384 (initLayout, owned by batch_019); the route is the lead in label_021.md.')

e('AbstractFlashcardViewer$5.<init>', 'AbstractFlashcardViewer$5.onClick', 'REGISTER',
  'the ease-button listener is set on the four ease layouts in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:396-426, 1348, 1353, 1358, 1363',
  note='The builder does not follow REGISTER. Registrations at lines 1348, 1353, 1358 and 1363 (initLayout, batch_019). The route is the lead in label_021.md.')

e('AbstractFlashcardViewer$6.<init>', 'AbstractFlashcardViewer$6.onTouch', 'REGISTER',
  'the gesture and long-click touch listener is set on the touch layer in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:428-466, 1333',
  note='The builder does not follow REGISTER. The registration is mTouchLayer.setOnTouchListener at line 1333 (initLayout, batch_019).')

e('AbstractFlashcardViewer$7.<init>', 'AbstractFlashcardViewer$7.onLongClick', 'REGISTER',
  'the long-click listener is set on the touch layer in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:468-481, 1335',
  note='onLongClick is batch_022. The builder does not follow REGISTER. The registration is at line 1335 (initLayout, batch_019).')

e('AbstractFlashcardViewer$10.<init>', 'AbstractFlashcardViewer$10.onPreExecute', 'REGISTER',
  'the answer-card task listener (mAnswerCardHandler) is a field; DeckTask calls its callbacks',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-651, 1320-1321',
  note='The builder does not follow REGISTER. The ASYNC route from AbstractFlashcardViewer.answerCard is written in label_019.py. Other ANSWER_CARD and UNDO launches with this listener are leads in label_021.md.')

e('AbstractFlashcardViewer$10.<init>', 'AbstractFlashcardViewer$10.onProgressUpdate', 'REGISTER',
  'the answer-card task listener (mAnswerCardHandler) is a field; DeckTask calls its callbacks',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-651, 1320-1321',
  note='The builder does not follow REGISTER. The ASYNC route from AbstractFlashcardViewer.answerCard is written in label_019.py. Other ANSWER_CARD and UNDO launches with this listener are leads in label_021.md.')

e('AbstractFlashcardViewer$10.<init>', 'AbstractFlashcardViewer$10.onPostExecute', 'REGISTER',
  'the answer-card task listener (mAnswerCardHandler) is a field; DeckTask calls its callbacks',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-651, 1320-1321',
  note='The builder does not follow REGISTER. The ASYNC route from AbstractFlashcardViewer.answerCard is written in label_019.py. Other ANSWER_CARD and UNDO launches with this listener are leads in label_021.md.')

e('AbstractFlashcardViewer$10.<init>', 'AbstractFlashcardViewer$10.onCancelled', 'REGISTER',
  'the answer-card task listener (mAnswerCardHandler) is a field; DeckTask calls its callbacks',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-651; SRC com/ichi2/async/DeckTask.java:368-369',
  note='The builder does not follow REGISTER. onCancelled is UNREACHABLE (no_trigger_in_app, below), so no route is written for it.')

e('AbstractFlashcardViewer$11.<init>', 'AbstractFlashcardViewer$11.run', 'REGISTER',
  'the chosen-answer clearing runnable is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:825-830',
  note='The builder does not follow REGISTER. The route is the FRAMEWORK edge AbstractFlashcardViewer.answerCard -> $11.run (batch_019, line 1316), a lead in label_021.md.')

e('AbstractFlashcardViewer$12.<init>', 'AbstractFlashcardViewer$12.onReceive', 'REGISTER',
  'the unmount receiver is created in registerExternalStorageListener and registered at line 1137',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1127-1134, 1137',
  note='The builder does not follow REGISTER. registerExternalStorageListener is batch_020; the broadcast source is a lead in label_021.md.')

e('AbstractFlashcardViewer$13.<init>', 'AbstractFlashcardViewer$13.onPositive', 'REGISTER',
  'the delete-note dialog callback is created in showDeleteNoteDialog',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1248-1254',
  note='The builder does not follow REGISTER. The route is the dialog callback edge from showDeleteNoteDialog (batch_020, lead in label_021.md).')

e('AbstractFlashcardViewer$14.<init>', 'AbstractFlashcardViewer$14.onClick', 'REGISTER',
  'the lookup icon listener is set in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1418-1428',
  note='The builder does not follow REGISTER. Registration at line 1418 (initLayout, batch_019). The route is the GUI lead from the S_REVIEWER page (label_021.md).')

e('AbstractFlashcardViewer$15.<init>', 'AbstractFlashcardViewer$15.shouldOverrideUrlLoading', 'REGISTER',
  'the WebViewClient is set on the card web view in createWebView',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1454, 1458; FW-SRC core/java/android/webkit/WebViewClient.java:49',
  note='The builder does not follow REGISTER. The registration is at line 1454 (createWebView, batch_019). The route is the WebView link-navigation lead in label_021.md.')

e('AbstractFlashcardViewer$15.<init>', 'AbstractFlashcardViewer$15.onPageFinished', 'REGISTER',
  'the WebViewClient is set on the card web view in createWebView',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1454, 1542-1545',
  note='The builder does not follow REGISTER. The registration is at line 1454 (createWebView, batch_019). The route is the WebView page-finished lead in label_021.md.')

e('AbstractFlashcardViewer$16.<init>', 'AbstractFlashcardViewer$16.onEditorAction', 'REGISTER',
  'the answer-field editor action listener is set in initControls',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1689-1698; FW-SRC core/java/android/widget/TextView.java:7430',
  note='The builder does not follow REGISTER. Registration at line 1689 (initControls, batch_019).')

e('AbstractFlashcardViewer$17.<init>', 'AbstractFlashcardViewer$17.onKey', 'REGISTER',
  'the answer-field key listener is set in initControls',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1699-1709; FW-SRC core/java/android/view/View.java:11709',
  note='The builder does not follow REGISTER. Registration at line 1699 (initControls, batch_019).')

e('AbstractFlashcardViewer$18.<init>', 'AbstractFlashcardViewer$18.run', 'REGISTER',
  'the show-question timeout runnable is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1863-1871, 2031-2033',
  note='The builder does not follow REGISTER. The route is the postDelayed lead from displayCardAnswer (batch_019, line 2033).')

e('AbstractFlashcardViewer$19.<init>', 'AbstractFlashcardViewer$19.run', 'REGISTER',
  'the show-answer timeout runnable is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1873-1880, 1947-1949',
  note='The builder does not follow REGISTER. The route is the postDelayed lead from displayCardQuestion (batch_019, line 1949).')

e('AbstractFlashcardViewer$20.<init>', 'AbstractFlashcardViewer$20.onChronometerTick', 'REGISTER',
  'the card timer tick listener is set in initTimer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1901-1910',
  note='The builder does not follow REGISTER. Registration at line 1901 (initTimer, batch_019). Chronometer is not in fw_src: INFERRED.')

e('AbstractFlashcardViewer$21.<init>', 'AbstractFlashcardViewer$21.handleMessage', 'REGISTER',
  'the fullscreen handler is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2763-2770, 2772-2775',
  note='The builder does not follow REGISTER. The route is the FRAMEWORK lead from delayedHide (batch_019, line 2774).')

# --- FRAMEWORK edges from a listener of this batch to a callback that the framework dispatches, or that a view performs.
e('AbstractFlashcardViewer$2.run', 'AbstractFlashcardViewer$3.run', 'FRAMEWORK',
  'the 300 ms long-click timer posts the start-long-click runnable',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:364, 370; FW-SRC core/java/android/os/Handler.java:427',
  note='No gate: the post at line 370 is unconditional in run (the if at line 364 only controls the lookup toast). run is posted by AbstractFlashcardViewer$6.onTouch (800 ms, line 438).')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$2.run', 'FRAMEWORK',
  'an ACTION_DOWN touch posts the long-click test runnable after 800 ms',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:430-438; FW-SRC core/java/android/os/Handler.java:427',
  note='MISSING GATE MG152: the post at line 438 runs only when the gesture detector did not consume the event (line 431), the action is ACTION_DOWN (line 436), and the two flags at line 434 (mDisableClipboard and mLongClickWorkaround) are both false. The detector result and the flags form one condition that no predefined ENV or STATE kind covers. env and needs_state unset.')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$MyGestureDetector.onFling', 'FRAMEWORK',
  'a fling on the touch layer: the gesture detector created in initLayout dispatches it from onTouchEvent',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:431, 1343, 2661, 2664; FW-SRC core/java/android/view/GestureDetector.java:115, 490, 655',
  note='The gesture is input, not a gate. MyGestureDetector (line 2661) extends SimpleOnGestureListener, so onFling is batch_022; it is written here because the source is in batch 021. The dispatch in GestureDetector.onTouchEvent is at line 655. The hop from GestureDetectorCompat (line 1343) to the framework GestureDetector is not in fw_src: INFERRED.')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$MyGestureDetector.onDoubleTap', 'FRAMEWORK',
  'a double tap on the touch layer: the gesture detector dispatches it from onTouchEvent',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:431, 1343, 2711; FW-SRC core/java/android/view/GestureDetector.java:142, 565',
  note='The gesture is input, not a gate. The dispatch is GestureDetector.onTouchEvent at line 565; the GestureDetectorCompat hop is not in fw_src: INFERRED. The callback is batch_022.')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$MyGestureDetector.onSingleTapUp', 'FRAMEWORK',
  'a single-tap-up on the touch layer: the gesture detector dispatches it from onTouchEvent',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:431, 1343, 2720; FW-SRC core/java/android/view/GestureDetector.java:75, 640',
  note='The gesture is input, not a gate. The dispatch is GestureDetector.onTouchEvent at line 640; the GestureDetectorCompat hop is not in fw_src: INFERRED. The callback is batch_022.')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$MyGestureDetector.onSingleTapConfirmed', 'FRAMEWORK',
  'a confirmed single tap on the touch layer: the gesture detector dispatches it from onTouchEvent',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:431, 1343, 2730; FW-SRC core/java/android/view/GestureDetector.java:134, 642',
  note='The gesture is input, not a gate. The dispatch is GestureDetector.onTouchEvent at line 642; the GestureDetectorCompat hop is not in fw_src: INFERRED. The callback is batch_022.')

e('AbstractFlashcardViewer$15.shouldOverrideUrlLoading', 'AbstractFlashcardViewer$1.handleMessage', 'FRAMEWORK',
  'the card link with the playsound: scheme is intercepted and its sound path is sent to the handler that plays it',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1458-1465; FW-SRC core/java/android/os/Handler.java:97, 536',
  note='MISSING GATE MG153: the card page must contain a sound link that produces a playsound: URL, and the user must tap it (the URL comes from the card HTML and page JavaScript, not in this dataset). No predefined kind covers it. env and needs_state unset.')

e('AbstractFlashcardViewer$15.shouldOverrideUrlLoading', 'AbstractFlashcardViewer$4.onClick', 'FRAMEWORK',
  'the typeentertext: link performs a click on the flip-card layout, which calls the show-answer listener',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1477-1483; FW-SRC core/java/android/view/View.java:6289-6294',
  note='MISSING GATE MG154: the card must be a type-in-the-answer card (typeAnswer() true, line 1688) and the user must press Enter in the typing box so the page loads the typeentertext: URL. No predefined kind covers it. env and needs_state unset.')

e('AbstractFlashcardViewer$18.run', 'AbstractFlashcardViewer$5.onClick', 'FRAMEWORK',
  'the auto-advance question timer clicks the Again (ease 1) layout, which calls the ease listener',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1863-1871, 2031-2033; FW-SRC core/java/android/view/View.java:6289-6294',
  note='MISSING GATE MG155: the timer is posted only when mPrefUseTimer and mWaitQuestionSecond > 0 (line 2031, displayCardAnswer), and the click happens only when mEase1Layout is enabled and visible (line 1867, checked in run). No predefined kind covers the view state. env and needs_state unset.')

e('AbstractFlashcardViewer$19.run', 'AbstractFlashcardViewer$4.onClick', 'FRAMEWORK',
  'the auto-advance answer timer clicks the flip-card layout, which calls the show-answer listener',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1873-1880, 1947-1949; FW-SRC core/java/android/view/View.java:6289-6294',
  note='MISSING GATE MG156: the timer is posted only when mPrefUseTimer and mWaitAnswerSecond > 0 (line 1947, displayCardQuestion), and the click happens only when mFlipCardLayout is enabled and visible (line 1876, checked in run). No predefined kind covers the view state. env and needs_state unset.')

# --- UNREACHABLE
UNREACHABLE['AbstractFlashcardViewer$10.onCancelled'] = (
    'no_trigger_in_app',
    "AsyncTask calls onCancelled only after cancel(true) on the task (FW-SRC AsyncTask.java:462-463 and 479). DeckTask forwards the call to its listener (DeckTask.java:368-369). "
    "The only app code that cancels a DeckTask is DeckTask.cancelTask() and cancelTask(int) (DeckTask.java:168-186). cancelTask(int) cancels only when the latest task has the given type, and "
    "every caller passes TASK_TYPE_SEARCH_CARDS or TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). No caller passes a type that this listener serves: "
    "TASK_TYPE_ANSWER_CARD (DeckTask.java:69) is launched at AbstractFlashcardViewer.java:1076, 1092 and 1320-1321 and at Reviewer.java:110, and TASK_TYPE_UNDO is launched at AbstractFlashcardViewer.java:1172, "
    "all with mAnswerCardHandler. TaskOperations.stopTaskGracefully (TaskOperations.java:30-33) is called only with other activities' tasks (LoadPronounciationActivity.java:474-478, TranslationActivity.java:405). "
    "No code in the dataset cancels this listener's task, so onCancelled never runs.",
    'SRC com/ichi2/anki/AbstractFlashcardViewer.java:578, 649-651, 1076, 1092, 1172, 1320-1321; SRC com/ichi2/anki/Reviewer.java:110; SRC com/ichi2/async/DeckTask.java:69, 168-186, 368-369; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-33; SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405; FW-SRC core/java/android/os/AsyncTask.java:462-463, 479',
    'SOURCE')

# ---- part 021 sup (orchestrator, 2026-10-28): only SEARCH_CARDS and RENDER_BROWSER_QA are cancelled (DeckTask.java:181-185), so the answer-card listener never gets onCancelled
sup(('DeckTask.onCancelled', 'AbstractFlashcardViewer$10.onCancelled'))

# ---- part 022 (2026-10-28)
# AnkiDroid batch 022 (LABEL helper). AbstractFlashcardViewer part 4: 25 methods. The full row list is in
# graphs/AnkiDroid/parts/label_022.md. Methods: $7.onLongClick, $8 and $9 (DeckTask.TaskListener anonymous classes),
# $AnkiDroidWebChromeClient, $MyGestureDetector, $MyWebView and the two scroll runnables $MyWebView$1 and $MyWebView$2.
#
# Route ownership:
# - CALL edges from the outer constructor, createWebView and initLayout into the inner <init> methods, and the
#   DeckTask.TaskListener default calls into $8 and $9 (DeckTask.java 1300, 1306, 1312), come from auto_calls.json.
#   They are not written here. Neither are the in-method CALL edges that auto_calls.json already holds.
# - The ASYNC launch edges into $8 and $9 (DismissCard in dismiss, batch 019, and UPDATE_FACT in onActivityResult)
#   are not written here. label_019.py:43 writes the one into $8.onPostExecute.
# - The run body of the long-click runnable ($3.run, AbstractFlashcardViewer.java:373-378) is batch 021. The ASYNC edge
#   into it from $7.onLongClick is written here, because the source is in this batch.
# - Extractor anomaly: auto_calls.json maps $8.onProgressUpdate (AbstractFlashcardViewer.java:492) and $8.onPostExecute
#   (:501) to $8 itself, but the source calls mAnswerCardHandler ($10). No CALL edge is written for this; it is a lead.
#
# Gates: MG162-MG166 (batch range MG162-MG171). Predefined constants used: STATE_SETTINGS (long-click registration,
# which needs two preferences), STATE_CARDS (gesture edges). Page node: S_REVIEWER.

# --- Long-click on the touch layer (registered in initLayout, AbstractFlashcardViewer.java:1334-1335).
e('S_REVIEWER', 'AbstractFlashcardViewer$7.onLongClick', 'GUI',
  'long-press the card area (the touch layer) when the long-click workaround is on',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['long-press the card area (the touch layer) when the long-click workaround is on'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:468-481, 1333-1336, 1719-1720; FW-SRC core/java/android/view/View.java:6368-6374',
  note='The listener is set only when !mDisableClipboard and mLongClickWorkaround (the dictionary preference is not "0", and textSelectionLongclickWorkaround is true). The two preferences are STATE_SETTINGS. The long-press dispatch is View.performLongClickInternal (View.java:6368-6374).')

e('AbstractFlashcardViewer$7.onLongClick', 'AbstractFlashcardViewer$3.run', 'ASYNC',
  'the long-click handler posts the start-long-click runnable with a 300 ms delay',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:373-378, 478; FW-SRC core/java/android/os/Handler.java:427, 97-98, 789-790',
  note='The run body (executeCommand(mGestureLongclick)) is batch 021. The post is in this batch (AbstractFlashcardViewer.java:478). The dispatch to run is the Handler route in fw_src.')

# --- WebChromeClient (created in createWebView, AbstractFlashcardViewer.java:1448).
e('S_REVIEWER', 'AbstractFlashcardViewer$AnkiDroidWebChromeClient.onJsAlert', 'FRAMEWORK',
  'the card content runs a JavaScript alert(); the WebView calls the chrome client onJsAlert',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1448, 2583-2590',
  note='MISSING GATE MG162: the card HTML must call alert() (a card template with a script that runs alert). No predefined ENV or STATE kind covers the card content. env and needs_state unset. The WebView dispatch to WebChromeClient is not in fw_src: INFERRED.')

# --- MyWebView (created in createWebView, AbstractFlashcardViewer.java:1436).
e('S_REVIEWER', 'AbstractFlashcardViewer$MyWebView.onCheckIsTextEditor', 'FRAMEWORK',
  'an input method (keyboard) attached to the card WebView asks whether the view is a text editor',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1436, 1727, 2622-2628; FW-SRC core/java/android/view/View.java:12527',
  note='MISSING GATE MG163: an input method is attached to the card WebView (the card view has the focus). The override returns true only when mInputWorkaround is set (the input workaround preference, AbstractFlashcardViewer.java:1727), and super otherwise. The IME dispatch is not in fw_src: INFERRED. env and needs_state unset.')

e('S_REVIEWER', 'AbstractFlashcardViewer$MyWebView.onScrollChanged', 'GUI',
  'drag or fling the card content so that the card WebView scrolls',
  env=None,
  gui=['drag or fling the card content so that the card WebView scrolls'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2632-2643; FW-SRC core/java/android/view/View.java:13505, 15226-15239',
  note='MISSING GATE MG164: the card content is larger than the card WebView, so a drag moves it (a content scroll). The WebView content scroll that calls onScrollChanged is Chromium code, not in fw_src: INFERRED. env and needs_state unset.')

e('AbstractFlashcardViewer$MyWebView.onScrollChanged', 'AbstractFlashcardViewer$MyWebView$1.run', 'ASYNC',
  'a horizontal scroll change posts the x-scroll reset runnable with a 300 ms delay',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2634-2637, 2646-2650; FW-SRC core/java/android/os/Handler.java:427, 97-98, 789-790',
  note='MISSING GATE MG165: the horizontal branch is taken only when abs(horiz - oldHoriz) is larger than abs(vert - oldVert) (AbstractFlashcardViewer.java:2634). env and needs_state unset.')

e('AbstractFlashcardViewer$MyWebView.onScrollChanged', 'AbstractFlashcardViewer$MyWebView$2.run', 'ASYNC',
  'a vertical scroll change posts the y-scroll reset runnable with a 300 ms delay',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2634, 2638-2641, 2652-2656; FW-SRC core/java/android/os/Handler.java:427, 97-98, 789-790',
  note='MISSING GATE MG166: the else branch is taken when abs(vert - oldVert) is at least abs(horiz - oldHoriz) (AbstractFlashcardViewer.java:2634, 2638). env and needs_state unset.')

# --- MyGestureDetector (created in initLayout, AbstractFlashcardViewer.java:1343; the touch layer uses it at 1333).
e('S_REVIEWER', 'AbstractFlashcardViewer$MyGestureDetector.onDoubleTap', 'GUI',
  'double-tap the card area (a second tap within the double-tap timeout)',
  env=None,
  needs_state=STATE_CARDS,
  gui=['double-tap the card area (a second tap within the double-tap timeout)'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1333, 1343, 2711-2716; FW-SRC core/java/android/view/GestureDetector.java:565',
  note='The command runs only when mGesturesEnabled is set (AbstractFlashcardViewer.java:2711-2716; set from AnkiDroidApp.initiateGestures at 1737). The second-tap branch is GestureDetector.java:565.')

e('S_REVIEWER', 'AbstractFlashcardViewer$MyGestureDetector.onFling', 'GUI',
  'swipe across the card area (a fling longer than the swipe thresholds)',
  env=None,
  needs_state=STATE_CARDS,
  gui=['swipe across the card area (a fling longer than the swipe thresholds)'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1333, 1343, 2664-2707; FW-SRC core/java/android/view/GestureDetector.java:655',
  note='The swipe commands run only when mGesturesEnabled is set (AbstractFlashcardViewer.java:2670). The fling branch is GestureDetector.java:655.')

e('S_REVIEWER', 'AbstractFlashcardViewer$MyGestureDetector.onSingleTapConfirmed', 'GUI',
  'single tap on the card area with no second tap',
  env=None,
  needs_state=STATE_CARDS,
  gui=['single tap on the card area with no second tap'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1333, 1343, 2730-2759; FW-SRC core/java/android/view/GestureDetector.java:642',
  note='The tap-zone commands run only when mGesturesEnabled is set and no text selection is active (mIsSelecting, AbstractFlashcardViewer.java:2730-2759). The confirm call is GestureDetector.java:642 (ACTION_UP with the double-tap listener set).')

e('S_REVIEWER', 'AbstractFlashcardViewer$MyGestureDetector.onSingleTapUp', 'GUI',
  'lift the finger after a tap on the card area',
  env=None,
  needs_state=STATE_CARDS,
  gui=['lift the finger after a tap on the card area'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1333, 1343, 2720-2726; FW-SRC core/java/android/view/GestureDetector.java:640',
  note='The body only clears mTouchStarted and removes longClickTestRunnable, then returns false. No command runs from this callback.')

# --- UNREACHABLE: no DISMISS (type 11) or UPDATE_FACT (type 7) DeckTask is ever cancelled, so onCancelled never runs.
_CANCEL_REASON = ("DeckTask.onCancelled calls the listener onCancelled (DeckTask.java:368-370) only after a cancel. "
                  "The in-app cancels of a DeckTask all go through DeckTask.cancelTask(int) (DeckTask.java:181-184), "
                  "which cancels the latest task only when its mType equals the argument. The only callers pass "
                  "TASK_TYPE_SEARCH_CARDS (30) and TASK_TYPE_RENDER_BROWSER_QA (37) (CardBrowser.java:528-529, 796-797, 1155). "
                  "The no-argument cancelTask() (DeckTask.java:168-178) has no caller besides cancelTask(int). "
                  "The other cancel(true) calls act on non-DeckTask tasks: TaskOperations.stopTaskGracefully (TaskOperations.java:33), "
                  "Connection (Connection.java:541), Statistics (Statistics.java:543, 574, 681, 692). "
                  "So the DISMISS task (DeckTask.java:73) and the UPDATE_FACT task (DeckTask.java:71) are never cancelled.")
_CANCEL_SOURCE = ('SRC com/ichi2/async/DeckTask.java:168-184, 368-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
                  'SRC com/ichi2/anki/runtimetools/TaskOperations.java:33; SRC com/ichi2/async/Connection.java:541; '
                  'SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692')

UNREACHABLE['AbstractFlashcardViewer$8.onCancelled'] = ('no_trigger_in_app', _CANCEL_REASON, _CANCEL_SOURCE, 'SOURCE')
UNREACHABLE['AbstractFlashcardViewer$9.onCancelled'] = ('no_trigger_in_app', _CANCEL_REASON, _CANCEL_SOURCE, 'SOURCE')

# ---- part 022 sup (orchestrator, 2026-10-28): DISMISS and UPDATE_FACT tasks are never cancelled (cancelTask(int) takes only SEARCH_CARDS and RENDER_BROWSER_QA, DeckTask.java:181-185)
sup(('DeckTask.onCancelled', 'AbstractFlashcardViewer$8.onCancelled'), ('DeckTask.onCancelled', 'AbstractFlashcardViewer$9.onCancelled'))

# ---- part 020 (2026-10-28)
# AnkiDroid batch 020 (LABEL helper). AbstractFlashcardViewer part 2: 40 methods.
# The full row list is in graphs/AnkiDroid/parts/label_020.md (40 method rows and 11 edge rows).
#
# Route ownership:
# - Page edges whose destination is in this batch are written here (S_REVIEWER, S_NOTEEDITOR, S_DECKOPTIONS).
# - ASYNC launch edges from the methods in this batch (onActivityResult, undo) are written here. Each launch method
#   gets one edge to the listener's onPostExecute.
# - REGISTER edges from registerExternalStorageListener and showDeleteNoteDialog are written here.
# - onCreate, onPause and onResume LIFECYCLE edges come from lc_chain (graph_def.py:158) and are not written here.
#   onDestroy is skipped by lc_chain (LC_NO_TRIGGER, graph_def.py:37), so its edge is written here.
# - Automatic CALL edges from auto_calls.json are not written here. The keyboard path Reviewer.onKeyUp -> super
#   (Reviewer.java:391) is a CALL, so no GUI edge is written to AbstractFlashcardViewer.onKeyUp.
#
# Gates: MG142-MG146. MG142 playVideo (video media), MG143 removeFrontSideAudio (FrontSide audio template),
# MG144 type-answer methods (type: field), MG145 undo (an undo step), MG146 showLookupButtonIfNeeded (clipboard state).
# Predefined constants used: ENV_CONFIG_CHANGE, ENV_SDCARD_EVENT, STATE_SETTINGS. Page nodes: S_REVIEWER,
# S_NOTEEDITOR, S_DECKOPTIONS.

# --- Keyboard input on the reviewer page (hardware keys dispatched to the viewer).
e('S_REVIEWER', 'AbstractFlashcardViewer.onKeyDown', 'GUI',
  'hardware key press on the reviewer page: page up and page down scroll the card',
  env=None,
  needs_state=None,
  gui=['hardware page up and page down keys scroll the card (always on)'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:977-1007',
  note='Reviewer does not override onKeyDown. The scrolling_buttons branches (PICTSYMBOLS, SWITCH_CHARSET) are preference-gated inside the method. The Activity key dispatch is not printed: INFERRED.')

# --- Back key (framework dispatch through Activity.onKeyUp).
e('S_REVIEWER', 'AbstractFlashcardViewer.onBackPressed', 'FRAMEWORK',
  'back key: the framework calls onBackPressed from Activity.onKeyUp',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:967-974; FW-SRC core/java/android/app/Activity.java:2975-2980',
  note='Activity.onKeyUp calls onBackPressed at 2980 when targetSdk is at least ECLAIR. Outside the drawer the method calls closeReviewer(RESULT_DEFAULT, false).')

# --- Device configuration change (rotation, locale, screen size) on Reviewer.
e('S_REVIEWER', 'AbstractFlashcardViewer.onConfigurationChanged', 'SYSTEM',
  'device configuration changes while the reviewer runs (rotation, locale, screen size)',
  env=ENV_CONFIG_CHANGE,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:867-871; AndroidManifest.xml (src/main) 171-173; FW-SRC core/java/android/app/Activity.java:2198',
  note='The manifest declares configChanges="keyboardHidden|orientation|locale|screenSize" on Reviewer (line 173), so the system calls this method instead of recreating the activity.')

# --- Activity destroy. lc_chain skips onDestroy (LC_NO_TRIGGER), so the edge is written here.
e('S_REVIEWER', 'AbstractFlashcardViewer.onDestroy', 'LIFECYCLE',
  'the reviewer activity is destroyed (the framework calls onDestroy)',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:949-963; graph_def.py:37, 158; FW-SRC core/java/android/app/Activity.java:7208',
  note='performDestroy calls onDestroy at Activity.java:7208. The lc_chain call at graph_def.py:158 lists onDestroy but skips it because LC_NO_TRIGGER contains onDestroy (graph_def.py:37).')

# --- Result from the note editor (edit current card).
e('S_NOTEEDITOR', 'AbstractFlashcardViewer.onActivityResult', 'RESULT',
  'the note editor returns to the reviewer after the user edits the card',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:937-951 (RESULT_OK at 940); com/ichi2/anki/AbstractFlashcardViewer.java:1060-1098, 1183-1189',
  note='closeNoteEditor sets RESULT_OK only when the note changed (mChanged). Otherwise RESULT_CANCELED, and the card is redrawn with fillFlashcard (AbstractFlashcardViewer.java:1088).')

# --- Result from deck options (preference change).
e('S_DECKOPTIONS', 'AbstractFlashcardViewer.onActivityResult', 'RESULT',
  'the deck options screen returns RESULT_OK after a preference change',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckOptions.java:589-595; com/ichi2/anki/AbstractFlashcardViewer.java:1090-1094; com/ichi2/anki/Reviewer.java:208-211',
  note='closeWithResult sets RESULT_OK only when mPreferenceChanged is set. STATE_SETTINGS is the changed preference. The launch is Reviewer.java:208-211 with DECK_OPTIONS.')

# --- ASYNC launches from onActivityResult: UPDATE_FACT (listener $9) and ANSWER_CARD (listener $10).
e('AbstractFlashcardViewer.onActivityResult', 'AbstractFlashcardViewer$9.onPostExecute', 'ASYNC',
  'UPDATE_FACT task launched on mUpdateCardHandler when the note editor saved the card',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1084-1085; com/ichi2/async/DeckTask.java:360-362',
  note='The listener onPostExecute is reached through DeckTask.onPostExecute (DeckTask.java:360-362).')

e('AbstractFlashcardViewer.onActivityResult', 'AbstractFlashcardViewer$10.onPostExecute', 'ASYNC',
  'ANSWER_CARD task launched on mAnswerCardHandler after a reloadRequired result or a deck options change',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1076-1077, 1092-1093; com/ichi2/async/DeckTask.java:360-362',
  note='Two launch sites in this method (reloadRequired at 1076 and DECK_OPTIONS at 1092) share one edge to the same listener.')

# --- ASYNC launch from undo (listener $10).
e('AbstractFlashcardViewer.undo', 'AbstractFlashcardViewer$10.onPostExecute', 'ASYNC',
  'TASK_TYPE_UNDO launched on mAnswerCardHandler when an undo step exists',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1170-1174; com/ichi2/async/DeckTask.java:360-362',
  note='The undo gate (getCol().undoAvailable()) is MG145 (no predefined constant covers an undo step).')

# --- Media-eject receiver registration (ENV_SDCARD_EVENT).
e('AbstractFlashcardViewer.registerExternalStorageListener', 'AbstractFlashcardViewer$12.onReceive', 'REGISTER',
  'the SD card is ejected while the reviewer is open (MEDIA_EJECT broadcast)',
  env=ENV_SDCARD_EVENT,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1125-1139',
  note='The receiver is registered at line 1137 with SdCardReceiver.MEDIA_EJECT. onReceive calls finishWithoutAnimation (1131).')

# --- Delete dialog positive callback (registered when the dialog is shown).
e('AbstractFlashcardViewer.showDeleteNoteDialog', 'AbstractFlashcardViewer$13.onPositive', 'REGISTER',
  'the user taps the positive button of the delete-note dialog',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1239-1256',
  note='The callback is set at 1248-1254. onPositive calls dismiss(Collection.DismissType.DELETE_NOTE) at 1252.')

# ---- part 024 (2026-10-28)
# AnkiDroid batch 024 (LABEL helper). AnkiActivity part 2: startActivityWithAnimation and startActivityWithoutAnimation.
# Both methods are REACHABLE (rows in label_024.md). This part has no edge calls and no UNREACHABLE entries.
# Their outgoing calls are bytecode CALL edges written by the builder (enable/disable animation helpers), and the
# framework startActivity call, whose target is set by the caller's Intent (the caller's part owns that edge).

# ---- part 026 (2026-10-28)
# AnkiDroid batch 026 (LABEL helper). CardTemplateEditor part 2 of 2: 24 methods. The full row list is in
# graphs/AnkiDroid/parts/label_026.md.
# Edges here: source in batch 026, or page S_CARDTEMPLATEEDITOR with destination in batch 026.
# Not written here (other parts or the builder): OnPageChangeListener.onPageSelected -> updateCss, the DeckTask launch
# edges, the ConfirmationDialog positive dispatch into the confirm() methods, and the automatic CALL edges.
# Gates: no MG id is used. The catch routes of $4 and $5 use the predefined ENV_NETWORK and STATE_ACCOUNT (rows only).

# --- Text watcher $1 (registered on mFront, mCss and mBack in CardTemplateFragment.onCreateView, lines 416-418).
e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment$1.afterTextChanged', 'GUI',
  'type in the front, back or styling text box of a card template',
  env=None,
  gui=['type in the front, back or styling text box of a card template'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:398-418; FW-SRC core/java/android/widget/TextView.java:9375-9382, 11935-11939',
  note='Typing reaches the watcher through ChangeWatcher.afterTextChanged (TextView.java:11939) and sendAfterTextChanged (TextView.java:9375-9382). No gate: the editor is open on a note type.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment$1.beforeTextChanged', 'GUI',
  'type in the front, back or styling text box of a card template',
  env=None,
  gui=['type in the front, back or styling text box of a card template'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:398-418; FW-SRC core/java/android/widget/TextView.java:11918, 9309-9316',
  note='Typing reaches the watcher through ChangeWatcher.beforeTextChanged (TextView.java:11918) and sendBeforeTextChanged (TextView.java:9309-9316). The body is empty (CardTemplateEditor.java:412). No gate.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment$1.onTextChanged', 'GUI',
  'type in the front, back or styling text box of a card template',
  env=None,
  gui=['type in the front, back or styling text box of a card template'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:398-418; FW-SRC core/java/android/widget/TextView.java:11921-11926, 9359-9366, 9432-9452',
  note='Typing reaches the watcher through ChangeWatcher.onTextChanged (TextView.java:11926), then handleTextChanged, which calls sendOnTextChanged (TextView.java:9451). The body is empty (CardTemplateEditor.java:414). No gate.')

# --- The same watcher reached from updateCss: setText on the styling box (CardTemplateEditor.java:435) runs the watchers.
e('CardTemplateEditor$CardTemplateFragment.updateCss', 'CardTemplateEditor$CardTemplateFragment$1.afterTextChanged', 'FRAMEWORK',
  'setText of the styling box runs the after-change watcher',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:432-438; FW-SRC core/java/android/widget/TextView.java:5300-5304, 5402-5403, 9375-9382',
  note='updateCss sets the styling box text (CardTemplateEditor.java:435). TextView.setText calls sendAfterTextChanged when the box has listeners (TextView.java:5300-5304, 5402-5403). The watcher is the one registered on mCss (CardTemplateEditor.java:417). Framework dispatch, not an app CALL.')

e('CardTemplateEditor$CardTemplateFragment.updateCss', 'CardTemplateEditor$CardTemplateFragment$1.beforeTextChanged', 'FRAMEWORK',
  'setText of the styling box runs the before-change watcher',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:432-438; FW-SRC core/java/android/widget/TextView.java:5291-5296, 9309-9316',
  note='The same setText call (CardTemplateEditor.java:435) runs sendBeforeTextChanged when notifyBefore is set (TextView.java:5291-5296). The body is empty.')

e('CardTemplateEditor$CardTemplateFragment.updateCss', 'CardTemplateEditor$CardTemplateFragment$1.onTextChanged', 'FRAMEWORK',
  'setText of the styling box runs the on-change watcher',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:432-438; FW-SRC core/java/android/widget/TextView.java:5397, 9359-9366',
  note='The same setText call runs sendOnTextChanged (TextView.java:5397). The body is empty (CardTemplateEditor.java:414).')

# --- Pager adapter entries from the page (ViewPager populates the adapter after setAdapter, CardTemplateEditor.java:213).
# Support library, not in fw_src: INFERRED.
e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$TemplatePagerAdapter.getItem', 'FRAMEWORK',
  'the card template pager creates a page after setAdapter',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:213, 318-320',
  note='INFERRED: the support-library ViewPager and FragmentPagerAdapter call getItem when they create a page after setAdapter (CardTemplateEditor.java:213). getItem returns CardTemplateFragment.newInstance(position, mModelId, mNoteId). No gate.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$TemplatePagerAdapter.getItemId', 'FRAMEWORK',
  'the card template pager creates a page after setAdapter',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:213, 322-326',
  note='INFERRED: the support-library FragmentPagerAdapter asks for the item id when it builds the fragment tag for a page. The id is baseId plus the position (CardTemplateEditor.java:325). No gate.')

# --- UNREACHABLE entries (no_trigger_in_app). Full argument: see the rows of graphs/AnkiDroid/parts/label_026.md.
UNREACHABLE['CardTemplateEditor$CardTemplateFragment$2.onCancelled'] = (
    'no_trigger_in_app',
    ("DeckTask.onCancelled calls the listener onCancelled (DeckTask.java:367-370) only after the task is cancelled. "
     "The SAVE_MODEL task (TASK_TYPE_SAVE_MODEL = 47, DeckTask.java:100) is never cancelled in the app. "
     "DeckTask.cancelTask(int) (DeckTask.java:181-186) cancels the latest task only when its type equals the argument, "
     "and its only callers pass TASK_TYPE_SEARCH_CARDS and TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). "
     "The no-argument DeckTask.cancelTask (DeckTask.java:168-178) has no caller except cancelTask(int) (DeckTask.java:184). "
     "The other cancel(true) calls act on other tasks: TaskOperations.stopTaskGracefully (TaskOperations.java:33; its callers "
     "LoadPronounciationActivity.java:474-478 and TranslationActivity.java:405 pass their own tasks), Connection.java:541, "
     "Statistics.java:543, 574, 681, 692. DeckTask.getInstance (DeckTask.java:1548-1549) returns the latest task, and its only caller "
     "(Finder.java:1040) reads isCancelled() and never cancels. So no SAVE_MODEL task is cancelled and onCancelled never runs."),
    ('SRC com/ichi2/async/DeckTask.java:100, 168-186, 367-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
     'SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-36; SRC com/ichi2/async/Connection.java:541; '
     'SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; '
     'SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; '
     'SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405; SRC com/ichi2/libanki/Finder.java:1040; '
     'SRC com/ichi2/async/DeckTask.java:1548-1549'),
    'SOURCE')

UNREACHABLE['CardTemplateEditor$CardTemplateFragment$2.onProgressUpdate'] = (
    'no_trigger_in_app',
    ("DeckTask.onProgressUpdate (DeckTask.java:352-355) runs only when a DeckTask calls publishProgress. "
     "The publishProgress calls in DeckTask.java are at lines 380, 420, 422, 457, 565, 601, 633, 659, 809, 859 and 1349 "
     "(1349 forwards from ProgressCallback, which exists only from line 750). "
     "None is inside doInBackgroundSaveModel (DeckTask.java:1070-1079), and the ProgressCallback (DeckTask.java:1320-1350) "
     "is built only in doInBackgroundImportAdd (DeckTask.java:750). So a SAVE_MODEL task never publishes progress, "
     "and the listener onProgressUpdate (CardTemplateEditor.java:572-573) never runs."),
    ('SRC com/ichi2/async/DeckTask.java:330-331, 352-355, 750, 1070-1079, 1310-1313, 1320-1350 '
     '(publishProgress at lines 380, 420, 422, 457, 565, 601, 633, 659, 809, 859, 1349); '
     'SRC com/ichi2/anki/CardTemplateEditor.java:572-573'),
    'SOURCE')

# ---- part 026 sup (2026-10-28)
sup(('DeckTask.onCancelled', 'CardTemplateEditor$CardTemplateFragment$2.onCancelled'))
sup(('DeckTask$TaskListener.onProgressUpdate', 'CardTemplateEditor$CardTemplateFragment$2.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@CardTemplateEditor$CardTemplateFragment$2', 'CardTemplateEditor$CardTemplateFragment$2.onProgressUpdate'))

# ---- part 023 (2026-10-28)
UNREACHABLE['AnkiActivity.addContentView'] = ('no_trigger_in_app', 'Overridden in AnkiActivity but no app code calls it. The only addContentView( lines under src/main are this definition, its super call, and the AppCompatPreferenceActivity override, which belongs to a class that extends PreferenceActivity, not AnkiActivity. The framework Activity.java has no call to it (definition only). No trigger in the app.', 'SRC com/ichi2/anki/AnkiActivity.java:143-148; SRC com/ichi2/ui/AppCompatPreferenceActivity.java:84-85; FW-SRC core/java/android/app/Activity.java:2716-2717', 'SOURCE')

UNREACHABLE['AnkiActivity.animationEnabled'] = ('no_trigger_in_app', 'Public method with no app caller. The only reference to it is inside the private static helper StyledProgressDialog.animationEnabled(Context) (StyledProgressDialog.java:78), and that helper (lines 76-82) has no caller under src/main. No trigger in the app.', 'SRC com/ichi2/anki/AnkiActivity.java:119-121; SRC com/ichi2/themes/StyledProgressDialog.java:76-82', 'SOURCE')

UNREACHABLE['AnkiActivity.disableViewAnimation'] = ('branch_never_taken', 'Protected. Its only call is in enableViewAnimation (AnkiActivity.java:219), inside the branch guarded by animationDisabled() (line 218). animationDisabled() reads the eInkDisplay preference with default false (AnkiActivity.java:115). eInkDisplay appears nowhere else in src/main, so the branch is never taken.', 'SRC com/ichi2/anki/AnkiActivity.java:212-214, 217-223, 113-116', 'SOURCE')

UNREACHABLE['AnkiActivity.setContentView(View,LayoutParams)'] = ('no_trigger_in_app', 'Overridden in AnkiActivity but no app code calls it. The only lines under src/main with setContentView( and a comma are the two definitions and the super or delegate calls (AnkiActivity.java:134, 138; AppCompatPreferenceActivity.java:79-80, a different class). Activity.java defines the framework version (2704-2705) and has no call to it. No trigger in the app.', 'SRC com/ichi2/anki/AnkiActivity.java:133-139; SRC com/ichi2/ui/AppCompatPreferenceActivity.java:79-80; FW-SRC core/java/android/app/Activity.java:2704-2705', 'SOURCE')

UNREACHABLE['AnkiActivity.showSimpleMessageDialog(String,String)'] = ('no_trigger_in_app', 'Protected two-String overload that forwards to the three-argument form (AnkiActivity.java:386). No app line calls it with two Strings. The app calls have three shapes only: one String (DeckPicker.java:245, 282, 1209, 1232, 1526, 2183), String with boolean (AnkiActivity.java:382; DeckPicker.java:286, 1170), and String, String, boolean (DeckPicker.java:1070). The two-String shape never occurs.', 'SRC com/ichi2/anki/AnkiActivity.java:385-387; SRC com/ichi2/anki/DeckPicker.java:245, 282, 286, 1070, 1170, 1209, 1232, 1526, 2183', 'SOURCE')

# ---- part 023 sup (2026-10-28)
sup(('StyledProgressDialog.animationEnabled', 'AnkiActivity.animationEnabled'))
sup(('AnkiActivity.enableViewAnimation', 'AnkiActivity.disableViewAnimation'))

# ---- part 030 (2026-10-28)
# AnkiDroid batch 030 (LABEL helper). Info (the About page and the new-version page) and its inner classes: 11 methods,
# all REACHABLE. The full row list is in graphs/AnkiDroid/parts/label_030.md.
#
# Route ownership:
# - Automatic CALL edges from auto_calls.json are not written here: Info.onCreate -> Info$1.<init> (Info.java:77),
#   Info.onCreate -> Info$2.<init> (:87), Info.onCreate -> Info$3.<init> (:148), Info$2.onClick -> Info.finishWithAnimation
#   (:108), Info$3.onClick -> Info.copyDebugInfo (:151), Info.onKeyDown -> Info.finishWithAnimation (:174).
# - The graph_def.py INTENT edge DeckPicker.showStartupScreensAndDialogs -> Info.<init> is not written here. Its only
#   start in the source is behind VersionUtils.isReleaseVersion() (DeckPicker.java:938), which is false for the build
#   here (versionCode 20600206), so that route is closed.
# - No gate in this batch needs an MG id or a state or environment constant, so no UNREACHABLE entries are written.

# --- The About row of the advanced settings starts Info as TYPE_ABOUT.
e('S_PREFERENCES', 'Info.<init>', 'INTENT',
  'the About row of the advanced settings starts Info with no TYPE_EXTRA, so the page is TYPE_ABOUT',
  env=None,
  evidence='SRC res/xml/preferences_advanced.xml:137-143; SRC res/xml/preference_headers.xml:65-73; SRC com/ichi2/anki/NavigationDrawerActivity.java:273-277; SRC com/ichi2/anki/Preferences.java:233, 307-308, 785-788; SRC com/ichi2/anki/Info.java:66; FW-SRC core/java/android/preference/PreferenceScreen.java:240-249; FW-SRC core/java/android/preference/Preference.java:1129, 1151-1153',
  note='The Settings item of the navigation drawer starts Preferences. The advanced header is a SettingsFragment with the subscreen extra; its onCreate calls initSubscreen, which adds the advanced preferences. The About row has an intent with targetClass com.ichi2.anki.Info and no TYPE_EXTRA. A tap goes to PreferenceScreen.onItemClick, then Preference.performClick, which calls startActivity(mIntent).')

# --- Info.onCreate lays out the page (S_INFO is entered from this method).
e('Info.onCreate', 'S_INFO', 'ENTERS',
  'Info.onCreate lays out the About page or the new-version page',
  env=None,
  evidence='SRC com/ichi2/anki/Info.java:59-68, 143-166; FW-SRC core/java/android/app/Activity.java:6993-6999',
  note='Activity.performCreate calls onCreate when the activity starts. The page node S_INFO is entered from this method.')

# --- GUI taps and key presses on the About page.
e('S_INFO', 'Info$2.onClick', 'GUI',
  'tap the market button on the About page (rate the app, or the Amazon link on a Kindle)',
  env=None,
  gui=['tap the market button on the About page (rate the app, or the Amazon link on a Kindle)'],
  evidence='SRC com/ichi2/anki/Info.java:86-99; SRC res/layout/info.xml:60-61',
  note='The TYPE_ABOUT branch (Info.java:90-99) is the route. The new-version branch (101-108) is not used on the About page.')

e('S_INFO', 'Info$3.onClick', 'GUI',
  'tap the debug copy button on the About page (copies the debug info to the clipboard)',
  env=None,
  gui=['tap the debug copy button on the About page (copies the debug info to the clipboard)'],
  evidence='SRC com/ichi2/anki/Info.java:145-153; SRC res/layout/info.xml:53-58',
  note='The button is gone in the layout and is made VISIBLE in the TYPE_ABOUT case (Info.java:147).')

e('S_INFO', 'Info.onKeyDown', 'GUI',
  'press the back key on the About page',
  env=None,
  gui=['press the back key on the About page'],
  evidence='SRC com/ichi2/anki/Info.java:170-178; FW-SRC core/java/android/app/Activity.java:3255-3272; FW-SRC core/java/android/view/KeyEvent.java:2687-2691',
  note='KEYCODE_BACK with repeat count 0 (Info.java:171). Activity.dispatchKeyEvent ends with event.dispatch, which calls receiver.onKeyDown.')

# --- Framework callback: the WebView progress report while the About page loads.
e('S_INFO', 'Info$1.onProgressChanged', 'FRAMEWORK',
  'the WebView reports load progress while the About page loads (INFERRED: the WebView dispatch is not in fw_src, source not read)',
  env=None,
  evidence='SRC com/ichi2/anki/Info.java:77-84, 143; INFERRED (source not read): WebView progress callback',
  note='When progress is 100 the progress bar is hidden (Info.java:80-81). The WebView dispatch to WebChromeClient is not in fw_src.')

# ---- part 028 (2026-10-28)
# AnkiDroid batch 028 (LABEL helper). DeckOptions part 2 of 2: 13 methods (scratch/batches/batch_028.txt).
# The full row list is in graphs/AnkiDroid/parts/label_028.md.
#
# Route ownership:
# - E1 and E4 have a page source (S_DECKOPTIONS) and a destination in this batch, so they belong to this part.
# - E2 and E3 have their source in this batch (remConf launches the conf-remove DeckTask at DeckOptions.java:403-405).
# - Automatic CALL edges from graphs/AnkiDroid/auto_calls.json are not re-added: Editor.commit -> remConf (line 28447),
#   Editor$1.onPositive -> remConf (line 22223), Editor.commit -> Editor$1.<init> (line 28439), Editor.<init> ->
#   Editor$2.<init> (line 28343), buildLists -> JSONNameComparator.<init> (lines 27330-27331).
# - Gates: MG222 (the schema is unchanged since the last upload; stored state, no predefined constant) and MG223 (a
#   second options group exists; no predefined constant). env and needs_state are left unset on every edge below.
# - Lead for the orchestrator (not suppressed here): the automatic CALL edges DeckTask$TaskListener.onProgressUpdate ->
#   Editor$2.onProgressUpdate (auto_calls.json lines 2092-2093) and DeckTask.onCancelled -> Editor$2.onCancelled
#   (lines 3324-3325) point into the two UNREACHABLE methods below. They are generic dispatch edges.

e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack$Editor.putString', 'GUI',
  'tap OK in the confAdd or confRename text dialog (EditTextPreference), which persists the value',
  gui=['tap OK in the confAdd or confRename text dialog (EditTextPreference), which persists the value'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:338-341, 488-495; SRC res/xml/deck_options.xml:29-30, 43-44; FW-SRC core/java/android/preference/EditTextPreference.java:142-150, 88-100; FW-SRC core/java/android/preference/Preference.java:1609-1629, 1587-1598',
  note='EditTextPreference.onDialogClosed calls setText (EditTextPreference.java:148), which calls persistString (line 94), which calls putString (Preference.java:1625). The editor is DeckPreferenceHack.edit() because DeckOptions.getSharedPreferences returns mPref (DeckOptions.java:491-495). Editor.apply (DeckOptions.java:352-354) runs commit, which handles the confRename and confAdd keys (DeckOptions.java:218-242). No gate on a fresh install.')

e('DeckOptions$DeckPreferenceHack$Editor.remConf', 'DeckOptions$DeckPreferenceHack$Editor$2.onPreExecute', 'ASYNC',
  'the conf-remove DeckTask starts and calls its listener onPreExecute (shows the reordering dialog)',
  evidence='SRC com/ichi2/anki/DeckOptions.java:363-369, 399-410; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1298-1301; FW-SRC core/java/android/os/AsyncTask.java:644-650',
  note='MISSING GATE MG223: a second options group must exist (id != 1), because remConf runs only for a non-default group (DeckOptions.java:243-251). env and needs_state unset. DeckTask.launchDeckTask (DeckOptions.java:403-405) runs AsyncTask.execute, which calls onPreExecute (AsyncTask.java:648); DeckTask.onPreExecute forwards to the listener (DeckTask.java:344-347); the TaskListener default calls the no-argument onPreExecute, which is this method (DeckTask.java:1298-1301).')

e('DeckOptions$DeckPreferenceHack$Editor.remConf', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute', 'ASYNC',
  'the conf-remove DeckTask finishes and calls its listener onPostExecute (rebuild the lists and restart the activity)',
  evidence='SRC com/ichi2/anki/DeckOptions.java:378-386, 399-410; SRC com/ichi2/async/DeckTask.java:129-134, 358-365, 1298-1313; FW-SRC core/java/android/os/AsyncTask.java:691-698',
  note='MISSING GATE MG223: a second options group must exist (id != 1), because remConf runs only for a non-default group (DeckOptions.java:243-251). env and needs_state unset. AsyncTask.finish calls onPostExecute (AsyncTask.java:691-698); DeckTask.onPostExecute forwards to the listener (DeckTask.java:358-365); the TaskListener default forwards to this method (DeckTask.java:1298-1313). Body: cacheValues, buildLists, updateSummaries, dismiss, restartActivity (DeckOptions.java:378-386).')

e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack$Editor$1.onPositive', 'GUI',
  'tap OK on the full-sync confirmation dialog shown after removing an options group that needs a full sync',
  gui=['tap OK on the full-sync confirmation dialog shown after removing an options group that needs a full sync'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:243-271; SRC com/ichi2/libanki/Collection.java:337-344, 364-376, 395-407; SRC com/ichi2/libanki/Decks.java:708-712; SRC com/ichi2/libanki/sync/FullSyncer.java:154; SRC com/ichi2/libanki/Storage.java:317-319',
  note='MISSING GATE MG222: the confirmation dialog appears only when the schema marker is unchanged since the last full upload (Collection.modSchema throws when schemaChanged() is false, Collection.java:364-376; Collection.beforeUpload sets mLs = mScm at line 407, and FullSyncer calls it at line 154; a fresh collection has ls = 0, Storage.java:317-319). MISSING GATE MG223: a second options group must exist (DeckOptions.java:243-251). env and needs_state unset. The route continues with mCol.modSchemaNoCheck (Collection.java:337-344) and then remConf (automatic CALL, auto_calls.json line 22223).')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.putStringSet'] = ('framework_never_calls',
  'The only framework caller of putStringSet is Preference.persistStringSet (Preference.java:1662-1682, putStringSet at 1678). No code in this app calls persistStringSet, and res/xml/deck_options.xml has no MultiSelectListPreference (the XML uses EditTextPreference, ListPreference, CheckBoxPreference, CustomDialogPreference, StepsPreference, NumberRangePreference and Preference). MultiSelectListPreference is not in fw_src. The method is a TODO stub that returns null.',
  'SRC com/ichi2/anki/DeckOptions.java:358-361; FW-SRC core/java/android/preference/Preference.java:1662-1682; SRC res/xml/deck_options.xml:18-186; grep of com/ichi2 and res/xml finds no persistStringSet or MultiSelect use',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.remove'] = ('no_trigger_in_app',
  'Editor.remove only removes the key from mUpdate. Nothing calls it: the framework preference package has no editor remove call, and the app preference classes in com/ichi2/preferences have no remove call (grep of both finds none). The only Editor.remove is the definition itself.',
  'SRC com/ichi2/anki/DeckOptions.java:345-349; grep of FW-SRC core/java/android/preference and SRC com/ichi2/preferences finds no editor remove call',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor$2.onCancelled'] = ('no_trigger_in_app',
  'DeckTask.onCancelled runs only after AsyncTask.cancel(true); AsyncTask.finish calls onCancelled only when isCancelled() is true. In-app DeckTask cancels go through DeckTask.cancelTask(int), which cancels only when the latest task has the given type. Every in-app caller passes SEARCH_CARDS or RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). cancelTask() has no caller except cancelTask(int) (DeckTask.java:184). TaskOperations.stopTaskGracefully cancels a generic AsyncTask, not a DeckTask. So the conf-remove task is never cancelled. The automatic CALL DeckTask.onCancelled -> Editor$2.onCancelled (auto_calls.json lines 3324-3325) is a generic over-approximation.',
  'SRC com/ichi2/async/DeckTask.java:168-184, 368-370; FW-SRC core/java/android/os/AsyncTask.java:691-698; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-36; SRC com/ichi2/anki/DeckOptions.java:388-392',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor$2.onProgressUpdate'] = ('framework_never_calls',
  'AsyncTask calls onProgressUpdate only after publishProgress (AsyncTask.java:430-436). DeckTask.onProgressUpdate forwards only that call (DeckTask.java:350-355). The conf-remove body (DeckTask.java:961-982) contains no publishProgress (grep over lines 961-1000 finds none), and Sched.resortConf (Sched.java:2273-2286) does not publish. No conf task publishes progress, so the framework never calls this callback for this listener.',
  'SRC com/ichi2/anki/DeckOptions.java:373-374; SRC com/ichi2/async/DeckTask.java:350-355, 961-982; SRC com/ichi2/libanki/Sched.java:2273-2286; FW-SRC core/java/android/os/AsyncTask.java:430-436',
  'SOURCE')

# ---- part 028 sup (2026-10-28)
sup(('DeckTask.onCancelled', 'DeckOptions$DeckPreferenceHack$Editor$2.onCancelled'))
sup(('DeckTask$TaskListener.onProgressUpdate', 'DeckOptions$DeckPreferenceHack$Editor$2.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@DeckOptions$DeckPreferenceHack$Editor$2', 'DeckOptions$DeckPreferenceHack$Editor$2.onProgressUpdate'))

# ---- part 029 (2026-10-28)
# AnkiDroid batch 029 (LABEL helper). FilteredDeckOptions: 37 methods. The full row list is in
# graphs/AnkiDroid/parts/label_029.md.
#
# Gates: MG232 (Editor.commit -> onDestroy) and MG233 (onCreate -> onDestroy). Predefined constants used: STATE_DECK
# (the screen is open for a filtered deck; the check is FilteredDeckOptions.java:369-373) and ENV_SDCARD_EVENT
# (the SD card eject receiver). Page nodes: S_FILTEREDDECKOPTIONS (the screen) and S_STUDYOPTIONS_FRAG.
#
# Automatic CALL edges (auto_calls.json) are not written here. S_STUDYOPTIONS_FRAG -> FilteredDeckOptions.<init> is
# written here by the destination rule, but graph_def.py:1148-1149 assigns page edges from S_STUDYOPTIONS_FRAG to
# batch 038: the orchestrator should dedupe it.

# --- Entry from the study options page (StudyOptionsFragment) and the lifecycle.
e('S_STUDYOPTIONS_FRAG', 'FilteredDeckOptions.<init>', 'INTENT',
  'open the filtered deck options from the study options screen',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:138-139, 149-153, 296-297, 558; SRC com/ichi2/anki/FilteredDeckOptions.java:59',
  note='The intent is built at StudyOptionsFragment.java:150 and started at line 152. The call at line 297 is under the filtered-deck check (lines 296-297); the call at line 558 was not checked for its guard. Dedupe with batch 038 (graph_def.py:1148-1149).')

e('FilteredDeckOptions.onCreate', 'FilteredDeckOptions.getSharedPreferences', 'FRAMEWORK',
  'the preference screen is inflated and the framework asks the activity for its preference store',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:343-347, 369-378; FW-SRC core/java/android/preference/PreferenceActivity.java:638, 1546-1551',
  note='The inflate at line 378 runs only after the filtered-deck check (lines 369-373). The hop from the screen to its child preferences is INFERRED (PreferenceGroup is not in fw_src).')

e('FilteredDeckOptions.onCreate', 'FilteredDeckOptions.onSharedPreferenceChanged', 'REGISTER',
  'the screen registers itself as a listener of its preference store',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:322, 375-376',
  note='The registration at line 376 is after the filtered-deck check (lines 369-373). The listener is called from Editor.commit (see that edge).')

e('FilteredDeckOptions.onCreate', 'FilteredDeckOptions.onDestroy', 'FRAMEWORK',
  'the screen finishes at once (no collection, or the deck is not a filtered deck) and the framework destroys it',
  env=None,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:355-357, 369-373; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='MISSING GATE MG233: the collection is null (lines 355-357) or the deck is not a filtered deck (lines 369-373; finish at line 372). No predefined kind covers this. env and needs_state unset.')

e('FilteredDeckOptions.closeDeckOptions', 'FilteredDeckOptions.onDestroy', 'FRAMEWORK',
  'the screen closes (back key or up button) and the framework destroys it',
  env=None,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:431-438; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='finish at line 436, after the optional rebuild (lines 432-435). Both callers are user actions on the screen, so no gate is written.')

e('FilteredDeckOptions$1.onReceive', 'FilteredDeckOptions.onDestroy', 'FRAMEWORK',
  'the SD card is ejected while the screen is open, the screen finishes and the framework destroys it',
  env=ENV_SDCARD_EVENT,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:503-508; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='finish at line 507 inside the MEDIA_EJECT check (line 506 onwards).')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.commit', 'FilteredDeckOptions.onDestroy', 'FRAMEWORK',
  'saving the filtered deck fails (a RuntimeException), the screen finishes and the framework destroys it',
  env=None,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:185-192; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='MISSING GATE MG232: the save throws (caught at lines 185-192, finish at line 191). No predefined kind covers a save failure. env and needs_state unset.')

# --- Screen page edges (back key, up button, SD card eject, preference change).
e('S_FILTEREDDECKOPTIONS', 'FilteredDeckOptions.onKeyDown', 'GUI',
  'press the back key on the filtered deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['press the back key on the filtered deck options screen'],
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:421-429; FW-SRC core/java/android/app/Activity.java:3266-3272; FW-SRC core/java/android/view/KeyEvent.java:2684-2691',
  note='Repeat count 0 and KEYCODE_BACK (line 423) call closeDeckOptions (automatic CALL, line 425).')

e('S_FILTEREDDECKOPTIONS', 'FilteredDeckOptions.onOptionsItemSelected', 'GUI',
  'press the up button in the action bar of the filtered deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['press the up button in the action bar of the filtered deck options screen'],
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:398-410; FW-SRC core/java/android/app/Activity.java:3439-3450',
  note='The android.R.id.home case calls closeDeckOptions (automatic CALL, line 406). The support action bar hop is not in fw_src: INFERRED.')

e('S_FILTEREDDECKOPTIONS', 'FilteredDeckOptions$1.onReceive', 'SYSTEM',
  'the SD card is ejected while the filtered deck options screen is open',
  env=ENV_SDCARD_EVENT,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:503-513; SRC com/ichi2/anki/receiver/SdCardReceiver.java:37, 42-47; AndroidManifest.xml:269, 278',
  note='The receiver is registered at lines 511-513. The system-to-manifest hop is INFERRED (not in fw_src).')

e('S_FILTEREDDECKOPTIONS', 'FilteredDeckOptions$DeckPreferenceHack.edit', 'GUI',
  'change a setting on the filtered deck options screen (the preference is persisted through the store)',
  env=None,
  needs_state=STATE_DECK,
  gui=['change a setting on the filtered deck options screen (the preference is persisted through the store)'],
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:272-275; FW-SRC core/java/android/preference/PreferenceManager.java:674-686; FW-SRC core/java/android/preference/TwoStatePreference.java:81; FW-SRC core/java/android/preference/EditTextPreference.java:94',
  note='Preference.persistX calls PreferenceManager.getEditor, which calls getSharedPreferences().edit(). The check box path is TwoStatePreference.setChecked (line 81); the text path is EditTextPreference.setText (line 94).')

# --- Restore path: the framework reads the stored values when the screen is inflated.
e('FilteredDeckOptions.getSharedPreferences', 'FilteredDeckOptions$DeckPreferenceHack.contains', 'FRAMEWORK',
  'the screen restores its settings: the framework asks whether each key has a stored value',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:267-270, 343-347; FW-SRC core/java/android/preference/Preference.java:1547-1560',
  note='dispatchSetInitialValue calls contains on the object that getSharedPreferences returns (line 346). The screen gate is the onCreate inflate (see the getSharedPreferences edge).')

e('FilteredDeckOptions.getSharedPreferences', 'FilteredDeckOptions$DeckPreferenceHack.getBoolean', 'FRAMEWORK',
  'the screen restores a check box: its saved boolean is read',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:285-287, 343-347; SRC res/xml/cram_deck_options.xml:38, 43; FW-SRC core/java/android/preference/TwoStatePreference.java:187-188; FW-SRC core/java/android/preference/Preference.java:1909-1919',
  note='TwoStatePreference.onSetInitialValue calls getPersistedBoolean, which reads the store. CheckBoxPreference extends TwoStatePreference (FW-SRC core/java/android/preference/CheckBoxPreference.java:35).')

e('FilteredDeckOptions.getSharedPreferences', 'FilteredDeckOptions$DeckPreferenceHack.getInt', 'FRAMEWORK',
  'the screen restores the limit entry: its saved int is read',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:297-299, 343-347; SRC com/ichi2/preferences/NumberRangePreference.java:75-76; FW-SRC core/java/android/preference/EditTextPreference.java:159-160; FW-SRC core/java/android/preference/Preference.java:1747-1757',
  note='EditTextPreference.onSetInitialValue leads to NumberRangePreference.getPersistedString (lines 75-76), then getPersistedInt, then getSharedPreferences().getInt. The limit entry is res/xml/cram_deck_options.xml:26.')

# --- Write path: a preference change goes through edit, the put methods, apply, then commit.
e('FilteredDeckOptions$DeckPreferenceHack.edit', 'FilteredDeckOptions$DeckPreferenceHack$Editor.putBoolean', 'FRAMEWORK',
  'a check box changes: the framework writes its boolean through the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:208-211, 272-275; FW-SRC core/java/android/preference/Preference.java:1878-1894',
  note='Preference.persistBoolean calls editor.putBoolean on the editor returned by edit().')

e('FilteredDeckOptions$DeckPreferenceHack.edit', 'FilteredDeckOptions$DeckPreferenceHack$Editor.putInt', 'FRAMEWORK',
  'the limit entry changes: the framework writes its int through the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:222-225, 272-275; FW-SRC core/java/android/preference/Preference.java:1716-1732; SRC com/ichi2/preferences/NumberRangePreference.java:179-182',
  note='NumberRangePreference.setValue(int) calls persistInt (line 182), which calls editor.putInt.')

e('FilteredDeckOptions$DeckPreferenceHack.edit', 'FilteredDeckOptions$DeckPreferenceHack$Editor.putString', 'FRAMEWORK',
  'a text entry changes: the framework writes its string through the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:236-239, 272-275; FW-SRC core/java/android/preference/Preference.java:1609-1626; FW-SRC core/java/android/preference/EditTextPreference.java:94',
  note='Preference.persistString calls editor.putString. EditTextPreference.setText calls persistString at line 94.')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.putBoolean', 'FilteredDeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the check box value is committed: tryCommit applies the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:208-211, 250-254; FW-SRC core/java/android/preference/Preference.java:1587-1590',
  note='Preference.tryCommit calls editor.apply (lines 1587-1590). apply calls commit only when mAllowCommit is set (line 252, automatic CALL).')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.putInt', 'FilteredDeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the limit entry is committed: tryCommit applies the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:222-225, 250-254; FW-SRC core/java/android/preference/Preference.java:1587-1590',
  note='Preference.tryCommit calls editor.apply (lines 1587-1590). apply calls commit only when mAllowCommit is set (line 252, automatic CALL).')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.putString', 'FilteredDeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the text entry is committed: tryCommit applies the editor',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:236-239, 250-254; FW-SRC core/java/android/preference/Preference.java:1587-1590',
  note='Preference.tryCommit calls editor.apply (lines 1587-1590). apply calls commit only when mAllowCommit is set (line 252, automatic CALL).')

e('FilteredDeckOptions$DeckPreferenceHack$Editor.commit', 'FilteredDeckOptions.onSharedPreferenceChanged', 'CALL',
  'the save notifies the registered listeners, which include the screen',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:199-200, 376, 413-418',
  note='The listener loop (lines 199-200) calls every registered listener; the screen registers at line 376. Not an automatic edge: the loop is an interface call over a list.')

# --- UNREACHABLE: 10 methods (no call site, or no framework route).
UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.getAll'] = (
  'no_trigger_in_app',
  'No call site. The only getAll() declarations are FilteredDeckOptions.java:279 and DeckOptions.java:427. No caller in com/ichi2 and none in the framework preference package.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:279-281; grep of SRC com/ichi2 and FW-SRC core/java/android/preference (no call)',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.getFloat'] = (
  'framework_never_calls',
  'The only framework path is Preference.getPersistedFloat (FW-SRC Preference.java:1801), and its only caller in fw_src is persistFloat, which has no caller. No entry on the screen stores a float.',
  'FW-SRC core/java/android/preference/Preference.java:1770-1786, 1801; SRC com/ichi2/anki/FilteredDeckOptions.java:290-293; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.getLong'] = (
  'framework_never_calls',
  'The only framework path is Preference.getPersistedLong (FW-SRC Preference.java:1855), and its only caller in fw_src is persistLong, which has no caller. No entry on the screen stores a long.',
  'FW-SRC core/java/android/preference/Preference.java:1824-1840, 1855; SRC com/ichi2/anki/FilteredDeckOptions.java:303-305; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.getStringSet'] = (
  'framework_never_calls',
  'The only framework path is Preference.getPersistedStringSet (FW-SRC Preference.java:1693, reads at 1700 and 1703), which is called only by persistStringSet (lines 1662-1668), and persistStringSet has no caller in fw_src. No entry on the screen stores a string set.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:333-336; FW-SRC core/java/android/preference/Preference.java:1662-1668, 1693, 1700, 1703; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack.unregisterOnSharedPreferenceChangeListener'] = (
  'no_trigger_in_app',
  'No call site has this store as receiver. The app callers (Preferences.java:168, 806) unregister on the preference screen store, not this one. fw_src has only the definition (SharedPreferencesImpl.java:223).',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:327-329; SRC com/ichi2/anki/Preferences.java:168, 806; FW-SRC core/java/android/app/SharedPreferencesImpl.java:223',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.clear'] = (
  'no_trigger_in_app',
  'The editor is returned only by DeckPreferenceHack.edit, and this store is handed out only by FilteredDeckOptions.getSharedPreferences (line 346). The framework preference package never calls Editor.clear. The app clear (DeckPicker.java:967) is on another store.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:117-121, 272-275, 343-347; SRC com/ichi2/anki/DeckPicker.java:967; grep of FW-SRC core/java/android/preference (no editor clear call)',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.putFloat'] = (
  'framework_never_calls',
  'persistFloat (FW-SRC Preference.java:1770-1786) has no caller in fw_src or in com/ichi2, and no entry on the screen stores a float.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:215-218; FW-SRC core/java/android/preference/Preference.java:1770-1786; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.putLong'] = (
  'framework_never_calls',
  'persistLong (FW-SRC Preference.java:1824-1840) has no caller in fw_src or in com/ichi2, and no entry on the screen stores a long.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:229-232; FW-SRC core/java/android/preference/Preference.java:1824-1840; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.putStringSet'] = (
  'framework_never_calls',
  'Returns null (lines 258-261). persistStringSet (FW-SRC Preference.java:1662-1668) has no caller in fw_src, and no entry on the screen stores a string set.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:258-261; FW-SRC core/java/android/preference/Preference.java:1662-1668; SRC res/xml/cram_deck_options.xml:22-50',
  'SOURCE')

UNREACHABLE['FilteredDeckOptions$DeckPreferenceHack$Editor.remove'] = (
  'no_trigger_in_app',
  'The app remove calls (DeckPicker.java:854, 979; com/ichi2/compat/CompatHelper.java:125-134; Preferences.java:535) are on other stores. This store is handed out only by FilteredDeckOptions.getSharedPreferences (line 346), and the framework preference package never calls Editor.remove.',
  'SRC com/ichi2/anki/FilteredDeckOptions.java:243-247, 343-347; SRC com/ichi2/anki/DeckPicker.java:854, 979; SRC com/ichi2/compat/CompatHelper.java:125-134; SRC com/ichi2/anki/Preferences.java:535; grep of FW-SRC core/java/android/preference (no editor remove call)',
  'SOURCE')

# ---- part 027 (2026-10-28)
# AnkiDroid batch 027 (LABEL helper). DeckOptions: 40 methods (graphs/AnkiDroid/scratch/batches/batch_027.txt).
# The full row list is in graphs/AnkiDroid/parts/label_027.md.
#
# Page node: S_DECKOPTIONS (the deck options preference screen).
# Gates: STATE_DECK on the page GUI edges (a deck exists); STATE_SETTINGS on the preference write edges and the
# commit DeckTask ASYNC edges (the changed preference value selects the route); ENV_SDCARD_EVENT on the SD eject receiver.
# Route ownership:
# - The <init> INTENT edges from DeckPicker and Reviewer are already in graph_def.py (lines 1285, 1318).
#   The lifecycle edge <init> -> onCreate comes from lc_chain (graph_def.py:173-174). Neither is written here.
# - The page edge S_STUDYOPTIONS_FRAG -> DeckOptions.<init> is written here by the destination rule. Batch 038 must not repeat it.
# - The RESULT edges from S_DECKOPTIONS are owned by batches 007, 008 and 020.
#   S_DECKOPTIONS -> Editor$1.onPositive and remConf -> Editor$2 ASYNC edges are owned by batch 028.
# - Automatic bytecode CALL edges (auto_calls.json) are not repeated. The one CALL written here,
#   Editor.commit -> onSharedPreferenceChanged, is missing from auto_calls.json.

# --- Read route: onCreate inflates the preference XML and reads each stored value through the store.
e('DeckOptions.onCreate', 'DeckOptions.getSharedPreferences', 'FRAMEWORK',
  'the inflate in onCreate asks the activity for its preference store',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:491-495, 523; FW-SRC core/java/android/preference/Preference.java:1199-1204; FW-SRC core/java/android/preference/PreferenceManager.java:506-510',
  note='The store is mPref (set at DeckOptions.java:520). The route is PreferenceActivity.addPreferencesFromResource (PreferenceActivity.java:1546-1549), then Preference.onAttachedToHierarchy (Preference.java:1320-1328).')

e('DeckOptions.onCreate', 'DeckOptions$DeckPreferenceHack.contains', 'FRAMEWORK',
  'the initial-value dispatch checks each keyed preference for a stored value during the inflate',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:415-417, 523; FW-SRC core/java/android/preference/Preference.java:1547-1560',
  note='Preference.dispatchSetInitialValue calls contains(key) (Preference.java:1554-1555) and calls onSetInitialValue only when the key is present.')

e('DeckOptions.onCreate', 'DeckOptions$DeckPreferenceHack.getBoolean', 'FRAMEWORK',
  'the checkbox preferences read their stored values during the inflate (newBury, revBury, showAnswerTimer, autoPlayAudio, replayQuestion)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:433-435, 523; SRC res/xml/deck_options.xml:100-102, 131-133, 174-181; FW-SRC core/java/android/preference/TwoStatePreference.java:187-189; FW-SRC core/java/android/preference/Preference.java:1909-1921',
  note='TwoStatePreference.onSetInitialValue calls getPersistedBoolean (TwoStatePreference.java:187-189), which calls the store getBoolean (Preference.java:1909-1921). getBoolean delegates to getString (DeckOptions.java:434).')

e('DeckOptions.onCreate', 'DeckOptions$DeckPreferenceHack.getInt', 'FRAMEWORK',
  'the number preferences read their stored values during the inflate (newPerDay, newGradIvl, newEasy, newFactor, revPerDay, easyBonus, revIvlFct, revMaxIvl, lapNewIvl, lapMinIvl, lapLeechThres, maxAnswerTime)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:445-447, 523; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; SRC res/xml/deck_options.xml:76-168; FW-SRC core/java/android/preference/Preference.java:1747-1758; FW-SRC core/java/android/preference/EditTextPreference.java:157-161',
  note='NumberRangePreference.getPersistedString calls getPersistedInt (NumberRangePreference.java:74-77), which calls the store getInt (Preference.java:1747-1758). EditTextPreference.onSetInitialValue (EditTextPreference.java:157-161) starts the route.')

e('DeckOptions.onCreate', 'DeckOptions$DeckPreferenceHack.getString', 'FRAMEWORK',
  'the list and text preferences read their stored values during the inflate (deckConf, newOrder, lapLeechAct, desc)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:457-464, 523; SRC res/xml/deck_options.xml:20-22, 71-74, 162-164, 185-186; FW-SRC core/java/android/preference/ListPreference.java:294-295; FW-SRC core/java/android/preference/EditTextPreference.java:159-160',
  note='ListPreference.onSetInitialValue (ListPreference.java:294-295) and EditTextPreference.onSetInitialValue (EditTextPreference.java:159-160) call getPersistedString, which calls the store getString. updateSummaries and buildLists also call getString (automatic CALL, not repeated here).')

# --- Page GUI edges (STATE_DECK: the screen is open for a deck).
e('S_DECKOPTIONS', 'DeckOptions.onOptionsItemSelected', 'GUI',
  'tap the Up button in the action bar of the deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap the Up button in the action bar of the deck options screen'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:545-552',
  note='The android.R.id.home item calls closeWithResult (DeckOptions.java:547-548). LC_NO_TRIGGER lists this method (graph_def.py:37), but the route is a GUI callback, so the page edge is written here.')

e('S_DECKOPTIONS', 'DeckOptions.onKeyDown', 'GUI',
  'press the Back key on the deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['press the Back key on the deck options screen'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:579-587, 589-597',
  note='KEYCODE_BACK with repeat count 0 calls closeWithResult (DeckOptions.java:581-583), which sets the result and calls finish (589-597).')

e('S_DECKOPTIONS', 'DeckOptions.onPreferenceTreeClick', 'GUI',
  'tap any preference row on the deck options screen',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap any preference row on the deck options screen'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:565-576; FW-SRC core/java/android/preference/Preference.java:1140-1148; FW-SRC core/java/android/preference/PreferenceActivity.java:638-639',
  note='Preference.performClick calls the tree-click listener, which is this activity (PreferenceActivity.java:639). The body only sets a dialog background (DeckOptions.java:570-573) and returns false (575).')

# --- Preference write route (STATE_SETTINGS: the tap changes a stored value).
e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack.edit', 'GUI',
  'a preference value changes on the deck options screen',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['a preference value changes on the deck options screen'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:421-423; FW-SRC core/java/android/preference/PreferenceManager.java:674-687; FW-SRC core/java/android/preference/Preference.java:1878-1896',
  note='The persist path calls PreferenceManager.getEditor, which calls getSharedPreferences().edit() (PreferenceManager.java:686), which is this method. The automatic CALL to Editor.<init> (DeckOptions.java:422) is not repeated.')

e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack$Editor.putBoolean', 'GUI',
  'tap a checkbox on the deck options screen (newBury, revBury, showAnswerTimer, autoPlayAudio, replayQuestion)',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['tap a checkbox on the deck options screen (newBury, revBury, showAnswerTimer, autoPlayAudio, replayQuestion)'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:310-313; FW-SRC core/java/android/preference/TwoStatePreference.java:60-66, 75-82; FW-SRC core/java/android/preference/Preference.java:1878-1896',
  note='TwoStatePreference.onClick calls setChecked (60-66), which calls persistBoolean (75-82, 81), which calls putBoolean (Preference.java:1893).')

e('S_DECKOPTIONS', 'DeckOptions$DeckPreferenceHack$Editor.putInt', 'GUI',
  'tap OK on a number dialog on the deck options screen (NumberRangePreference keys)',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['tap OK on a number dialog on the deck options screen (NumberRangePreference keys)'],
  evidence='SRC com/ichi2/anki/DeckOptions.java:324-327; SRC com/ichi2/preferences/NumberRangePreference.java:81-83; FW-SRC core/java/android/preference/EditTextPreference.java:90-96, 142-150; FW-SRC core/java/android/preference/Preference.java:1716-1734',
  note='EditTextPreference.onDialogClosed (142-150) calls setText (90-96), which calls persistString (94). NumberRangePreference.persistString (81-83) turns the value into persistInt, which calls putInt (Preference.java:1731).')

e('DeckOptions$DeckPreferenceHack$Editor.putBoolean', 'DeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the framework commits the checkbox value',
  env=None,
  evidence='FW-SRC core/java/android/preference/Preference.java:1587-1591, 1878-1896; SRC com/ichi2/anki/DeckOptions.java:352-354',
  note='persistBoolean calls tryCommit (Preference.java:1894), and tryCommit calls editor.apply (Preference.java:1590). apply calls commit (DeckOptions.java:353), an automatic CALL.')

e('DeckOptions$DeckPreferenceHack$Editor.putInt', 'DeckOptions$DeckPreferenceHack$Editor.apply', 'FRAMEWORK',
  'the framework commits the number value',
  env=None,
  evidence='FW-SRC core/java/android/preference/Preference.java:1587-1591, 1716-1734; SRC com/ichi2/anki/DeckOptions.java:352-354',
  note='persistInt calls tryCommit (Preference.java:1732), and tryCommit calls editor.apply (Preference.java:1590).')

# --- Commit route: the listener loop and the conf-change DeckTask launches.
e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckOptions.onSharedPreferenceChanged', 'CALL',
  'the commit notifies the registered listener (DeckOptions) that a preference changed',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:301-303, 521, 556-560',
  note='The listener loop in commit (DeckOptions.java:301-303) calls onSharedPreferenceChanged, which sets mPreferenceChanged and calls updateSummaries (556-559). This CALL is missing from auto_calls.json, so it is written here.')

e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckOptions$DeckPreferenceHack$Editor$2.onPreExecute', 'ASYNC',
  'a changed conf, order, reset or subdeck value starts a conf-change DeckTask whose listener onPreExecute runs',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckOptions.java:170-171, 223-224, 232-233, 276-277, 363-369; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1298-1301',
  note='launchDeckTask (DeckTask.java:129-134) runs execute, which calls onPreExecute (DeckTask.java:344-347); the TaskListener default forwards to this method (DeckTask.java:1298-1301). The launches are at lines 170 (newOrder), 223 (deckConf), 232 (confReset) and 276 (confSetSubdecks), so the gate is the changed preference.')

e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute', 'ASYNC',
  'the conf-change DeckTask finishes and calls its listener onPostExecute (cacheValues, buildLists, updateSummaries, dismiss, restartActivity)',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckOptions.java:170-171, 223-224, 232-233, 276-277, 378-385; SRC com/ichi2/async/DeckTask.java:358-365, 1298-1313',
  note='onPostExecute (DeckTask.java:358-365) forwards to the listener, and the TaskListener default forwards to this method (DeckTask.java:1305-1307). The body is at DeckOptions.java:378-385.')

# --- SD card eject receiver and lifecycle close.
e('S_DECKOPTIONS', 'DeckOptions$1.onReceive', 'SYSTEM',
  'the SD card is ejected while the deck options screen is open (MEDIA_EJECT broadcast)',
  env=ENV_SDCARD_EVENT,
  evidence='SRC com/ichi2/anki/DeckOptions.java:762-772; SRC com/ichi2/anki/receiver/SdCardReceiver.java:37, 41-46',
  note='The receiver is registered in onCreate (DeckOptions.java:514, 772). SdCardReceiver re-broadcasts MEDIA_EJECT (41-46); onReceive calls finish (766). Precedent: label_013.py:105-109.')

e('S_DECKOPTIONS', 'DeckOptions.onDestroy', 'LIFECYCLE',
  'the deck options screen closes (Up, back, SD eject or an error finish)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:601-606, 505, 518, 133; graph_def.py:37, 45-46',
  note='lc_chain skips onDestroy (LC_NO_TRIGGER, graph_def.py:37; skip at lines 45-46), so this page edge is the only route. onDestroy unregisters the receiver (DeckOptions.java:603-604).')

# --- UNREACHABLE entries.
UNREACHABLE['DeckOptions.addMissingValues'] = ('branch_never_taken',
  'The only call is the JSONException catch in DeckPreferenceHack.cacheValues (the try block is DeckOptions.java:95-130). The standard configuration has every key (Decks.defaultConf sets replayq, restoreToDefault copies it, the default deck has conf and desc, both fixture collections have one conf with replayq), so the catch is not taken. Caveat: a legacy collection whose conf lacks a key would take it.',
  'SRC com/ichi2/anki/DeckOptions.java:95-134, 777-789; grep: DeckOptions.java:132 is the only call; SRC com/ichi2/libanki/Decks.java:51-59, 85-88, 117-121, 754-762; fixtures final_java_only/_fixtures/Download/sample_deck.apkg and final_java_only/AnkiDroid/app/AnkiDroid-#4200/tools/test-decks/templates.apkg',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack.getAll'] = ('framework_never_calls',
  'No caller of getAll on this store. The framework preference package and the app source root have no call.',
  'SRC com/ichi2/anki/DeckOptions.java:427-429; grep of FW-SRC core/java/android/preference and the app source root: no call',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack.getFloat'] = ('framework_never_calls',
  'Only reached through Preference.getPersistedFloat (Preference.java:1801-1811), which has no caller in the framework preference package or the app source root. deck_options.xml has no float preference.',
  'SRC com/ichi2/anki/DeckOptions.java:439-441; FW-SRC core/java/android/preference/Preference.java:1801-1811; grep: no caller of getPersistedFloat',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack.getStringSet'] = ('framework_never_calls',
  'The only framework path is Preference.persistStringSet and getPersistedStringSet (Preference.java:1662-1703), and neither has a caller in the framework preference package or the app source root. deck_options.xml has no multi-select preference.',
  'SRC com/ichi2/anki/DeckOptions.java:481-484; FW-SRC core/java/android/preference/Preference.java:1662-1703; grep: no caller',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack.unregisterOnSharedPreferenceChangeListener'] = ('framework_never_calls',
  'No caller on this store. The two app callers (Preferences.java:168, 806) unregister on the Preferences screen own store, not on DeckOptions mPref, and the framework never calls this method.',
  'SRC com/ichi2/anki/DeckOptions.java:475-477; SRC com/ichi2/anki/Preferences.java:168, 806 (other object); grep of FW-SRC core/java/android/preference: no caller',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.clear'] = ('framework_never_calls',
  'The framework preference package never calls Editor.clear on a preference store. The only app caller is DeckPicker.java:967, which clears the app preferences object (AnkiDroidApp.getSharedPrefs, AnkiDroidApp.java:219), not the DeckOptions store.',
  'SRC com/ichi2/anki/DeckOptions.java:143-147; SRC com/ichi2/anki/DeckPicker.java:964-968; SRC com/ichi2/anki/AnkiDroidApp.java:219; grep of FW-SRC core/java/android/preference: no edit().clear()',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.putFloat'] = ('framework_never_calls',
  'persistFloat (Preference.java:1770-1785) has no caller in the framework preference package or the app source root. deck_options.xml has no float preference.',
  'SRC com/ichi2/anki/DeckOptions.java:317-320; FW-SRC core/java/android/preference/Preference.java:1770-1785; grep: no caller of persistFloat',
  'SOURCE')

UNREACHABLE['DeckOptions$DeckPreferenceHack$Editor.putLong'] = ('framework_never_calls',
  'persistLong (Preference.java:1824-1839) has no caller in the framework preference package or the app source root. deck_options.xml has no long preference. FilteredDeckOptions.java:229 has its own putLong in a different class.',
  'SRC com/ichi2/anki/DeckOptions.java:331-334; FW-SRC core/java/android/preference/Preference.java:1824-1839; grep: no caller of persistLong; SRC com/ichi2/anki/FilteredDeckOptions.java:229',
  'SOURCE')

e('S_STUDYOPTIONS_FRAG', 'DeckOptions.<init>', 'INTENT',
  'open the deck options from the study options screen',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:296-300; SRC com/ichi2/anki/DeckOptions.java:71')

# part 027: the JSONException catch in cacheValues (DeckOptions.java:132) is never taken in a standard collection (see HANDOFF_V2)
sup(('DeckOptions$DeckPreferenceHack.cacheValues', 'DeckOptions.addMissingValues'))

# ---- part 032 (2026-10-28)
e('S_DLG_CONFIRMATION', 'ModelBrowser$7.confirm', 'GUI',
  'press OK on the first delete note type confirmation (the default path on a fresh collection)',
  env=None,
  gui=['press OK on the delete note type confirmation dialog'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:448-466, 451-460; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44; SRC com/ichi2/libanki/Collection.java:364-382; SRC com/ichi2/libanki/Storage.java:317-319',
  note='No gate written: the first dialog is shown when mModelIds.size() > 1 (ModelBrowser.java:448) and col.modSchema() does not throw, which holds while the schema flag is set (a fresh collection has scm > ls = 0). The positive button reaches ConfirmationDialog.onPositive -> confirm() (ConfirmationDialog.java:42-44); the MaterialDialog dispatch is INFERRED (library not in the dataset). The show call (ModelBrowser.java:466) is in deleteModelDialog, outside this batch.')

e('S_DLG_CONFIRMATION', 'ModelBrowser$7.cancel', 'GUI',
  'press Cancel on the first delete note type confirmation',
  env=None,
  gui=['press Cancel on the delete note type confirmation dialog'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:461-463; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='No gate written (same first-dialog path as the confirm edge). The negative button reaches ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49); the MaterialDialog dispatch is INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelBrowser$8.confirm', 'GUI',
  'press OK on the second delete note type confirmation (shown after a sync)',
  env=None,
  gui=['press OK on the full sync confirmation dialog for deleting a note type'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:467-484; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44; SRC com/ichi2/libanki/Collection.java:364-382; SRC com/ichi2/libanki/sync/Syncer.java:423-428',
  note='MISSING GATE MG262: the catch branch runs only when col.modSchema() throws, which needs schemaChanged() false (scm <= ls), that is a completed sync since the last schema change. No predefined ENV or STATE kind covers this flag, so env and needs_state are unset. The dialog text is R.string.full_sync_confirmation (ModelBrowser.java:483).')

e('S_DLG_CONFIRMATION', 'ModelBrowser$8.cancel', 'GUI',
  'press Cancel on the second delete note type confirmation (shown after a sync)',
  env=None,
  gui=['press Cancel on the full sync confirmation dialog for deleting a note type'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:467-484; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='MISSING GATE MG262 (same condition as the confirm edge). env and needs_state are unset. The negative button reaches ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49); the MaterialDialog dispatch is INFERRED.')

e('S_MODELBROWSER', 'ModelBrowser$DisplayPairAdapter.getView', 'FRAMEWORK',
  'the note type list draws each visible row through its adapter',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:268-269, 657-673; FW-SRC core/java/android/widget/ListView.java:775-786, 841-847, 1624, 1798, 2037-2052; FW-SRC core/java/android/widget/AbsListView.java:2335-2348, 2365',
  note='No gate: the adapter is set in fillModelList (ModelBrowser.java:268-269) and the list is laid out after that. Route: ListView.layoutChildren (1624) calls fillFromTop (1798) -> fillDown (775, makeAndAddView at 786) -> makeAndAddView (2037, obtainView at 2052) -> AbsListView.obtainView (2335, mAdapter.getView at 2348 and 2365). The framework steps are in fw_src.')

UNREACHABLE['ModelBrowser$DisplayPair.toString'] = ('framework_never_calls', "No app code calls DisplayPair.toString. DisplayPair is referenced only in ModelBrowser.java (grep over src/main/java). No line calls toString() on a DisplayPair (ModelBrowser.java:381, 424, 512 call toString on an EditText and on JSONObjects). DisplayPairAdapter.getView (ModelBrowser.java:657-673) overrides ArrayAdapter.getView and does not call super.getView, so the ArrayAdapter path that calls item.toString() (ArrayAdapter.java:445, inside createViewFromResource, reached from getView at 405-407) is never taken for this adapter. The adapter is set only on the list (ModelBrowser.java:268-269), so the spinner path getDropDownView (ArrayAdapter.java:490-493) is not reached. The filter path (ArrayFilter.performFiltering, value.toString() at ArrayAdapter.java:581) needs getFilter() and a text filter, and neither is set (no setTextFilterEnabled in ModelBrowser.java; no textFilterEnabled in res/layout/model_browser.xml). So no framework path calls toString on a DisplayPair.", "SRC com/ichi2/anki/ModelBrowser.java:268-269, 381, 424, 512, 641-644, 651-674; SRC res/layout/model_browser.xml; FW-SRC core/java/android/widget/ArrayAdapter.java:405-408, 445, 490-493, 550-581", 'SOURCE')
