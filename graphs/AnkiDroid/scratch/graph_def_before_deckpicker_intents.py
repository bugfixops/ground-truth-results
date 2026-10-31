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

for cb, lsrc in lc_chain('Preferences', ('onCreate', 'onCreateDialog', 'onResume', 'onPause')):
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
