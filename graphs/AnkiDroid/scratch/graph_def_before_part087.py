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

# ---- addendum (2026-10-28): buildLists sorts with JSONNameComparator; part 028 has the REACHABLE row but no edge
e('DeckOptions.buildLists', 'DeckOptions$JSONNameComparator.compare', 'CALL',
  'Collections.sort in buildLists calls the comparator when a second options group exists',
  env=None,
  note='MISSING GATE MG223: a second options group must exist (id != 1); DeckOptions.java:236-242 creates it. The sort is java.util and not in fw_src (source not read), so the call is INFERRED from the JDK contract.',
  evidence='SRC com/ichi2/anki/DeckOptions.java:653-656, 741-754; INFERRED (JDK Collections.sort, source not read)')

# ---- part 031 (2026-10-28)
# AnkiDroid batch 031 (LABEL helper). ModelBrowser part 1: 40 methods (ModelBrowser, its listeners $1 to $6$1 and their constructors).
# The full row list is in graphs/AnkiDroid/parts/label_031.md.
# Edges here: source in batch 031, or page S_* with the destination in batch 031. Automatic CALL edges (auto_calls.json)
# are not written here. The ASYNC launch edges use the launching method as the source.

# --- Options menu of the note type list (page S_MODELBROWSER).
e('S_MODELBROWSER', 'ModelBrowser.onCreateOptionsMenu', 'FRAMEWORK',
  'the note type list builds its options menu (the add button in the toolbar)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388; SRC com/ichi2/anki/ModelBrowser.java:203-207',
  note='The framework calls onCreatePanelMenu, which calls onCreateOptionsMenu (Activity.java:3388). The menu is inflated from R.menu.model_browser (ModelBrowser.java:205). No gate.')

e('S_MODELBROWSER', 'ModelBrowser.onOptionsItemSelected', 'GUI',
  'tap the add button or the up arrow in the note type list toolbar',
  env=None,
  gui=['tap the add button or the up arrow in the note type list toolbar'],
  evidence='FW-SRC core/java/android/app/Activity.java:3439-3450; SRC com/ichi2/anki/ModelBrowser.java:210-221; RES src/main/res/menu/model_browser.xml:5-8',
  note='Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). The add item is shown always (model_browser.xml:5-8). The up arrow (android.R.id.home) calls onBackPressed (ModelBrowser.java:212-213). No gate.')

# --- List rows (the list is filled in fillModelList after COUNT_MODELS delivers the note types).
e('S_MODELBROWSER', 'ModelBrowser$4.onItemClick', 'GUI',
  'tap a note type in the list (opens its field editor)',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['tap a note type in the list (opens its field editor)'],
  evidence='FW-SRC core/java/android/widget/AdapterView.java:314-318; SRC com/ichi2/anki/ModelBrowser.java:271-281, 108-118, 240',
  note='The listener is set in fillModelList (ModelBrowser.java:271-281), which runs after COUNT_MODELS delivers the list (ModelBrowser.java:108-118, 240). Before that the list is empty, so the gate is STATE_COLLECTION. The click is dispatched by AdapterView.performItemClick (AdapterView.java:318).')

e('S_MODELBROWSER', 'ModelBrowser$5.onItemLongClick', 'GUI',
  'long-press a note type in the list (opens the note type context menu)',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['long-press a note type in the list (opens the note type context menu)'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3237, 3314; SRC com/ichi2/anki/ModelBrowser.java:283-292, 108-118, 240',
  note='Same list gate as the click edge: the listener is set in fillModelList after the collection loads (ModelBrowser.java:283-292, 240). AbsListView calls the listener at AbsListView.java:3237 and :3314.')

# --- Context menu of a note type row (page S_DLG_MODELBROWSER_CONTEXT).
e('S_DLG_MODELBROWSER_CONTEXT', 'ModelBrowser$3.onSelection', 'GUI',
  'tap Template, Rename or Delete in the note type long-press menu',
  env=None,
  gui=['tap Template, Rename or Delete in the note type long-press menu'],
  evidence='SRC com/ichi2/anki/dialogs/ModelBrowserContextMenu.java:12-14, 28-41; SRC com/ichi2/anki/ModelBrowser.java:160-175, 288-289',
  note='The menu is built with itemsCallback(mContextMenuListener) (ModelBrowserContextMenu.java:39). The three entries are MODEL_TEMPLATE, MODEL_RENAME and MODEL_DELETE (ModelBrowserContextMenu.java:32-34). The menu opens from the long press (ModelBrowser.java:288-289). No gate of its own: the list gate is on the long-press edge.')

# --- Add note type dialog (opened by the add button; the dialog has no page node of its own).
e('S_MODELBROWSER', 'ModelBrowser$6.onPositive', 'GUI',
  'tap OK in the Add note type dialog that the add button opens',
  env=None,
  gui=['tap OK in the Add note type dialog that the add button opens'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:215-217, 309-390',
  note='The dialog is a MaterialDialog built in addNewNoteTypeDialog (ModelBrowser.java:353-390), not a DialogFragment, so it has no page node; its page is S_MODELBROWSER. addNewNoteTypeDialog is called from onOptionsItemSelected (ModelBrowser.java:216, automatic CALL). No gate.')

# --- Field editor and template editor (INTENT).
e('ModelBrowser$4.onItemClick', 'ModelFieldEditor.<init>', 'INTENT',
  'open the field editor of the tapped note type (explicit Intent with noteTypeID)',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:274-279; SRC com/ichi2/anki/AnkiActivity.java:186-190',
  note='INTENT check: explicit component (ModelFieldEditor.class), no framework gate. The extras are title and noteTypeID (ModelBrowser.java:277-278). The start goes through AnkiActivity.startActivityForResultWithAnimation (AnkiActivity.java:186-190). The ModelFieldEditor.<init> node is the constructor of the lifecycle chain (graph_def.py:191-192).')

e('ModelBrowser.openTemplateEditor', 'CardTemplateEditor.<init>', 'INTENT',
  'open the card template editor of the chosen note type (explicit Intent with modelId)',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:549-553; SRC com/ichi2/anki/AnkiActivity.java:186-190',
  note='INTENT check: explicit component (CardTemplateEditor.class) with the modelId extra (ModelBrowser.java:550-551), started with REQUEST_TEMPLATE_EDIT (ModelBrowser.java:552). No framework gate. The same destination is used by graph_def.py:2134 (NoteEditor).')

# --- Result of the template editor (page S_CARDTEMPLATEEDITOR is the child).
e('S_CARDTEMPLATEEDITOR', 'ModelBrowser.onActivityResult', 'RESULT',
  'return from the card template editor to the note type list (request code 3)',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:60, 552, 677-682; FW-SRC core/java/android/app/Activity.java:5679, 7259-7266',
  note='Page edge; S_CARDTEMPLATEEDITOR is the child launched by openTemplateEditor (edge above). The framework dispatches the result to onActivityResult (Activity.java:7266). Request code 3 relaunches COUNT_MODELS (ModelBrowser.java:679-680). No gate: the child returns to the parent in any result code.')

# --- Collection loaded (same pattern as the CardBrowser precedent, label_009.py:35-39).
e('ModelBrowser.onCreate', 'ModelBrowser.onCollectionLoaded', 'ASYNC',
  'the collection loader delivers onLoadFinished after startLoadingCollection',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:182-192, 237-241; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290',
  note='startLoadingCollection restarts the loader (AnkiActivity.java:261), and AnkiActivity.onLoadFinished calls onCollectionLoaded (AnkiActivity.java:286). The loader callback that reaches onLoadFinished is the Android LoaderManager, not in fw_src: INFERRED. The call from onLoadFinished to onCollectionLoaded is automatic.')

# --- DeckTask launch sites for the COUNT_MODELS listener $1. The DeckTask.TaskListener default edges into $1 are automatic.
e('ModelBrowser.onCollectionLoaded', 'ModelBrowser$1.onPreExecute', 'ASYNC',
  'the COUNT_MODELS task starts (launched from onCollectionLoaded) and runs its pre-execute callback',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:240, 103-105; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1299-1301; FW-SRC core/java/android/os/AsyncTask.java:632-648',
  note='AsyncTask.executeOnExecutor calls onPreExecute (AsyncTask.java:648); DeckTask.onPreExecute delegates to the listener (DeckTask.java:346); the interface default into $1 is automatic (DeckTask.java:1300). This edge is the launch link.')

e('ModelBrowser.onCollectionLoaded', 'ModelBrowser$1.onPostExecute', 'ASYNC',
  'the COUNT_MODELS task finishes and delivers its result to the note type list',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:240, 108-118; SRC com/ichi2/async/DeckTask.java:129-134, 360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='AsyncTask.finish calls onPostExecute when the task is not cancelled (AsyncTask.java:693-695); DeckTask.onPostExecute delegates to the listener (DeckTask.java:362); the interface default into $1 is automatic (DeckTask.java:1306). This edge is the launch link.')

e('ModelBrowser.fullRefresh', 'ModelBrowser$1.onPreExecute', 'ASYNC',
  'a full reload of the note type list starts the COUNT_MODELS task again',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:571-573, 103-105; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1299-1301; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='fullRefresh is called from addNewNoteType (ModelBrowser.java:432, automatic CALL). The launch link is the same as the onCollectionLoaded edge; the launch is in fullRefresh (ModelBrowser.java:572).')

e('ModelBrowser.fullRefresh', 'ModelBrowser$1.onPostExecute', 'ASYNC',
  'the reloaded COUNT_MODELS task delivers the note types to the list',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:571-573, 108-118; SRC com/ichi2/async/DeckTask.java:129-134, 360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='Same launch link as above, for the result: AsyncTask.finish calls onPostExecute (AsyncTask.java:695), DeckTask forwards it (DeckTask.java:362), and the interface default is automatic (DeckTask.java:1306).')

e('ModelBrowser.onActivityResult', 'ModelBrowser$1.onPreExecute', 'ASYNC',
  'returning from the template editor reloads the note type list (COUNT_MODELS starts)',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:677-682; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1299-1301; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='The launch is in onActivityResult for request code 3 (ModelBrowser.java:679-680). The launch link is the same as the onCollectionLoaded edge.')

e('ModelBrowser.onActivityResult', 'ModelBrowser$1.onPostExecute', 'ASYNC',
  'the COUNT_MODELS task started after the template editor returns delivers the list',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:677-682, 108-118; SRC com/ichi2/async/DeckTask.java:129-134, 360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='Same launch link for the result, as in the onCollectionLoaded edge.')

# --- Delete note type task: DELETE_MODEL listener $2 (launched from deleteModel).
e('ModelBrowser.deleteModel', 'ModelBrowser$2.onPreExecute', 'ASYNC',
  'the DELETE_MODEL task starts (launched from deleteModel) and shows the progress bar',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:578-586, 137-140; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1299-1301; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='deleteModel launches DELETE_MODEL with the listener $2 (ModelBrowser.java:579-580). AsyncTask.executeOnExecutor calls onPreExecute (AsyncTask.java:648); the interface default into $2 is automatic (DeckTask.java:1300).')

e('ModelBrowser.deleteModel', 'ModelBrowser$2.onPostExecute', 'ASYNC',
  'the DELETE_MODEL task finishes and refreshes the note type list',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:578-586, 143-149; SRC com/ichi2/async/DeckTask.java:129-134, 360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='AsyncTask.finish calls onPostExecute when not cancelled (AsyncTask.java:695); DeckTask forwards it (DeckTask.java:362); the interface default into $2 is automatic (DeckTask.java:1306). The body calls refreshList (ModelBrowser.java:148).')

# --- Second dialog of the add note type flow (MaterialDialog, no page node). Its OK callback is $6$1 (batch 032 owns $6$1.onPositive).
e('ModelBrowser$6.onPositive', 'ModelBrowser$6$1.onPositive', 'FRAMEWORK',
  'tap OK in the second Add note type dialog (the name input) that the first OK opens',
  env=None,
  gui=['tap OK in the second Add note type dialog (the name input) that the first OK opens'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:374-386',
  note='Method edge: $6.onPositive builds the second MaterialDialog with the ButtonCallback $6$1 (:374-378) and shows it (.show() at :386). The OK dispatch to $6$1.onPositive is library code (not in the dataset): INFERRED. $6$1.onPositive calls addNewNoteType at :382 (batch 032). No gate.')

# --- Rename note type dialog (MaterialDialog, no page node). Its OK callback is $9 (batch 032 owns $9.onPositive).
e('ModelBrowser.renameModelDialog', 'ModelBrowser$9.onPositive', 'FRAMEWORK',
  'tap OK in the rename note type dialog (opened by the context menu Rename entry)',
  env=None,
  gui=['tap OK in the rename note type dialog (opened by the context menu Rename entry)'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:503-508, 531',
  note='Method edge: renameModelDialog builds the MaterialDialog with the ButtonCallback $9 (:503-508) and shows it (.show() at :531). The OK dispatch is library code (not in the dataset): INFERRED. No gate.')

# --- Delete note type confirmation (ConfirmationDialog page). Two show calls: :466 and :484. Confirm and cancel callbacks are batch 032.
e('ModelBrowser.deleteModelDialog', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the delete note type confirmation dialog (ConfirmationDialog) is shown',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:448, 466, 484, 490',
  note='MISSING GATE MG252: the dialog opens only when the note type list holds at least two note types (mModelIds.size() > 1, ModelBrowser.java:448); no predefined STATE kind covers the count. Two show calls use this page: :466 (dialog d, when col.modSchema() does not throw at :450) and :484 (dialog c, the catch branch at :467, full-sync text). The confirm and cancel callbacks are batch 032 (label_032.py). The else branch shows the last-model toast (:490).')

# --- Context menu of a note type row (ModelBrowserContextMenu page), shown by the long-press listener.
e('ModelBrowser$5.onItemLongClick', 'S_DLG_MODELBROWSER_CONTEXT', 'ENTERS',
  'the note type context menu is shown for the long-pressed row',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:283-292 (newInstance at :288, showDialogFragment at :289)',
  note='ENTERS edge: method to page. The listener runs only after the list is filled (STATE_COLLECTION on the S_MODELBROWSER edge above). No gate of its own.')

# --- UNREACHABLE: the listener callbacks onCancelled and onProgressUpdate of $1 (COUNT_MODELS) and $2 (DELETE_MODEL).
UNREACHABLE['ModelBrowser$1.onCancelled'] = ('no_trigger_in_app',
  ("DeckTask.onCancelled (DeckTask.java:367-370) calls the listener onCancelled only after the task is cancelled. "
   "COUNT_MODELS (41) is never cancelled in the app: DeckTask.cancelTask(int) (DeckTask.java:181-184) cancels the latest task only when its type equals the argument, "
   "and its only callers pass TASK_TYPE_SEARCH_CARDS and TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). "
   "The no-argument cancelTask() (DeckTask.java:168-178) is called only from cancelTask(int) (DeckTask.java:184)."
   "No class extends DeckTask. The other cancel(true) calls act on non-DeckTask tasks (Connection.java:541; Statistics.java:543, 574, 681, 692; "
   "TaskOperations.java:33 with the LoadPronounciationActivity and TranslationActivity callers). So ModelBrowser$1.onCancelled never runs."),
  ('SRC com/ichi2/async/DeckTask.java:168-184, 367-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
   'SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-33; SRC com/ichi2/async/Connection.java:541; '
   'SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; SRC com/ichi2/anki/ModelBrowser.java:98-100'),
  'SOURCE')

UNREACHABLE['ModelBrowser$1.onProgressUpdate'] = ('no_trigger_in_app',
  ("DeckTask.onProgressUpdate (DeckTask.java:352-355) calls the listener only when a DeckTask calls publishProgress. "
   "COUNT_MODELS (DeckTask.java:1089-1126) does not publish: no publishProgress call lies in DeckTask.java:1089-1139, and the publishProgress calls "
   "(DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659, 809, 859) all lie outside that range. "
   "The listener body is empty (ModelBrowser.java:121-123: 'This decktask does not publish updates'). So ModelBrowser$1.onProgressUpdate never runs."),
  ('SRC com/ichi2/async/DeckTask.java:352-355, 380, 420, 422, 457, 565, 601, 633, 659, 809, 859, 1089-1139; SRC com/ichi2/anki/ModelBrowser.java:121-123'),
  'SOURCE')

UNREACHABLE['ModelBrowser$2.onCancelled'] = ('no_trigger_in_app',
  ("DeckTask.onCancelled (DeckTask.java:367-370) calls the listener onCancelled only after the task is cancelled. "
   "DELETE_MODEL (42) is never cancelled in the app: DeckTask.cancelTask(int) (DeckTask.java:181-184) cancels the latest task only when its type equals the argument, "
   "and its only callers pass TASK_TYPE_SEARCH_CARDS and TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). "
   "The no-argument cancelTask() (DeckTask.java:168-178) is called only from cancelTask(int) (DeckTask.java:184)."
   "No class extends DeckTask. The other cancel(true) calls act on non-DeckTask tasks (Connection.java:541; Statistics.java:543, 574, 681, 692; "
   "TaskOperations.java:33 with the LoadPronounciationActivity and TranslationActivity callers). The listener body is empty (ModelBrowser.java:133-135). So ModelBrowser$2.onCancelled never runs."),
  ('SRC com/ichi2/async/DeckTask.java:168-184, 367-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
   'SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-33; SRC com/ichi2/async/Connection.java:541; '
   'SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; SRC com/ichi2/anki/ModelBrowser.java:133-135'),
  'SOURCE')

UNREACHABLE['ModelBrowser$2.onProgressUpdate'] = ('no_trigger_in_app',
  ("DeckTask.onProgressUpdate (DeckTask.java:352-355) calls the listener only when a DeckTask calls publishProgress. "
   "DELETE_MODEL (DeckTask.java:1127-1139) does not publish: no publishProgress call lies in DeckTask.java:1089-1139, and the publishProgress calls "
   "(DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659, 809, 859) all lie outside that range. "
   "The listener body is empty (ModelBrowser.java:152-154: 'This decktask does not publish updates'). So ModelBrowser$2.onProgressUpdate never runs."),
  ('SRC com/ichi2/async/DeckTask.java:352-355, 380, 420, 422, 457, 565, 601, 633, 659, 809, 859, 1089-1139; SRC com/ichi2/anki/ModelBrowser.java:152-154'),
  'SOURCE')
# DeckTask cancel(true) reaches only SEARCH_CARDS and RENDER_BROWSER_QA; COUNT_MODELS and DELETE_MODEL never publish progress
sup(('DeckTask.onCancelled', 'ModelBrowser$1.onCancelled'), ('DeckTask.onCancelled', 'ModelBrowser$2.onCancelled'))
sup(('DeckTask$TaskListener.onProgressUpdate', 'ModelBrowser$1.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@ModelBrowser$1', 'ModelBrowser$1.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate', 'ModelBrowser$2.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@ModelBrowser$2', 'ModelBrowser$2.onProgressUpdate'))

# ---- part 034 (2026-10-28)
# AnkiDroid batch 034 (LABEL helper). ModelFieldEditor part 2: 16 methods. Row list: graphs/AnkiDroid/parts/label_034.md.
# Gate used: MISSING GATE MG282 (schema-changed flag; env and needs_state unset). No predefined ENV or STATE kind fits.
# Edges owned: GUI from the S_DLG_CONFIRMATION and S_DLG_MODELEDITOR_CONTEXT pages (owned by the destination),
# the FRAMEWORK edge from $6.<init> to $6.onPositive, and the ASYNC launch edges into the $8 listener from the launch methods.
# UNREACHABLE: ModelFieldEditor$8.onCancelled and ModelFieldEditor$8.onProgressUpdate.

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$5$1.confirm', 'GUI',
  'press OK on the rename field confirmation shown when the schema change needs confirmation',
  gui=['press OK on the rename field confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:312-334; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382; SRC com/ichi2/libanki/Models.java:665-666; SRC com/ichi2/libanki/Storage.java:317-319',
  note='MISSING GATE MG282: the dialog appears only when renameField() throws ConfirmModSchemaException, which needs Collection.schemaChanged() false (mScm <= mLs, Collection.java:380-382) when Models.renameField calls modSchema(true) (Models.java:665-666). A fresh collection (Storage.java:317-319: scm set, ls 0) does not throw. env and needs_state unset. The MaterialDialog OK dispatch to ConfirmationDialog is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$6$1.confirm', 'GUI',
  'press OK on the reposition confirmation shown when the schema change needs confirmation',
  gui=['press OK on the reposition confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:375-395; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382',
  note='MISSING GATE MG282: the dialog is created only when modSchema() throws in $6.onPositive (ModelFieldEditor.java:375, 379-382), which needs Collection.schemaChanged() false (Collection.java:364-371, 380-382). env and needs_state unset. The MaterialDialog OK dispatch to ConfirmationDialog is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$6$1.cancel', 'GUI',
  'press Cancel on the reposition confirmation shown when the schema change needs confirmation',
  gui=['press Cancel on the reposition confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:397-399; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382',
  note='MISSING GATE MG282: same dialog and schema-changed condition as the OK edge (ModelFieldEditor.java:375-382; Collection.java:364-371, 380-382). env and needs_state unset. The MaterialDialog cancel dispatch is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$7.confirm', 'GUI',
  'press OK on the sort-field confirmation shown when the schema change needs confirmation',
  gui=['press OK on the sort-field confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:456-471; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382',
  note='MISSING GATE MG282: the dialog is created only when modSchema() throws in sortByField (ModelFieldEditor.java:460-465), which needs Collection.schemaChanged() false (Collection.java:364-371, 380-382). env and needs_state unset. The MaterialDialog OK dispatch is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$7.cancel', 'GUI',
  'press Cancel on the sort-field confirmation shown when the schema change needs confirmation',
  gui=['press Cancel on the sort-field confirmation shown when the schema change needs confirmation'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:473-475; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-49; SRC com/ichi2/libanki/Collection.java:364-382',
  note='MISSING GATE MG282: same dialog and schema-changed condition as the OK edge (ModelFieldEditor.java:460-465; Collection.java:364-371, 380-382). env and needs_state unset. The MaterialDialog cancel dispatch is library code: INFERRED.')

e('S_DLG_MODELEDITOR_CONTEXT', 'ModelFieldEditor$9.onSelection', 'GUI',
  'tap a row of the field context menu (sort, reposition, delete or rename)',
  gui=['tap a row of the field context menu (sort, reposition, delete or rename)'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:137-139, 592-607; SRC com/ichi2/anki/dialogs/ModelEditorContextMenu.java:40-44',
  note='The menu is created and shown in ModelFieldEditor$1.onItemClick (ModelFieldEditor.java:137-139, batch 033) with itemsCallback(mContextMenuListener) (ModelEditorContextMenu.java:40-44). The ListCallback dispatch is library code: INFERRED. No gate.')

e('ModelFieldEditor$6.<init>', 'ModelFieldEditor$6.onPositive', 'FRAMEWORK',
  'press OK on the reposition dialog (MaterialDialog ButtonCallback)',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:356-360, 376-378',
  note='The ButtonCallback object created by $6.<init> is the one the dialog calls on OK. The library dispatch is not in the dataset (source not read): INFERRED, as label_001 and label_005. No gate: the dialog is shown on each reposition request.')

e('ModelFieldEditor$6.onPositive', 'ModelFieldEditor$8.onPreExecute', 'ASYNC',
  'the reposition task starts: onPreExecute runs on the UI thread inside execute()',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:376-378, 528-533; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1296-1302; FW-SRC core/java/android/os/AsyncTask.java:645-650',
  note='launchDeckTask (DeckTask.java:129-134) calls execute(), which calls onPreExecute() before the background work (AsyncTask.java:648). The dispatch to the listener is exact at DeckTask.java:1300. Fresh-collection direct path; the dialog path is the $6$1.confirm edge.')

e('ModelFieldEditor$6.onPositive', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the reposition task finishes in the background and posts its result to the UI thread',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:376-378, 536-543; SRC com/ichi2/async/DeckTask.java:360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-698, 714-715',
  note='AsyncTask.finish calls onPostExecute (AsyncTask.java:691-698) through the handler (714-715). DeckTask.onPostExecute calls the listener (DeckTask.java:360-365; exact dispatch at 1306). The body closes the activity on a DB error (ModelFieldEditor.java:537-538) and refreshes the list.')

e('ModelFieldEditor$6$1.confirm', 'ModelFieldEditor$8.onPreExecute', 'ASYNC',
  'the reposition task starts after the schema confirmation: onPreExecute runs on the UI thread inside execute()',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:388-390, 528-533; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1296-1302; FW-SRC core/java/android/os/AsyncTask.java:645-650',
  note='MISSING GATE MG282 on the route into $6$1.confirm (schema unchanged, see the S_DLG_CONFIRMATION edge). env and needs_state unset. Same dispatch as the $6.onPositive edge (AsyncTask.java:648; DeckTask.java:1300).')

e('ModelFieldEditor$6$1.confirm', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the reposition task finishes after the schema confirmation and posts its result to the UI thread',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:388-390, 536-543; SRC com/ichi2/async/DeckTask.java:360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-698, 714-715',
  note='MISSING GATE MG282 on the route into $6$1.confirm (schema unchanged). env and needs_state unset. Same finish path as the $6.onPositive edge (AsyncTask.java:691-698; DeckTask.java:1306).')

e('ModelFieldEditor$7.confirm', 'ModelFieldEditor$8.onPreExecute', 'ASYNC',
  'the sort-field task starts after the schema confirmation: onPreExecute runs on the UI thread inside execute()',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:468-469, 528-533; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1296-1302; FW-SRC core/java/android/os/AsyncTask.java:645-650',
  note='MISSING GATE MG282 on the route into $7.confirm (schema unchanged, see the S_DLG_CONFIRMATION edge). env and needs_state unset. Same dispatch as the $6.onPositive edge (AsyncTask.java:648; DeckTask.java:1300).')

e('ModelFieldEditor$7.confirm', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the sort-field task finishes after the schema confirmation and posts its result to the UI thread',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:468-469, 536-543; SRC com/ichi2/async/DeckTask.java:360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-698, 714-715',
  note='MISSING GATE MG282 on the route into $7.confirm (schema unchanged). env and needs_state unset. Same finish path as the $6.onPositive edge (AsyncTask.java:691-698; DeckTask.java:1306).')

UNREACHABLE['ModelFieldEditor$8.onCancelled'] = ('no_trigger_in_app',
  'No in-app event cancels a field task. The four field types 43-46 (DeckTask.java:96-99: DeleteField, RepositionField, AddField, ChangeSortField) all pass mChangeFieldHandler (ModelFieldEditor.java:198, 208, 281, 376, 388, 461, 468) and discard the returned task. DeckTask.cancelTask(int) cancels the latest task only when its mType equals the argument (DeckTask.java:181-184); the only callers pass 30 and 37 (CardBrowser.java:528-529, 796-797, 1155). The no-argument cancelTask() (DeckTask.java:168-178) is called only from line 184. The other cancel(true) calls act on other task objects (TaskOperations.java:33; Connection.java:541; Statistics.java:543, 574, 681, 692). For review: the automatic CALL DeckTask.onCancelled to ModelFieldEditor$8.onCancelled (DeckTask.java:369, cha) makes it look reachable.',
  'SRC com/ichi2/async/DeckTask.java:96-99, 168-184, 368-370; SRC com/ichi2/anki/ModelFieldEditor.java:198, 208, 281, 376, 388, 461, 468; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:33; SRC com/ichi2/async/Connection.java:541; SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692',
  'SOURCE')

UNREACHABLE['ModelFieldEditor$8.onProgressUpdate'] = ('no_trigger_in_app',
  'Body is empty ("This decktask does not publish updates", ModelFieldEditor.java:546-548). The only route is publishProgress, and none of the four field bodies calls it (DeckTask.java:1144-1227: doInBackGroundDeleteField, RepositionField, AddField, ChangeSortField). The ten publishProgress call sites are at DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659, 809, 859; the AsyncTask.publishProgress definition is FW-SRC AsyncTask.java:684-689. For review: the automatic CALL DeckTask$TaskListener.onProgressUpdate@ModelFieldEditor$8 to ModelFieldEditor$8.onProgressUpdate (DeckTask.java:1312, exact) is in auto_calls.json.',
  'SRC com/ichi2/anki/ModelFieldEditor.java:546-548; SRC com/ichi2/async/DeckTask.java:352-355, 380, 420, 422, 457, 565, 601, 633, 659, 809, 859, 1144-1227, 1296-1314; FW-SRC core/java/android/os/AsyncTask.java:684-689',
  'SOURCE')
# DeckTask cancel(true) reaches only SEARCH_CARDS and RENDER_BROWSER_QA; field tasks never publish progress
sup(('DeckTask.onCancelled', 'ModelFieldEditor$8.onCancelled'))
sup(('DeckTask$TaskListener.onProgressUpdate', 'ModelFieldEditor$8.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@ModelFieldEditor$8', 'ModelFieldEditor$8.onProgressUpdate'))

# ---- part 035 (2026-10-28)
# AnkiDroid batch 035 (LABEL helper). MyAccount login activity: 22 methods. The full row list is in
# graphs/AnkiDroid/parts/label_035.md.
#
# Route ownership:
# - CALL edges inside MyAccount (onCreate, initAllContentViews, the $1-$4 constructors and click callbacks, login,
#   logout, resetPassword, saveUserInformation, switchToState, onKeyDown), and the Connection-to-$5 chain
#   (Connection.onPreExecute/onPostExecute/onProgressUpdate/launchConnectionTask), come from auto_calls.json.
#   They are not written here.
# - The INTENT edge DeckPicker.loginToSyncServer -> MyAccount.<init> and the LIFECYCLE chain are already in
#   graph_def.py (lines 1259 and 194-195). They are not written here.
# - Gates: MG292 (logged-out state, login view), MG293 (device offline, $5.onDisconnected, row only),
#   MG294 (request or reply of at least 1024 bytes before the progress callback). Batch range MG292-MG301.

# --- Login view (shown when no hkey is stored; MyAccount.java:92-95).
e('S_MYACCOUNT', 'MyAccount$1.onClick', 'GUI',
  'tap the login button in the login view (both fields filled in)',
  gui=['tap the login button in the login view (both fields filled in)'],
  evidence='SRC com/ichi2/anki/MyAccount.java:177-184, 139-142; SRC com/ichi2/anki/MyAccount.java:92-95',
  note='MISSING GATE MG292: the login view is shown only when no hkey is stored (logged out). No STATE constant covers the logged-out state (STATE_ACCOUNT is logged in). env and needs_state unset. login runs only when both fields are non-empty (MyAccount.java:139-140).')

e('S_MYACCOUNT', 'MyAccount$2.onClick', 'GUI',
  'tap the reset password button in the login view',
  gui=['tap the reset password button in the login view'],
  evidence='SRC com/ichi2/anki/MyAccount.java:187-193, 92-95',
  note='MISSING GATE MG292: the login view is shown only when no hkey is stored (logged out). env and needs_state unset. The handler calls resetPassword (auto CALL, MyAccount.java:191).')

e('S_MYACCOUNT', 'MyAccount$3.onClick', 'GUI',
  'tap the sign up button in the login view (opens the registration page in an external browser)',
  gui=['tap the sign up button in the login view (opens the registration page in an external browser)'],
  evidence='SRC com/ichi2/anki/MyAccount.java:196-202, 92-95',
  note='MISSING GATE MG292: the login view is shown only when no hkey is stored (logged out). env and needs_state unset. The handler calls openUrl (auto CALL, MyAccount.java:199).')

# --- Back key on the MyAccount screen (framework dispatch; no state gate).
e('S_MYACCOUNT', 'MyAccount.onKeyDown', 'GUI',
  'press the back key on the MyAccount screen',
  env=None,
  gui=['press the back key on the MyAccount screen'],
  evidence='SRC com/ichi2/anki/MyAccount.java:221-285; FW-SRC core/java/android/view/KeyEvent.java:2684-2691; FW-SRC core/java/android/app/Activity.java:3255-3272',
  note='Framework route: Activity.dispatchKeyEvent -> KeyEvent.dispatch -> receiver.onKeyDown. The handler finishes the activity with a fade when the key is BACK and the repeat count is 0 (finishWithAnimation, auto CALL).')

# --- Login listener $5 (Connection.TaskListener) on the login task started by MyAccount.login.
e('MyAccount.login', 'MyAccount$5.onPreExecute', 'ASYNC',
  'the login task starts; the listener shows the progress dialog before the background login runs',
  env=ENV_NETWORK,
  evidence='FW-SRC core/java/android/os/AsyncTask.java:632-651; SRC com/ichi2/async/Connection.java:81-87, 124-131; SRC com/ichi2/anki/MyAccount.java:221-285',
  note='Edge from the launcher to the listener callback (label_019 convention). AsyncTask calls onPreExecute on the caller thread (AsyncTask.java:648). Connection.onPreExecute forwards to the listener (auto CALL, Connection.java:129). The task is launched only when isOnline is true (Connection.java:83), so env is ENV_NETWORK.')

e('MyAccount.login', 'MyAccount$5.onPostExecute', 'ASYNC',
  'the background login finishes; the listener saves the account and finishes, or shows an error snackbar',
  env=ENV_NETWORK,
  evidence='FW-SRC core/java/android/os/AsyncTask.java:327-341, 691-697; SRC com/ichi2/async/Connection.java:138-145; SRC com/ichi2/anki/MyAccount.java:221-285',
  note='Edge from the launcher to the listener callback (label_019 convention). AsyncTask.finish calls onPostExecute on the UI thread (AsyncTask.java:695). The success path needs a 200 reply with a key (Connection.java:221-225). Its CALLs (saveUserInformation, finishWithAnimation, snackbars) are in auto_calls.json.')

e('MyAccount.login', 'MyAccount$5.onProgressUpdate', 'ASYNC',
  'the login reply is read and progress is published; the listener body is empty',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:291-319, 393-402; SRC com/ichi2/async/Connection.java:196-225, 471-472; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718; SRC com/ichi2/anki/MyAccount.java:221-226',
  note='MISSING GATE MG294: the progress publish runs only when bytesReceived or bytesSent reaches 1024 (HttpSyncer.java:93-94, 312; the request-body writer calls publishProgress at HttpSyncer.java:400), so a login whose request and reply are both under 1024 bytes never reaches this callback. The network part of the route is ENV_NETWORK. Route after publish: Connection.publishProgress (Connection.java:471-472), AsyncTask.publishProgress (AsyncTask.java:684-689), InternalHandler (AsyncTask.java:715), Connection.onProgressUpdate (auto CALL, Connection.java:155).')

# --- UNREACHABLE: the logged-in view is never shown in a standard run (no hkey at launch; notLoggedIn always set).
UNREACHABLE['MyAccount.logout'] = ('branch_never_taken',
  "The only caller is MyAccount$4.onClick (auto CALL, MyAccount.java:211, via access$200). A grep of logout() over the source root shows no other caller. "
  "The logged-in view is shown only by switchToState(STATE_LOGGED_IN): from onCreate when hkey is stored (MyAccount.java:92-93), or from the success path when the notLoggedIn extra is absent (MyAccount.java:250-256). "
  "A standard launch has no hkey (DeckPicker.java:1278-1282, 1422-1430) and always sends notLoggedIn=true (DeckPicker.java:1571-1573), so the success path finishes (MyAccount.java:251-252) and neither branch runs.",
  'SRC com/ichi2/anki/MyAccount.java:147-161, 211, 92-95, 250-256; SRC com/ichi2/anki/DeckPicker.java:1278-1282, 1422-1430, 1569-1574',
  'SOURCE')

UNREACHABLE['MyAccount$4.onClick'] = ('branch_never_taken',
  "Logout button of the logged-in view. That view is shown only through switchToState(STATE_LOGGED_IN), which a standard run never reaches: hkey is empty at launch (DeckPicker.java:1278-1282, 1422-1430) and the launch always sends notLoggedIn=true (DeckPicker.java:1571-1573), so the success path finishes instead (MyAccount.java:251-252). "
  "The only route to this onClick goes through that view, so the branch is never taken. Its CALL to MyAccount.logout (MyAccount.java:211) is in auto_calls.json.",
  'SRC com/ichi2/anki/MyAccount.java:207-214, 92-95, 250-256; SRC com/ichi2/anki/DeckPicker.java:1278-1282, 1422-1430, 1571-1573',
  'SOURCE')

# MyAccount$4.onClick (logout button of the logged-in view) is UNREACHABLE: that view needs switchToState(STATE_LOGGED_IN), which a standard launch never reaches
sup(('MyAccount$4.onClick', 'MyAccount.logout'))

# ---- part 033 (2026-10-28)
# AnkiDroid batch 033 (LABEL helper). ModelFieldEditor part 1: 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_033.md. No method in this batch is UNREACHABLE, so there are no UNREACHABLE entries.
#
# Route ownership:
# - CALL edges inside ModelFieldEditor and into its anonymous classes come from auto_calls.json (for example
#   onOptionsItemSelected -> addFieldDialog, renameField -> Models.renameField). They are not written here.
# - The ASYNC launch edges into ModelFieldEditor$8.onPostExecute are written here, because the launch sites are in
#   this batch. The onPreExecute of $8 is not linked from the launch sites (label_019 convention).
# - Edges into methods outside this batch belong to the batch that holds those methods. The page edges from
#   S_MODELFIELDEDITOR and the ENTERS edges from these methods are written here, because their sources are in this batch.
#
# Gate MG272 (batch range MG272-MG281): the sync-required schema branch, which is the catch of
# ConfirmModSchemaException (Collection.modSchema(true) throws only when the schema is not yet marked changed,
# Collection.java:364-373). No predefined STATE kind covers that collection state, so env and needs_state are unset on
# the gated edges. Predefined constant used: STATE_COLLECTION on the page edges. Page node: S_MODELFIELDEDITOR.

# --- Lifecycle callback that starts the collection loader (ModelFieldEditor.onCreate, line 75).
e('ModelFieldEditor.onCreate', 'ModelFieldEditor.onCollectionLoaded', 'ASYNC',
  'the collection loader started by onCreate calls onCollectionLoaded when the collection is ready',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:72-75, 115-120; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-286',
  note='startLoadingCollection (AnkiActivity.java:255-262) restarts the loader, and AnkiActivity.onLoadFinished (283-286) calls onCollectionLoaded. Same route as the ModelBrowser precedent (label_031.py). No gate.')

# --- Page edges into the editor methods.
e('S_MODELFIELDEDITOR', 'ModelFieldEditor.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu of the field editor screen',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:102-107; FW-SRC core/java/android/app/Activity.java:3386-3388',
  note='The menu is inflated from res/menu/model_editor.xml, which holds the add button action_add_new_model. No gate.')

e('S_MODELFIELDEDITOR', 'ModelFieldEditor.onOptionsItemSelected', 'GUI',
  'tap the home arrow or the add button in the editor toolbar',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['tap the home arrow or the add button in the editor toolbar'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:553-564; RES res/menu/model_editor.xml:4-8; FW-SRC core/java/android/app/Activity.java:3439-3450',
  note='The home arrow (android.R.id.home) calls onBackPressed (line 556). The add button calls addFieldDialog (line 559). STATE_COLLECTION: the collection file exists, so the editor has loaded its note type.')

e('S_MODELFIELDEDITOR', 'ModelFieldEditor.onBackPressed', 'GUI',
  'press the system back key on the field editor screen',
  env=None,
  gui=['press the system back key on the field editor screen'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:584-587; FW-SRC core/java/android/app/Activity.java:2976-2983',
  note='The framework key-up path calls onBackPressed (Activity.java:2976-2983). The screen is the page, so no state or environment gate is set.')

e('S_MODELFIELDEDITOR', 'ModelFieldEditor$1.onItemClick', 'GUI',
  'tap a field name row on the field editor screen',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['tap a field name row on the field editor screen'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:116-120, 135-142; RES res/layout/model_field_editor.xml:12-19',
  note='The list is filled after the collection loads (onCollectionLoaded, line 116-120). STATE_COLLECTION: the collection file exists.')

e('ModelFieldEditor$1.onItemClick', 'S_DLG_MODELEDITOR_CONTEXT', 'ENTERS',
  'the field context menu (rename, reposition, sort, delete) is shown for the tapped row',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:137-141; SRC com/ichi2/anki/dialogs/ModelEditorContextMenu.java:34-38, 43',
  note='showDialogFragment(mContextMenu) at line 139. The menu entries are in ModelEditorContextMenu.java:34-38; their callback (batch 034) selects the field action. No gate.')

e('S_MODELFIELDEDITOR', 'ModelFieldEditor$2.onPositive', 'GUI',
  'tap the add button in the editor toolbar, type a field name and tap OK',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['tap the add button in the editor toolbar, type a field name and tap OK'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:149-163, 183, 186-199, 558-559; RES res/menu/model_editor.xml:4-8',
  note='The dialog is created by addFieldDialog (auto CALL from onOptionsItemSelected). mMod is set by setupLabels (line 151) after the collection loads, so STATE_COLLECTION is needed. The MaterialDialog OK dispatch is library code: INFERRED (source not read).')

e('ModelFieldEditor$2.onPositive', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the ADD_FIELD task launched from the add-field OK path; DeckTask calls the listener onPostExecute after the task',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:196-199; SRC com/ichi2/async/DeckTask.java:129-134, 324-325, 360-362, 1305-1307',
  note='The destination ModelFieldEditor$8.onPostExecute is batch 034 (mChangeFieldHandler). The edge is owned here because the launch site is in this batch. No gate on this route (modSchema() does not throw on a fresh install).')

e('ModelFieldEditor$2.onPositive', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the sync-required add-field dialog (full sync confirmation) is shown when the schema change needs confirmation',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:200-219; SRC com/ichi2/libanki/Collection.java:364-374; SRC com/ichi2/libanki/Storage.java:317-319; SRC com/ichi2/libanki/sync/Syncer.java:424-429',
  note='MISSING GATE MG272: the catch branch of modSchema() at line 197. A fresh install does not throw (Storage.java:317-319 sets scm = now and ls = 0), so this branch needs a collection whose schema is already marked changed. A sync sets ls (Syncer.java:428). env and needs_state unset.')

e('ModelFieldEditor$2$1.confirm', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the ADD_FIELD task relaunched after the user confirms the sync-required schema change; DeckTask calls the listener onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:208-209; SRC com/ichi2/async/DeckTask.java:129-134, 324-325, 360-362, 1305-1307',
  note='MISSING GATE MG272: reached only from the catch branch of the add-field OK path. The destination ModelFieldEditor$8.onPostExecute is batch 034. env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$2$1.confirm', 'GUI',
  'tap OK on the sync-required add-field dialog (full sync confirmation)',
  env=None,
  gui=['tap OK on the sync-required add-field dialog (full sync confirmation)'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:204-211; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch (ModelFieldEditor$2.onPositive). The dialog OK dispatch is ConfirmationDialog.onPositive -> confirm() (ConfirmationDialog.java:40-44). env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$2$1.cancel', 'GUI',
  'tap Cancel on the sync-required add-field dialog',
  env=None,
  gui=['tap Cancel on the sync-required add-field dialog'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:213-215; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch. ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49). env and needs_state unset.')

# --- Field delete (deleteField): the ASYNC launch of DELETE_FIELD.
e('ModelFieldEditor.deleteField', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the DELETE_FIELD task launched by deleteField; DeckTask calls the listener onPostExecute after the task',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:280-286; SRC com/ichi2/async/DeckTask.java:129-134, 318-319, 360-362, 1305-1307',
  note='The destination ModelFieldEditor$8.onPostExecute is batch 034 (mChangeFieldHandler). The edge is owned here because the launch site is in this batch. deleteField is called from the delete confirm methods ModelFieldEditor$3.confirm (ungated) and ModelFieldEditor$4.confirm (MISSING GATE MG272). No gate on this edge.')

# --- Field delete dialogs (deleteFieldDialog). The ENTERS edge covers both dialogs.
e('ModelFieldEditor.deleteFieldDialog', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the field delete warning is shown from the field context menu (delete); a second sync-required dialog uses the same page',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:239-256, 273-274',
  note='One ENTERS edge covers both dialogs shown from deleteFieldDialog: the delete warning (line 256, ungated) and the sync-required dialog (line 274, MISSING GATE MG272). The MG272 gate is carried by the S_DLG_CONFIRMATION -> ModelFieldEditor$4 edges below, so the triple is not duplicated. env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$3.confirm', 'GUI',
  'tap OK on the field delete warning',
  env=None,
  gui=['tap OK on the field delete warning'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:241-256; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44',
  note='The delete warning is the ungated branch (modSchema() does not throw on a fresh install). ConfirmationDialog.onPositive -> confirm() (ConfirmationDialog.java:40-44). No gate.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$3.cancel', 'GUI',
  'tap Cancel on the field delete warning',
  env=None,
  gui=['tap Cancel on the field delete warning'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:251-253; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='The delete warning is the ungated branch. ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49). No gate.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$4.confirm', 'GUI',
  'tap OK on the sync-required field delete dialog (full sync confirmation)',
  env=None,
  gui=['tap OK on the sync-required field delete dialog (full sync confirmation)'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:259-267; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch of deleteFieldDialog (line 257). ConfirmationDialog.onPositive -> confirm() (ConfirmationDialog.java:40-44). env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$4.cancel', 'GUI',
  'tap Cancel on the sync-required field delete dialog',
  env=None,
  gui=['tap Cancel on the sync-required field delete dialog'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:269-271; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch of deleteFieldDialog. ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49). env and needs_state unset.')

# --- Sort field (sortByField): the ASYNC launch and the sync-required dialog.
e('ModelFieldEditor.sortByField', 'ModelFieldEditor$8.onPostExecute', 'ASYNC',
  'the CHANGE_SORT_FIELD task launched by sortByField; DeckTask calls the listener onPostExecute after the task',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:458-462; SRC com/ichi2/async/DeckTask.java:129-134, 327-328, 360-362, 1305-1307',
  note='The destination ModelFieldEditor$8.onPostExecute is batch 034. The edge is owned here because the launch site is in this batch. The direct launch (line 461) runs when modSchema() does not throw, so no gate on this edge.')

e('ModelFieldEditor.sortByField', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the sync-required sort field dialog is shown when the schema change needs confirmation',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:458-479',
  note='MISSING GATE MG272: the catch branch of sortByField (modSchema() call at line 460, catch at line 463, dialog shown at line 478). The dialog is ModelFieldEditor$7 (batch 034). A fresh install does not throw, so this needs a collection whose schema is already marked changed. env and needs_state unset.')

# --- Rename dialog (renameFieldDialog).
e('S_MODELFIELDEDITOR', 'ModelFieldEditor$5.onPositive', 'GUI',
  'long-press a field row, choose Rename in the context menu, then tap OK in the rename dialog',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['long-press a field row, choose Rename in the context menu, then tap OK in the rename dialog'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:293-304, 116-120, 135-142; SRC com/ichi2/anki/dialogs/ModelEditorContextMenu.java:12-14, 34-38',
  note='The route goes through the field context menu (S_DLG_MODELEDITOR_CONTEXT, selection by ModelFieldEditor$9.onSelection, batch 034, FIELD_RENAME = 2). The rename dialog is shown over this page. STATE_COLLECTION: the field list is loaded.')

e('ModelFieldEditor$5.onPositive', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the sync-required rename dialog is shown when renameField throws ConfirmModSchemaException',
  env=None,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:315-336; SRC com/ichi2/libanki/Collection.java:364-374',
  note='MISSING GATE MG272: the catch branch of renameField at line 316 (renameField calls Models.renameField, which calls mCol.modSchema(true)). The dialog is ModelFieldEditor$5$1. env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ModelFieldEditor$5$1.cancel', 'GUI',
  'tap Cancel on the sync-required rename dialog',
  env=None,
  gui=['tap Cancel on the sync-required rename dialog'],
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:330-332; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49',
  note='MISSING GATE MG272: the dialog is shown only from the catch branch of renameField. ConfirmationDialog.onNegative -> cancel() (ConfirmationDialog.java:46-49). The confirm method ModelFieldEditor$5$1.confirm is outside this batch. env and needs_state unset.')

# ---- part 038 (2026-10-28)
# AnkiDroid batch 038 (LABEL helper). StudyOptionsFragment: 38 methods. The full row list is in
# graphs/AnkiDroid/parts/label_038.md.
#
# Ownership: CALL edges (auto_calls.json) and the lc_chain LIFECYCLE edges (graph_def.py:215-216) are not written here.
# The two existing INTENT edges (S_STUDYOPTIONS_FRAG -> FilteredDeckOptions.<init>, DeckOptions.<init>) and the sup()
# pairs (graph_def.py:1235-1236) are not repeated here.
# Page-sourced edges into batch-038 methods are written here (start button, toolbar menu, phone back arrow), and the
# custom study page edge (graph_def.py:1148-1149). DeckTask ASYNC launch edges go from the launcher to the listener
# callback $3.onPostExecute, as in label_019.py:43.
#
# Gates: MG324 (1000 new cards), MG323 and MG325 (toolbar items), MG327 (phone layout), MG329 (congrats button).
# Predefined constants used: STATE_CARDS (start button), STATE_DECK (toolbar and custom study).
# Page nodes: S_STUDYOPTIONS_FRAG (the fragment, in both hosts) and S_DLG_CUSTOM_STUDY.

# --- Page edges into the fragment's own methods.

# Start button (R.id.studyoptions_start), set in initAllContentViews (StudyOptionsFragment.java:265).
e('S_STUDYOPTIONS_FRAG', 'StudyOptionsFragment$1.onClick', 'GUI',
  'tap the Start button of the study options page (study the deck, or open custom study on the congrats content)',
  env=None,
  needs_state=STATE_CARDS,
  gui=['tap the Start button of the study options page (study the deck, or open custom study on the congrats content)'],
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:120-136, 265, 570-586',
  note='The Start button is shown with the study-options content only when cards are due or learning (lines 581-585), so STATE_CARDS is the gate. On the congrats content (lines 570-574) the same button opens custom study (line 130); that case is MISSING GATE MG329: it needs a non-filtered deck with no cards due.')

# Toolbar menu (configureToolbar sets the listener to the fragment at StudyOptionsFragment.java:343).
e('S_STUDYOPTIONS_FRAG', 'StudyOptionsFragment.onMenuItemClick', 'GUI',
  'tap an item of the study options toolbar menu (undo, deck options, custom study, unbury, rebuild, empty, rename, delete, export)',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap an item of the study options toolbar menu (undo, deck options, custom study, unbury, rebuild, empty, rename, delete, export)'],
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:186, 287-343, 346-370',
  note='Item gates: MISSING GATE MG322 for unbury (visible only when cards are buried, line 370); MISSING GATE MG323 for custom study (lines 346-357); MISSING GATE MG325 for rebuild and empty (visible only for a filtered deck, lines 346-348). Rename, delete and export (lines 328-335) call DeckPicker methods: confirmDeckDeletion and exportDeck have edges from S_STUDYOPTIONS_FRAG in label_002.py:207-212; renameDeckDialog has no edge in any part (lead). Undo, deck options and custom study call openReviewer, openFilteredDeckOptions and showCustomStudyContextMenu by CALL (auto_calls.json).')

# Back arrow on the fragment toolbar, set in configureToolbar (lines 380-388) only when mFragmented is false.
e('S_STUDYOPTIONS_FRAG', 'StudyOptionsFragment$2.onClick', 'GUI',
  'tap the back arrow of the study options toolbar in the phone layout (hosted by StudyOptionsActivity)',
  env=None,
  gui=['tap the back arrow of the study options toolbar in the phone layout (hosted by StudyOptionsActivity)'],
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:180, 380-388',
  note='MISSING GATE MG327: the arrow exists only when mFragmented is false, which is the StudyOptionsActivity host (phone layout, StudyOptionsFragment.java:180). No predefined ENV or STATE covers the device layout. env and needs_state unset.')

# Custom study page edge (graph_def.py:1148-1149 ownership). The dialog callbacks are label_002 and label_007.
e('StudyOptionsFragment.showCustomStudyContextMenu', 'S_DLG_CUSTOM_STUDY', 'ENTERS',
  'the custom study menu dialog is created and shown by showCustomStudyContextMenu (toolbar item, or the congrats start button)',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:272-276; SRC com/ichi2/anki/StudyOptionsFragment.java:127-131, 306-307',
  note='The user step is the GUI edge S_STUDYOPTIONS_FRAG -> StudyOptionsFragment.onMenuItemClick (label_038). MISSING GATE MG323: the toolbar item is hidden for filtered decks and on the congrats content (StudyOptionsFragment.java:346-357). MISSING GATE MG329: the congrats button is shown only for a non-filtered deck with no cards due (lines 570-574). The custom study dialog callbacks are label_002 (DeckPicker) and label_007 (StudyOptionsActivity).')

# --- DeckTask ASYNC launch edges into the listener callback $3.onPostExecute (same pattern as label_019.py:43).

e('StudyOptionsFragment.onMenuItemClick', 'StudyOptionsFragment$3.onPostExecute', 'ASYNC',
  'the rebuild or empty cram task started from the toolbar finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:314-327, 503-504, 511; SRC com/ichi2/async/DeckTask.java:129, 358-365, 1306-1309',
  note='MISSING GATE MG325: the rebuild and empty items are visible only for a filtered deck (StudyOptionsFragment.java:346-348). Task types: TASK_TYPE_REBUILD_CRAM (line 318) and TASK_TYPE_EMPTY_CRAM (line 325). The launch CALL inside DeckTask.launchDeckTask (DeckTask.java:129) is not written here. needs_state unset.')

e('StudyOptionsFragment.refreshInterface(boolean,boolean)', 'StudyOptionsFragment$3.onPostExecute', 'ASYNC',
  'the update-values task started by the interface refresh finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:489-494, 511; SRC com/ichi2/async/DeckTask.java:77, 129, 358-365, 1306-1309',
  note='Task type TASK_TYPE_UPDATE_VALUES_FROM_DECK (23, DeckTask.java:77). The refresh is reached from onCreateView (line 190) and onResume (line 209), so no gate is needed. The launch CALL (DeckTask.java:129) is not written here.')

# --- Full new count thread (StudyOptionsFragment.java:618-641), gated by a deck with at least 1000 new cards.

e('StudyOptionsFragment$3.onPostExecute', 'StudyOptionsFragment$3$1.run', 'ASYNC',
  'the full new count thread starts when the deck has at least 1000 new cards (the count was truncated)',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:608-618, 641; INFERRED JVM Thread.start (not in fw_src, source not read)',
  note='MISSING GATE MG324: totalNew must be at least NEW_CARD_COUNT_TRUNCATE_THRESHOLD = 1000 (StudyOptionsFragment.java:65, 608). This is a data state with no predefined STATE constant and it is not in the standard fixture. needs_state unset.')

e('StudyOptionsFragment$3$1.run', 'StudyOptionsFragment$3$1$1.run', 'ASYNC',
  'the count thread posts the full new count text to the new-cards view',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:628-636; FW-SRC core/java/android/view/View.java:15777-15787; FW-SRC core/java/android/os/Handler.java:97, 355-357, 776-781, 789',
  note='MISSING GATE MG324 as in the thread start edge, and fullNewCount must be above 0 (StudyOptionsFragment.java:628). The post goes to the attach handler or to the run queue (View.java:15777-15787), and Handler dispatch runs it (Handler.java:97, 789).')

# --- UNREACHABLE entries.

# onActivityResult: the fragment is never a result target. Every startActivityForResult in this class is called on
# getActivity() (lines 152, 230, 300), and the request codes are small (BROWSE_CARDS=3, STATISTICS=4, DECK_OPTIONS=5,
# lines 53-55), so the support-library fragment index bits are zero. The host activities receive the results.
UNREACHABLE['StudyOptionsFragment.onActivityResult'] = ('framework_never_calls', 'the fragment is never a result target: every startActivityForResult in StudyOptionsFragment is called on getActivity() (lines 152, 230, 300), so results go to the host activity; the request codes are small (BROWSE_CARDS=3, STATISTICS=4, DECK_OPTIONS=5, lines 53-55), so the support-library fragment index bits are zero; the host activities handle their own results (StudyOptionsActivity.onActivityResult, DeckPicker.onActivityResult). INFERRED: support-library dispatch is not in fw_src (source not read).', 'SRC com/ichi2/anki/StudyOptionsFragment.java:53-55, 152, 230, 300, 393; SRC com/ichi2/anki/StudyOptionsActivity.java:83-91; SRC com/ichi2/anki/DeckPicker.java:634', 'INFERRED')

# closeStudyOptions: the only caller is onActivityResult (line 402), which is unreachable.
UNREACHABLE['StudyOptionsFragment.closeStudyOptions'] = ('framework_never_calls', 'the only caller is onActivityResult (line 402), and the framework never calls onActivityResult on this fragment (support-library result dispatch, INFERRED: source not read)', 'SRC com/ichi2/anki/StudyOptionsFragment.java:213-224, 401-403', 'INFERRED')

# setFragmentContentView: the only caller in the app tree is onActivityResult (line 444).
UNREACHABLE['StudyOptionsFragment.setFragmentContentView'] = ('framework_never_calls', 'the only caller in the app tree is onActivityResult (line 444), and the framework never calls onActivityResult on this fragment (support-library result dispatch, INFERRED: source not read)', 'SRC com/ichi2/anki/StudyOptionsFragment.java:279-283, 443-444', 'INFERRED')

# $3.onCancelled: no DeckTask of the three types used here is ever cancelled.
UNREACHABLE['StudyOptionsFragment$3.onCancelled'] = ('no_trigger_in_app', 'DeckTask.onCancelled calls the listener only after an AsyncTask cancel (DeckTask.java:368-370). The only DeckTask cancel path is cancelTask(int) (DeckTask.java:181-184), which cancels only when the latest task type matches; its callers pass SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). The no-argument cancelTask() (DeckTask.java:168-178) is called only from cancelTask(int). The three task types this fragment launches (23 UPDATE_VALUES_FROM_DECK, 26 REBUILD_CRAM, 27 EMPTY_CRAM) are never cancelled. TaskOperations.stopTaskGracefully cancels a non-DeckTask task (TaskOperations.java:33).', 'SRC com/ichi2/anki/StudyOptionsFragment.java:668-670; SRC com/ichi2/async/DeckTask.java:77-80, 168-184, 368-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:33', 'SOURCE')

# $3.onProgressUpdate: none of the three task bodies calls publishProgress.
UNREACHABLE['StudyOptionsFragment$3.onProgressUpdate'] = ('no_trigger_in_app', 'the listener onProgressUpdate runs only when a task calls publishProgress (DeckTask.java:352-355). The publishProgress calls are in other task bodies (DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659). None is in doInBackgroundUpdateValuesFromDeck (697-718), doInBackgroundRebuildCram (728-735) or doInBackgroundEmptyCram (736-743), the only three task types this fragment launches (TASK_TYPE_UPDATE_VALUES_FROM_DECK 23, TASK_TYPE_REBUILD_CRAM 26, TASK_TYPE_EMPTY_CRAM 27).', 'SRC com/ichi2/anki/StudyOptionsFragment.java:663-665; SRC com/ichi2/async/DeckTask.java:352-355, 380-659, 697-743', 'SOURCE')

# ---- sup for part 038 (2026-10-28): automatic edges into batch 038 UNREACHABLE methods; the sources are never triggered (see label_038.md)
sup(('DeckTask.onCancelled', 'StudyOptionsFragment$3.onCancelled'))
sup(('DeckTask$TaskListener.onProgressUpdate', 'StudyOptionsFragment$3.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@StudyOptionsFragment$3', 'StudyOptionsFragment$3.onProgressUpdate'))
sup(('StudyOptionsFragment.onActivityResult', 'StudyOptionsFragment.setFragmentContentView'))
sup(('StudyOptionsFragment.onActivityResult', 'StudyOptionsFragment.closeStudyOptions'))

# ---- part 039 (2026-10-28)
e('S_VIDEOPLAYER', 'VideoPlayer.onConfigurationChanged', 'SYSTEM',
  'the device configuration changes while the video player is open (rotation, locale, screen size); the activity is not restarted because the manifest lists these in configChanges',
  env=ENV_CONFIG_CHANGE,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:73-76; SRC final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/AndroidManifest.xml:184; FW-SRC core/java/android/app/ActivityThread.java:4893-4896, 4942',
  note='Delivery path: ActivityThread.handleConfigurationChanged (4971), loop at 5031-5037, performConfigurationChangedForActivity (4803-4809), activity.onConfigurationChanged (4942). The body call to Sound.notifyConfigurationChanged (line 75) is not written here. Constant ENV_CONFIG_CHANGE is graph_def.py:126.')

e('S_VIDEOPLAYER', 'VideoPlayer$1.onCompletion', 'FRAMEWORK',
  'the video reaches its end; the MediaPlayer completion listener is set directly on the player by Sound.playSound',
  env=None,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:50-59; SRC com/ichi2/libanki/Sound.java:322, 325-326, 328; FW-SRC media/java/android/media/MediaPlayer.java:3235-3240',
  note='MediaPlayer handles MEDIA_PLAYBACK_COMPLETE and calls onCompletionListener.onCompletion (FW-SRC MediaPlayer.java:3235-3240). The MediaPlayer step is FW-SRC grounded; the listener registration is Sound.java:325-326.')

e('S_VIDEOPLAYER', 'VideoPlayer.surfaceCreated', 'FRAMEWORK',
  'the video surface is created while the player screen is shown (SurfaceHolder callback registered at VideoPlayer.java:45)',
  env=None,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:45, 49-50; SRC com/ichi2/libanki/Sound.java:268, 292-293',
  note='INFERRED: the SurfaceHolder dispatch is not read because SurfaceView is absent from fw_src (source not read). Body calls Sound.playSound with the path, the completion listener and mVideoView (lines 50-59).')

e('S_VIDEOPLAYER', 'VideoPlayer.surfaceChanged', 'FRAMEWORK',
  'the video surface changes size or format while the player screen is shown (SurfaceHolder callback registered at VideoPlayer.java:45)',
  env=None,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:45, 61-66',
  note='INFERRED: the SurfaceHolder dispatch is not read because SurfaceView is absent from fw_src (source not read). The body is an empty TODO, so the call has no effect.')

e('S_VIDEOPLAYER', 'VideoPlayer.surfaceDestroyed', 'FRAMEWORK',
  'the video surface is destroyed when the player leaves the foreground or finishes (SurfaceHolder callback registered at VideoPlayer.java:45)',
  env=None,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:45, 68-71',
  note='INFERRED: the SurfaceHolder dispatch is not read because SurfaceView is absent from fw_src (source not read). Body stops the sounds (line 69) and finishes the activity (line 70).')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$1.onSelection', 'GUI',
  'the user taps a saved-search name in the LIST dialog',
  gui=['tap a saved-search name in the saved searches list dialog'],
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:65-76; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:73',
  note='MISSING GATE MG332: at least one saved search must exist before the LIST dialog has a row to tap. No predefined STATE constant covers saved searches, so env and needs_state are unset. The MaterialDialog list callback dispatch is INFERRED (library not read). The listener target CardBrowser$3.OnSelection is written in graph_def.py:1659.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$2.onInput', 'GUI',
  'the user types a name in the save-search dialog and confirms',
  gui=['type a name in the save searches dialog and confirm'],
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:77-87; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:85',
  note='The MaterialDialog input callback dispatch is INFERRED (library not read). The listener target CardBrowser$3.OnSaveSearch is written in graph_def.py:1675. No gate: the save dialog is opened by the action_save_search menu item.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$3.onPositive', 'GUI',
  'the user taps OK on the remove-search confirmation dialog',
  gui=['tap OK on the remove saved search confirmation dialog'],
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:102-121; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:112',
  note='MISSING GATE MG332: a saved search must exist so that removeSearch shows the confirmation dialog (line 103). No predefined STATE constant covers saved searches, so env and needs_state are unset. The MaterialDialog button callback dispatch is INFERRED (library not read). The listener target CardBrowser$3.OnRemoveSearch is written in graph_def.py:1667.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$MySearchesArrayAdapter$1.onClick', 'GUI',
  'the user taps the remove button of a saved-search row in the LIST dialog',
  gui=['tap the remove button on a saved-search row in the saved searches list dialog'],
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:161-166; SRC res/layout/card_browser_item_my_searches_dialog.xml:25; FW-SRC core/java/android/view/View.java:6289-6294',
  note='MISSING GATE MG332: a saved-search row must exist to render the remove button (getView, line 143). No predefined STATE constant covers saved searches, so env and needs_state are unset. Body calls removeSearch through access$700 (line 164, auto CALL).')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$MySearchesArrayAdapter.getView', 'FRAMEWORK',
  'the LIST dialog lays out a saved-search row',
  env=None,
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2335, 2365; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:143-168',
  note='MISSING GATE MG332: at least one saved search must exist so that the list has a row. No predefined STATE constant covers saved searches, so env and needs_state are unset. The AbsListView.obtainView path is FW-SRC grounded; the library setAdapter call is INFERRED (library not read).')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowserMySearchesDialog$MySearchesArrayAdapter.areAllItemsEnabled', 'FRAMEWORK',
  'the list view queries whether all items are enabled when the LIST dialog adapter is set',
  env=None,
  evidence='FW-SRC core/java/android/widget/ListView.java:552, 573; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:67-70, 182-184',
  note='The ListView.setAdapter call is INFERRED (the MaterialDialog builder path is not read). No gate: the LIST dialog itself is enough. Body returns true.')

e('CardBrowserMySearchesDialog$MySearchesArrayAdapter.notifyDataSetChanged', 'CardBrowserMySearchesDialog$MySearchesArrayAdapter$2.compare', 'CALL',
  'Collections.sort inside notifyDataSetChanged calls the comparator to order the saved-search names',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:171-177',
  note='INFERRED: the JDK sort path is not in fw_src, so the comparator call is not read. No auto CALL edge exists for this pair in auto_calls.json, so the edge is written here.')

# ---- part 036 (2026-10-28)
# AnkiDroid batch 036 (LABEL helper). NavigationDrawerActivity (the navigation drawer) and Previewer: 30 methods.
# The full row list is in graphs/AnkiDroid/parts/label_036.md. This part writes 22 edges and no UNREACHABLE entries.
#
# Route ownership:
# - Automatic CALL edges (bytecode builder) are not written here, for example DeckPicker.onCreate -> initNavigationDrawer,
#   Previewer.onCreate -> disableDrawerSwipe and showBackIcon, and DeckPicker.onBackPressed -> super.onBackPressed.
# - Edges whose source is in another part are not written here: AnkiActivity.onLoadFinished -> Previewer.onCollectionLoaded,
#   AbstractFlashcardViewer.onCollectionLoaded -> Previewer.initLayout / setTitle / updateScreenCounts,
#   AbstractFlashcardViewer.onResume -> Previewer.updateScreenCounts, and the start-long-click runnable (batch 021) ->
#   Previewer.executeCommand.
# - The virtual dispatch from NavigationDrawerActivity.onNavigationItemSelected to the DeckPicker and Reviewer
#   openCardBrowser overrides is written here (E9, E10).
#
# Gates: MG302 (the chosen drawer item is not already checked), MG303 (the activity has a toolbar). Predefined constants
# used: ENV_CONFIG_CHANGE, STATE_SETTINGS. Page nodes used: S_ENTRY, S_DECKPICKER, S_STUDYOPTIONS, S_CARDBROWSER,
# S_STATISTICS, S_REVIEWER, S_PREVIEWER.

# --- Drawer page edges (the drawer is on five screens; the destination is in this part).
e('S_DECKPICKER', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the deck list',
  env=None,
  gui=['pick an item in the navigation drawer on the deck list'],
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:68, 249-290; SRC com/ichi2/anki/DeckPicker.java:110',
  note='Page edge. The NavigationView dispatch is the support library, not in fw_src: INFERRED.')

e('S_STUDYOPTIONS', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the study options screen',
  env=None,
  gui=['pick an item in the navigation drawer on the study options screen'],
  evidence='SRC com/ichi2/anki/StudyOptionsActivity.java:31; SRC com/ichi2/anki/NavigationDrawerActivity.java:249-290',
  note='Page edge. The same drawer listener as S_DECKPICKER.')

e('S_CARDBROWSER', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the card browser',
  env=None,
  gui=['pick an item in the navigation drawer on the card browser'],
  evidence='SRC com/ichi2/anki/CardBrowser.java:86; SRC com/ichi2/anki/NavigationDrawerActivity.java:249-290',
  note='Page edge. The same drawer listener as S_DECKPICKER.')

e('S_STATISTICS', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the statistics screen',
  env=None,
  gui=['pick an item in the navigation drawer on the statistics screen'],
  evidence='SRC com/ichi2/anki/Statistics.java:59; SRC com/ichi2/anki/NavigationDrawerActivity.java:249-290',
  note='Page edge. The same drawer listener as S_DECKPICKER.')

e('S_REVIEWER', 'NavigationDrawerActivity.onNavigationItemSelected', 'GUI',
  'pick an item in the navigation drawer on the reviewer',
  env=None,
  gui=['pick an item in the navigation drawer on the reviewer'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:110; SRC com/ichi2/anki/Reviewer.java:56; SRC com/ichi2/anki/NavigationDrawerActivity.java:249-290',
  note='Page edge. The Reviewer is an AbstractFlashcardViewer, which extends NavigationDrawerActivity.')

# --- Drawer items (MG302: the item must not already be checked, NavigationDrawerActivity.java:252).
e('NavigationDrawerActivity.onNavigationItemSelected', 'DeckPicker.<init>', 'INTENT',
  'choose the Decks item in the drawer: start DeckPicker with CLEAR_TOP and NEW_TASK',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:252-260',
  note='MISSING GATE MG302: the Decks item is not already checked (NavigationDrawerActivity.java:252 returns true when it is). env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'Statistics.<init>', 'INTENT',
  'choose the Statistics item in the drawer: start Statistics with the selected deck',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:265-268',
  note='MISSING GATE MG302: the Statistics item is not already checked (NavigationDrawerActivity.java:252). The request code is REQUEST_STATISTICS. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'Preferences.<init>', 'INTENT',
  'choose the Settings item in the drawer: start Preferences with REQUEST_PREFERENCES_UPDATE',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:273-277',
  note='MISSING GATE MG302: the Settings item is not already checked (NavigationDrawerActivity.java:252). graph_def.py:1240 is a different edge (DeckPicker.onCreate to Preferences.<init>). env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'DeckPicker.openCardBrowser', 'CALL',
  'choose the Card browser item in the drawer on the deck list (virtual dispatch to the DeckPicker override)',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:262-264; SRC com/ichi2/anki/DeckPicker.java:1707-1713',
  note='MISSING GATE MG302: the Card browser item is not already checked (NavigationDrawerActivity.java:252). The call at line 263 resolves to the DeckPicker override by virtual dispatch. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'Reviewer.openCardBrowser', 'CALL',
  'choose the Card browser item in the drawer on the reviewer (virtual dispatch to the Reviewer override)',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:262-264; SRC com/ichi2/anki/Reviewer.java:507-513',
  note='MISSING GATE MG302: the Card browser item is not already checked (NavigationDrawerActivity.java:252). The call at line 263 resolves to the Reviewer override by virtual dispatch. env and needs_state unset.')

e('NavigationDrawerActivity.openCardBrowser', 'CardBrowser.<init>', 'INTENT',
  'open the card browser from the drawer on the study options or statistics screen',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:295-299',
  note='Start CardBrowser with the selected deck and REQUEST_BROWSE_CARDS. The DeckPicker and Reviewer overrides already have this edge (graph_def.py:1272, 1331).')

e('NavigationDrawerActivity.onNavigationItemSelected', 'NavigationDrawerActivity$2.onCheckedChanged', 'FRAMEWORK',
  'choose the night-mode item in the drawer: performClick toggles the switch and fires its listener',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:270-272, 89-105',
  note='MISSING GATE MG302: the night-mode item is not already checked (NavigationDrawerActivity.java:252). The click dispatch on SwitchCompat/CompoundButton is the support library, not in fw_src: INFERRED. env and needs_state unset.')

# --- Night-mode switch and toolbar button (page edges), and drawer listener edges.
e('S_DECKPICKER', 'NavigationDrawerActivity$2.onCheckedChanged', 'GUI',
  'toggle the night-mode switch in the drawer on the deck list',
  env=None,
  gui=['toggle the night-mode switch in the drawer on the deck list'],
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:89-105',
  note='Page edge. The listener saves the invertedColors preference and restarts the activity (NavigationDrawerActivity.java:96-103).')

e('S_DECKPICKER', 'NavigationDrawerActivity$1.onClick', 'GUI',
  'tap the toolbar navigation button on the deck list (opens the drawer)',
  env=None,
  gui=['tap the toolbar navigation button on the deck list (opens the drawer)'],
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:69-86',
  note='MISSING GATE MG303: the activity has a toolbar (NavigationDrawerActivity.java:69-70 tests toolbar != null). mNavButtonGoesBack stays false on the deck list, so the listener opens the drawer (line 83). env and needs_state unset.')

e('NavigationDrawerActivity$1.onClick', 'NavigationDrawerActivity$3.onDrawerOpened', 'FRAMEWORK',
  'openDrawer at line 83 calls the drawer listener, which runs onDrawerOpened',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:83, 116-120',
  note='The DrawerLayout dispatch to the listener is the support library, not in fw_src: INFERRED.')

e('NavigationDrawerActivity.onNavigationItemSelected', 'NavigationDrawerActivity$3.onDrawerClosed', 'FRAMEWORK',
  'closeDrawers at line 288 calls the drawer listener, which runs onDrawerClosed',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:288, 110-113',
  note='The DrawerLayout dispatch to the listener is the support library, not in fw_src: INFERRED.')

e('NavigationDrawerActivity.onBackPressed', 'NavigationDrawerActivity$3.onDrawerClosed', 'FRAMEWORK',
  'closeDrawers at line 243 calls the drawer listener, which runs onDrawerClosed',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:241-243, 110-113',
  note='The Back key with the drawer open closes it. The DrawerLayout dispatch to the listener is the support library, not in fw_src: INFERRED.')

# --- Configuration change and lifecycle.
e('S_ENTRY', 'NavigationDrawerActivity.onConfigurationChanged', 'SYSTEM',
  'the device configuration changes while the app runs (rotation, locale, screen size)',
  env=ENV_CONFIG_CHANGE,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:173-180; FW-SRC core/java/android/app/ActivityThread.java:4785-4804; FW-SRC core/java/android/app/Activity.java:2196-2200; SRC final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/AndroidManifest.xml:132-138',
  note='DeckPicker declares configChanges keyboardHidden, orientation, screenSize, locale (AndroidManifest.xml lines 132-138), so the change reaches the running activity without a restart.')

e('S_DECKPICKER', 'NavigationDrawerActivity.onPostCreate', 'LIFECYCLE',
  'the framework calls onPostCreate after the deck list starts',
  env=None,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2757-2760; SRC com/ichi2/anki/NavigationDrawerActivity.java:164-171; FW-SRC core/java/android/app/Activity.java:1198-1202',
  note='S_DECKPICKER is entered by DeckPicker.onCreate (ENTERS, graph_def.py:835). The framework callback path (callActivityOnPostCreate) is FW-SRC; the dispatch from the page is the lifecycle order.')

# --- Previewer.
e('S_PREVIEWER', 'Previewer.displayCardAnswer', 'GUI',
  'tap the show-answer control on the preview screen',
  env=None,
  gui=['tap the show-answer control on the preview screen'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:382-394, 1384; SRC com/ichi2/anki/Previewer.java:67-74',
  note='Page edge. The flip listener calls displayCardAnswer at AbstractFlashcardViewer.java:392, which dispatches virtually to this override.')

e('Previewer.onCollectionLoaded', 'S_PREVIEWER', 'ENTERS',
  'the preview screen is shown after the card loads and the question is displayed',
  env=None,
  evidence='SRC com/ichi2/anki/Previewer.java:45-51',
  note='Method to page (ENTERS). The loader delivery edge into onCollectionLoaded is the AnkiActivity part (AnkiActivity.java:283-286).')

e('S_PREVIEWER', 'Previewer.executeCommand', 'GUI',
  'long-press the card area on the preview screen when the long-click workaround is on',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['long-press the card area on the preview screen when the long-click workaround is on'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:373-378, 468-481, 1334-1335, 1719-1720; SRC com/ichi2/anki/Previewer.java:83-86',
  note='The long-click listener is set only when !mDisableClipboard and mLongClickWorkaround (the dictionary preference is not "0", and textSelectionLongclickWorkaround is true). Both are STATE_SETTINGS. The gesture branches (AbstractFlashcardViewer.java:2681-2752) reach the same override only when gestures are on (STATE_SETTINGS); the run body of the long-click runnable is batch 021.')

# ---- addenda (2026-10-28): method-level INTENT edges that the build showed were missing.
# StudyOptionsFragment.openReviewer is owned by batch 038; AbstractFlashcardViewer.playVideo by batch 020.
e('StudyOptionsFragment.openReviewer', 'Reviewer.<init>', 'INTENT',
  'open the reviewer from the study options page (start button, undo item)',
  env=None,
  evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:227-228',
  note='Reached from the start button (line 128, shown only with cards; see S_STUDYOPTIONS_FRAG -> StudyOptionsFragment$1.onClick) and from the undo item (line 292). No STATE constant is set on this edge, so the gate stays on the callers.')

e('AbstractFlashcardViewer.playVideo', 'VideoPlayer.<init>', 'INTENT',
  'start the video player for a video file of the card',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2799-2802',
  note='MISSING GATE MG142: the card must have a video file (playVideo is called from Sound.java:292 only when the sound is a video). No STATE constant fits, so needs_state is unset.')

# ---- part 037 (2026-10-28)
# AnkiDroid batch 037 (Statistics, 39 methods), LABEL helper. Writes the page, lifecycle, framework, GUI and
# cross-batch edges for the Statistics screen and its fragments, plus the UNREACHABLE entries. Method-level labels and
# sources are in graphs/AnkiDroid/parts/label_037.md (one row per method, and one EDGE row per edge below).
# No imports: e() and UNREACHABLE are the ones defined by graph_def.py, which loads this part.
# Automatic CALL edges come from graphs/AnkiDroid/auto_calls.json (dispatch exact or cha) and are not written here.
# onDestroy is on LC_NO_TRIGGER (graph_def.py:37), so the two onDestroy FRAMEWORK edges are written by hand.
# Support-library steps (Fragment lifecycle, FragmentPagerAdapter, ViewPager, AppCompat options menu) are not in
# fw_src: they are INFERRED, source not read. Framework spinner steps are read from fw_src (Spinner.java, AdapterView.java).
# AbsSpinner is not in fw_src, so the default spinner selection and the spinner draw path are INFERRED.
# No gate applies (the menus, the spinner and the Back key work once the collection has loaded): env is None and
# needs_state is not set on any edge. Gates MG312-MG321 are not needed.

# --- Existing page and framework edges (6) ---

e('S_STATISTICS', 'Statistics.onBackPressed', 'GUI',
  'the user presses the Back key on the statistics screen',
  gui=['the user presses the Back key on the statistics screen'],
  env=None,
  note='Back key route. Activity.onKeyUp calls onBackPressed (Activity.java:2979). The key tracking starts in onKeyDown (targetSdk >= ECLAIR).',
  evidence='SRC com/ichi2/anki/Statistics.java:698-711; FW-SRC core/java/android/app/Activity.java:2886-2893, 2976-2981')

e('Statistics.onCreate', 'Statistics.onCollectionLoaded', 'ASYNC',
  'the collection loader delivers onLoadFinished after startLoadingCollection',
  env=None,
  note='ASYNC edge from onCreate to the collection-loaded callback. Written by hand: it is driven by the loader, not by a direct call.',
  evidence='SRC com/ichi2/anki/Statistics.java:88, 92; SRC com/ichi2/anki/AnkiActivity.java:255-262, 282-290')

e('Statistics.onCollectionLoaded', 'Statistics.onCreateOptionsMenu', 'FRAMEWORK',
  'supportInvalidateOptionsMenu at the end of onCollectionLoaded makes the framework build the options panel',
  env=None,
  note='Framework edge. The AppCompat path (supportInvalidateOptionsMenu) is in the support library, not fw_src: INFERRED, source not read. Activity.onCreatePanelMenu is read (Activity.java:3386-3388).',
  evidence='SRC com/ichi2/anki/Statistics.java:132, 170-177; FW-SRC core/java/android/app/Activity.java:3386-3388')

e('S_STATISTICS', 'Statistics.onOptionsItemSelected', 'GUI',
  'the user taps a time range (month, year, all) or the chooser in the options menu',
  gui=['the user taps a time range (month, year, all) or the chooser in the options menu'],
  env=None,
  note='Options menu item route. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3439-3450). No gate.',
  evidence='SRC res/menu/anki_stats.xml (src/main, lines 7-20); SRC com/ichi2/anki/Statistics.java:203-239; FW-SRC core/java/android/app/Activity.java:3439-3450')

e('S_STATISTICS', 'Statistics.onPrepareOptionsMenu', 'GUI',
  'the user opens the options panel of the statistics screen',
  gui=['the user opens the options panel of the statistics screen'],
  env=None,
  note='Options panel open route. The framework calls onPrepareOptionsMenu through onPreparePanel (Activity.java:3404-3406).',
  evidence='SRC com/ichi2/anki/Statistics.java:180-201; FW-SRC core/java/android/app/Activity.java:3404-3406')

e('Statistics.onCollectionLoaded', 'Statistics.onPrepareOptionsMenu', 'FRAMEWORK',
  'supportInvalidateOptionsMenu at the end of onCollectionLoaded prepares the panel',
  env=None,
  note='Framework edge. The AppCompat path is INFERRED (support library not read); the Activity.onPreparePanel path is read.',
  evidence='SRC com/ichi2/anki/Statistics.java:132, 180-201; FW-SRC core/java/android/app/Activity.java:3404-3406')

# --- Edges added for batch 037 (16) ---

e('Statistics.onCollectionLoaded', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the spinner draws the deck selector rows from the adapter set in onCollectionLoaded',
  env=None,
  note='Cross-batch edge: DeckDropDownAdapter.getView belongs to another batch. Written here as the caller part (precedent graph_def_before_part013.py). The spinner draw path is framework (AbsSpinner not in fw_src): INFERRED.',
  evidence='SRC com/ichi2/anki/Statistics.java:100; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:61-92, 90')

e('S_STATISTICS', 'Statistics$SectionsPagerAdapter.getItem', 'FRAMEWORK',
  'the pager asks for the fragment of a tab',
  env=None,
  note='The pager is a support-library FragmentPagerAdapter, so the call is framework-invoked (INFERRED, source not read). Body calls newInstance (306) and checkAndUpdate (307).',
  evidence='SRC com/ichi2/anki/Statistics.java:304-309')

e('S_STATISTICS', 'Statistics$SectionsPagerAdapter.getCount', 'FRAMEWORK',
  'the pager asks for the number of tabs',
  env=None,
  note='Support-library call (INFERRED, source not read). Returns 9 (Statistics.java:313).',
  evidence='SRC com/ichi2/anki/Statistics.java:311-314')

e('Statistics.onCollectionLoaded', 'Statistics$SectionsPagerAdapter.getItemPosition', 'FRAMEWORK',
  'the pager refreshes its tabs after mSectionsPagerAdapter.notifyDataSetChanged() at line 133',
  env=None,
  note='Refresh path: notifyDataSetChanged, then FragmentPagerAdapter calls getItemPosition (INFERRED, support library). getItemPosition runs checkAndUpdate (automatic CHA, line 298).',
  evidence='SRC com/ichi2/anki/Statistics.java:133, 293-302')

e('Statistics.selectDropDownItem', 'Statistics$SectionsPagerAdapter.getItemPosition', 'FRAMEWORK',
  'the pager refreshes its tabs after notifyDataSetChanged at line 256',
  env=None,
  note='Same refresh path as the onCollectionLoaded edge (INFERRED, support library).',
  evidence='SRC com/ichi2/anki/Statistics.java:256, 293-302')

e('Statistics.onOptionsItemSelected', 'Statistics$SectionsPagerAdapter.getItemPosition', 'FRAMEWORK',
  'the pager refreshes its tabs after a time range is changed at lines 215, 223 or 231',
  env=None,
  note='Same refresh path (INFERRED, support library).',
  evidence='SRC com/ichi2/anki/Statistics.java:215, 223, 231, 293-302')

e('S_STATISTICS', 'Statistics$SectionsPagerAdapter.getPageTitle', 'FRAMEWORK',
  'the tab strip draws the tab titles',
  env=None,
  note='Tab titles are set by SlidingTabLayout.populateTabStrip (SlidingTabLayout.java:222), reached from onCollectionLoaded line 126 via SlidingTabLayout.setViewPager. The edge is drawn from the page node; the middle of the chain is in another batch. The framework-invoked call is INFERRED.',
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:222; SRC com/ichi2/anki/Statistics.java:126, 317')

e('Statistics$ChartFragment.<init>', 'Statistics$ChartFragment.onCreate', 'LIFECYCLE',
  'fragment lifecycle: onCreate follows the constructor',
  env=None,
  note='Fragment lifecycle (support library not read: INFERRED). The lifecycle edges at graph_def.py:209-210 cover only the Statistics activity, so this fragment edge is written here.',
  evidence='SRC com/ichi2/anki/Statistics.java:416-418, 556-559')

e('Statistics$ChartFragment.onCreate', 'Statistics$ChartFragment.onCreateView', 'LIFECYCLE',
  'fragment lifecycle: onCreateView follows onCreate',
  env=None,
  note='Fragment lifecycle (INFERRED, support library not read).',
  evidence='SRC com/ichi2/anki/Statistics.java:556-559, 420-421')

e('Statistics$ChartFragment.onCreateView', 'Statistics$StatisticFragment.onResume', 'LIFECYCLE',
  'fragment lifecycle: onResume follows onCreateView; the inherited onResume calls checkAndUpdate',
  env=None,
  note='Fragment lifecycle (INFERRED). Dispatches to ChartFragment.checkAndUpdate (automatic CHA, line 393).',
  evidence='SRC com/ichi2/anki/Statistics.java:420-481, 390-395')

e('Statistics$OverviewStatisticsFragment.<init>', 'Statistics$OverviewStatisticsFragment.onCreateView', 'LIFECYCLE',
  'fragment lifecycle: onCreateView follows the constructor',
  env=None,
  note='Fragment lifecycle (INFERRED). No onCreate override in this fragment.',
  evidence='SRC com/ichi2/anki/Statistics.java:587-589, 592-594')

e('Statistics$OverviewStatisticsFragment.onCreateView', 'Statistics$StatisticFragment.onResume', 'LIFECYCLE',
  'fragment lifecycle: onResume follows onCreateView; the inherited onResume calls checkAndUpdate',
  env=None,
  note='Fragment lifecycle (INFERRED). Dispatches to OverviewStatisticsFragment.checkAndUpdate (automatic CHA, line 393).',
  evidence='SRC com/ichi2/anki/Statistics.java:592-646, 390-395')

e('Statistics.onBackPressed', 'Statistics$ChartFragment.onDestroy', 'FRAMEWORK',
  'the activity finishes from the Back key and its fragments are torn down',
  env=None,
  note='onDestroy is on LC_NO_TRIGGER (graph_def.py:37), so this hand-written edge is its route in. Fragment teardown is INFERRED (FragmentManager not in fw_src).',
  evidence='SRC com/ichi2/anki/Statistics.java:698-711, 570-576; SRC graphs/AnkiDroid/graph_def.py:37')

e('Statistics.onBackPressed', 'Statistics$OverviewStatisticsFragment.onDestroy', 'FRAMEWORK',
  'the activity finishes from the Back key and its fragments are torn down',
  env=None,
  note='Same as the ChartFragment edge: onDestroy is on LC_NO_TRIGGER (graph_def.py:37); teardown INFERRED.',
  evidence='SRC com/ichi2/anki/Statistics.java:698-711, 688-694; SRC graphs/AnkiDroid/graph_def.py:37')

e('Statistics.onCollectionLoaded', 'Statistics$1.onItemSelected', 'FRAMEWORK',
  'the spinner fires onItemSelected for the initial selection when its layout ends',
  env=None,
  note='Spinner layout ends with checkSelectionChanged (Spinner.java:681), which reaches AdapterView.fireOnSelected (AdapterView.java:937-947).',
  evidence='SRC com/ichi2/anki/Statistics.java:100-104; FW-SRC core/java/android/widget/Spinner.java:676-684; FW-SRC core/java/android/widget/AdapterView.java:937-947')

e('S_STATISTICS', 'Statistics$1.onItemSelected', 'GUI',
  'the user picks a deck in the toolbar spinner',
  gui=['the user picks a deck in the toolbar spinner'],
  env=None,
  note='Spinner selection route. onItemSelected calls selectDropDownItem (Statistics.java:104).',
  evidence='SRC com/ichi2/anki/Statistics.java:101-105; FW-SRC core/java/android/widget/AdapterView.java:937-947')

# --- UNREACHABLE entries (3) ---

UNREACHABLE['Statistics$1.onNothingSelected'] = ('framework_never_calls', "AdapterView fires onNothingSelected only when the selected position is negative (AdapterView.java:937-947, read). The deck spinner adapter DeckDropDownAdapter.getCount returns decks.size() + 1 (DeckDropDownAdapter.java:40-41), so it always has at least one row (the all-decks row) and the selection is never negative. The default selection when the adapter is set is in AbsSpinner, which is not in fw_src: INFERRED for that step.", 'SRC com/ichi2/anki/Statistics.java:107-110; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:40-41; FW-SRC core/java/android/widget/AdapterView.java:937-947', 'INFERRED')

UNREACHABLE['Statistics$ChartFragment.invalidateView'] = ('no_trigger_in_app', "No call site in the source root: the only occurrences are the abstract declaration in StatisticFragment (397), this override (563) and the OverviewStatisticsFragment override (661). No auto_calls.json row calls it, and no framework route to it is known (the Fragment base class is in the support library, not in fw_src: INFERRED).", 'SRC com/ichi2/anki/Statistics.java:397, 563-567, 661', 'SOURCE')

UNREACHABLE['Statistics$OverviewStatisticsFragment.invalidateView'] = ('no_trigger_in_app', "Same finding as ChartFragment.invalidateView: no call site in the source root (grep matches only 397, 563, 661), no auto_calls.json row, and no known framework route (Fragment base class not in fw_src: INFERRED).", 'SRC com/ichi2/anki/Statistics.java:397, 660-665', 'SOURCE')

# ---- part 040 (2026-10-28)
# AnkiDroid batch 040 (LABEL helper). ConfirmationDialog (8 methods) and CustomStudyDialog (27 methods).
# The full row list is in graphs/AnkiDroid/parts/label_040.md.
# Gates: MG342 (an empty card exists, empty-cards confirmation), MG343 (custom study session launch).
# Predefined constant: STATE_DECK (non-dynamic deck, custom study menu).
# Automatic CALL pairs NOT written here, to be suppressed (named in the final report):
#   DeckTask.onCancelled -> CustomStudyDialog$4.onCancelled (DeckTask.java:369)
#   DeckTask$TaskListener.onProgressUpdate -> CustomStudyDialog$4.onProgressUpdate
# Lifecycle edges for onCreateDialog of both dialogs already come from lc_chain in graph_def; none written here.

# --- ConfirmationDialog: empty-cards confirmation (DeckPicker.handleEmptyCards).
e('S_DLG_CONFIRMATION', 'ConfirmationDialog$1.onNegative', 'GUI',
  'tap Cancel in the empty-cards confirmation dialog',
  gui=['tap Cancel in the empty-cards confirmation dialog'],
  evidence='SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49; SRC com/ichi2/anki/DeckPicker.java:2180-2195',
  note='MISSING GATE MG342: an empty card exists (the find-empty-cards task returns at least one card, DeckPicker.java:2182-2195). The MaterialDialog callback dispatch is not in the dataset: INFERRED. env and needs_state unset.')

e('S_DLG_CONFIRMATION', 'ConfirmationDialog$1.onPositive', 'GUI',
  'tap OK in the empty-cards confirmation dialog',
  gui=['tap OK in the empty-cards confirmation dialog'],
  evidence='SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44; SRC com/ichi2/anki/DeckPicker.java:2180-2195',
  note='MISSING GATE MG342: same gate as the cancel edge (an empty card exists). The callback calls confirm() (ConfirmationDialog.java:43), overridden at DeckPicker.java:2186-2193. The MaterialDialog callback dispatch is INFERRED. env and needs_state unset.')

# --- CustomStudyDialog: custom study menu (deck long-press route) and number dialogs.
e('S_DLG_CUSTOM_STUDY', 'CustomStudyDialog$1.onSelection', 'GUI',
  'tap one row of the custom study context menu',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap one row of the custom study context menu'],
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:119-122, 124-189; SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:105-107, 132-137',
  note='The menu opens from the deck long-press only for a non-dynamic deck (DeckPickerContextMenu.java:105-107). The ListCallback dispatch is not in the dataset: INFERRED.')

e('S_DLG_TAGS', 'CustomStudyDialog$1$1.onPositive', 'GUI',
  'tap OK in the tag selection dialog opened from the custom study menu',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap OK in the tag selection dialog opened from the custom study menu'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:162-167; SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:139-151, 175-179',
  note='The TagsDialog positive callback calls mTagsDialogListener.onPositive (TagsDialog.java:165-166). The tags item is the CUSTOM_STUDY_TAGS case (CustomStudyDialog.java:139). The dialog opens only through the custom study menu. The button dispatch is INFERRED.')

e('S_DLG_CUSTOM_STUDY', 'CustomStudyDialog$2.onPositive', 'GUI',
  'tap OK in the custom study number dialog (a number is typed)',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap OK in the custom study number dialog (a number is typed)'],
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:226-231, 233-282, 291-301',
  note='The OK button is enabled only when the number field is not empty (CustomStudyDialog.java:291-301). The dialog opens from the custom study menu default branch (CustomStudyDialog.java:182-187). The button dispatch is INFERRED.')

e('S_DLG_CUSTOM_STUDY', 'CustomStudyDialog$2.onNegative', 'GUI',
  'tap Cancel in the custom study number dialog',
  env=None,
  needs_state=STATE_DECK,
  gui=['tap Cancel in the custom study number dialog'],
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:286-288',
  note='The negative callback dismisses all dialog fragments (CustomStudyDialog.java:287). The button dispatch is INFERRED.')

e('S_DLG_CUSTOM_STUDY', 'CustomStudyDialog$3.onKey', 'FRAMEWORK',
  'type or delete text in the custom study number field (the key event reaches the attached listener)',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:291-301; FW-SRC core/java/android/view/View.java:11705-11709',
  note='The OnKeyListener is set on the number field (CustomStudyDialog.java:291). View.dispatchKeyEvent calls the attached listener first (View.java:11707-11709). The key events reach the view through the window: INFERRED (not read).')

e('CustomStudyDialog.createCustomStudySession', 'CustomStudyDialog$4.onPreExecute', 'FRAMEWORK',
  'the rebuild task starts (DeckTask.launchDeckTask executes it); AsyncTask calls onPreExecute on the UI thread',
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:454, 460-462; SRC com/ichi2/async/DeckTask.java:129-134; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='MISSING GATE MG343: the launch is reached only when the custom study deck name is free or names a dynamic deck (CustomStudyDialog.java:423-431). env and needs_state unset. The DeckTask delegation to the listener onPreExecute is automatic (DeckTask.java:344-347).')

e('CustomStudyDialog.createCustomStudySession', 'CustomStudyDialog$4.onPostExecute', 'ASYNC',
  'the rebuild task finishes in the background and the result is posted to the UI thread',
  evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:454, 465-468; SRC com/ichi2/async/DeckTask.java:359-365; FW-SRC core/java/android/os/AsyncTask.java:691-698',
  note='MISSING GATE MG343: same launch gate as the onPreExecute edge. finish calls onPostExecute when the task is not cancelled (AsyncTask.java:695). The DeckTask delegation at DeckTask.java:359-365 is automatic. env and needs_state unset.')

# --- UNREACHABLE: the REBUILD_CRAM listener methods onCancelled and onProgressUpdate.
UNREACHABLE['CustomStudyDialog$4.onCancelled'] = (
    'no_trigger_in_app',
    "no_trigger_in_app: the REBUILD_CRAM task is never cancelled, so DeckTask.onCancelled (DeckTask.java:367-370) never runs for it. "
    "In-app cancels go through DeckTask.cancelTask(int) (DeckTask.java:181-186), which cancels only when the latest task type equals the argument. "
    "Its callers pass TASK_TYPE_SEARCH_CARDS or TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155), and none passes REBUILD_CRAM. "
    "The no-argument cancelTask (DeckTask.java:168-178) is called only from cancelTask(int) (line 184). "
    "The other cancel(true) calls act on non-DeckTask tasks (TaskOperations.java:33, Connection.java:541, Statistics.java:543, 574, 681, 692). "
    "A grep for 'extends DeckTask' finds no subclass. "
    "The automatic CALL DeckTask.onCancelled -> CustomStudyDialog$4.onCancelled (DeckTask.java:369) must be suppressed.",
    "SRC com/ichi2/async/DeckTask.java:168-186, 367-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; "
    "SRC com/ichi2/anki/runtimetools/TaskOperations.java:33; SRC com/ichi2/async/Connection.java:541; "
    "SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692",
    'SOURCE')

UNREACHABLE['CustomStudyDialog$4.onProgressUpdate'] = (
    'no_trigger_in_app',
    "no_trigger_in_app: the REBUILD_CRAM body never publishes progress. doInBackgroundRebuildCram (DeckTask.java:728-733) calls the scheduler rebuild "
    "and doInBackgroundUpdateValuesFromDeck only, and no publishProgress call lies in that range. "
    "The only new ProgressCallback in the source root is at DeckTask.java:750 (the import body). "
    "So the DeckTask.onProgressUpdate delegation (DeckTask.java:351-355) never runs for this listener. "
    "The automatic CALL DeckTask$TaskListener.onProgressUpdate -> CustomStudyDialog$4.onProgressUpdate must be suppressed.",
    "SRC com/ichi2/async/DeckTask.java:351-355, 728-733, 750; "
    "SRC com/ichi2/async/DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659, 809, 859",
    'SOURCE')

# ---- sup for part 040 (2026-10-28): automatic edges into batch 040 UNREACHABLE methods; the sources are never triggered (see label_040.md)
sup(('DeckTask.onCancelled', 'CustomStudyDialog$4.onCancelled'))
sup(('DeckTask$TaskListener.onProgressUpdate', 'CustomStudyDialog$4.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@CustomStudyDialog$4', 'CustomStudyDialog$4.onProgressUpdate'))

# ---- part 042 (2026-10-28)
# AnkiDroid batch 042 (LABEL helper). Five DeckPicker dialog classes, 36 methods: DeckPickerBackupNoSpaceLeftDialog,
# DeckPickerConfirmDeleteDeckDialog, DeckPickerContextMenu, DeckPickerExportCompleteDialog, DeckPickerNoSpaceLeftDialog.
# The full row list is in graphs/AnkiDroid/parts/label_042.md. All 36 methods are REACHABLE; there are no UNREACHABLE entries.
#
# Route ownership:
# - CALL edges from the dialog methods into their callees and the newInstance/constructor calls come from auto_calls.json.
#   They are not written here. The automatic edge DeckPickerContextMenu$1.onSelection -> DeckPicker.renameDeckDialog()
#   (DeckPickerContextMenu.java:142) is present in auto_calls.json, so it is not repeated.
# - Button and cancel listeners are dispatched by the MaterialDialog library (not in fw_src), so every GUI edge below is INFERRED.
# - The page edges below belong here because their destination is a method of this batch.
# - Existing label_002 page edges (S_DLG_DECKPICKER_CONTEXT -> DeckPicker.confirmDeckDeletion() and emptyFiltered,
#   S_DLG_DECKPICKER_DELETE_DECK -> DeckPicker.deleteContextMenuDeck, S_DLG_DECKPICKER_EXPORT_DONE -> DeckPicker.emailFile)
#   skip these listeners. They are not changed here.
#
# Gates: MG362 (NO_SPACE page, free space below the threshold). MG363 (DeckPickerExportCompleteDialog.getDialogHandlerMessage,
# the activity is stopped; no edge written, see the .md row). STATE_SETTINGS (BACKUP_NO_SPACE page, noSpaceLeft preference).

# --- DeckPickerContextMenu (long-press menu of a deck row). Page: S_DLG_DECKPICKER_CONTEXT.
e('S_DLG_DECKPICKER_CONTEXT', 'DeckPickerContextMenu$1.onSelection', 'GUI',
  'tap a row of the deck long-press context menu',
  env=None,
  gui=['tap a row of the deck long-press context menu'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:60-74, 117-119',
  note='The list callback mContextMenuListener is set on the builder at line 72. Each case calls an automatic CALL edge. The GUI dispatch is the MaterialDialog library (not in fw_src): INFERRED. The CHA edge DeckPickerContextMenu$1.onSelection -> StudyOptionsActivity.onRequireDeckListUpdate (line 154) cannot run here: DeckPicker is the activity and implements StudyOptionsListener (DeckPicker.java:110-111). It is already listed in the sup() of graph_def.py (line 1236).')

# --- DeckPickerConfirmDeleteDeckDialog. Page: S_DLG_DECKPICKER_DELETE_DECK.
e('S_DLG_DECKPICKER_DELETE_DECK', 'DeckPickerConfirmDeleteDeckDialog$1.onPositive', 'GUI',
  'press the positive (delete) button of the confirm-delete dialog',
  env=None,
  gui=['press the positive (delete) button of the confirm-delete dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerConfirmDeleteDeckDialog.java:34-39',
  note='The button callback is set at line 34. Body: deleteContextMenuDeck (automatic CALL, line 37), then dismissAllDialogFragments (line 38). The existing label_002 GUI edge from the same page to DeckPicker.deleteContextMenuDeck skips this listener. Library dispatch INFERRED.')

e('S_DLG_DECKPICKER_DELETE_DECK', 'DeckPickerConfirmDeleteDeckDialog$1.onNegative', 'GUI',
  'press the negative (cancel) button of the confirm-delete dialog',
  env=None,
  gui=['press the negative (cancel) button of the confirm-delete dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerConfirmDeleteDeckDialog.java:41-44',
  note='Body: dismissAllDialogFragments (automatic CALL, line 43). Library dispatch INFERRED.')

# --- DeckPickerBackupNoSpaceLeftDialog. Page: S_DLG_DECKPICKER_BACKUP_NO_SPACE (shown only when the noSpaceLeft preference is set).
e('S_DLG_DECKPICKER_BACKUP_NO_SPACE', 'DeckPickerBackupNoSpaceLeftDialog$2.onPositive', 'GUI',
  'press OK on the backup-no-space dialog',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['press OK on the backup-no-space dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerBackupNoSpaceLeftDialog.java:30-34; SRC com/ichi2/anki/DeckPicker.java:851-854',
  note='The page is shown only when the noSpaceLeft preference is true (DeckPicker.java:851; the preference is set by BackupManager.performBackup at BackupManager.java:156). The preference is STATE_SETTINGS. Body: finishWithoutAnimation (automatic CALL, line 33). Library dispatch INFERRED.')

e('S_DLG_DECKPICKER_BACKUP_NO_SPACE', 'DeckPickerBackupNoSpaceLeftDialog$1.onCancel', 'GUI',
  'cancel the backup-no-space dialog (back key or outside tap)',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['cancel the backup-no-space dialog (back key or outside tap)'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerBackupNoSpaceLeftDialog.java:36-41',
  note='cancelable(true) at line 36. The page gate is STATE_SETTINGS, as on the OK edge. Body: finishWithoutAnimation (automatic CALL, line 40). Library cancel dispatch INFERRED.')

# --- DeckPickerExportCompleteDialog. Page: S_DLG_DECKPICKER_EXPORT_DONE.
e('S_DLG_DECKPICKER_EXPORT_DONE', 'DeckPickerExportCompleteDialog$1.onPositive', 'GUI',
  'press OK on the export-complete dialog (email the exported file)',
  env=None,
  gui=['press OK on the export-complete dialog (email the exported file)'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerExportCompleteDialog.java:32-37',
  note='Body: dismissAllDialogFragments (line 35), then DeckPicker.emailFile (automatic CALL, line 36). The existing label_002 GUI edge from the same page to DeckPicker.emailFile skips this listener. Library dispatch INFERRED.')

e('S_DLG_DECKPICKER_EXPORT_DONE', 'DeckPickerExportCompleteDialog$1.onNegative', 'GUI',
  'press Cancel on the export-complete dialog',
  env=None,
  gui=['press Cancel on the export-complete dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerExportCompleteDialog.java:39-42',
  note='Body: dismissAllDialogFragments (automatic CALL, line 41). Library dispatch INFERRED.')

# --- DeckPickerNoSpaceLeftDialog. Page: S_DLG_DECKPICKER_NO_SPACE (MISSING GATE MG362: shown only when free space is low).
e('S_DLG_DECKPICKER_NO_SPACE', 'DeckPickerNoSpaceLeftDialog$2.onPositive', 'GUI',
  'press OK on the no-space-left dialog',
  env=None,
  gui=['press OK on the no-space-left dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerNoSpaceLeftDialog.java:28-32; SRC com/ichi2/anki/DeckPicker.java:848-850',
  note='MISSING GATE MG362: the page is shown only when BackupManager.enoughDiscSpace is false (free space below MIN_FREE_SPACE, BackupManager.java:207-209). No predefined ENV or STATE kind covers low free space, so env and needs_state are unset. Body: startLoadingCollection (automatic CALL, line 31). Library dispatch INFERRED.')

e('S_DLG_DECKPICKER_NO_SPACE', 'DeckPickerNoSpaceLeftDialog$1.onCancel', 'GUI',
  'cancel the no-space-left dialog (back key or outside tap)',
  env=None,
  gui=['cancel the no-space-left dialog (back key or outside tap)'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerNoSpaceLeftDialog.java:26, 34-39',
  note='MISSING GATE MG362, as on the OK edge (the page is shown only when free space is low); env and needs_state are unset. cancelable(true) at line 26. Body: startLoadingCollection (automatic CALL, line 37). Library cancel dispatch INFERRED.')

# ---- part 041 (2026-10-28)
# AnkiDroid batch 041 (LABEL helper). DatabaseErrorDialog: 35 methods. The full row list is in
# graphs/AnkiDroid/parts/label_041.md.
# Methods: <clinit>, <init>, dismissAllDialogFragments, getDialogHandlerMessage, getMessage, getNotificationMessage,
# getNotificationTitle, getTitle, newInstance, onCreateDialog, and the anonymous callbacks $1 to $11.
#
# Route ownership:
# - CALL edges (for example onCreateDialog -> $N.<init>, and the callback bodies calling DeckPicker methods) come from
#   auto_calls.json. They are not written here.
# - The callbacks of the page S_DLG_DATABASE_ERROR are written here: an edge belongs to the part that contains its
#   destination method.
# - $2 (DB_ERROR, id 1) is never created. No caller passes DIALOG_DB_ERROR (grep over the source root).
#
# Gates: MG352 (load failure), MG353 (sqlite3 present), MG355 (a backup exists). MG354 is on method rows only.
# Predefined constants are not used: no ENV or STATE kind fits these gates.
# Page node: S_DLG_DATABASE_ERROR.

# --- Load-failed dialog (id 0, LOAD_FAILED case, DatabaseErrorDialog.java:73-94).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$1.onPositive', 'GUI',
  'tap error handling options on the load-failed dialog',
  gui=['tap error handling options on the load-failed dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:80-87; SRC com/ichi2/anki/DeckPicker.java:433, 1243-1245, 1478-1479',
  note='MISSING GATE MG352: the load-failed dialog opens only after a collection open failure or a database or I/O failure (DeckPicker.java:433, 1243-1245, 1478-1479). No predefined ENV or STATE kind covers it; env and needs_state unset.')

e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$1.onNegative', 'GUI',
  'tap close on the load-failed dialog (DeckPicker.exit)',
  gui=['tap close on the load-failed dialog (DeckPicker.exit)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:89-92',
  note='MISSING GATE MG352: the load-failed dialog opens only after a collection open failure or a database or I/O failure. No predefined ENV or STATE kind covers it; env and needs_state unset.')

# --- Error handling list (id 2, ERROR_HANDLING case, DatabaseErrorDialog.java:129-199).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$3.onSelection', 'GUI',
  'pick one repair option in the error handling list',
  gui=['pick one repair option in the error handling list'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:134-156, 168-196',
  note='The list itself has no gate: the list is offered from the no-backup restore dialog (standard route) and from the load-failed dialog (MG352). Option 1 (check database) is offered only when the collection is open (line 134). Option 2 (repair) is offered only with sqlite3 (line 144, MISSING GATE MG353).')

# --- Repair (id 3, REPAIR case, DatabaseErrorDialog.java:201-214).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$4.onPositive', 'GUI',
  'tap repair on the repair dialog (repairDeck)',
  gui=['tap repair on the repair dialog (repairDeck)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:65-70, 144-147, 207-212',
  note='MISSING GATE MG353: the repair option is offered only when the sqlite3 command runs with exit code 0 (Runtime exec sqlite3 --version, DatabaseErrorDialog.java:65-70). No predefined ENV or STATE kind covers it; env and needs_state unset.')

# --- Restore, no backup (id 5, RESTORE_BACKUP case, DatabaseErrorDialog.java:216-234).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$5.onPositive', 'GUI',
  'tap OK on the no-backup restore dialog (back to the error handling list)',
  gui=['tap OK on the no-backup restore dialog (back to the error handling list)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:224-234; SRC com/ichi2/anki/BackupManager.java:311-326',
  note='No gate on the standard route: the menu item action_restore_backup has no enabled attribute (res/menu/deck_picker.xml:35-38 (src/main)). Caveat: a fresh install is assumed to have no backup file. env and needs_state unset.')

# --- Restore with backups (ids 7 and 6, DatabaseErrorDialog.java:235-273).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$6.onSelection', 'GUI',
  'pick a backup date in the restore list (restoreFromBackup)',
  gui=['pick a backup date in the restore list (restoreFromBackup)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:251-270; SRC com/ichi2/anki/BackupManager.java:311-326',
  note='MISSING GATE MG355: the restore list is built only when at least one backup .apkg exists (BackupManager.getBackups non-empty, BackupManager.java:311-326). No predefined ENV or STATE kind covers it; env and needs_state unset.')

e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$7.onNegative', 'GUI',
  'tap cancel on the restore list (dismiss only)',
  gui=['tap cancel on the restore list (dismiss only)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:243-248',
  note='MISSING GATE MG355: the restore list is built only when at least one backup .apkg exists (BackupManager.getBackups non-empty, BackupManager.java:311-326). No predefined ENV or STATE kind covers it; env and needs_state unset.')

# --- New collection (id 5, NEW_COLLECTION case, DatabaseErrorDialog.java:275-292).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$8.onPositive', 'GUI',
  'tap create on the new-collection dialog (the old database moves to the broken folder)',
  gui=['tap create on the new-collection dialog (the old database moves to the broken folder)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:280-290',
  note='No gate on the standard route: the error handling list always offers option 5 (DatabaseErrorDialog.java:155-156, 192-194). env and needs_state unset.')

# --- Database check (id 6, CONFIRM_DATABASE_CHECK case, DatabaseErrorDialog.java:294-306).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$9.onPositive', 'GUI',
  'tap OK on the database-check confirmation (integrityCheck)',
  gui=['tap OK on the database-check confirmation (integrityCheck)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:139-141, 299-304; SRC com/ichi2/anki/DeckPicker.java:528, 595-598',
  note='No gate on the error handling list route (option 1 is offered when the collection is open, line 134). The menu route (action_check_database) needs ENV_STORAGE (DeckPicker.java:528; res/menu/deck_picker.xml:20-24 (src/main)). env and needs_state unset.')

# --- Restore confirmation (id 7, CONFIRM_RESTORE_BACKUP case, DatabaseErrorDialog.java:308-320).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$10.onPositive', 'GUI',
  'tap continue on the restore confirmation (the restore dialog for id 4 follows)',
  gui=['tap continue on the restore confirmation (the restore dialog for id 4 follows)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:313-318; SRC com/ichi2/anki/DeckPicker.java:616-619',
  note='No gate: the menu item action_restore_backup has no enabled attribute and is hidden only on ChromeOS (DeckPicker.java:535). env and needs_state unset.')

# --- Full sync from server (id 8, FULL_SYNC_FROM_SERVER case, DatabaseErrorDialog.java:322-334).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$11.onPositive', 'GUI',
  'tap overwrite on the full-sync confirmation (sync download)',
  gui=['tap overwrite on the full-sync confirmation (sync download)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:155-156, 188-191, 327-332',
  note='No gate on the dialog: the error handling list always offers option 4 (DatabaseErrorDialog.java:151-153). The sync it starts needs ENV_NETWORK and belongs to the sync batch; env and needs_state unset.')

# --- DB_ERROR (id 1): never created. Grep over the source root: no caller passes DIALOG_DB_ERROR, and the replayed
# dialogType (DialogHandler.java:87) is the stored id of a fragment, which is never 1.
UNREACHABLE['DatabaseErrorDialog$2.<init>'] = ('branch_never_taken',
    "The DB_ERROR case (id 1, DatabaseErrorDialog.java:96-127) is never entered. DIALOG_DB_ERROR (1) has no caller in the source root. The ids passed to showDatabaseErrorDialog and newInstance are 0, 2, 3, 4, 5, 6, 7, 8 and 9 (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The replayed id (DialogHandler.java:87) is the stored dialogType of a fragment, so it is never 1 either.",
    'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:28, 47-53, 96-106; SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1243-1245; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 87',
    'SOURCE')

UNREACHABLE['DatabaseErrorDialog$2.onNegative'] = ('branch_never_taken',
    "The DB_ERROR case (id 1, DatabaseErrorDialog.java:96-127) is never entered. DIALOG_DB_ERROR (1) has no caller in the source root. The ids passed to showDatabaseErrorDialog and newInstance are 0, 2, 3, 4, 5, 6, 7, 8 and 9 (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The replayed id (DialogHandler.java:87) is the stored dialogType of a fragment, so it is never 1 either. The callback is created only with the DB_ERROR dialog, so it never runs.",
    'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:96-106, 113-117; SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1243-1245; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 87',
    'SOURCE')

UNREACHABLE['DatabaseErrorDialog$2.onNeutral'] = ('branch_never_taken',
    "The DB_ERROR case (id 1, DatabaseErrorDialog.java:96-127) is never entered. DIALOG_DB_ERROR (1) has no caller in the source root. The ids passed to showDatabaseErrorDialog and newInstance are 0, 2, 3, 4, 5, 6, 7, 8 and 9 (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The replayed id (DialogHandler.java:87) is the stored dialogType of a fragment, so it is never 1 either. The callback is created only with the DB_ERROR dialog, so it never runs.",
    'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:96-106, 119-122; SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1243-1245; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 87',
    'SOURCE')

UNREACHABLE['DatabaseErrorDialog$2.onPositive'] = ('branch_never_taken',
    "The DB_ERROR case (id 1, DatabaseErrorDialog.java:96-127) is never entered. DIALOG_DB_ERROR (1) has no caller in the source root. The ids passed to showDatabaseErrorDialog and newInstance are 0, 2, 3, 4, 5, 6, 7, 8 and 9 (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The replayed id (DialogHandler.java:87) is the stored dialogType of a fragment, so it is never 1 either. The callback is created only with the DB_ERROR dialog, so it never runs.",
    'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:96-111; SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1243-1245; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 87',
    'SOURCE')

# ---- sup for part 041 (2026-10-28): automatic edge into a batch 041 UNREACHABLE constructor; DIALOG_DB_ERROR (1) has no caller (see label_041.md)
sup(('DatabaseErrorDialog.onCreateDialog', 'DatabaseErrorDialog$2.<init>'))

# ---- part 025 (2026-10-28)
# AnkiDroid batch 025 (LABEL helper). CardTemplateEditor part 1: 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_025.md.
#
# Route ownership:
# - Automatic CALL edges (graphs/AnkiDroid/auto_calls.json) are not written here. They cover the direct calls inside
#   CardTemplateEditor, $1, $3 and the fragment, the AnkiActivity virtual dispatches into showProgressBar,
#   hideProgressBar and onCollectionLoaded, and the DeckTask listener defaults into $1.
# - Edges into batch 026 methods (updateCss, the fragment $2 save listener, the fragment $3, $4 and $5 confirm methods,
#   TemplatePagerAdapter) are not written here.
# - Page edges (S_CARDTEMPLATEEDITOR, S_PREVIEWER) are written here only when the destination is in this batch.
# - Launch edges into $1 (ASYNC) are written from addNewTemplate and deleteTemplate, as label_031 does for ModelBrowser.
#
# Gates: MG192 (model changed), MG193 (two or more templates), MG194 (framework saves state), MG195 (one template at add),
# MG196 (no note card for the position), MG198 (schema not yet modified). MG197 and MG199 to MG201 are not used.
# No STATE or ENV constant fits these gates, so env and needs_state are unset.

# --- Activity: collection load, save state, Up arrow, pager listener, discard dialog.

e('CardTemplateEditor.onCreate', 'CardTemplateEditor.onCollectionLoaded', 'ASYNC',
  'the collection loader delivers onLoadFinished after startLoadingCollection',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:157, 205-206; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290',
  note='Precedent label_009 (CardBrowser.onCreate -> onCollectionLoaded). The restart is in AnkiActivity.startLoadingCollection (AnkiActivity.java:261); the result reaches onCollectionLoaded through AnkiActivity.onLoadFinished (AnkiActivity.java:286, automatic CALL). The library delivery step is not in the tree.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor.onSaveInstanceState', 'FRAMEWORK',
  'the framework saves the editor state when the activity is stopped and not finishing',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:161-168; FW-SRC core/java/android/app/ActivityThread.java:4020-4027',
  note='Page edge, destination in this part. MISSING GATE MG194: the not-finishing and saveState conditions are framework state with no STATE kind, so env and needs_state are unset. Precedent: DeckPicker.onPause -> onSaveInstanceState (label_003).')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor.onOptionsItemSelected', 'GUI',
  'tap the Up (home) arrow in the toolbar of the template editor',
  env=None,
  gui=['tap the Up (home) arrow in the toolbar of the template editor'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:171-184; FW-SRC core/java/android/app/Activity.java:3439-3450',
  note='Page edge, destination in this part. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). The discard dialog branch needs MISSING GATE MG192 (the model was edited); otherwise the editor finishes.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$2.onPageScrolled', 'FRAMEWORK',
  'the support-library ViewPager dispatches a scroll step to the page-change listener while the user swipes between templates',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:214, 216-217',
  note='Page edge, destination in this part. INFERRED: ViewPager dispatch, source not read. The body is empty. MISSING GATE MG193: a swipe needs two or more templates.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$2.onPageScrollStateChanged', 'FRAMEWORK',
  'the support-library ViewPager dispatches a scroll-state change to the page-change listener while the user swipes',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:214, 228-229',
  note='Page edge, destination in this part. INFERRED: ViewPager dispatch, source not read. The body is empty. MISSING GATE MG193: a swipe needs two or more templates.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$2.onPageSelected', 'FRAMEWORK',
  'the support-library ViewPager dispatches the selected page to the page-change listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:214, 220-225, 290',
  note='Page edge, destination in this part. INFERRED: ViewPager dispatch, source not read. Also reached from selectTemplate (setCurrentItem at CardTemplateEditor.java:290). The body calls instantiateItem and fragment.updateCss (automatic CALL, line 223).')

e('CardTemplateEditor$3.<init>', 'CardTemplateEditor$3.onPositive', 'FRAMEWORK',
  'the discard dialog calls onPositive when its positive button is tapped (MaterialDialog.ButtonCallback)',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:255-260, 262-268',
  note='Library dispatch (MaterialDialog, INFERRED, source not read). The dialog is shown after $3.<init> is constructed in showDiscardChangesDialog (automatic CALL, CardTemplateEditor.java:259). MISSING GATE MG192: the dialog needs an edited model. Precedent: DeckPicker$23.<init> -> onPositive (label_005).')

# --- Template task listener $1: launch edges from the add and delete methods of the fragment.

e('CardTemplateEditor$CardTemplateFragment.addNewTemplate', 'CardTemplateEditor$1.onPreExecute', 'ASYNC',
  'the ADD_TEMPLATE task starts and runs the pre-execute callback of the editor listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:718-719, 86-88; SRC com/ichi2/async/DeckTask.java:344-347, 1298-1300',
  note='Launch link, as in label_031 (ModelBrowser launch edges). DeckTask.onPreExecute calls mListener.onPreExecute(this) (DeckTask.java:346), which the TaskListener default (DeckTask.java:1298-1300) forwards to the no-argument onPreExecute that $1 overrides.')

e('CardTemplateEditor$CardTemplateFragment.addNewTemplate', 'CardTemplateEditor$1.onPostExecute', 'ASYNC',
  'the ADD_TEMPLATE task finishes and delivers its result to the editor listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:718-719, 95-113; SRC com/ichi2/async/DeckTask.java:360-365, 1304-1306',
  note='DeckTask.onPostExecute delegates to the listener (DeckTask.java:362); the success branch calls selectTemplate (automatic CALL, CardTemplateEditor.java:100).')

e('CardTemplateEditor$CardTemplateFragment.deleteTemplate', 'CardTemplateEditor$1.onPreExecute', 'ASYNC',
  'the REMOVE_TEMPLATE task starts and runs the pre-execute callback of the editor listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:664-665, 86-88; SRC com/ichi2/async/DeckTask.java:344-347, 1298-1300',
  note='Launch link, as in label_031 (ModelBrowser launch edges). DeckTask.onPreExecute calls mListener.onPreExecute(this) (DeckTask.java:346), which the TaskListener default (DeckTask.java:1298-1300) forwards to the no-argument onPreExecute that $1 overrides.')

e('CardTemplateEditor$CardTemplateFragment.deleteTemplate', 'CardTemplateEditor$1.onPostExecute', 'ASYNC',
  'the REMOVE_TEMPLATE task finishes and delivers its result to the editor listener',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:664-665, 95-113; SRC com/ichi2/async/DeckTask.java:360-365, 1304-1306',
  note='DeckTask.onPostExecute delegates to the listener (DeckTask.java:362); the success branch calls selectTemplate (automatic CALL, CardTemplateEditor.java:100). The "removeTemplateFailed" branch shows a toast (CardTemplateEditor.java:104-107).')

# --- Fragment: preview result, menu, add and delete routes.

e('S_PREVIEWER', 'CardTemplateEditor$CardTemplateFragment.onActivityResult', 'RESULT',
  'the preview returns to the template editor, which hands the result to the fragment',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:503-504, 557-560',
  note='Page edge, destination in this part. Launched by startActivityForResult(i, REQUEST_PREVIEWER) (CardTemplateEditor.java:504). The hand-off to the fragment is support-library FragmentActivity dispatch (INFERRED, source not read). Precedent: S_CARDTEMPLATEEDITOR -> NoteEditor.onActivityResult (label_012).')

e('CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected', 'Previewer.<init>', 'INTENT',
  'open the previewer for the template being edited (explicit Intent to Previewer, card id extra)',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:485, 488-491, 503-504',
  note='Explicit component (Previewer.class) started for a result. The card is the note card when noteId is set and the position exists; otherwise the dummy card path (MISSING GATE MG196). The source is in this part, so the edge is written here; label_036 has no edge into Previewer.<init>.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected', 'GUI',
  'tap an action in the template editor toolbar menu (add, delete, preview, done)',
  env=None,
  gui=['tap an action in the template editor toolbar menu (add, delete, preview, done)'],
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:442-446, 449-521',
  note='Page edge, destination in this part. The fragment inflates the menu (CardTemplateEditor.java:444). The dispatch from the activity menu to the fragment is support-library code (INFERRED, source not read).')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'the options menu is built and the fragment inflates its menu',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:420, 442-446',
  note='Page edge, destination in this part. INFERRED: support-library FragmentActivity dispatches onCreateOptionsMenu to fragments that called setHasOptionsMenu(true) (CardTemplateEditor.java:420). Source not read.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment.onCreateView', 'FRAMEWORK',
  'the pager creates each template page and the fragment inflates its view',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:213, 318-320, 380-425',
  note='Page edge, destination in this part. INFERRED: support-library ViewPager and FragmentPagerAdapter create the page after setAdapter (CardTemplateEditor.java:213) through TemplatePagerAdapter.getItem (batch 026 edge). Source not read.')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$CardTemplateFragment.onResume', 'FRAMEWORK',
  'the editor resumes and the attached fragment receives onResume',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:427-430',
  note='Page edge, destination in this part. INFERRED: support-library dispatch of onResume to attached fragments (source not read). The body calls super only.')

# --- UNREACHABLE entries (text inline; no module-level names).

UNREACHABLE['CardTemplateEditor$1.onCancelled'] = (
    'no_trigger_in_app',
    ("DeckTask.onCancelled calls the listener onCancelled (DeckTask.java:367-370) only after a DeckTask is cancelled. "
     "The ADD_TEMPLATE and REMOVE_TEMPLATE tasks (TASK_TYPE_ADD_TEMPLATE = 39, TASK_TYPE_REMOVE_TEMPLATE = 40, DeckTask.java:92-93) "
     "are never cancelled in the app. DeckTask.cancelTask(int) (DeckTask.java:181-186) cancels the latest task only when its type "
     "equals the argument, and its only callers pass TASK_TYPE_SEARCH_CARDS and TASK_TYPE_RENDER_BROWSER_QA "
     "(CardBrowser.java:528-529, 796-797, 1155). The no-argument DeckTask.cancelTask (DeckTask.java:168-178) has no caller except "
     "cancelTask(int) (DeckTask.java:184). The other cancel(true) calls act on other tasks: TaskOperations.stopTaskGracefully "
     "(TaskOperations.java:33; its callers pass pronunciation and translation tasks), Connection.java:541, Statistics.java:543, 574, "
     "681, 692. So no template task is cancelled and onCancelled never runs. Suppress candidate: the automatic CALL "
     "DeckTask.onCancelled -> CardTemplateEditor$1.onCancelled (DeckTask.java:369, cha) would reach this method."),
    ('SRC com/ichi2/async/DeckTask.java:92-93, 168-186, 367-370, 1028-1065; '
     'SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
     'SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-33; '
     'SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; '
     'SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405; '
     'SRC com/ichi2/async/Connection.java:541; '
     'SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; SRC com/ichi2/anki/CardTemplateEditor.java:84, 116-118'),
    'SOURCE')

UNREACHABLE['CardTemplateEditor$1.onProgressUpdate'] = (
    'no_trigger_in_app',
    ("DeckTask.onProgressUpdate (DeckTask.java:352-355) runs only when a DeckTask calls publishProgress. The ADD_TEMPLATE and "
     "REMOVE_TEMPLATE bodies (DeckTask.java:1028-1065) never call it. The publishProgress calls (DeckTask.java:380, 420, 422, "
     "457, 565, 601, 633, 659, 809, 859) are inside other task bodies. The only ProgressCallback is built for the import task "
     "(DeckTask.java:750) and its class is at DeckTask.java:1320-1325. So the template listener never receives progress. "
     "Suppress candidate: the automatic CALL DeckTask$TaskListener.onProgressUpdate -> CardTemplateEditor$1.onProgressUpdate "
     "(DeckTask.java:1312, cha), and its specialized copy DeckTask$TaskListener.onProgressUpdate@CardTemplateEditor$1, would reach this method."),
    ('SRC com/ichi2/async/DeckTask.java:352-355, 380, 420, 422, 457, 565, 601, 633, 659, 750, 809, 859, 1028-1065, 1312, 1320-1325; '
     'SRC com/ichi2/anki/CardTemplateEditor.java:91-92'),
    'SOURCE')

# ---- sup for part 025 (2026-10-28): automatic edges into batch 025 UNREACHABLE methods; the DeckTask sources are never cancelled or publish progress for the template editor (see label_025.md)
sup(('DeckTask.onCancelled', 'CardTemplateEditor$1.onCancelled'))
sup(('DeckTask$TaskListener.onProgressUpdate', 'CardTemplateEditor$1.onProgressUpdate'),
    ('DeckTask$TaskListener.onProgressUpdate@CardTemplateEditor$1', 'CardTemplateEditor$1.onProgressUpdate'))

# ---- part 043 (2026-10-28)
# AnkiDroid batch 043 (LABEL helper). ExportDialog and ImportDialog: 27 methods. The full row list is in
# graphs/AnkiDroid/parts/label_043.md. All 27 methods are REACHABLE, so this part has no UNREACHABLE entries.
#
# Route ownership:
# - Auto CALL edges (auto_calls.json) are not written here: the button callbacks, the DialogHandler and IntentHandler
#   routes, the newInstance factories and the anonymous-class constructors.
# - Written here: the page edges from S_DLG_EXPORT and S_DLG_IMPORT to the anonymous callbacks (the page is the source,
#   so the edge belongs to this part), and the two dismissAllDialogFragments forwards to AnkiActivity, which
#   auto_calls.json does not record.
# - Batch 002 has S_DLG_EXPORT -> DeckPicker.exportApkg and S_DLG_IMPORT -> DeckPicker.importAdd / importReplace
#   directly. Those routes coexist with the callback routes written here.
#
# Gates: MG372 (no importable .apkg file, as on a fresh install: the SELECT list is empty). Range MG372-MG381.
# Predefined constants used: STATE_APKG (an .apkg file is available to import).

# --- Export dialog page (S_DLG_EXPORT, created by DeckPicker.java:624 and 1916).
e('S_DLG_EXPORT', 'ExportDialog$1.onClick', 'GUI',
  'the Cancel button of the export dialog is tapped',
  env=None,
  gui=['the Cancel button of the export dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:104-109',
  note='The negative button callback. Its only call is the auto CALL to ExportDialog.dismissAllDialogFragments at line 107.')

e('S_DLG_EXPORT', 'ExportDialog$2.onClick', 'GUI',
  'the OK button of the export dialog is tapped',
  env=None,
  gui=['the OK button of the export dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:96-103',
  note='The positive button callback: exportApkg at line 100 (auto CALL to DeckPicker.exportApkg) and dismiss at line 101 (auto CALL). Batch 002 also has S_DLG_EXPORT -> DeckPicker.exportApkg directly; both routes stay.')

e('S_DLG_EXPORT', 'ExportDialog$3.onSelection', 'GUI',
  'an export option (schedule or media) is checked or unchecked',
  env=None,
  gui=['an export option (schedule or media) is checked or unchecked'],
  evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:75-95',
  note='The multi-choice callback sets mIncludeSched and mIncludeMedia (lines 81-93); the positive button reads them at line 100.')

# --- Import dialog page (S_DLG_IMPORT, created by DeckPicker.java:1096 and reached from action_import at 563).
e('S_DLG_IMPORT', 'ImportDialog$1.onNegative', 'GUI',
  'the Cancel button of the import hint dialog is tapped',
  env=None,
  gui=['the Cancel button of the import hint dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:80-82; SRC com/ichi2/anki/DeckPicker.java:561-563',
  note='The hint dialog comes from action_import, which has no guard. Its only call is the auto CALL to ImportDialog.dismissAllDialogFragments at line 81.')

e('S_DLG_IMPORT', 'ImportDialog$1.onPositive', 'GUI',
  'the OK button of the import hint dialog is tapped',
  env=None,
  gui=['the OK button of the import hint dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:75-77',
  note='Calls DeckPicker.showImportDialog(int) with DIALOG_IMPORT_SELECT (auto CALL, cha, line 76).')

e('S_DLG_IMPORT', 'ImportDialog$2.onShow', 'FRAMEWORK',
  'the import list is empty, so the dialog is shown and closes at once',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:89-97; FW-SRC core/java/android/app/Dialog.java:333, 392-395, 1367',
  note='MISSING GATE MG372: no .apkg file is importable (the import folder is empty, as on a fresh install). No predefined ENV or STATE constant covers this, so env and needs_state are unset. The framework path is Dialog.show calling sendShowMessage (Dialog.java:333, 392-395), and the handler calling onShow (Dialog.java:1367). The MaterialDialog hop from showListener to setOnShowListener is not in fw_src: INFERRED.')

e('S_DLG_IMPORT', 'ImportDialog$3.onSelection', 'GUI',
  'an .apkg file is chosen from the import list',
  env=None,
  needs_state=STATE_APKG,
  gui=['an .apkg file is chosen from the import list'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:108-122',
  note='The list exists only when at least one .apkg file is importable (STATE_APKG). Line 116 chooses REPLACE_CONFIRM for collection.apkg and line 119 chooses ADD_CONFIRM otherwise; auto_calls.json records the same DeckPicker.showImportDialog(int,String) pair at line 119 only.')

e('S_DLG_IMPORT', 'ImportDialog$4.onPositive', 'GUI',
  'the Add button of the add confirmation is tapped',
  env=None,
  needs_state=STATE_APKG,
  gui=['the Add button of the add confirmation is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:131-137',
  note='Calls DeckPicker.importAdd (auto CALL, cha, line 134) and ImportDialog.dismissAllDialogFragments (auto CALL, line 135).')

e('S_DLG_IMPORT', 'ImportDialog$5.onPositive', 'GUI',
  'the Replace button of the replace confirmation is tapped',
  env=None,
  needs_state=STATE_APKG,
  gui=['the Replace button of the replace confirmation is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:145-151',
  note='Calls DeckPicker.importReplace (auto CALL, cha, line 148) and ImportDialog.dismissAllDialogFragments (auto CALL, line 149).')

# --- Missing listener forwards to the activity (auto_calls.json has no record for these two pairs).
e('ExportDialog.dismissAllDialogFragments', 'AnkiActivity.dismissAllDialogFragments', 'CALL',
  'the export dialog asks its activity to dismiss the dialog stack (listener call at line 115)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:114-116; SRC com/ichi2/anki/AnkiActivity.java:464-466; SRC com/ichi2/anki/DeckPicker.java:110-112',
  note='The call goes through the ExportDialogListener interface, which DeckPicker implements. DeckPicker does not declare dismissAllDialogFragments, so the target is AnkiActivity.dismissAllDialogFragments (AnkiActivity.java:464).')

e('ImportDialog.dismissAllDialogFragments', 'AnkiActivity.dismissAllDialogFragments', 'CALL',
  'the import dialog asks its activity to dismiss the dialog stack (listener call at line 160)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:159-161; SRC com/ichi2/anki/AnkiActivity.java:464-466; SRC com/ichi2/anki/DeckPicker.java:110-112',
  note='The call goes through the ImportDialogListener interface, which DeckPicker implements. DeckPicker does not declare dismissAllDialogFragments, so the target is AnkiActivity.dismissAllDialogFragments (AnkiActivity.java:464).')

# ---- part 045 (2026-10-28)
# Batch 045 (LABEL helper). SyncErrorDialog, 31 methods. Rows are in graphs/AnkiDroid/parts/label_045.md.
# Edges owned here: 11 GUI edges from page S_DLG_SYNC_ERROR into the anonymous ButtonCallback methods of
# SyncErrorDialog (the destinations are in this batch). UNREACHABLE: SyncErrorDialog$2 (3 entries).
# Automatic CALL edges from auto_calls.json are not written here.

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$1.onPositive', 'GUI',
  'tap Log in on the not-logged-in sync dialog (type 0)',
  gui=['tap Log in on the not-logged-in sync dialog (type 0)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:78-84; SRC com/ichi2/anki/DeckPicker.java:1277-1283',
  note='MISSING GATE MG393: no account is logged in (the hkey preference is empty, DeckPicker.java:1281-1282). No constant fits, so env and needs_state are unset. The callback runs the activity listener loginToSyncServer (automatic CALL). The button dispatch is MaterialDialog (library, source not read): INFERRED. The direct edge S_DLG_SYNC_ERROR -> DeckPicker.loginToSyncServer (graph_def.py:1039) bypasses this callback; both routes exist.')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$3.onPositive', 'GUI',
  'tap keep local on the sync conflict dialog (type 2)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap keep local on the sync conflict dialog (type 2)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:111-116; SRC com/ichi2/anki/DeckPicker.java:1450-1458',
  note='Type 2 opens from the fullSync answer when the local collection is not empty (DeckPicker.java:1457). The answer needs the network and a stored hkey. The tap calls showSyncErrorDialog(3) (automatic CALL to DeckPicker.showSyncErrorDialog(int)).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$3.onNegative', 'GUI',
  'tap keep remote on the sync conflict dialog (type 2)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap keep remote on the sync conflict dialog (type 2)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:118-122; SRC com/ichi2/anki/DeckPicker.java:1450-1458',
  note='Same route as the keep-local tap (type 2 opens from the fullSync answer, DeckPicker.java:1457). The tap calls showSyncErrorDialog(4) (automatic CALL to DeckPicker.showSyncErrorDialog(int)).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$3.onNeutral', 'GUI',
  'tap Cancel on the sync conflict dialog (type 2)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap Cancel on the sync conflict dialog (type 2)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:124-127; SRC com/ichi2/anki/DeckPicker.java:1450-1458',
  note='Same route as the keep-local tap (type 2 opens from the fullSync answer, DeckPicker.java:1457). The callback calls dismissAllDialogFragments (SyncErrorDialog.java:126) and no server call.')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$4.onPositive', 'GUI',
  'confirm overwrite with the local collection (type 3)',
  gui=['confirm overwrite with the local collection (type 3)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:135-142, 114-115',
  note='MISSING GATE MG394: type 3 is on screen only after the local-version tap on type 2 (SyncErrorDialog.java:114-115). No constant fits, so env and needs_state are unset. The callback calls sync("upload") and dismissAllDialogFragments (lines 139-140).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$5.onPositive', 'GUI',
  'confirm overwrite with the remote collection (type 4)',
  gui=['confirm overwrite with the remote collection (type 4)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:149-156, 119-121',
  note='MISSING GATE MG394: type 4 is on screen only after the remote-version tap on type 2 (SyncErrorDialog.java:119-121). No constant fits, so env and needs_state are unset. The callback calls sync("download") and dismissAllDialogFragments (lines 153-154).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$6.onPositive', 'GUI',
  'tap keep local on the sanity-check error dialog (type 6)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap keep local on the sanity-check error dialog (type 6)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:164-170; SRC com/ichi2/anki/DeckPicker.java:1486-1489',
  note='Type 6 opens from the sanityCheckError answer (DeckPicker.java:1486-1489). The answer needs the network and a stored hkey. The tap calls showSyncErrorDialog(7) (automatic CALL to DeckPicker.showSyncErrorDialog(int)).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$6.onNeutral', 'GUI',
  'tap keep remote on the sanity-check error dialog (type 6)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap keep remote on the sanity-check error dialog (type 6)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:171-175; SRC com/ichi2/anki/DeckPicker.java:1486-1489',
  note='Same route as the keep-local tap (type 6 opens from the sanityCheckError answer, DeckPicker.java:1486-1489). The tap calls showSyncErrorDialog(8) (automatic CALL to DeckPicker.showSyncErrorDialog(int)).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$7.onPositive', 'GUI',
  'confirm overwrite with the local collection after a sanity error (type 7)',
  gui=['confirm overwrite with the local collection after a sanity error (type 7)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:183-189, 167-168',
  note='MISSING GATE MG394: type 7 is on screen only after the local-version tap on type 6 (SyncErrorDialog.java:167-168). No constant fits, so env and needs_state are unset. The callback calls sync("upload") and dismissAllDialogFragments (lines 186-187).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$8.onPositive', 'GUI',
  'confirm overwrite with the remote collection after a sanity error (type 8)',
  gui=['confirm overwrite with the remote collection after a sanity error (type 8)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:196-202, 173-174',
  note='MISSING GATE MG394: type 8 is on screen only after the remote-version tap on type 6 (SyncErrorDialog.java:173-174). No constant fits, so env and needs_state are unset. The callback calls sync("download") and dismissAllDialogFragments (lines 199-200).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$9.onPositive', 'GUI',
  'tap Check media on the media sync error dialog (type 9)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap Check media on the media sync error dialog (type 9)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:207-213; SRC com/ichi2/anki/DeckPicker.java:1492-1496',
  note='Type 9 opens from the mediaSyncServerError answer (DeckPicker.java:1493-1495). The answer needs the network and a stored hkey. The callback calls mediaCheck() (automatic CALL) and dismissAllDialogFragments (line 211). The direct edge S_DLG_SYNC_ERROR -> DeckPicker.mediaCheck (graph_def.py:1044) bypasses this callback; both routes exist.')

UNREACHABLE['SyncErrorDialog$2.<init>'] = (
    'branch_never_taken',
    'Created only in the case for id 1 (DIALOG_CONNECTION_ERROR, SyncErrorDialog.java:86). No caller passes 1: newInstance is called with 0, 2, 6 and 9 (DeckPicker.java:1282, 1430, 1457, 1488, 1495), and the taps pass 3, 4, 7 and 8 (SyncErrorDialog.java:115, 121, 168, 174). The only other sender of MSG_SHOW_SYNC_ERROR_DIALOG is getDialogHandlerMessage (SyncErrorDialog.java:291), which copies the dialogType of an existing instance (line 293), so id 1 cannot be created. Grep over the source root finds DIALOG_CONNECTION_ERROR only at its declaration (SyncErrorDialog.java:13) and in the switch labels (lines 86 and 255), and no showSyncErrorDialog(1) call.',
    'com/ichi2/anki/dialogs/SyncErrorDialog.java:12-13, 86-91, 255, 288-297; com/ichi2/anki/DeckPicker.java:1049-1061, 1282, 1430, 1457, 1488, 1495; com/ichi2/anki/dialogs/DialogHandler.java:38, 67-70',
    'SOURCE')

UNREACHABLE['SyncErrorDialog$2.onNegative'] = (
    'branch_never_taken',
    'Callback of the case for id 1 (SyncErrorDialog.java:86), which is never taken because no caller creates id 1 (see SyncErrorDialog$2.<init>). Its only call is dismissAllDialogFragments (line 100).',
    'com/ichi2/anki/dialogs/SyncErrorDialog.java:86-102',
    'SOURCE')

UNREACHABLE['SyncErrorDialog$2.onPositive'] = (
    'branch_never_taken',
    'Callback of the case for id 1 (SyncErrorDialog.java:86), which is never taken because no caller creates id 1 (see SyncErrorDialog$2.<init>). Its sync() call and dismissAllDialogFragments (lines 94-95) are in that branch only.',
    'com/ichi2/anki/dialogs/SyncErrorDialog.java:86-96',
    'SOURCE')

# ---- sup for part 045
sup(('SyncErrorDialog.onCreateDialog', 'SyncErrorDialog$2.<init>'))

# ---- part 044 (2026-10-28)
# AnkiDroid batch 044 (LABEL helper). Dialogs: MediaCheckDialog (with $1, $2, $3), ModelBrowserContextMenu,
# ModelEditorContextMenu, NoteEditorRescheduleCard (with $1), SimpleMessageDialog (with $1). 35 methods, all REACHABLE.
# The full row list is in graphs/AnkiDroid/parts/label_044.md.
#
# Route ownership:
# - Page edges (S_DLG_*) belong to the part that contains the destination, so they are written here.
# - Lifecycle edges from the <init> methods to onCreateDialog already exist in graph_def.py (lines 260-273); not repeated.
# - CALL edges (auto_calls.json, the builder's automatic edges) are not repeated here.
# - Shortcut overlap (not changed here): graph_def.py 1026-1033 has S_DLG_MEDIA_CHECK -> DeckPicker.mediaCheck and
#   S_DLG_MEDIA_CHECK -> DeckPicker.deleteUnused, which skip the callbacks MediaCheckDialog$1.onPositive and $2.onNegative.
#
# Gates: MG382 (results dialog shows unused media files), MG383 (results dialog shows no unused media files).
# Constants: ENV_STORAGE (the Check media menu item is enabled only when storage is mounted, DeckPicker.java:525-529),
# STATE_NOTE (the reschedule item is shown only when an existing note is edited, NoteEditor.java:803-808).

# --- MediaCheckDialog page (confirm dialog and results dialog share the page S_DLG_MEDIA_CHECK).
e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$1.onPositive', 'GUI',
  'the OK button of the confirm dialog (check media) is tapped and the media check starts',
  env=ENV_STORAGE,
  gui=['the OK button of the confirm dialog (check media) is tapped and the media check starts'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:67-73; SRC com/ichi2/anki/DeckPicker.java:525-529, 600-603, 1190-1191',
  note='The confirm dialog is opened from the Check media menu item, enabled only when storage is mounted (ENV_STORAGE). The next step, DeckPicker.mediaCheck, is an automatic CHA CALL (MediaCheckDialog.java:70). The button dispatch is the MaterialDialog library (not read: INFERRED).')

e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$1.onNegative', 'GUI',
  'the Cancel button of the confirm dialog is tapped and the dialogs are dismissed',
  env=ENV_STORAGE,
  gui=['the Cancel button of the confirm dialog is tapped and the dialogs are dismissed'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:76-79',
  note='The confirm dialog exists only when the menu item is enabled (ENV_STORAGE). The dismiss call (line 77-78) is not in auto_calls.json. The button dispatch is the MaterialDialog library (not read: INFERRED).')

e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$2.onPositive', 'GUI',
  'the OK button of the media check results dialog is tapped when unused media files exist (the dialog only dismisses)',
  gui=['the OK button of the media check results dialog is tapped when unused media files exist (the dialog only dismisses)'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:116-124',
  note='MISSING GATE MG382: the results dialog has unused media files (MediaCheckDialog.java:116-118). No predefined ENV or STATE kind covers the content of the media folder. env and needs_state unset.')

e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$2.onNegative', 'GUI',
  'the Delete unused button of the media check results dialog is tapped',
  gui=['the Delete unused button of the media check results dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:116-131',
  note='MISSING GATE MG382: the same condition as MediaCheckDialog$2.onPositive (unused media files exist). The callback calls DeckPicker.deleteUnused (automatic CHA CALL, line 128) and then dismisses the dialogs (line 129). The page shortcut in graph_def.py (lines 1030-1033) reaches DeckPicker.deleteUnused without this callback. env and needs_state unset.')

e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$3.onPositive', 'GUI',
  'the OK button of the media check results dialog is tapped when no unused media files were found',
  gui=['the OK button of the media check results dialog is tapped when no unused media files were found'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:132-139',
  note='MISSING GATE MG383: the results dialog has no unused media files (the else branch, MediaCheckDialog.java:132). No predefined ENV or STATE kind covers this. env and needs_state unset.')

# --- SimpleMessageDialog page.
e('S_DLG_SIMPLE_MESSAGE', 'SimpleMessageDialog$1.onPositive', 'GUI',
  'the OK button of the simple message dialog is tapped',
  gui=['the OK button of the simple message dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/SimpleMessageDialog.java:40-47; SRC com/ichi2/anki/AnkiActivity.java:453-460',
  note='No gate. The callback calls AnkiActivity.dismissSimpleMessageDialog (automatic CHA CALL, SimpleMessageDialog.java:44). That method restarts DeckPicker only when reload is set (AnkiActivity.java:455-458).')

# --- NoteEditorRescheduleCard page.
e('S_DLG_RESCHEDULE_CARD', 'NoteEditorRescheduleCard$1.onInput', 'GUI',
  'a day count is typed in the reschedule dialog (the input callback)',
  needs_state=STATE_NOTE,
  gui=['a day count is typed in the reschedule dialog (the input callback)'],
  evidence='SRC com/ichi2/anki/dialogs/NoteEditorRescheduleCard.java:27-33; SRC com/ichi2/anki/NoteEditor.java:801-808, 871-874, 973-979',
  note='The menu item is shown only when the editor is not adding a note (NoteEditor.java:803-808), so an existing note exists (STATE_NOTE). The library calls InputCallback.onInput with the typed text (library not read: INFERRED). The callback calls NoteEditor.onRescheduleCard (automatic exact CALL, NoteEditorRescheduleCard.java:31). The input range (inputRange(1,4), line 26) is library validation (INFERRED).')

# ---- part 046 (2026-10-28)
# AnkiDroid batch 046 (LABEL helper). TagsDialog: 36 methods. The full row list is in graphs/AnkiDroid/parts/label_046.md.
#
# Route ownership:
# - The DialogFragment lifecycle edges from TagsDialog.<init> to onCreate and onCreateDialog are in graph_def.py (lines 278-279). Not written here.
# - The callers of newInstance, setTagsDialogListener and the showTagsDialog methods are in other batches. Their automatic CALL edges
#   into this batch (the <init> methods, adjustToolbar, addTag, sortData, getFilter) come from auto_calls.json. Not written here.
# - The listener dispatch to CardBrowser$12, NoteEditor$10 and CustomStudyDialog$1$1 is the existing S_DLG_TAGS page edges and the
#   automatic CHA CALL edge from TagsDialog$2.onPositive. Not written here.
# - Page node: S_DLG_TAGS (graph_def.py line 102). A page edge belongs to the part that contains its destination, so the page edges
#   into this batch are written here.
#
# Gates (MG402-MG406): MG402 at least one tag is listed; MG403 the dialog type is TYPE_ADD_TAG; MG404 the dialog type is not
# TYPE_ADD_TAG; MG405 at least two tags are listed; MG406 the add item opens the input dialog (search view not expanded with a
# non-empty query). None of the predefined ENV or STATE constants fits, so env and needs_state are unset.

# --- Page edges from S_DLG_TAGS (the dialog is entered by CardBrowser.showTagsDialog, NoteEditor.showTagsDialog or CustomStudyDialog).

e('S_DLG_TAGS', 'TagsDialog$2.onPositive', 'GUI',
  'tap the positive button of the tags dialog (OK or Select)',
  env=None,
  gui=['tap the positive button of the tags dialog (OK or Select)'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:158-168',
  note='The button callback is the MaterialDialog ButtonCallback (TagsDialog.java:162). The library dispatch from the button to onPositive is not in the dataset: INFERRED (source not read). The call to the listener at TagsDialog.java:165-166 is an automatic CHA CALL edge and is not repeated here.')

e('S_DLG_TAGS', 'TagsDialog$1.onCheckedChanged', 'GUI',
  'choose one of the three options (all cards, new cards, due cards) in the options radio group',
  env=None,
  gui=['choose one of the three options (all cards, new cards, due cards) in the options radio group'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:138-143, 146-148; res/layout/tags_dialog.xml:18-36',
  note='MISSING GATE MG404: the options group is hidden for TYPE_ADD_TAG (TagsDialog.java:148), so the radio options exist only for the filter and custom study types. The RadioGroup dispatch to the listener is android.widget code, not in fw_src: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$4.onMenuItemClick', 'GUI',
  'tap the add (+) item in the tags dialog toolbar',
  env=None,
  gui=['tap the add (+) item in the tags dialog toolbar'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:193-196, 268-274; res/menu/tags_dialog_menu.xml:12-16',
  note='MISSING GATE MG403: the add item is set invisible for every type other than TYPE_ADD_TAG (TagsDialog.java:272-273). The toolbar item click dispatch is support library code, not in the dataset: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$6.onMenuItemClick', 'GUI',
  'tap the select-all item in the tags dialog toolbar',
  env=None,
  gui=['tap the select-all item in the tags dialog toolbar'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:244-266; res/menu/tags_dialog_menu.xml:18-22',
  note='No gate: the select-all item is not hidden for any dialog type (TagsDialog.java:268-274 changes only the add item). The toolbar dispatch is support library code: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$5.onQueryTextChange', 'GUI',
  'type in the filter search field of the toolbar (the SearchView is expanded)',
  env=None,
  gui=['type in the filter search field of the toolbar (the SearchView is expanded)'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:229, 237-240; res/menu/tags_dialog_menu.xml:5-10',
  note='No gate. The SearchView text listener is set at TagsDialog.java:229. The SearchView dispatch is support library code, not in the dataset: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$5.onQueryTextSubmit', 'GUI',
  'submit the query in the filter search field (search key)',
  env=None,
  gui=['submit the query in the filter search field (search key)'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:229-234',
  note='No gate. The body clears the focus of the SearchView and returns true. The dispatch is support library code: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$3.filter', 'FRAMEWORK',
  'type a character into the filter search field (the InputFilter rejects a space)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:181-192, 226',
  note='No gate. The InputFilter is set on the search EditText at TagsDialog.java:226. The EditText dispatch to InputFilter.filter is android.text code, not in fw_src: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$TagsArrayAdapter$2.onClick', 'GUI',
  'tap a tag row to check or uncheck the tag',
  env=None,
  gui=['tap a tag row to check or uncheck the tag'],
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:340-353',
  note='MISSING GATE MG402: a row exists only when at least one tag is listed (TagsDialog.java:359-361, 366-367). The row click listener is set in onCreateViewHolder (TagsDialog.java:341). The View click dispatch is framework code whose source was not read: INFERRED.')

e('S_DLG_TAGS', 'TagsDialog$TagsArrayAdapter.onCreateViewHolder', 'FRAMEWORK',
  'the RecyclerView creates a row for a tag',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:124-125, 335-340',
  note='MISSING GATE MG402: no row is created while the tag list is empty. The RecyclerView dispatch is support library code, not in the dataset: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$TagsArrayAdapter.onBindViewHolder', 'FRAMEWORK',
  'the RecyclerView binds a tag name and its checked state to a row',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:124-125, 358-362',
  note='MISSING GATE MG402: no row is bound while the tag list is empty. The RecyclerView dispatch is support library code: INFERRED (source not read).')

e('S_DLG_TAGS', 'TagsDialog$TagsArrayAdapter.getItemCount', 'FRAMEWORK',
  'the RecyclerView asks how many rows the tag list has',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:124-125, 365-367',
  note='No gate: getItemCount is asked on every layout and returns 0 for an empty list. The RecyclerView dispatch is support library code: INFERRED (source not read).')

# --- Edges inside the dialog's own methods.

e('TagsDialog$4.onMenuItemClick', 'TagsDialog$4$1.onInput', 'FRAMEWORK',
  'confirm the add-tag input dialog with OK; the input dialog calls onInput with the typed text',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:197-216',
  note='MISSING GATE MG406: the input dialog opens only when the search view is not expanded with a non-empty query (TagsDialog.java:197-201). The add item is visible only for TYPE_ADD_TAG (MG403). The MaterialDialog InputCallback dispatch is library code, not in the dataset: INFERRED (source not read). The call to addTag at TagsDialog.java:210 is an automatic CALL edge.')

e('TagsDialog$4.onMenuItemClick', 'TagsDialog$3.filter', 'FRAMEWORK',
  'type a character into the add-tag input dialog (the InputFilter rejects a space)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:181-192, 215-216',
  note='MISSING GATE MG406: the input dialog opens only when the search view is not expanded with a non-empty query (TagsDialog.java:197-201), and the add item needs MG403. The EditText dispatch to InputFilter.filter is android.text code, not in fw_src: INFERRED (source not read).')

e('TagsDialog$5.onQueryTextChange', 'TagsDialog$TagsArrayAdapter$TagsFilter.performFiltering', 'ASYNC',
  'the search text changes: Filter.filter posts the constraint and performFiltering runs on the filter worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:237-240, 383; FW-SRC core/java/android/widget/Filter.java:101-126, 227-234',
  note='No gate: an empty constraint still runs performFiltering. The getFilter call at TagsDialog.java:238 is an automatic CALL edge. The posting and the RequestHandler path are in Filter.java (fw_src), read only at the lines cited.')

e('TagsDialog$TagsArrayAdapter$TagsFilter.performFiltering', 'TagsDialog$TagsArrayAdapter$TagsFilter.publishResults', 'ASYNC',
  'the filter results are posted back and publishResults runs on the UI thread',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:383-408; FW-SRC core/java/android/widget/Filter.java:239-241, 279-282',
  note='No gate. The result post is Filter.java:239-241, and ResultsHandler.handleMessage calls publishResults at Filter.java:282.')

e('TagsDialog$TagsArrayAdapter.sortData', 'TagsDialog$TagsArrayAdapter$1.compare', 'FRAMEWORK',
  'Collections.sort calls the Comparator to order the tag list (checked tags first)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:322-331',
  note='MISSING GATE MG405: the comparator runs only when the list has at least two tags. java.util.Collections.sort is not in the dataset: INFERRED (source not read).')

# ---- part 048 (2026-10-28)
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

# ---- sup for part 048
sup(('MultimediaEditFieldActivity.onCreate', 'MultimediaEditFieldActivity.createSpareMenu'))
sup(('MultimediaEditFieldActivity.createSpareMenu', 'MultimediaEditFieldActivity.gtxt'))
sup(('MultimediaEditFieldActivity.createSpareMenu', 'MultimediaEditFieldActivity$1.<init>'))
sup(('MultimediaEditFieldActivity.createSpareMenu', 'MultimediaEditFieldActivity$2.<init>'))
sup(('MultimediaEditFieldActivity.createSpareMenu', 'MultimediaEditFieldActivity$3.<init>'))
sup(('MultimediaEditFieldActivity.createSpareMenu', 'MultimediaEditFieldActivity$4.<init>'))

# ---- part 047 (2026-10-28)
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

# ---- part 049 (2026-10-28)
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

# ---- part 052 (2026-10-28)
# AnkiDroid batch 052 (LABEL helper). FieldEditText (10 methods), FlashCardsContract nested classes in the api
# module (14), Lookup (10) and Manifest (2). The full row list is in graphs/AnkiDroid/parts/label_052.md.
# Written here: two page-to-batch e() edges and 16 UNREACHABLE entries. CALL edges that auto_calls.json already
# holds (the <clinit> chains and the Lookup and NoteEditor callers) are not repeated.

# LayoutInflater creates the FieldEditText named in card_multimedia_editline.xml through the (Context, AttributeSet)
# constructor, by reflection. The editor opens from DeckPicker add note (DeckPicker.java:841).
e('S_NOTEEDITOR', 'FieldEditText.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the note editor inflates card_multimedia_editline.xml, which instantiates the FieldEditText view',
  env=None,
  cls='non_standard',
  via='android.view.LayoutInflater XML inflation (framework, FW-SRC core/java/android/view/LayoutInflater.java:615, 647)',
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1099; SRC com/ichi2/anki/FieldEditText.java:23-25; FW-SRC core/java/android/view/LayoutInflater.java:615, 647',
  note='Opened from DeckPicker add note (DeckPicker.java:841) and CardBrowser (493, 631). populateEditFields is called from setNote (NoteEditor.java:1380), updateFieldsFromMap (1497) and the note-type spinner (1637). The layout is src/main/res/layout/card_multimedia_editline.xml lines 8-16. Edit mode also needs a note (STATE_NOTE). The class initializer FieldEditText.<clinit> runs on the same reflective construction.')

# The dictionary dialog callback. The user taps a language in the LEO dialog built by Lookup.lookUp (Lookup.java:110-123).
# The lookup button is shown only when Lookup.isAvailable() (AbstractFlashcardViewer.java:1219).
e('S_REVIEWER', 'Lookup$1.onSelection', 'GUI',
  'tap the lookup button, then pick a language in the LEO dictionary dialog',
  env=ENV_BROWSER,
  needs_state=STATE_SETTINGS,
  gui=['tap the lookup button, then pick a language in the LEO dictionary dialog'],
  evidence='SRC com/ichi2/anki/Lookup.java:110-121; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1210, 1219, 1424',
  note='The dialog opens only for the LEO dictionaries (preference 3 or 4, Lookup.java:94-95). The LEO web variant needs a browser (ENV_BROWSER). The LEO app variant (preference 4) needs org.leo.android.dict installed (ENV_OTHER_APP_INTENT). The callback calls storeLanguage (Lookup.java:118, empty body) and lookupLeo (Lookup.java:119).')

UNREACHABLE['FieldEditText.<init>(Context)'] = ('no_trigger_in_app', 'No new FieldEditText( anywhere in src/main or api. LayoutInflater never uses the one-argument signature; it calls the (Context,AttributeSet) constructor (FW-SRC LayoutInflater.java:90-91). No class extends FieldEditText.', 'SRC com/ichi2/anki/FieldEditText.java:18-20', 'SOURCE')
UNREACHABLE['FieldEditText.<init>(Context,int,String,String)'] = ('no_trigger_in_app', 'No new FieldEditText( with four arguments exists in src/main or api. NoteEditor builds fields from XML (NoteEditor.java:1099) and calls init directly (NoteEditor.java:1247), so this constructor is never reached.', 'SRC com/ichi2/anki/FieldEditText.java:33-36', 'SOURCE')
UNREACHABLE['FieldEditText.<init>(Context,AttributeSet,int)'] = ('no_trigger_in_app', 'No new FieldEditText( with three arguments exists. LayoutInflater uses only the two-argument signature. The two-argument constructor calls super(context, attr) (FieldEditText.java:24), not this(...), so nothing chains into this one. No subclass exists.', 'SRC com/ichi2/anki/FieldEditText.java:28-30', 'SOURCE')
UNREACHABLE['FieldEditText.cleanText'] = ('no_trigger_in_app', 'The only occurrence of cleanText( in src/main is its definition (FieldEditText.java:70). No caller in src/main or api.', 'SRC com/ichi2/anki/FieldEditText.java:70-75', 'SOURCE')
UNREACHABLE['FieldEditText.getName'] = ('no_trigger_in_app', 'No .getName() call in src/main has a FieldEditText receiver. The receivers are File, Backup, list items of other types, and reflection Field and Class objects. No caller.', 'SRC com/ichi2/anki/FieldEditText.java:51-53', 'SOURCE')
UNREACHABLE['FlashCardsContract.<init>'] = ('no_trigger_in_app', 'Private constructor (api FlashCardsContract.java:119-120, "Don\'t create instances of this class"). No new FlashCardsContract( in src/main or api. The api file is outside the checker roots, so the source cell cites the provider import.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:41-42', 'SOURCE')
UNREACHABLE['FlashCardsContract$Card.<init>'] = ('no_trigger_in_app', 'Implicit constructor of the nested static class (api FlashCardsContract.java:708). No new Card( or new FlashCardsContract.Card( in the files that reference FlashCardsContract (CardContentProvider.java, NoteInfo.java, AddContentApi.java).', 'SRC com/ichi2/anki/provider/CardContentProvider.java:41-42', 'SOURCE')
UNREACHABLE['FlashCardsContract$CardTemplate.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:500). No new CardTemplate( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:42', 'SOURCE')
UNREACHABLE['FlashCardsContract$Deck.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:1078). No new Deck( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:368', 'SOURCE')
UNREACHABLE['FlashCardsContract$Model.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:438). No new Model( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:265', 'SOURCE')
UNREACHABLE['FlashCardsContract$Note.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:252). No new Note( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:139', 'SOURCE')
UNREACHABLE['FlashCardsContract$ReviewInfo.<init>'] = ('no_trigger_in_app', 'Implicit constructor (api FlashCardsContract.java:899). No new ReviewInfo( in the files that reference FlashCardsContract.', 'SRC com/ichi2/anki/provider/CardContentProvider.java:313', 'SOURCE')
UNREACHABLE['Lookup.<init>'] = ('no_trigger_in_app', 'Lookup has no explicit constructor (Lookup.java:17) and there is no new Lookup( in src/main or api. Every member is static, so the implicit constructor never runs.', 'SRC com/ichi2/anki/Lookup.java:17', 'SOURCE')
UNREACHABLE['Lookup.getSearchStringTitle'] = ('closed_by_api_level', 'Only caller: Reviewer.onCreateOptionsMenu (Reviewer.java:298-300), inside if (!CompatHelper.isHoneycomb() && !mDisableClipboard). isHoneycomb is SDK 11 or higher (CompatHelper.java:61-62). On the standard API 27 config the guard is false, so the branch never runs. minSdkVersion is 10 (build.gradle), so the branch is reachable only on API 10.', 'SRC com/ichi2/anki/Reviewer.java:298-300; SRC com/ichi2/compat/CompatHelper.java:61-62', 'SOURCE')
UNREACHABLE['Manifest.<init>'] = ('no_trigger_in_app', 'Generated class from aapt; its input is the permission declaration at AndroidManifest.xml:58. The generated file is not in the source tree. No new Manifest( in src/main or api. The app source refers only to android.Manifest (DeckPicker.java:24, CollectionHelper.java:19), a different class. confirmed_by INFERRED, not by a source line.', 'SRC AndroidManifest.xml:58', 'INFERRED')
UNREACHABLE['Manifest$permission.<init>'] = ('no_trigger_in_app', 'Nested class generated from the same permission declaration (AndroidManifest.xml:58). No new anywhere in src/main or api. confirmed_by INFERRED, not by a source line. A conflicts.md entry is needed; this helper may not write it, so the orchestrator must add it.', 'SRC AndroidManifest.xml:58', 'INFERRED')

# ---- sup for part 052
sup(('Reviewer.onCreateOptionsMenu', 'Lookup.getSearchStringTitle'))

# ---- part 050 (2026-10-28)
# AnkiDroid batch 050 (LABEL helper). AppCompatPreferenceActivity (17 methods) and AnkiFont (10 methods).
# The full row list is in graphs/AnkiDroid/parts/label_050.md.
#
# Route ownership:
# - The automatic CALL edges (super calls, getDelegate, AnkiFont internal calls, cross-class AnkiFont calls,
#   and the subclass constructor calls into AppCompatPreferenceActivity.<init>) come from auto_calls.json.
#   They are not written here.
# - The LIFECYCLE edges for AppCompat onCreate and onStop are generated by graph_def.py:300 and are not written here.
# - onDestroy and onConfigurationChanged are in LC_NO_TRIGGER (graph_def.py:37), so their page edges are written here.
# Gates: no MISSING GATE is needed. Page node: S_PREFERENCES. Predefined constant used: ENV_CONFIG_CHANGE.

# --- Framework dispatch into the AppCompat overrides.
e('AppCompatPreferenceActivity.onCreate', 'AppCompatPreferenceActivity.setContentView(int)', 'FRAMEWORK',
  'PreferenceActivity.onCreate sets the content view with the layout resource, which dispatches to the AppCompat override',
  env=None,
  evidence='SRC com/ichi2/ui/AppCompatPreferenceActivity.java:43-47, 69-71; FW-SRC core/java/android/preference/PreferenceActivity.java:575',
  note='AppCompat.onCreate reaches PreferenceActivity.onCreate through its super call (line 46). The delegate call at line 70 is an automatic CALL edge and is not written here.')

e('AppCompatPreferenceActivity.onPostCreate', 'AppCompatPreferenceActivity.onTitleChanged', 'FRAMEWORK',
  'Activity.onPostCreate calls onTitleChanged for a top-level activity',
  env=None,
  evidence='SRC com/ichi2/ui/AppCompatPreferenceActivity.java:50-53, 94-98; FW-SRC core/java/android/app/Activity.java:1200-1203',
  note='AppCompat.onPostCreate reaches the framework call through its super call (line 51). The delegate call at line 52 is an automatic CALL edge and is not written here.')

e('S_PREFERENCES', 'AppCompatPreferenceActivity.onPostCreate', 'FRAMEWORK',
  'the framework runs the post-create callback after the settings screen is created',
  env=None,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2760; FW-SRC core/java/android/app/Instrumentation.java:1284-1286; SRC com/ichi2/ui/AppCompatPreferenceActivity.java:50-53',
  note='ActivityThread calls Instrumentation.callActivityOnPostCreate, which calls activity.onPostCreate.')

e('S_PREFERENCES', 'AppCompatPreferenceActivity.onPostResume', 'FRAMEWORK',
  'the settings screen resumes (Activity.performResume calls onPostResume)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:7128-7131; SRC com/ichi2/ui/AppCompatPreferenceActivity.java:89-92',
  note='The override calls super (line 90) and then the delegate (line 91, automatic CALL edge).')

e('S_PREFERENCES', 'AppCompatPreferenceActivity.onConfigurationChanged', 'SYSTEM',
  'a configuration change that the manifest handles (orientation, locale, screenSize, keyboardHidden) reaches the running settings screen',
  env=ENV_CONFIG_CHANGE,
  evidence='SRC AndroidManifest.xml:191-196; FW-SRC core/java/android/app/ActivityThread.java:4940-4942; SRC com/ichi2/ui/AppCompatPreferenceActivity.java:101-104',
  note='The Preferences manifest entry lists the configChanges on line 194. onConfigurationChanged is in LC_NO_TRIGGER (graph_def.py:37), so no lifecycle edge is written for it.')

e('S_PREFERENCES', 'AppCompatPreferenceActivity.onDestroy', 'FRAMEWORK',
  'the user leaves the settings screen and the framework destroys it (performDestroy calls onDestroy)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:7204-7208; SRC com/ichi2/ui/AppCompatPreferenceActivity.java:113-116',
  note='onDestroy is in LC_NO_TRIGGER (graph_def.py:37), so the lifecycle chain writes no edge for it. Preferences has no onDestroy override; DeckOptions and FilteredDeckOptions override it and call super.')

e('S_PREFERENCES', 'AppCompatPreferenceActivity.getMenuInflater', 'GUI',
  'open the options menu of the settings screen (menu key or overflow)',
  env=None,
  gui=['open the options menu of the settings screen (menu key or overflow)'],
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:627-633; FW-SRC core/java/android/app/Activity.java:3386-3393; SRC com/ichi2/ui/AppCompatPreferenceActivity.java:63-66',
  note='PhoneWindow calls onCreatePanelMenu, which passes getMenuInflater into the fragment dispatch. The settings screens handle options items (Preferences onOptionsItemSelected at com/ichi2/anki/Preferences.java:152).')

# --- UNREACHABLE: AppCompat overrides that no route reaches.
UNREACHABLE['AppCompatPreferenceActivity.addContentView'] = (
    'no_trigger_in_app',
    'No call reaches this override. The three subclasses (Preferences, DeckOptions, FilteredDeckOptions) never call addContentView, and no other app code calls it on their instances. The AppCompat library source is not in the dataset, so library-internal calls are not checked.',
    'SRC com/ichi2/ui/AppCompatPreferenceActivity.java:84-86; SRC com/ichi2/anki/AnkiActivity.java:143-148; SRC com/ichi2/anki/Preferences.java:90; SRC com/ichi2/anki/DeckOptions.java:71; SRC com/ichi2/anki/FilteredDeckOptions.java:59; FW-SRC core/java/android/app/Activity.java:2716-2717',
    'SOURCE')

UNREACHABLE['AppCompatPreferenceActivity.setContentView(View)'] = (
    'no_trigger_in_app',
    'No caller on the three subclasses: their files contain no setContentView call. PreferenceActivity.onCreate calls the int overload only (core/java/android/preference/PreferenceActivity.java:575). No other app code calls setContentView on an instance of this class. The AppCompat library source is not in the dataset, so library-internal calls are not checked.',
    'SRC com/ichi2/ui/AppCompatPreferenceActivity.java:74-76; SRC com/ichi2/anki/Preferences.java:90; SRC com/ichi2/anki/DeckOptions.java:71; SRC com/ichi2/anki/FilteredDeckOptions.java:59; FW-SRC core/java/android/preference/PreferenceActivity.java:575',
    'SOURCE')

UNREACHABLE['AppCompatPreferenceActivity.setContentView(View,LayoutParams)'] = (
    'no_trigger_in_app',
    'No caller on the three subclasses: their files contain no setContentView call. PreferenceActivity.onCreate calls the int overload only (core/java/android/preference/PreferenceActivity.java:575). No other app code calls setContentView on an instance of this class. The AppCompat library source is not in the dataset, so library-internal calls are not checked.',
    'SRC com/ichi2/ui/AppCompatPreferenceActivity.java:79-81; SRC com/ichi2/anki/Preferences.java:90; SRC com/ichi2/anki/DeckOptions.java:71; SRC com/ichi2/anki/FilteredDeckOptions.java:59; FW-SRC core/java/android/preference/PreferenceActivity.java:575',
    'SOURCE')

UNREACHABLE['AppCompatPreferenceActivity.setSupportActionBar'] = (
    'no_trigger_in_app',
    'No caller on the three subclasses. They call getSupportActionBar only. The app setSupportActionBar calls are in other activities (for example com/ichi2/anki/Info.java:72), which do not extend this class. The framework has no setSupportActionBar. The AppCompat library source is not in the dataset, so library-internal calls are not checked.',
    'SRC com/ichi2/ui/AppCompatPreferenceActivity.java:59-61; SRC com/ichi2/anki/Info.java:71-73; SRC com/ichi2/anki/Preferences.java:128-129; SRC com/ichi2/anki/DeckOptions.java:540; SRC com/ichi2/anki/FilteredDeckOptions.java:399',
    'SOURCE')

UNREACHABLE['AppCompatPreferenceActivity.invalidateOptionsMenu'] = (
    'framework_never_calls',
    'The framework calls Activity.invalidateOptionsMenu only from Activity.setActionBar (core/java/android/app/Activity.java:2634), from the fragment host callback (core/java/android/app/Activity.java:7674), and from Fragment.setHasOptionsMenu and Fragment.setMenuVisibility (core/java/android/app/Fragment.java:944, 962). None of these runs for the three settings screens: those files contain no setActionBar, setHasOptionsMenu, setMenuVisibility or FragmentTransaction call. The app options-menu fragments (CardTemplateEditor.java:420, Statistics.java:423, :595) belong to other classes. The AppCompat library source is not in the dataset, so library-internal calls are not checked.',
    'SRC com/ichi2/ui/AppCompatPreferenceActivity.java:118-120; FW-SRC core/java/android/app/Activity.java:2634, 7674; FW-SRC core/java/android/app/Fragment.java:940-947, 959-965; SRC com/ichi2/anki/CardTemplateEditor.java:420; SRC com/ichi2/anki/Statistics.java:423, 595; SRC com/ichi2/anki/StudyOptionsActivity.java:101',
    'SOURCE')

# ---- part 051 (2026-10-28)
# AnkiDroid batch 051 (LABEL helper). BackupManager (21 methods, including BackupManager$1), CollectionHelper (7 methods
# and CollectionHelper$LazyHolder.<init>) and CustomExceptionHandler (10 methods). The full row list is in
# graphs/AnkiDroid/parts/label_051.md.
#
# Route ownership:
# - The bytecode CALL edges, including the creation of the anonymous thread (BackupManager$1.<init>, BackupManager.java:174),
#   come from auto_calls.json. They are not written here.
# - The ASYNC edge from performBackupInBackground(String,int,boolean) into BackupManager$1.run (thread.start() at
#   BackupManager.java:202) is written here, because its source method is in this batch.
#
# UNREACHABLE entries: 15 (all no_trigger_in_app). The reasons repeat the reasons in label_051.md.

e('BackupManager.performBackupInBackground(String,int,boolean)', 'BackupManager$1.run', 'ASYNC',
  'the backup thread is started with thread.start() after the guards pass',
  env=None,
  evidence='SRC com/ichi2/anki/BackupManager.java:174-202',
  note='The guards are at BackupManager.java:105-164. The run body (zip of the collection, then deleteDeckBackups at line 193) is batch 051 as well. thread.start() is plain java.lang.Thread, not framework code.')

UNREACHABLE['BackupManager.<init>'] = ('no_trigger_in_app',
  "The constructor is private and the class is a static utility. No code in the source root creates a BackupManager (grep for new BackupManager finds nothing).",
  'com/ichi2/anki/BackupManager.java:60-62', 'SOURCE')

UNREACHABLE['BackupManager.deleteDeckBackups(File,int)'] = ('no_trigger_in_app',
  "No caller. The String overload (line 331) and the backup run body (line 193, a String path) bind to other overloads. No call in the source root passes a File to this overload.",
  'com/ichi2/anki/BackupManager.java:335-337, 330-332, 193', 'SOURCE')

UNREACHABLE['BackupManager.isActivated'] = ('no_trigger_in_app',
  "No caller in the source root (grep finds only the declaration). mUseBackups is set only at its declaration (line 53, true), so the method would return true if called.",
  'com/ichi2/anki/BackupManager.java:53, 65-67', 'SOURCE')

UNREACHABLE['BackupManager.performBackupInBackground(String,int)'] = ('no_trigger_in_app',
  "No caller. The one-argument call (DeckPicker.java:807) and the (String,boolean) call (DeckTask.java:814) bind to other overloads. The (String) and (String,boolean) overloads call (String,int,boolean) directly (lines 89 and 94).",
  'com/ichi2/anki/BackupManager.java:98-100, 88-95; com/ichi2/anki/DeckPicker.java:807; com/ichi2/async/DeckTask.java:814', 'SOURCE')

UNREACHABLE['CollectionHelper$LazyHolder.<init>'] = ('no_trigger_in_app',
  "The implicit constructor of the private holder class is never invoked. getInstance (line 76) reads the static field INSTANCE, which runs the holder static initializer, not an instance constructor. No other reference to LazyHolder exists in the source root.",
  'com/ichi2/anki/CollectionHelper.java:68-70, 75-77', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.<init>'] = ('no_trigger_in_app',
  "The class has no explicit constructor, so this is the default constructor. The only instantiation is in getInstance (line 50), and getInstance has no caller in src/main/java (the only reference, AnkiDroidApp.java:249, is commented out).",
  'com/ichi2/anki/CustomExceptionHandler.java:38, 48-51; com/ichi2/anki/AnkiDroidApp.java:249', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.collectInformation'] = ('no_trigger_in_app',
  "Private. Its only caller is the 4-arg uncaughtException (line 136). That method is reached only through the 3-arg and 2-arg overloads and the JVM dispatch, and no instance of the class is ever created (see <init>), so no route exists.",
  'com/ichi2/anki/CustomExceptionHandler.java:83-119, 136', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.getAvailableInternalMemorySize'] = ('no_trigger_in_app',
  "Private helper. Its only caller is collectInformation (line 113), which is unreachable (see collectInformation).",
  'com/ichi2/anki/CustomExceptionHandler.java:65-71, 113', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.getInstance'] = ('no_trigger_in_app',
  "Static accessor. The only reference to the class outside its own file is the commented-out call at AnkiDroidApp.java:249. grep of src/main/java for CustomExceptionHandler and UncaughtExceptionHandler finds no other caller.",
  'com/ichi2/anki/CustomExceptionHandler.java:48-55; com/ichi2/anki/AnkiDroidApp.java:249', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.getTotalInternalMemorySize'] = ('no_trigger_in_app',
  "Private helper. Its only caller is collectInformation (line 112), which is unreachable (see collectInformation).",
  'com/ichi2/anki/CustomExceptionHandler.java:74-80, 112', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.init'] = ('no_trigger_in_app',
  "Public, with no caller in src/main/java. It is the only place that calls Thread.setDefaultUncaughtExceptionHandler(this) (line 60), so the handler is never installed. It also needs an instance, and getInstance has no caller.",
  'com/ichi2/anki/CustomExceptionHandler.java:58-62; com/ichi2/anki/AnkiDroidApp.java:249', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.saveReportToFile'] = ('no_trigger_in_app',
  "Private. Its only caller is the 4-arg uncaughtException (line 192), which is unreachable (see uncaughtException(Thread,Throwable,String,String)).",
  'com/ichi2/anki/CustomExceptionHandler.java:200-217, 192', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.uncaughtException(Thread,Throwable)'] = ('no_trigger_in_app',
  "The @Override of Thread.UncaughtExceptionHandler. It runs only when this object is installed as a default or per-thread handler. No instance is ever created (getInstance has no caller), and init (the only installer, line 60) has no caller. No direct caller exists in src/main/java.",
  'com/ichi2/anki/CustomExceptionHandler.java:122-125, 58-62', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.uncaughtException(Thread,Throwable,String)'] = ('no_trigger_in_app',
  "Public overload. Its only caller in the class is the 2-arg uncaughtException (line 124). No caller exists outside the class, and the instance route is missing (see the 2-arg row).",
  'com/ichi2/anki/CustomExceptionHandler.java:128-130, 124', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.uncaughtException(Thread,Throwable,String,String)'] = ('no_trigger_in_app',
  "Public overload. Its only caller in the class is the 3-arg overload (line 129). The one outside reference, AnkiDroidApp.java:249, is commented out. The body calls collectInformation (line 136) and saveReportToFile (line 192).",
  'com/ichi2/anki/CustomExceptionHandler.java:133-197; com/ichi2/anki/AnkiDroidApp.java:249', 'SOURCE')

# ---- sup for part 051
sup(('CustomExceptionHandler.getInstance', 'CustomExceptionHandler.<init>'))
sup(('CustomExceptionHandler.collectInformation', 'CustomExceptionHandler.getAvailableInternalMemorySize'))
sup(('CustomExceptionHandler.collectInformation', 'CustomExceptionHandler.getTotalInternalMemorySize'))
sup(('CustomExceptionHandler.uncaughtException(Thread,Throwable)', 'CustomExceptionHandler.uncaughtException(Thread,Throwable,String)'))
sup(('CustomExceptionHandler.uncaughtException(Thread,Throwable,String)', 'CustomExceptionHandler.uncaughtException(Thread,Throwable,String,String)'))
sup(('CustomExceptionHandler.uncaughtException(Thread,Throwable,String,String)', 'CustomExceptionHandler.saveReportToFile'))
sup(('CustomExceptionHandler.uncaughtException(Thread,Throwable,String,String)', 'CustomExceptionHandler.collectInformation'))

# ---- part 053 (2026-10-28)
# AnkiDroid batch 053 (LABEL helper): MetaDB (21 methods) and ReadText (16 methods), package com.ichi2.anki.
# The full row list is in graphs/AnkiDroid/parts/label_053.md.
#
# Route ownership:
# - Automatic CALL edges (static calls into MetaDB and ReadText, and the anonymous-class constructors
#   ReadText$1.<init>, ReadText$2.<init>, ReadText$3.<init>) come from the builder. They are not written here.
# - E1 (S_REVIEWER -> ReadText$1.onSelection, GUI): the source is a page, so the edge is in the part that
#   contains the destination method (this batch).
# - E2 (ReadText.selectTts -> ReadText$2.run, ASYNC): Handler post with a 500 ms delay.
# - E3 (ReadText.initializeTts -> ReadText$3.onInit, FRAMEWORK): the TextToSpeech init callback.
#
# Gates: ENV_TTS (a TTS engine with at least one locale) and STATE_SETTINGS (the tts preference).
# No MISSING GATE is needed in this batch.

# --- Select TTS dialog: Reviewer menu action_select_tts -> AbstractFlashcardViewer.showSelectTtsDialogue -> ReadText.selectTts.
e('S_REVIEWER', 'ReadText$1.onSelection', 'GUI',
  'pick a language in the Select TTS list',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  gui=['pick a language in the Select TTS list'],
  evidence='SRC com/ichi2/anki/ReadText.java:114-131; SRC com/ichi2/anki/AbstractFlashcardViewer.java:2232-2243; SRC com/ichi2/anki/Reviewer.java:213-215, 305-307',
  note='The list is built only when at least one locale is available (ReadText.java:94-99). The select_tts menu item shows only when mSpeakText is set (Reviewer.java:305-307). The MaterialDialog click dispatch is not in fw_src: INFERRED (source not read).')

# --- Dialog show after a 500 ms delay (posted in ReadText.selectTts).
e('ReadText.selectTts', 'ReadText$2.run', 'ASYNC',
  'the Select TTS dialog is shown after a 500 ms delay',
  env=None,
  evidence='SRC com/ichi2/anki/ReadText.java:134-141; FW-SRC core/java/android/os/Handler.java:427-428, 97-99, 789-791',
  note='The Runnable calls builder.build().show() (ReadText.java:139). The dispatch to run is the Handler route in fw_src.')

# --- TTS engine init callback (created in ReadText.initializeTts, called from AbstractFlashcardViewer.onCollectionLoaded).
e('ReadText.initializeTts', 'ReadText$3.onInit', 'FRAMEWORK',
  'the TTS engine reports that its initialization has finished',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/ReadText.java:174-178, 180-196; the TextToSpeech init dispatch is not in fw_src (source not read)',
  note='initializeTts runs only when mSpeakText is set (AbstractFlashcardViewer.java:904-905). The engine calls onInit with a status; SUCCESS and at least one locale lead to ttsInitialized. The engine callback is INFERRED.')

# --- UNREACHABLE entries (7): no caller found in the app source.
UNREACHABLE['MetaDB.<init>'] = ('no_trigger_in_app',
  'MetaDB declares only static members and no constructor; nothing in the app source creates an instance (no "new MetaDB"), and every use is a static call.',
  'SRC com/ichi2/anki/MetaDB.java:25; grep for "new MetaDB" over src/main/java/com/ichi2 finds nothing',
  'SOURCE')

UNREACHABLE['MetaDB.getLookupDictionary'] = ('no_trigger_in_app',
  'public static getLookupDictionary has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:340-341; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['MetaDB.stripQuotes'] = ('no_trigger_in_app',
  'private helper stripQuotes has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:41, 48-52; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['MetaDB.resetDB'] = ('no_trigger_in_app',
  'public static resetDB has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:135-137; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['MetaDB.resetDeckLanguages'] = ('no_trigger_in_app',
  'public static resetDeckLanguages has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:266-268; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['MetaDB.storeLookupDictionary'] = ('no_trigger_in_app',
  'public static storeLookupDictionary has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:366-368; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['ReadText.<init>'] = ('no_trigger_in_app',
  'ReadText has only static members and no explicit constructor; the grep for "new ReadText" finds nothing, and every use is a static call.',
  'SRC com/ichi2/anki/ReadText.java:37; grep for "new ReadText" over src/main/java/com/ichi2 finds nothing',
  'SOURCE')

# ---- part 057 (2026-10-28)
# AnkiDroid batch 057 (LABEL helper). AudioView (31 methods) and BeolingusParser (4 methods): 35 methods.
# The full row list is in graphs/AnkiDroid/parts/label_057.md.
#
# Route ownership:
# - Automatic CALL edges (constructors and field-initializer listeners, the notify* fan-out, the recorder route from
#   BasicAudioFieldController.createUI, the processPostFinished calls into BeolingusParser, and the in-class calls such as
#   RecordButton$1.onClick -> notifyStopRecord) come from auto_calls.json. They are not written here.
# - GUI edges from the page S_MULTIMEDIA_EDIT_FIELD to the play, record and stop listeners (the destinations are in this batch).
# - FRAMEWORK edge from the IDLE play branch to the completion listener (MediaPlayer dispatch, MediaPlayer.java:3235-3240).
#
# Gates: ENV_PERM_RECORD (RECORD_AUDIO granted: the audio view and its buttons exist only then).
# MG512: a playable recording must exist in the audio field before the completion dispatch can run.

e('S_MULTIMEDIA_EDIT_FIELD', 'AudioView$PlayPauseButton$1.onClick', 'GUI',
  'tap the play button of an audio field in the multimedia field editor',
  env=ENV_PERM_RECORD,
  gui=['tap the play button of an audio field in the multimedia field editor'],
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:213-216, 290; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:128-133; FW-SRC core/java/android/view/View.java:6289-6294',
  note='The play listener is set in PlayPauseButton.<init> (AudioView.java:290). The audio view and its buttons are created only when RECORD_AUDIO is granted (MultimediaEditFieldActivity.java:128-133). Dispatch is View.performClick (View.java:6289-6294).')

e('S_MULTIMEDIA_EDIT_FIELD', 'AudioView$RecordButton$1.onClick', 'GUI',
  'tap the record button of an audio field in the multimedia field editor',
  env=ENV_PERM_RECORD,
  gui=['tap the record button of an audio field in the multimedia field editor'],
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:357-362, 437; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:128-133; FW-SRC core/java/android/view/View.java:6289-6294',
  note='The record listener is set in RecordButton.<init> (AudioView.java:437). The recorder view is created only when RECORD_AUDIO is granted (MultimediaEditFieldActivity.java:128-133). Dispatch is View.performClick (View.java:6289-6294).')

e('S_MULTIMEDIA_EDIT_FIELD', 'AudioView$StopButton$1.onClick', 'GUI',
  'tap the stop button of an audio field in the multimedia field editor',
  env=ENV_PERM_RECORD,
  gui=['tap the stop button of an audio field in the multimedia field editor'],
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:316-317, 338; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:128-133; FW-SRC core/java/android/view/View.java:6289-6294',
  note='The stop listener is set in StopButton.<init> (AudioView.java:338). The audio view and its buttons are created only when RECORD_AUDIO is granted (MultimediaEditFieldActivity.java:128-133). The action runs only in PAUSED or PLAYING (AudioView.java:316-323).')

e('AudioView$PlayPauseButton$1.onClick', 'AudioView$PlayPauseButton$1$1.onCompletion', 'FRAMEWORK',
  'MediaPlayer finishes playing the audio field recording and dispatches the completion listener',
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:224-226; FW-SRC media/java/android/media/MediaPlayer.java:3235-3240',
  note='MISSING GATE MG512: a playable recording must exist in the audio field before play is tapped, so that playback runs to the end. No predefined STATE or ENV kind covers a recorded file. The completion listener is set in the IDLE play branch (AudioView.java:226). The dispatch is MediaPlayer.java:3235-3240 (MEDIA_PLAYBACK_COMPLETE). env and needs_state unset.')

UNREACHABLE['AudioView.createPlayerInstance'] = ('no_trigger_in_app', 'No call site in src/main. grep for createPlayerInstance over src/main (java and res) finds only the definition at AudioView.java:79. The constructor it calls stays reachable through AudioView.java:125.', 'com/ichi2/anki/multimediacard/AudioView.java:79-82', 'SOURCE')

UNREACHABLE['AudioView.setRecordButtonVisible'] = ('no_trigger_in_app', 'No call site in src/main. grep for setRecordButtonVisible over src/main (java and res) finds only the definition at AudioView.java:141.', 'com/ichi2/anki/multimediacard/AudioView.java:141-147', 'SOURCE')

UNREACHABLE['BeolingusParser.<init>'] = ('no_trigger_in_app', 'The class has only static methods and no explicit constructor. No new BeolingusParser exists in src/main: grep finds the class declaration (BeolingusParser.java:25) and only the static calls at LoadPronounciationActivity.java:288 and 323.', 'com/ichi2/anki/multimediacard/beolingus/parsing/BeolingusParser.java:25, 132; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:288, 323', 'SOURCE')

# ---- part 055 (2026-10-28)
# AnkiDroid batch 055 (LABEL helper). AddContentApi (client API class in the api module): 39 methods. The full row list is
# in graphs/AnkiDroid/parts/label_055.md. Source: api/src/main/java/com/ichi2/anki/api/AddContentApi.java, cited relative to
# final_java_only/AnkiDroid/app/AnkiDroid-#4200/. The api module is outside the c1_check roots (AnkiDroid/src/main, fw_src),
# so every api/ cite is reported as file not found by the checker.
#
# Route ownership:
# - The 24 public methods and AddContentApi.<clinit> are the client API. A caller app (its own code, S_ENTRY) runs them in
#   its own process. The 25 ENTRY edges from S_ENTRY are written here. Methods that call the ContentResolver use
#   ENV_PROVIDER_CALL. <init>, <clinit>, getAnkiDroidPackageName and getApiHostSpecVersion use env unset and MG492.
# - Private helpers, getCompat and the Compat objects are reached by CALL edges that auto_calls.json holds. They are not
#   written here.
# - Configuration: getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() < 2. The manifest declares provider
#   spec 2 (AndroidManifest.xml:329), so CompatV2 runs. CompatV2 overrides queryNotes, insertNotes and findDuplicateNotes
#   without calling super, so the three CompatV1 bodies never run on the installed configuration.
# - CompatV1.<init> is reachable: CompatV2 extends CompatV1 (line 687), so new CompatV2() runs the CompatV1 constructor
#   through the implicit super() call.
# - Auto CALL edges from CompatV2 instance methods to AddContentApi.<clinit> (auto_calls.json, lines 690, 698, 717) are
#   suppression candidates. The outer class is already initialised when an inner instance exists. No sup() is written here.
#
# Gates: MG492 only (batch range MG492-MG501).

# --- Client API: public methods, called from the caller app (S_ENTRY). ENV_PROVIDER_CALL where ContentResolver is used.

e('S_ENTRY', 'AddContentApi.<init>', 'ENTRY',
  'the caller app code constructs the client (new AddContentApi(context)) in its own process',
  env=None,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:67-70',
  note='MISSING GATE MG492: the caller app code is outside AnkiDroid, so no predefined ENV kind covers it. env unset. The constructor only reads the application context and its ContentResolver (lines 68-69), no provider call.')

e('S_ENTRY', 'AddContentApi.<clinit>', 'ENTRY',
  'the caller app code first uses AddContentApi, so the class is initialised in the caller process',
  env=None,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:58-65',
  note='MISSING GATE MG492: same caller as <init>. PROJECTION (line 65) is a non-constant array, so the static initializer exists. env unset.')

e('S_ENTRY', 'AddContentApi.addNewBasic2Model', 'ENTRY',
  'another app calls addNewBasic2Model (new Basic2 note type)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:311-314',
  note='Calls addNewCustomModel (line 312). The provider writes are in addNewCustomModel (insert at 343, update at 356).')

e('S_ENTRY', 'AddContentApi.addNewBasicModel', 'ENTRY',
  'another app calls addNewBasicModel (new Basic note type)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:299-302',
  note='Calls addNewCustomModel (line 300). The provider writes are in addNewCustomModel.')

e('S_ENTRY', 'AddContentApi.addNewCustomModel', 'ENTRY',
  'another app calls addNewCustomModel (new note type with its fields and templates)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:329-359',
  note='ContentResolver.insert on Model.CONTENT_URI (line 343) and update of each template (line 356).')

e('S_ENTRY', 'AddContentApi.addNewDeck', 'ENTRY',
  'another app calls addNewDeck (new deck)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:466-476',
  note='ContentResolver.insert on Deck.CONTENT_ALL_URI (line 470).')

e('S_ENTRY', 'AddContentApi.addNote', 'ENTRY',
  'another app calls addNote (one new note with fields and tags)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:81-87',
  note='Calls addNoteInternal (line 82). Provider insert at line 100 and cards query and update at lines 106 and 116.')

e('S_ENTRY', 'AddContentApi.addNotes', 'ENTRY',
  'another app calls addNotes (bulk add of notes into one deck)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:133-152',
  note='An empty list returns 0 (line 149). Otherwise getCompat().insertNotes (line 151); on the live spec-2 branch that is CompatV2.insertNotes (bulkInsert, line 698).')

e('S_ENTRY', 'AddContentApi.findDuplicateNotes(long,String)', 'ENTRY',
  'another app calls findDuplicateNotes for one key',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:161-167',
  note='Calls getCompat().findDuplicateNotes (line 162). On the live spec-2 branch that is CompatV2.findDuplicateNotes.')

e('S_ENTRY', 'AddContentApi.findDuplicateNotes(long,List)', 'ENTRY',
  'another app calls findDuplicateNotes for a list of keys',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:176-178',
  note='Calls getCompat().findDuplicateNotes (line 177). On the live spec-2 branch that is CompatV2.findDuplicateNotes.')

e('S_ENTRY', 'AddContentApi.getAnkiDroidPackageName', 'ENTRY',
  'the caller app code calls the static getAnkiDroidPackageName(context)',
  env=None,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:547-555',
  note='MISSING GATE MG492: same caller as <init>. env unset. Uses PackageManager.resolveContentProvider (line 549), no ContentResolver call. Returns null when AnkiDroid is not installed (lines 550-553).')

e('S_ENTRY', 'AddContentApi.getApiHostSpecVersion', 'ENTRY',
  'the caller app code calls getApiHostSpecVersion',
  env=None,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:571-583; AndroidManifest.xml:329',
  note='MISSING GATE MG492: same caller as <init>. env unset. Reads the provider spec meta-data via PackageManager (lines 574-579), no ContentResolver call. Also called by getCompat (line 594).')

e('S_ENTRY', 'AddContentApi.getCurrentModelId', 'ENTRY',
  'another app calls getCurrentModelId',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:365-380',
  note='ContentResolver.query on Model.CONTENT_URI (line 368).')

e('S_ENTRY', 'AddContentApi.getDeckList', 'ENTRY',
  'another app calls getDeckList',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:502-519',
  note='ContentResolver.query on Deck.CONTENT_ALL_URI (line 504).')

e('S_ENTRY', 'AddContentApi.getDeckName', 'ENTRY',
  'another app calls getDeckName for one deck id',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:527-537',
  note='Calls getDeckList() (line 528).')

e('S_ENTRY', 'AddContentApi.getFieldList', 'ENTRY',
  'another app calls getFieldList for one note type',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:388-405',
  note='ContentResolver.query on the model URI (line 391).')

e('S_ENTRY', 'AddContentApi.getModelList()', 'ENTRY',
  'another app calls getModelList()',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:411-413',
  note='Calls getModelList(1) (line 412). Provider query in getModelList(int) at line 422.')

e('S_ENTRY', 'AddContentApi.getModelList(int)', 'ENTRY',
  'another app calls getModelList with a minimum field count',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:420-442',
  note='ContentResolver.query on Model.CONTENT_URI (line 422).')

e('S_ENTRY', 'AddContentApi.getModelName', 'ENTRY',
  'another app calls getModelName for one note type id',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:449-459',
  note='Calls getModelList() (line 451).')

e('S_ENTRY', 'AddContentApi.getNote', 'ENTRY',
  'another app calls getNote for one note id',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:224-238',
  note='ContentResolver.query on the note URI (line 226).')

e('S_ENTRY', 'AddContentApi.getNoteCount', 'ENTRY',
  'another app calls getNoteCount for one note type',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:185-195',
  note='Calls getCompat().queryNotes (line 186). On the live spec-2 branch that is CompatV2.queryNotes.')

e('S_ENTRY', 'AddContentApi.getSelectedDeckName', 'ENTRY',
  'another app calls getSelectedDeckName',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:482-496',
  note='ContentResolver.query on Deck.CONTENT_SELECTED_URI (line 483).')

e('S_ENTRY', 'AddContentApi.previewNewNote', 'ENTRY',
  'another app calls previewNewNote (card HTML for a field list, then the temporary note is deleted)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:262-292',
  note='The guard at line 263 is false on API 27, so the SecurityException is not thrown. Calls addNoteInternal (line 267), query (271) and delete (290).')

e('S_ENTRY', 'AddContentApi.updateNoteFields', 'ENTRY',
  'another app calls updateNoteFields for one note',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:215-217',
  note='Calls updateNote (line 216), which calls ContentResolver.update (line 250).')

e('S_ENTRY', 'AddContentApi.updateNoteTags', 'ENTRY',
  'another app calls updateNoteTags for one note',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:204-206',
  note='Calls updateNote (line 205), which calls ContentResolver.update (line 250).')

# --- UNREACHABLE entries (configuration and API level).

UNREACHABLE['AddContentApi$CompatV1.queryNotes'] = ('closed_by_configuration',
  'Overridden by CompatV2.queryNotes (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:689-692). getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() is below 2. On an installed AnkiDroid the manifest declares provider spec 2 (AndroidManifest.xml:329), so CompatV2 is chosen. The value -1 (lines 575-576) appears only when AnkiDroid is not installed, and then no provider call here can succeed. CompatV2 does not call super, so this body never runs on the installed configuration.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:623-631, 594; AndroidManifest.xml:329',
  'SOURCE')

UNREACHABLE['AddContentApi$CompatV1.insertNotes'] = ('closed_by_configuration',
  'Overridden by CompatV2.insertNotes (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:695-699). getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() is below 2. The manifest declares provider spec 2 (AndroidManifest.xml:329), so CompatV2 is chosen on the installed configuration. The value -1 (lines 575-576) appears only when AnkiDroid is not installed, and then no provider call here can succeed. CompatV2 does not call super, so this body never runs on the installed configuration.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:633-643, 594; AndroidManifest.xml:329',
  'SOURCE')

UNREACHABLE['AddContentApi$CompatV1.findDuplicateNotes'] = ('closed_by_configuration',
  'Overridden by CompatV2.findDuplicateNotes (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:702-741). getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() is below 2. The manifest declares provider spec 2 (AndroidManifest.xml:329), so CompatV2 is chosen on the installed configuration. The value -1 (lines 575-576) appears only when AnkiDroid is not installed, and then no provider call here can succeed. CompatV2 does not call super, so this body never runs on the installed configuration.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:645-671, 594; AndroidManifest.xml:329',
  'SOURCE')

UNREACHABLE['AddContentApi.hasReadWritePermission'] = ('closed_by_api_level',
  'The only caller is previewNewNote (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:263). The guard SDK_INT < Build.VERSION_CODES.M && !hasReadWritePermission() short-circuits on API 27, where SDK_INT (27) is not below M (23), so the call never runs. minSdkVersion is 10 (AnkiDroid/build.gradle:12), so the call is reachable only on API 10 to 22.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:263, 585-588',
  'SOURCE')

# ---- sup for part 055
sup(('AddContentApi.addNotes', 'AddContentApi$CompatV1.insertNotes'))
sup(('AddContentApi.findDuplicateNotes(long,String)', 'AddContentApi$CompatV1.findDuplicateNotes'))
sup(('AddContentApi.findDuplicateNotes(long,List)', 'AddContentApi$CompatV1.findDuplicateNotes'))
sup(('AddContentApi.getNoteCount', 'AddContentApi$CompatV1.queryNotes'))
sup(('AddContentApi.previewNewNote', 'AddContentApi.hasReadWritePermission'))

# ---- part 054 (2026-10-28)
e('S_REVIEWER', 'Whiteboard.onDraw', 'FRAMEWORK', 'Review screen shows the whiteboard overlay and the view system draws it', env=None, needs_state=STATE_SETTINGS, evidence='SRC com/ichi2/anki/Whiteboard.java:98-103; SRC com/ichi2/anki/Reviewer.java:453-459, 476-483; FW-SRC fw_src/android-8.1.0_r1/core/java/android/view/View.java:19161-19192', note='Reviewer adds the whiteboard view (Reviewer.java:459) and shows it through setWhiteboardVisibility (476-483); View.draw calls onDraw (View.java:19192, 19308). Gate: whiteboard enabled for the deck (STATE_SETTINGS).')

UNREACHABLE['UIUtils.<init>'] = ('no_trigger_in_app', 'UIUtils declares no constructor, nothing instantiates or subclasses it, and all of its members are static', 'com/ichi2/anki/UIUtils.java:20', 'SOURCE')

UNREACHABLE['UIUtils$1.onCancelled'] = ('no_trigger_in_app', 'The SAVE_COLLECTION task is never cancelled: cancelTask(int) is only called with SEARCH_CARDS or RENDER_BROWSER_QA', 'com/ichi2/anki/UIUtils.java:134-135; com/ichi2/async/DeckTask.java:168-172, 181-184, 368-370; com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155', 'SOURCE')

UNREACHABLE['UIUtils$1.onProgressUpdate'] = ('no_trigger_in_app', 'Only the SAVE_COLLECTION task reaches this listener, and its body calls col.save() without publishProgress', 'com/ichi2/anki/UIUtils.java:129-130; com/ichi2/async/DeckTask.java:237-238, 352-355, 494-504', 'SOURCE')

# ---- sup for part 054
sup(('DeckTask.onCancelled', 'UIUtils$1.onCancelled'))
sup(('DeckTask$TaskListener.onProgressUpdate', 'UIUtils$1.onProgressUpdate'))
sup(('DeckTask$TaskListener.onProgressUpdate@UIUtils$1', 'UIUtils$1.onProgressUpdate'))

# ---- part 059 (2026-10-28)
# AnkiDroid batch 059 (LABEL helper). BasicImageFieldController (com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java)
# with its click listeners $1 and $2: 15 methods, all REACHABLE (no UNREACHABLE entries). The full row list is in
# graphs/AnkiDroid/parts/label_059.md.
#
# Route ownership:
# - The automatic CALL edges (BasicControllerFactory -> <init>, createUI -> $1/$2 <init>, recreateEditingUi -> createUI,
#   onActivityResult -> rotateAndCompress and setPreviewImage, the activity -> controller calls) come from auto_calls.json.
#   They are not written here.
# - The page edges into the listeners ($1.onClick, $2.onClick) are written here, because the destination is in this batch.
# - The RESULT edges from the two listeners into MultimediaEditFieldActivity.onActivityResult are written here, because the
#   source (the listener that starts the activity) is in this batch.
#
# Gates: MG532 (picker app returns a result), MG533 (camera app returns a result). Predefined constant used: ENV_STORAGE
# (the camera temp file is written to the public Pictures folder). Page node: S_MULTIMEDIA_EDIT_FIELD.

# --- REGISTER: the listeners are set on the two buttons in createUI (BasicImageFieldController.java:98-110).
e('BasicImageFieldController$1.<init>', 'BasicImageFieldController$1.onClick', 'REGISTER',
  'the gallery click listener is set on mBtnGallery',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:98-106',
  note='The builder does not follow REGISTER for reachability; the route is the S_MULTIMEDIA_EDIT_FIELD -> BasicImageFieldController$1.onClick edge below.')

e('BasicImageFieldController$2.<init>', 'BasicImageFieldController$2.onClick', 'REGISTER',
  'the camera click listener is set on mBtnCamera',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:108-110',
  note='The builder does not follow REGISTER for reachability; the route is the S_MULTIMEDIA_EDIT_FIELD -> BasicImageFieldController$2.onClick edge below.')

# --- GUI: the user taps the buttons of the image field editor (page node).
e('S_MULTIMEDIA_EDIT_FIELD', 'BasicImageFieldController$1.onClick', 'GUI',
  'tap the gallery button under the image preview of the image field editor',
  env=None,
  gui=['tap the gallery button under the image preview of the image field editor'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:98-106',
  note='Page edge; the destination is in this batch, so this part writes it. No state gate: the editor needs no data state. The page edges of the activity menu are in label_048.py.')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicImageFieldController$2.onClick', 'GUI',
  'tap the camera button under the gallery button of the image field editor (not on a Chromebook)',
  env=None,
  gui=['tap the camera button under the gallery button of the image field editor (not on a Chromebook)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:108-134',
  note='Page edge; the destination is in this batch. The button is hidden only on a Chromebook (BasicImageFieldController.java:131-134); the standard configuration is not one. No state gate.')

# --- RESULT: the listeners start an activity for a result; it returns to MultimediaEditFieldActivity.onActivityResult
#     (activity line 312-319), which forwards to the controller. The framework dispatch is FW-SRC Activity.java:7259-7266.
e('BasicImageFieldController$1.onClick', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'the picker app returns the selected image (ACTION_PICK, request ACTIVITY_SELECT_IMAGE)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:103-104, 156-166; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:312-319; FW-SRC core/java/android/app/Activity.java:7259-7266',
  note='MISSING GATE MG532: a picker app must be installed and return a result. No ENV or STATE kind covers another app returning a result. env and needs_state unset. The activity forwards the result to the controller (MultimediaEditFieldActivity.java:315).')

e('BasicImageFieldController$2.onClick', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'the camera app returns after the photo is taken (ACTION_IMAGE_CAPTURE, request ACTIVITY_TAKE_PICTURE)',
  env=ENV_STORAGE,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:117-125, 158; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:312-319; FW-SRC core/java/android/app/Activity.java:7259-7266',
  note='ENV_STORAGE: the temp file is created in the public Pictures folder (BasicImageFieldController.java:119-120); an IOException stops the launch (lines 126-128). MISSING GATE MG533: a camera app must be installed and return a result other than RESULT_CANCELED (line 158). No ENV or STATE kind covers another app returning a result, so that part is not set here. needs_state unset.')

# ---- part 056 (2026-10-28)
# AnkiDroid batch 056 (LABEL helper). 39 methods, all labelled in graphs/AnkiDroid/parts/label_056.md:
# 28 REACHABLE (rows only, no entry here) and 11 UNREACHABLE (entries below), plus 1 e() edge.
# The 21 api library methods (com.ichi2.anki.api, source under the api root, outside the app source root) are 18 REACHABLE
# and 3 UNREACHABLE. The 6 AnkiDroidCrashReportDialog methods are closed_by_configuration (confirmed_by INFERRED).
#
# Route ownership:
# - The 18 REACHABLE api methods are reached from S_ENTRY through public AddContentApi methods (ENTRY edges written in
#   batch 055, parts/label_055.py). Every later step is an auto CALL record in graphs/AnkiDroid/auto_calls.json, so no
#   e() CALL edge is written here for them.
# - Automatic bytecode CALL edges (DialogHandler$1.<init> from DialogHandler.handleMessage, ContextMenuHelper statics from the
#   DeckPickerContextMenu and CustomStudyDialog callers, UnknownHttpResponseException.getResponseCode from Connection) come from
#   auto_calls.json and are not written here.
# - Edges into the REACHABLE methods from other batches (DeckPicker, IntentHandler, AnkiActivity, Connection, Decks,
#   HttpSyncer, RemoteMediaServer) are not written here.
# - One edge is written: the page S_DLG_CONFIRMATION (destination in this batch) into DialogHandler$1.confirm.
# - No MG id is used: the gate is the predefined STATE_SETTINGS constant, or the path is closed by configuration.

e('S_DLG_CONFIRMATION', 'DialogHandler$1.confirm', 'GUI',
  'tap Yes in the force-full-sync dialog (shown only after an upgrade from an older stored version)',
  needs_state=STATE_SETTINGS,
  gui=['tap Yes in the force-full-sync dialog (shown only after an upgrade from an older stored version)'],
  evidence='SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:42-44, 58; com/ichi2/anki/dialogs/DialogHandler.java:88-98; com/ichi2/anki/DeckPicker.java:810, 824, 866-868, 896-897',
  note='ConfirmationDialog.onPositive (lines 42-44) calls the abstract confirm() (line 43). The anonymous override (DialogHandler.java:92-95) calls getCol().modSchemaNoCheck() (line 94); that call edge is the builder automatic edge and is not written here. The dialog is created by MSG_SHOW_FORCE_FULL_SYNC_DIALOG (DialogHandler.java:88-98), which DeckPicker sends at DeckPicker.java:824 only when mRecommendFullSync is set (DeckPicker.java:810). mRecommendFullSync is set only when the stored lastUpgradeVersion is below 20301208 (DeckPicker.java:896-897). A fresh install sets previous = current (DeckPicker.java:866-868), so the flag stays false. STATE_SETTINGS is the stored lastUpgradeVersion preference.')

UNREACHABLE['Basic2Model.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor of Basic2Model (Basic2Model.java:6). No new Basic2Model exists in the api root or the app root (grep over both). AddContentApi uses only the static arrays of Basic2Model (auto_calls.json record AddContentApi.addNewBasic2Model -> Basic2Model.<clinit>, AddContentApi.java:312), so no route from S_ENTRY constructs it.',
  'SRC api/src/main/java/com/ichi2/anki/api/Basic2Model.java:6; api/src/main/java/com/ichi2/anki/api/AddContentApi.java:312', 'SOURCE')

UNREACHABLE['BasicModel.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor of BasicModel (BasicModel.java:6). No new BasicModel exists in the api root or the app root (grep over both). AddContentApi uses only the static arrays of BasicModel (auto_calls.json record AddContentApi.addNewBasicModel -> BasicModel.<clinit>, AddContentApi.java:300), so no route from S_ENTRY constructs it.',
  'SRC api/src/main/java/com/ichi2/anki/api/BasicModel.java:6; api/src/main/java/com/ichi2/anki/api/AddContentApi.java:300', 'SOURCE')

UNREACHABLE['api.Utils.<init>'] = ('no_trigger_in_app',
  'Implicit constructor of the package-private class Utils (Utils.java:32). The class has only static methods. No new Utils exists in the api root or the app root (grep over both), and no auto_calls.json record targets api.Utils.<init>, so no route from S_ENTRY constructs it.',
  'SRC api/src/main/java/com/ichi2/anki/api/Utils.java:32', 'SOURCE')

UNREACHABLE['StorageAccessException.<init>()'] = ('no_trigger_in_app',
  'No-argument constructor (StorageAccessException.java:6-7). Every new StorageAccessException in the app passes a String (CollectionHelper.java:172, 175, 183), so this constructor has no caller.',
  'SRC com/ichi2/anki/exception/StorageAccessException.java:6-7; com/ichi2/anki/CollectionHelper.java:172, 175, 183', 'SOURCE')

UNREACHABLE['ContextMenuHelper.<init>'] = ('no_trigger_in_app',
  'Implicit constructor (ContextMenuHelper.java:21). The class has only static methods, and no new ContextMenuHelper exists in com/ichi2/anki (grep).',
  'SRC com/ichi2/anki/dialogs/ContextMenuHelper.java:21', 'SOURCE')

UNREACHABLE['AnkiDroidCrashReportDialog.<init>'] = ('closed_by_configuration',
  'Implicit constructor (AnkiDroidCrashReportDialog.java:34). The class is started only by ACRA crash reporting (reportDialogClass, mode DIALOG, AnkiDroidApp.java:54-59). In a debug build AnkiDroidApp.onCreate calls setAcraReportingMode(NEVER) (AnkiDroidApp.java:155-159), which writes acra.disable=true (AnkiDroidApp.java:328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED: it does not start this dialog in the standard debug configuration. The release branch (AnkiDroidApp.java:164-168, default ASK) is outside the standard configuration and is not labeled here.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:34; com/ichi2/anki/AnkiDroidApp.java:54-59, 152, 155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.buildCustomView'] = ('closed_by_configuration',
  'Private (AnkiDroidCrashReportDialog.java:69-84), called from onCreate (line 54). Reached only through the crash-report route, which is closed in the debug build: AnkiDroidApp.java:155-159 sets ACRA to NEVER and acra.disable=true (AnkiDroidApp.java:328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED. The release branch (AnkiDroidApp.java:164-168) is not labeled here.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:54, 69-84; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.onClick'] = ('closed_by_configuration',
  'Dialog button callback (AnkiDroidCrashReportDialog.java:86-105). The dialog is never shown in the standard debug configuration, because ACRA is set to NEVER (AnkiDroidApp.java:155-159, 328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED. The release branch (AnkiDroidApp.java:164-168) is not labeled here.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:86-105; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.onCreate'] = ('closed_by_configuration',
  'Activity onCreate (AnkiDroidCrashReportDialog.java:41-62). The activity is never started in the standard debug configuration, because ACRA is set to NEVER (AnkiDroidApp.java:155-159, 328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED. The release branch (AnkiDroidApp.java:164-168) is not labeled here.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:41-62; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.onDismiss'] = ('closed_by_configuration',
  'Dismiss callback (AnkiDroidCrashReportDialog.java:107-110). Reached only through the crash-report dialog, which is never started in the standard debug configuration because ACRA is set to NEVER (AnkiDroidApp.java:155-159, 328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:107-110; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.onSaveInstanceState'] = ('closed_by_configuration',
  'Activity callback (AnkiDroidCrashReportDialog.java:112-118). Reached only through the crash-report dialog, which is never started in the standard debug configuration because ACRA is set to NEVER (AnkiDroidApp.java:155-159, 328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:112-118; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')

# ---- sup for part 056
sup(('AnkiDroidCrashReportDialog.onCreate', 'AnkiDroidCrashReportDialog.buildCustomView'))

# ---- part 058 (2026-10-28)
# AnkiDroid batch 058 (LABEL helper). Audio field classes: AudioField (18 methods), BasicAudioFieldController
# (6 methods, plus its anonymous listener $1 with 2 methods), BasicControllerFactory (3 methods). 29 methods.
# The full row list is in graphs/AnkiDroid/parts/label_058.md.
#
# Route ownership:
# - Automatic CALL edges (factory to controller, activity to controller, note editor and NoteService to AudioField)
#   come from auto_calls.json. They are not written here.
# - The three GUI edges from the page S_MULTIMEDIA_EDIT_FIELD are owned by this part, because their destinations
#   (the listener and the controller methods) are in this batch.
#
# Gates: the recording and the audio controller need the RECORD_AUDIO permission (ENV_PERM_RECORD). No MG id is
# needed in this batch.
#
# UNREACHABLE entries are for AudioField methods (see label_058.md).

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicAudioFieldController$1.onRecordingFinish', 'GUI',
  'tap the record button, then the stop button, in the audio field editor (the audio view stops the recorder and fires the listener)',
  env=ENV_PERM_RECORD,
  gui=['tap the record button, then the stop button, in the audio field editor (the audio view stops the recorder and fires the listener)'],
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:192-205, 410-412; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:80-87',
  note='The stop button in RECORDING state calls AudioView.notifyStopRecord, which stops the recorder and calls the listener only when a recording is in progress. Recording starts only when RECORD_AUDIO is granted (ENV_PERM_RECORD). The listener sets the temporary audio path and the temporary flag on the field.')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicAudioFieldController.onDone', 'GUI',
  'tap the Done (save) menu item of the field editor while an audio field is shown',
  env=ENV_PERM_RECORD,
  gui=['tap the Done (save) menu item of the field editor while an audio field is shown'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:184-187, 242-244; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:92-95',
  note='The done route calls the controller onDone first. onDone dereferences the audio view, which exists only after createUI, so the route needs RECORD_AUDIO granted (ENV_PERM_RECORD). With the permission denied, onDone throws a NullPointerException (flagged in label_058.md).')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicAudioFieldController.onFocusLost', 'GUI',
  'tap the to-text or to-image menu item of the field editor while an audio field is shown',
  env=ENV_PERM_RECORD,
  gui=['tap the to-text or to-image menu item of the field editor while an audio field is shown'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:153, 155, 163-166, 170-173; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:101-104',
  note='The to-text and to-image items are visible for an audio field (menu lines 153 and 155). The activity calls onFocusLost before the type switch. onFocusLost dereferences the audio view, so the route needs RECORD_AUDIO granted (ENV_PERM_RECORD).')

UNREACHABLE['AudioField.getHtml'] = (
    'no_trigger_in_app',
    'Declared in the field interface only. Grep of the source root for getHtml( finds the declaration and the field overrides, and no caller. Body returns null.',
    'com/ichi2/anki/multimediacard/fields/IField.java:40; com/ichi2/anki/multimediacard/fields/AudioField.java:59-61',
    'SOURCE')

UNREACHABLE['AudioField.getImagePath'] = (
    'branch_never_taken',
    'All interface call sites are inside an IMAGE type branch that an AudioField never takes: the activity done (IMAGE test at line 250), NoteService.importMediaToDirectory (case IMAGE), and the image controller (built only for IMAGE by the factory). Body returns null.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:77-79; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:250-251; com/ichi2/anki/servicelayer/NoteService.java:158-164; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:91, 178; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:41-42',
    'SOURCE')

UNREACHABLE['AudioField.getName'] = (
    'no_trigger_in_app',
    'No caller of the field interface getName in the source root. Grep finds only the declarations (interface, image, audio, text fields) and an unrelated view class. Name is set only on TextField objects. Body returns mName.',
    'com/ichi2/anki/multimediacard/fields/IField.java:81; com/ichi2/anki/multimediacard/fields/AudioField.java:121-123',
    'SOURCE')

UNREACHABLE['AudioField.getText'] = (
    'branch_never_taken',
    'Interface call sites in the text controller are guarded: the loop skips every field whose type is not TEXT before calling getText. The other calls are on the text controller own field, and the factory builds that controller only for TEXT. Body returns null.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:97-99; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:218-241; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:37-39',
    'SOURCE')

UNREACHABLE['AudioField.isModified'] = (
    'branch_never_taken',
    'The only caller is MultimediaEditableNote.setField, inside the same-object guard (getField(index) == field). Every setField caller passes a new object or a deserialized copy, so the guard is never true: the note editor result handler (fields from the intent extras), the popup items (new AudioField, ImageField or TextField), and NoteService.updateMultimediaNoteFromJsonNote (new field per loop). Body returns the modified flag. Judgment call, flagged to the orchestrator.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:53-55; com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:104-113; com/ichi2/anki/NoteEditor.java:1036-1039, 1151-1171; com/ichi2/anki/servicelayer/NoteService.java:77-86',
    'SOURCE')

UNREACHABLE['AudioField.setHtml'] = (
    'no_trigger_in_app',
    'Declared in the field interface only. Grep of the source root finds no call. Body returns false.',
    'com/ichi2/anki/multimediacard/fields/IField.java:43; com/ichi2/anki/multimediacard/fields/AudioField.java:65-67',
    'SOURCE')

UNREACHABLE['AudioField.setImagePath'] = (
    'branch_never_taken',
    'Call sites are the image branch of NoteService.importMediaToDirectory (case IMAGE) and the image controller (built only for IMAGE by the factory). Neither gives an AudioField receiver. Body returns false.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:71-73; com/ichi2/anki/servicelayer/NoteService.java:181-186; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:166-176; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:41-42',
    'SOURCE')

UNREACHABLE['AudioField.setName'] = (
    'no_trigger_in_app',
    'The only setName call on a field in the source root is NoteService.createEmptyNote on a TextField local (uiTextField), so no call dispatches to AudioField. Body sets mName.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:126-129; com/ichi2/anki/servicelayer/NoteService.java:55-56',
    'SOURCE')

UNREACHABLE['AudioField.setText'] = (
    'branch_never_taken',
    'Interface call sites receive only TextField objects: the note editor text popup item (a new TextField), NoteService line 57 (TextField local), and the text controller onDone (TEXT-only controller, factory lines 37-39). Body returns false.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:103-105; com/ichi2/anki/NoteEditor.java:1167-1171; com/ichi2/anki/servicelayer/NoteService.java:55-57; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:340-341; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:37-39',
    'SOURCE')

UNREACHABLE['AudioField.setType'] = (
    'no_trigger_in_app',
    'Declared in the field interface only. Grep of the source root finds no call on a field (the only setType calls are on a card and an intent). Body returns false.',
    'com/ichi2/anki/multimediacard/fields/IField.java:33; com/ichi2/anki/multimediacard/fields/AudioField.java:47-49',
    'SOURCE')

# ---- sup for part 058
sup(('MultimediaEditFieldActivity.done', 'AudioField.getImagePath'))
sup(('BasicImageFieldController.createUI', 'AudioField.getImagePath'))
sup(('BasicImageFieldController.onActivityResult', 'AudioField.getImagePath'))
sup(('NoteService.importMediaToDirectory', 'AudioField.getImagePath'))
sup(('BasicTextFieldController.createUI', 'AudioField.getText'))
sup(('BasicTextFieldController.createCloneButton', 'AudioField.getText'))
sup(('MultimediaEditableNote.setField', 'AudioField.isModified'))
sup(('BasicImageFieldController.onActivityResult', 'AudioField.setImagePath'))
sup(('NoteService.importMediaToDirectory', 'AudioField.setImagePath'))
sup(('NoteEditor$11$1.onMenuItemClick', 'AudioField.setText'))
sup(('BasicTextFieldController.onDone', 'AudioField.setText'))

# ---- part 061 (2026-10-28)
# AnkiDroid batch 061 (LABEL helper). ImageField and TextField: 36 methods. Rows are in graphs/AnkiDroid/parts/label_061.md.
# No e() calls: every route into these methods is an automatic CALL edge from auto_calls.json.
# UNREACHABLE entries only. Each reason is inline (no module-level names).

UNREACHABLE['ImageField.getAudioPath'] = ('branch_never_taken', 'Returns null. Callers run only for AudioField receivers: MultimediaEditFieldActivity.done under getType()==AUDIO (lines 261-267), NoteService.importMediaToDirectory under case AUDIO (line 160), BasicAudioFieldController.createUI (line 52). ImageField.getType() is IMAGE, so the branch is never taken.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:91-93; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:261-267; com/ichi2/anki/servicelayer/NoteService.java:158-160; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:50-53; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:44-45', 'SOURCE')
UNREACHABLE['ImageField.getHtml'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for getHtml( finds only the declaration and the overrides. Nothing reads the HTML of a field.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:59-61; com/ichi2/anki/multimediacard/fields/IField.java:40', 'SOURCE')
UNREACHABLE['ImageField.getName'] = ('no_trigger_in_app', 'No call site on an IField receiver. grep for getName( finds only the definition, the declaration and unrelated calls on File, AnkiFont and Models.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:121-123; com/ichi2/anki/multimediacard/fields/IField.java:81', 'SOURCE')
UNREACHABLE['ImageField.getText'] = ('branch_never_taken', 'Returns null. Callers: BasicTextFieldController.createUI (line 73), where the text controller exists only for TEXT fields (BasicControllerFactory lines 38-39); and createCloneButton (line 241), guarded by getType()!=TEXT then continue (lines 223-225). An ImageField is never TEXT.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:97-99; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:70-74, 218-242; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:38-39', 'SOURCE')
UNREACHABLE['ImageField.isModified'] = ('branch_never_taken', 'The only call is MultimediaEditableNote.setField line 108, which runs only when getField(index) == field (line 107). No setField caller passes a field already stored in the note: NoteEditor lines 1039, 1158, 1164, 1171 and NoteService lines 58, 86 all pass new objects. Judgment call for the orchestrator.', 'com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:104-115; com/ichi2/anki/NoteEditor.java:1036-1039, 1157-1171; com/ichi2/anki/servicelayer/NoteService.java:50-58, 79-86; com/ichi2/anki/multimediacard/fields/ImageField.java:53-55', 'SOURCE')
UNREACHABLE['ImageField.setAudioPath'] = ('branch_never_taken', 'Returns false. Callers: NoteService.importMediaToDirectory line 183 (inside case AUDIO, which an ImageField never reaches because getType() is IMAGE), and BasicAudioFieldController.onRecordingFinish line 84 (AudioField receiver). BasicTextFieldController line 304 uses a separate AudioField.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:85-87; com/ichi2/anki/servicelayer/NoteService.java:181-186; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:82-86; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:303-304', 'SOURCE')
UNREACHABLE['ImageField.setHtml'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for setHtml( finds only the declaration and the overrides.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:65-67; com/ichi2/anki/multimediacard/fields/IField.java:43', 'SOURCE')
UNREACHABLE['ImageField.setName'] = ('no_trigger_in_app', 'No call site on an ImageField receiver. The only setName call on a field is NoteService line 56, on a TextField created at line 55.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:127-129; com/ichi2/anki/servicelayer/NoteService.java:55-56; com/ichi2/anki/multimediacard/fields/IField.java:84', 'SOURCE')
UNREACHABLE['ImageField.setText'] = ('branch_never_taken', 'Returns false. Callers: NoteEditor popup menu (line 1170), where the object is a TextField created at line 1169; and BasicTextFieldController.onDone (line 341), where mField is a TextField from BasicControllerFactory (lines 38-39). The receivers are always TextField.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:103-105; com/ichi2/anki/NoteEditor.java:1167-1172; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:338-342; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:38-39', 'SOURCE')
UNREACHABLE['ImageField.setType'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for setType( finds only the declarations and the overrides, plus unrelated Intent, Card and Sched calls.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:47-49; com/ichi2/anki/multimediacard/fields/IField.java:33', 'SOURCE')
UNREACHABLE['TextField.getAudioPath'] = ('branch_never_taken', 'Returns null. Callers are the same as for ImageField.getAudioPath: MultimediaEditFieldActivity.done (lines 261-267, AUDIO branch), NoteService.importMediaToDirectory (lines 158-160, case AUDIO), and BasicAudioFieldController.createUI (line 52, AudioField receiver). A TextField getType() is TEXT, so none reaches it.', 'com/ichi2/anki/multimediacard/fields/TextField.java:82-84; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:261-267; com/ichi2/anki/servicelayer/NoteService.java:158-160; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:50-53', 'SOURCE')
UNREACHABLE['TextField.getHtml'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for getHtml( finds only the declaration and the overrides.', 'com/ichi2/anki/multimediacard/fields/TextField.java:52-54; com/ichi2/anki/multimediacard/fields/IField.java:40', 'SOURCE')
UNREACHABLE['TextField.getImagePath'] = ('branch_never_taken', 'Returns null. Callers: MultimediaEditFieldActivity.done (line 256) under getType()==IMAGE (lines 250-251); BasicImageFieldController.createUI (line 91) and onActivityResult (line 178), whose receiver is always an ImageField from BasicControllerFactory (lines 41-42); and NoteService.importMediaToDirectory (case IMAGE, line 164). A TextField never reaches any of them.', 'com/ichi2/anki/multimediacard/fields/TextField.java:70-72; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:250-256; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:91, 170-179; com/ichi2/anki/servicelayer/NoteService.java:163-164', 'SOURCE')
UNREACHABLE['TextField.getName'] = ('no_trigger_in_app', 'No call site on an IField receiver. grep for getName( finds only the definition, the declaration and unrelated calls.', 'com/ichi2/anki/multimediacard/fields/TextField.java:114-116; com/ichi2/anki/multimediacard/fields/IField.java:81', 'SOURCE')
UNREACHABLE['TextField.hasTemporaryMedia'] = ('branch_never_taken', 'Returns false. The only call is NoteService.importMediaToDirectory line 177 (cha CALL), inside if (tmpMediaPath != null) (line 171). tmpMediaPath stays null for TEXT: it starts null (line 157) and the TEXT case breaks without assigning it (lines 167-169). So the call never runs for a TextField.', 'com/ichi2/anki/servicelayer/NoteService.java:157-177; com/ichi2/anki/multimediacard/fields/TextField.java:106-110', 'SOURCE')
UNREACHABLE['TextField.isModified'] = ('branch_never_taken', 'The only call is MultimediaEditableNote.setField line 108, which runs only when getField(index) == field (line 107). No setField caller passes a field already stored in the note (see ImageField.isModified). Judgment call for the orchestrator.', 'com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:104-115; com/ichi2/anki/NoteEditor.java:1036-1039, 1157-1171; com/ichi2/anki/servicelayer/NoteService.java:50-58, 79-86; com/ichi2/anki/multimediacard/fields/TextField.java:46-48', 'SOURCE')
UNREACHABLE['TextField.setAudioPath'] = ('branch_never_taken', 'Returns false. Callers: NoteService.importMediaToDirectory line 183 (case AUDIO, inside the tmpMediaPath block that a TEXT field never enters, line 171), and BasicAudioFieldController.onRecordingFinish line 84 (AudioField receiver). BasicTextFieldController line 304 sets the path on a separate AudioField.', 'com/ichi2/anki/multimediacard/fields/TextField.java:76-78; com/ichi2/anki/servicelayer/NoteService.java:171, 181-186; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:82-86; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:303-304', 'SOURCE')
UNREACHABLE['TextField.setHasTemporaryMedia'] = ('branch_never_taken', 'The body is empty. Callers: BasicImageFieldController.onActivityResult line 176 (receiver is an ImageField from BasicControllerFactory lines 41-42) and BasicAudioFieldController.onRecordingFinish line 85 (receiver is an AudioField). BasicTextFieldController line 306 calls it on an AudioField. None passes a TextField.', 'com/ichi2/anki/multimediacard/fields/TextField.java:102-103; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:170-179; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:82-86; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:303-306', 'SOURCE')
UNREACHABLE['TextField.setHtml'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for setHtml( finds only the declaration and the overrides.', 'com/ichi2/anki/multimediacard/fields/TextField.java:58-60; com/ichi2/anki/multimediacard/fields/IField.java:43', 'SOURCE')
UNREACHABLE['TextField.setImagePath'] = ('branch_never_taken', 'Returns false. Callers: BasicImageFieldController.onActivityResult lines 172 and 175 (receiver is always an ImageField from BasicControllerFactory lines 41-42), and NoteService.importMediaToDirectory line 186 (case IMAGE, inside the tmpMediaPath block that a TEXT field never enters, line 171).', 'com/ichi2/anki/multimediacard/fields/TextField.java:64-66; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:170-179; com/ichi2/anki/servicelayer/NoteService.java:171, 181-186', 'SOURCE')
UNREACHABLE['TextField.setType'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for setType( finds only the declarations and the overrides, plus unrelated Intent, Card and Sched calls.', 'com/ichi2/anki/multimediacard/fields/TextField.java:40-42; com/ichi2/anki/multimediacard/fields/IField.java:33', 'SOURCE')

# ---- sup for part 061
sup(('NoteEditor$11$1.onMenuItemClick', 'ImageField.setText'))
sup(('MultimediaEditableNote.setField', 'TextField.isModified'))
sup(('MultimediaEditableNote.setField', 'ImageField.isModified'))
sup(('MultimediaEditFieldActivity.done', 'TextField.getAudioPath'))
sup(('MultimediaEditFieldActivity.done', 'ImageField.getAudioPath'))
sup(('MultimediaEditFieldActivity.done', 'TextField.getImagePath'))
sup(('BasicTextFieldController.createUI', 'ImageField.getText'))
sup(('BasicTextFieldController.createCloneButton', 'ImageField.getText'))
sup(('BasicTextFieldController.onDone', 'ImageField.setText'))
sup(('BasicImageFieldController.createUI', 'TextField.getImagePath'))
sup(('BasicImageFieldController.onActivityResult', 'TextField.getImagePath'))
sup(('BasicImageFieldController.onActivityResult', 'TextField.setHasTemporaryMedia'))
sup(('BasicImageFieldController.onActivityResult', 'TextField.setImagePath'))
sup(('BasicAudioFieldController$1.onRecordingFinish', 'TextField.setHasTemporaryMedia'))
sup(('BasicAudioFieldController$1.onRecordingFinish', 'TextField.setAudioPath'))
sup(('BasicAudioFieldController$1.onRecordingFinish', 'ImageField.setAudioPath'))
sup(('BasicAudioFieldController.createUI', 'TextField.getAudioPath'))
sup(('BasicAudioFieldController.createUI', 'ImageField.getAudioPath'))
sup(('NoteService.importMediaToDirectory', 'TextField.setImagePath'))
sup(('NoteService.importMediaToDirectory', 'TextField.setAudioPath'))
sup(('NoteService.importMediaToDirectory', 'ImageField.setAudioPath'))
sup(('NoteService.importMediaToDirectory', 'TextField.hasTemporaryMedia'))
sup(('NoteService.importMediaToDirectory', 'TextField.getImagePath'))
sup(('NoteService.importMediaToDirectory', 'TextField.getAudioPath'))
sup(('NoteService.importMediaToDirectory', 'ImageField.getAudioPath'))

# ---- part 062 (2026-10-28)
UNREACHABLE['Meaning.setLanguage'] = ('no_trigger_in_app', 'No call site in the source root: setLanguage( calls outside glosbe/json are TTS and AnkiDroidApp methods. Meaning objects are built only by Gson (library, not in dataset: INFERRED); TranslationActivity reads them with getters only.', 'com/ichi2/anki/multimediacard/glosbe/json/Meaning.java:35-37; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:323-333', 'SOURCE')
UNREACHABLE['Meaning.setText'] = ('no_trigger_in_app', 'No call site: the setText( calls at TranslationActivity.java:116, 120, 133 and 152 are on TextView and Button objects (tv, tvFrom, tvTo, btnDone), not on Meaning. Meaning objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Meaning.java:45-47; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:116, 120, 133, 152', 'SOURCE')
UNREACHABLE['Phrase.setLanguage'] = ('no_trigger_in_app', 'No call site in the source root: setLanguage( calls outside glosbe/json are TTS and AnkiDroidApp methods. Phrase objects are built only by Gson (library: INFERRED); TranslationActivity reads them with getters only (lines 339-345).', 'com/ichi2/anki/multimediacard/glosbe/json/Phrase.java:35-37; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:339-345', 'SOURCE')
UNREACHABLE['Phrase.setText'] = ('no_trigger_in_app', 'No call site: the setText( calls at TranslationActivity.java:116, 120, 133 and 152 are on TextView and Button objects, not on Phrase. Phrase objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Phrase.java:45-47; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:116, 120, 133, 152', 'SOURCE')
UNREACHABLE['Response.getDest'] = ('no_trigger_in_app', 'No call site: grep for getDest() finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:36-38; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.getFrom'] = ('no_trigger_in_app', 'No call site: grep for getFrom() finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:46-48; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.getPhrase'] = ('no_trigger_in_app', 'No call site: the only getPhrase() call in the source root is tuc.getPhrase() at TranslationActivity.java:339, which is Tuc.getPhrase. Response.getPhrase returns String and nothing calls it.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:56-58; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:339', 'SOURCE')
UNREACHABLE['Response.setDest'] = ('no_trigger_in_app', 'No call site: grep for setDest( finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:41-43; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.setFrom'] = ('no_trigger_in_app', 'No call site: grep for setFrom( finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:51-53; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.setPhrase'] = ('no_trigger_in_app', 'No call site: grep for setPhrase( finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:61-63; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.setResult'] = ('no_trigger_in_app', 'No call site: the setResult( calls in the source root (for example AbstractFlashcardViewer.java:2600 and MyAccount.java:251) are Activity.setResult, not this method. Response is built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:71-73; com/ichi2/anki/AbstractFlashcardViewer.java:2600; com/ichi2/anki/MyAccount.java:251', 'SOURCE')
UNREACHABLE['Response.setTuc'] = ('no_trigger_in_app', 'No call site: grep for setTuc( finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:81-83; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Tuc.getAuthors'] = ('no_trigger_in_app', 'No call site: grep for getAuthors() finds no caller in the source root outside glosbe/json. Tuc objects are built only by Gson (library: INFERRED) and read at TranslationActivity.java:311-323.', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:34-36; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:311, 323', 'SOURCE')
UNREACHABLE['Tuc.getMeaningId'] = ('no_trigger_in_app', 'No call site: grep for getMeaningId() finds no caller in the source root outside glosbe/json. Tuc objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:44-46; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:311', 'SOURCE')
UNREACHABLE['Tuc.setAuthors'] = ('no_trigger_in_app', 'No call site: grep for setAuthors( finds no caller in the source root outside glosbe/json. Tuc objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:39-41; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:323', 'SOURCE')
UNREACHABLE['Tuc.setMeaningId'] = ('no_trigger_in_app', 'No call site: grep for setMeaningId( finds no caller in the source root outside glosbe/json. Tuc objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:49-51; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:311', 'SOURCE')
UNREACHABLE['Tuc.setMeanings'] = ('no_trigger_in_app', 'No call site: grep for setMeanings( finds no caller in the source root outside glosbe/json. TranslationActivity reads tuc.getMeanings() at line 323 only.', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:59-61; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:323', 'SOURCE')
UNREACHABLE['Tuc.setPhrase'] = ('no_trigger_in_app', 'No call site: grep for setPhrase( finds no caller in the source root outside glosbe/json. TranslationActivity reads tuc.getPhrase() at line 339 only.', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:69-71; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:339', 'SOURCE')

# ---- addendum for part 062 (orchestrator, 2026-10-28): Gson reflection at the fromJson call in showPickTranslationDialog (batch 049 method); batch 062 did not write these edges
e('TranslationActivity.showPickTranslationDialog', 'Response.<init>', 'CALL',
  'parse the Glosbe reply: Gson creates the root Response object (TranslationActivity.java:264)',
  env=None,
  cls='non_standard',
  via='com.google.gson.Gson.fromJson (library, not in the dataset)',
  evidence='INFERRED Gson reflection at TranslationActivity.java:264 (library source not read); SRC com/ichi2/anki/multimediacard/glosbe/json/Response.java:28',
  note='Implicit constructor of a Gson target class. The FAILED check at line 258 returns first, so the route exists only when the reply is not FAILED.')
e('TranslationActivity.showPickTranslationDialog', 'Tuc.<init>', 'CALL',
  'parse the Glosbe reply: Gson creates each Tuc in Response.tuc (TranslationActivity.java:264)',
  env=None,
  cls='non_standard',
  via='com.google.gson.Gson.fromJson (library, not in the dataset)',
  evidence='INFERRED Gson reflection at TranslationActivity.java:264 (library source not read); SRC com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:30-31',
  note='Implicit constructor of a Gson target class, reached through Response.tuc. Same FAILED-check gate as Response.<init>.')
e('TranslationActivity.showPickTranslationDialog', 'Meaning.<init>', 'CALL',
  'parse the Glosbe reply: Gson creates each Meaning in Tuc.meanings (TranslationActivity.java:264)',
  env=None,
  cls='non_standard',
  via='com.google.gson.Gson.fromJson (library, not in the dataset)',
  evidence='INFERRED Gson reflection at TranslationActivity.java:264 (library source not read); SRC com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:30',
  note='Implicit constructor of a Gson target class, reached through Tuc.meanings. Same FAILED-check gate as Response.<init>.')
e('TranslationActivity.showPickTranslationDialog', 'Phrase.<init>', 'CALL',
  'parse the Glosbe reply: Gson creates the Phrase of each Tuc (TranslationActivity.java:264)',
  env=None,
  cls='non_standard',
  via='com.google.gson.Gson.fromJson (library, not in the dataset)',
  evidence='INFERRED Gson reflection at TranslationActivity.java:264 (library source not read); SRC com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:31',
  note='Implicit constructor of a Gson target class, reached through Tuc.phrase. Same FAILED-check gate as Response.<init>.')

# ---- part 060 (2026-10-28)
# AnkiDroid batch 060 (LABEL helper). BasicTextFieldController (text editor of the multimedia field editor) and its
# listeners $1-$4, $3$1, the pick-dialog callback, the translation starters, plus FieldBase and FieldControllerBase.
# The full row list is in graphs/AnkiDroid/parts/label_060.md.
#
# Route ownership:
# - Automatic CALL edges (createUI -> createClearButton and the other create* methods, startTranslation* calls from the
#   dialog listeners, MultimediaEditFieldActivity -> FieldControllerBase setters, onDone, EFieldType.<clinit>) come from
#   auto_calls.json. They are not written here.
# - Edges written here: page edges from S_MULTIMEDIA_EDIT_FIELD and S_DLG_PICK_STRING into the listeners of this batch,
#   the INTENT edges from the say and translate paths, the ENTERS edges into the pick dialog, and the RESULT edge from the
#   ColorDict path (the source is in this batch).
#
# Gates: MG542 (clone button), MG543 (ColorDict installed). No predefined ENV_* or STATE_* constant fits, so env and
# needs_state are unset on the gated edges. Predefined constants used in this part: none.

# --- Text editor buttons (the page S_MULTIMEDIA_EDIT_FIELD is the text editor screen).
e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$1.onClick', 'GUI',
  'tap the clear button under the text box (built by createUI on every text editor)',
  env=None,
  gui=['tap the clear button under the text box (built by createUI on every text editor)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:83, 103-116; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:98, 116-146',
  note='createClearButton is called from createUI (line 83) with no condition. The listener sets the text box to an empty string (line 112).')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$2.onClick', 'GUI',
  'tap the say button (pronounce; built by createUI on every text editor)',
  env=None,
  gui=['tap the say button (pronounce; built by createUI on every text editor)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:93, 123-140',
  note='createPronounceButton is called from createUI (line 93) with no condition. Empty text shows a toast and returns (lines 131-134). Text starts LoadPronounciationActivity (edge below).')

e('BasicTextFieldController$2.onClick', 'LoadPronounciationActivity.<init>', 'INTENT',
  'the say button starts the pronunciation screen with the field text (non-empty text)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:136-138',
  note='Explicit intent to LoadPronounciationActivity with EXTRA_SOURCE, started with startActivityForResult. The network check is inside the child screen (page S_LOAD_PRONOUNCIATION, another batch), so no gate is set here. The RESULT edge S_LOAD_PRONOUNCIATION -> MultimediaEditFieldActivity.onActivityResult is already in graph_def.py.')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$3.onClick', 'GUI',
  'tap the translate button (built by createUI on every text editor)',
  env=None,
  gui=['tap the translate button (built by createUI on every text editor)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:92, 147-150',
  note='createTranslateButton is called from createUI (line 92) with no condition. Empty text shows a toast and returns (lines 156-159). Text with a space shows a warning toast and the flow goes on (lines 161-163).')

e('BasicTextFieldController$3.onClick', 'S_DLG_PICK_STRING', 'ENTERS',
  'non-empty text opens the translation source picker (Glosbe.com, and ColorDict unless a Chromebook)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:166, 168-173, 191; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='The picker is PickStringDialogFragment (page S_DLG_PICK_STRING), shown with the tag pick.translation.source (line 191). The ColorDict choice is listed only when CompatHelper.isChromebook() is false (lines 75-77).')

e('S_DLG_PICK_STRING', 'BasicTextFieldController$3$1.onClick', 'GUI',
  'pick a translation source in the picker (Glosbe.com or ColorDict)',
  env=None,
  gui=['pick a translation source in the picker (Glosbe.com or ColorDict)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:176-187; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='The anonymous listener $3$1 (line 176) calls startTranslationWithGlosbe (line 182) or startTranslationWithColorDict (line 184). Those two calls are automatic CALL edges and are not written here.')

e('BasicTextFieldController.startTranslationWithGlosbe', 'TranslationActivity.<init>', 'INTENT',
  'Glosbe.com chosen in the translation source picker: explicit intent to TranslationActivity with the field text, started for a result',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:393-398',
  note='Explicit component (TranslationActivity.class). The network check is in the child (TranslationActivity.translate, page S_TRANSLATION, another batch), so no gate is set here. The RESULT edge S_TRANSLATION -> MultimediaEditFieldActivity.onActivityResult is already in graph_def.py.')

e('BasicTextFieldController.startTranslationWithColorDict', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'ColorDict chosen and installed: the external picker returns to the editor, which forwards the result to the field controller',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:364-390; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:313-315',
  note='MISSING GATE MG543: ColorDict (an external app with no page node) must be installed. The check is isIntentAvailable (line 385); without the app the toast at line 386 shows and the method returns. No predefined ENV covers an app that AnkiDroid starts (ENV_OTHER_APP_INTENT is for apps that send intents to AnkiDroid). The Chromebook check (lines 75-77) also hides this choice. env and needs_state unset. The request code is REQUEST_CODE_TRANSLATE_COLORDICT (line 389).')

# --- Clone button (exists only when the note has another non-empty text field).
e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$4.onClick', 'GUI',
  'tap the clone button (only when the note has another non-empty text field)',
  env=None,
  gui=['tap the clone button (only when the note has another non-empty text field)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:82, 207-209, 246-256',
  note='MISSING GATE MG542: the clone button is built only when the note has more than one field (line 209) and at least one other non-empty TEXT field that is not this one (lines 216-243; return at 246-248). No predefined STATE or ENV fits (STATE_NOTE only says a note exists). env and needs_state unset. createCloneButton is called from createUI (line 82).')

e('BasicTextFieldController$4.onClick', 'S_DLG_PICK_STRING', 'ENTERS',
  'the clone source picker opens with the other non-empty text fields',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:256-266; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='MISSING GATE MG542 (inherited: the button exists only then). The choices are mPossibleClones (line 262), the listener is the controller (line 263), and the picker is shown with the tag pick.clone (line 266). env and needs_state unset.')

e('S_DLG_PICK_STRING', 'BasicTextFieldController.onClick', 'GUI',
  'pick a clone source: the field text is replaced with the chosen text',
  env=None,
  gui=['pick a clone source: the field text is replaced with the chosen text'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:263, 345-349; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='MISSING GATE MG542 (inherited from the clone button). The controller is the listener (line 263). onClick sets the text box to mPossibleClones[which] (line 348). env and needs_state unset.')

# --- UNREACHABLE: the identity guard in MultimediaEditableNote.setField is never true for a field the app passes in.
UNREACHABLE['FieldBase.getThisModified'] = (
    'branch_never_taken',
    'Only callers are the isModified methods of TextField, ImageField and AudioField. The one app call of isModified on a field is '
    'MultimediaEditableNote.setField line 108, which runs only inside the branch where the field passed in is the same object as the '
    'one already stored (line 107). Every app call of setField passes a newly created field or a field from the activity result '
    'extras (NoteEditor lines 1036-1039, NoteService lines 79-86, NoteFactory lines 19-33, NoteEditor lines 1157-1171). '
    'So the identity never holds, line 108 never runs, and getThisModified is never called.',
    'com/ichi2/anki/multimediacard/fields/FieldBase.java:36-38; com/ichi2/anki/multimediacard/fields/TextField.java:46-48; '
    'com/ichi2/anki/multimediacard/fields/ImageField.java:53-55; com/ichi2/anki/multimediacard/fields/AudioField.java:53-55; '
    'com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:104-113; com/ichi2/anki/NoteEditor.java:1034-1039, 1157-1158, '
    '1163-1164, 1169-1171; com/ichi2/anki/servicelayer/NoteService.java:79-86; com/ichi2/anki/multimediacard/impl/NoteFactory.java:19-33',
    'SOURCE')

# ---- sup for part 060
sup(('TextField.isModified', 'FieldBase.getThisModified'))
sup(('ImageField.isModified', 'FieldBase.getThisModified'))
sup(('AudioField.isModified', 'FieldBase.getThisModified'))

# ---- part 063 (2026-10-28)
# AnkiDroid batch 063 (LABEL helper). 34 methods: MultimediaEditableNote (11), NoteFactory (2), LanguageListerBase with $1 (6),
# LanguageListerBeolingus (1), LanguagesLister with $1 (5), LanguagesListerGlosbe (3), MockNoteFactory (2),
# MockPronounciationPageFetcher (2), MockTranslationFetcher (2). The full row list is in graphs/AnkiDroid/parts/label_063.md.
#
# Route ownership: the automatic CALL edges (auto_calls.json) into and out of these methods are not written here.
# Edges written here: the two Collections.sort -> Comparator.compare edges, whose source method is in this batch.
# The routes into the language listers and the mocks start from activities and buttons in other batches (NoteEditor,
# BasicTextFieldController, LoadPronounciationActivity, TranslationActivity).

e('LanguageListerBase.getLanguages', 'LanguageListerBase$1.compare', 'FRAMEWORK',
  'Collections.sort calls the anonymous Comparator to order the language names',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/language/LanguageListerBase.java:61-69',
  note='java.util.Collections is not in fw_src (no Collections.java under fw_src/android-8.1.0_r1): INFERRED (source not read). No gate: the sort calls compare for any list with at least two names, and both listers add more than two (com/ichi2/anki/multimediacard/language/LanguageListerBeolingus.java:36-38 adds three, com/ichi2/anki/multimediacard/language/LanguagesListerGlosbe.java:37-45 lists 19 codes). The automatic CALL into LanguageListerBase$1.<init> is not repeated here.')

UNREACHABLE['MultimediaEditableNote.circularSwap'] = ('no_trigger_in_app',
  'No call site in the app. The grep over the app source folder finds only the interface declaration and the implementation.',
  'SRC com/ichi2/anki/multimediacard/IMultimediaEditableNote.java:43; com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:41-56',
  'SOURCE')

UNREACHABLE['MultimediaEditableNote.getModelId'] = ('no_trigger_in_app',
  'The only call is in NoteService.updateJsonNoteFromMultimediaNote, and that method has no caller in the app (the grep finds only its declaration), so no route reaches getModelId.',
  'SRC com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:128-130; com/ichi2/anki/servicelayer/NoteService.java:101-104',
  'SOURCE')

UNREACHABLE['MultimediaEditableNote.isModified'] = ('no_trigger_in_app',
  'Implements IMultimediaEditableNote.isModified, but no code calls it on a note. Every isModified() call in the app is on an IField object, and the one in setField dispatches to the field class, not to this method.',
  'SRC com/ichi2/anki/multimediacard/IMultimediaEditableNote.java:40; com/ichi2/anki/multimediacard/fields/IField.java:36; com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:64-67, 104-109',
  'SOURCE')

UNREACHABLE['NoteFactory.<init>'] = ('no_trigger_in_app',
  'NoteFactory declares no constructor and is never instantiated. Its only member createNote is static and has no caller (the grep finds the class declaration only).',
  'SRC com/ichi2/anki/multimediacard/impl/NoteFactory.java:14-15',
  'SOURCE')

UNREACHABLE['NoteFactory.createNote'] = ('no_trigger_in_app',
  'No call site in the app. The grep over the app source folder finds no reference to NoteFactory or createNote.',
  'SRC com/ichi2/anki/multimediacard/impl/NoteFactory.java:15-36',
  'SOURCE')

UNREACHABLE['LanguagesLister.<init>'] = ('no_trigger_in_app',
  'No new LanguagesLister exists anywhere in the app. The class name occurs only in its own file (grep over the app source folder).',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:27-31',
  'SOURCE')

UNREACHABLE['LanguagesLister.getCodeFor'] = ('no_trigger_in_app',
  'The class is never instantiated (see LanguagesLister.<init>), and it does not extend LanguageListerBase, so no base-type call reaches this method.',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:27, 45-51',
  'SOURCE')

UNREACHABLE['LanguagesLister.getLanguages'] = ('no_trigger_in_app',
  'The class is never instantiated (see LanguagesLister.<init>), and it does not extend LanguageListerBase, so no base-type call reaches this method.',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:27, 54-64',
  'SOURCE')

UNREACHABLE['LanguagesLister$1.<init>'] = ('no_trigger_in_app',
  'The anonymous Comparator is created only in LanguagesLister.getLanguages, which has no route.',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:54-62',
  'SOURCE')

UNREACHABLE['LanguagesLister$1.compare'] = ('no_trigger_in_app',
  'Called only by Collections.sort inside LanguagesLister.getLanguages, which has no route.',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:54-62',
  'SOURCE')

UNREACHABLE['MockNoteFactory.<init>'] = ('no_trigger_in_app',
  'MockNoteFactory is a test helper with no constructor. No code creates an instance (the grep finds the class declaration only).',
  'SRC com/ichi2/anki/multimediacard/test/MockNoteFactory.java:27-30',
  'SOURCE')

UNREACHABLE['MockNoteFactory.makeNote'] = ('no_trigger_in_app',
  'No call site in the app. The grep over the app source folder finds only the class declaration.',
  'SRC com/ichi2/anki/multimediacard/test/MockNoteFactory.java:30-52',
  'SOURCE')

UNREACHABLE['MockPronounciationPageFetcher.<init>'] = ('no_trigger_in_app',
  'Test helper with no constructor. No code creates an instance.',
  'SRC com/ichi2/anki/multimediacard/test/MockPronounciationPageFetcher.java:22-25',
  'SOURCE')

UNREACHABLE['MockPronounciationPageFetcher.get'] = ('no_trigger_in_app',
  'The only reference is a commented-out call in LoadPronounciationActivity.doInBackground (test branch). No code calls get.',
  'SRC com/ichi2/anki/multimediacard/test/MockPronounciationPageFetcher.java:25-45; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:200-213',
  'SOURCE')

UNREACHABLE['MockTranslationFetcher.<init>'] = ('no_trigger_in_app',
  'Test helper with no constructor. No code creates an instance.',
  'SRC com/ichi2/anki/multimediacard/test/MockTranslationFetcher.java:22-25',
  'SOURCE')

UNREACHABLE['MockTranslationFetcher.get'] = ('no_trigger_in_app',
  'The only reference is a commented-out call in LoadPronounciationActivity.doInBackground (test branch). No code calls get.',
  'SRC com/ichi2/anki/multimediacard/test/MockTranslationFetcher.java:25-41; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:200-213',
  'SOURCE')

# ---- sup for part 063
sup(('NoteService.updateJsonNoteFromMultimediaNote', 'MultimediaEditableNote.getModelId'))
sup(('LanguagesLister.getLanguages', 'LanguagesLister$1.<init>'))


# ---- part 064 (2026-10-28)
# AnkiDroid batch 064 (LABEL helper). 18 methods; the full row list is in graphs/AnkiDroid/parts/label_064.md.
# Three UNREACHABLE entries and no e() calls. The other 15 methods are REACHABLE through automatic CALL edges (see the .md).
# Every string is written inline; no module-level names.

UNREACHABLE['TaskOperations.<init>'] = ('no_trigger_in_app', 'TaskOperations has only static methods and no explicit constructor. A grep for "new TaskOperations" over the app source root finds no instance creation; every use is a static call to stopTaskGracefully. No route creates an instance.', 'SRC com/ichi2/anki/runtimetools/TaskOperations.java:25-38; SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405', 'SOURCE')

UNREACHABLE['NoteService.<init>'] = ('no_trigger_in_app', 'NoteService has only static methods and no explicit constructor. A grep for "new NoteService" over the app source root finds nothing; every use is a static call in NoteEditor.', 'SRC com/ichi2/anki/servicelayer/NoteService.java:38-45; SRC com/ichi2/anki/NoteEditor.java:1037-1038; SRC com/ichi2/anki/NoteEditor.java:1055; SRC com/ichi2/anki/NoteEditor.java:1138-1139; SRC com/ichi2/anki/NoteEditor.java:1151-1152', 'SOURCE')

UNREACHABLE['NoteService.updateJsonNoteFromMultimediaNote'] = ('no_trigger_in_app', 'Public static method with no caller. A grep for the name over the app source root finds only its definition, so the reverse copy (multimedia note into the editor note) is never called.', 'SRC com/ichi2/anki/servicelayer/NoteService.java:101-113', 'SOURCE')

# ---- part 065 (2026-10-28)
# AnkiDroid batch 065 (LABEL helper). AnkiStatsTaskHandler (with its nested tasks CreateChartTask,
# CreateStatisticsOverview and DeckPreviewStatistics) and ChartBuilder: 35 methods. The full row list is in
# graphs/AnkiDroid/parts/label_065.md.
#
# Route ownership:
# - CALL edges (constructors, accessors, createChart, createStatisticsOverview, createReviewSummaryStatistics,
#   renderChart and its setup and tick methods, the <clinit> pseudo-edges) come from auto_calls.json. Not written here.
# - The ASYNC edges below have their source in this batch: the start of each AsyncTask (execute in the three
#   create methods, into the doInBackground of the task) and the hand-back from doInBackground to onPostExecute.
# - The cancel(true) edges into the onCancelled methods come from Statistics.java (Statistics batch). Not written here.
# - No gate is needed: the task edges carry no environment or state.
#
# Gates: none (no MG id used in this batch).

e('AnkiStatsTaskHandler.createChart', 'AnkiStatsTaskHandler$CreateChartTask.doInBackground', 'ASYNC',
  'execute() on a chart task runs doInBackground on the AsyncTask worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:65-69; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-654',
  note='execute calls executeOnExecutor, which runs onPreExecute on the caller thread (AsyncTask.java:648), then exec.execute(mFuture) (AsyncTask.java:651). The FutureTask (AsyncTask.java:345-359) runs the worker. CreateChartTask does not override onPreExecute.')

e('AnkiStatsTaskHandler$CreateChartTask.doInBackground', 'AnkiStatsTaskHandler$CreateChartTask.onPostExecute', 'ASYNC',
  'the chart result returns to the UI thread, where the chart is shown',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:94-114, 121-129; FW-SRC core/java/android/os/AsyncTask.java:369-375, 691-696, 700-713',
  note='doInBackground returns the PlotSheet. postResult sends a message to the UI thread handler (AsyncTask.java:369-375). InternalHandler calls finish (AsyncTask.java:712), and finish calls onPostExecute when the task was not cancelled (AsyncTask.java:691-695). The dispatch is the framework handler route.')

e('AnkiStatsTaskHandler.createStatisticsOverview', 'AnkiStatsTaskHandler$CreateStatisticsOverview.doInBackground', 'ASYNC',
  'execute() on the overview task runs doInBackground on the AsyncTask worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:70-74; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-654',
  note='Same dispatch as the chart task: executeOnExecutor runs onPreExecute on the caller thread (AsyncTask.java:648), then exec.execute(mFuture) (AsyncTask.java:651). CreateStatisticsOverview does not override onPreExecute.')

e('AnkiStatsTaskHandler$CreateStatisticsOverview.doInBackground', 'AnkiStatsTaskHandler$CreateStatisticsOverview.onPostExecute', 'ASYNC',
  'the overview HTML returns to the UI thread, where it is loaded into the WebView',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:143-162, 169-183; FW-SRC core/java/android/os/AsyncTask.java:369-375, 691-696, 700-713',
  note='Same hand-back as the chart task: postResult (AsyncTask.java:369-375), InternalHandler and finish (AsyncTask.java:691-695, 712), then onPostExecute when the task was not cancelled.')

e('AnkiStatsTaskHandler.createReviewSummaryStatistics', 'AnkiStatsTaskHandler$DeckPreviewStatistics.doInBackground', 'ASYNC',
  'execute() on the deck preview task runs doInBackground on the AsyncTask worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:75-79; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-654',
  note='Same dispatch as the chart task (executeOnExecutor, onPreExecute on the caller thread at AsyncTask.java:648, exec.execute at AsyncTask.java:651). DeckPreviewStatistics does not override onPreExecute.')

e('AnkiStatsTaskHandler$DeckPreviewStatistics.doInBackground', 'AnkiStatsTaskHandler$DeckPreviewStatistics.onPostExecute', 'ASYNC',
  'the studied-today text returns to the UI thread, where it is set on the deck list text view',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:197-237, 245-251; FW-SRC core/java/android/os/AsyncTask.java:369-375, 691-696, 700-713',
  note='Same hand-back as the chart task: postResult (AsyncTask.java:369-375), InternalHandler and finish (AsyncTask.java:691-695, 712), then onPostExecute when the task was not cancelled.')

UNREACHABLE['AnkiStatsTaskHandler$DeckPreviewStatistics.onCancelled'] = ('no_trigger_in_app', "DeckPreviewStatistics.onCancelled runs only after cancel(true) on that task. No in-app code holds or cancels a DeckPreviewStatistics: createReviewSummaryStatistics returns it and DeckPicker discards the result (DeckPicker.java:1873). The cancel(true) calls in Statistics.java (543, 574, 681, 692) cancel only the chart and overview tasks, and the DeckTask cancel (DeckTask.java:172) acts on a DeckTask. So the method never runs.", "SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:75-78, 240-242; SRC com/ichi2/anki/DeckPicker.java:1873; SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; SRC com/ichi2/async/DeckTask.java:172; FW-SRC core/java/android/os/AsyncTask.java:462-463, 691-693", 'SOURCE')

# ---- part 066 (2026-10-28)
# AnkiDroid batch 066 (LABEL helper). Batch file: graphs/AnkiDroid/scratch/batches/batch_066.txt (36 methods).
# Full row list: graphs/AnkiDroid/parts/label_066.md.
# Methods: ChartView (3 constructors, addFragment, onDraw, onSizeChanged, setData), OverviewStatsBuilder (constructor and
# private helpers), OverviewStatsBuilder$OverviewStats.<init>, StatsMetaInfo (implicit constructor and 18 accessors).
#
# Route ownership:
# - Automatic CALL edges into and out of these methods (Statistics -> addFragment, AnkiStatsTaskHandler -> setData and the
#   OverviewStatsBuilder constructor, the OverviewStatsBuilder internal calls, Stats.calculateDue -> StatsMetaInfo) come
#   from the builder. They are not written here.
# - The three framework edges below have the page S_STATISTICS as source, so they belong to this part (the destination is
#   a method of this batch).
# Gates: STATE_SETTINGS (the advanced statistics preference, for the StatsMetaInfo accessors reached through
# Stats.calculateDue). No MG id is used.

# --- Chart view inflated from fragment_anki_stats.xml (Statistics.ChartFragment.onCreateView, Statistics.java:428).
e('S_STATISTICS', 'ChartView.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the statistics chart pages inflate the chart view from fragment_anki_stats.xml',
  cls='non_standard',
  via=['layout XML and LayoutInflater reflection'],
  evidence='SRC com/ichi2/anki/Statistics.java:421-428; SRC res/layout/fragment_anki_stats.xml:5; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
  note='LayoutInflater builds the view with the (Context, AttributeSet) constructor by reflection (LayoutInflater.java:615). The page is opened from the navigation drawer (NavigationDrawerActivity.java:265-268) and its fragments come from SectionsPagerAdapter.getItem (Statistics.java:305-309). No gate.')

# --- View.draw calls onDraw (framework callback on the statistics page).
e('S_STATISTICS', 'ChartView.onDraw', 'FRAMEWORK',
  'the statistics screen draws the chart view; View.draw calls onDraw',
  evidence='SRC com/ichi2/anki/stats/ChartView.java:56-57; FW-SRC core/java/android/view/View.java:19161-19166, 19192, 19308',
  note='onDraw runs for the chart view on every draw of the page. With no data set it calls super.onDraw (ChartView.java:74-75). No gate.')

# --- View.setFrame -> sizeChange -> onSizeChanged (framework callback on the statistics page).
e('S_STATISTICS', 'ChartView.onSizeChanged', 'FRAMEWORK',
  'the chart view is laid out with a new size; View.setFrame calls sizeChange, which calls onSizeChanged',
  evidence='SRC com/ichi2/anki/stats/ChartView.java:91-92; FW-SRC core/java/android/view/View.java:19720, 19752-19753, 19791-19792',
  note='The override calls mFragment.checkAndUpdate() once addFragment has run (ChartView.java:95-96). No gate.')

# --- Unreachable: the layout inflater and the app never use these constructors.
UNREACHABLE['ChartView.<init>(Context)'] = ('framework_never_calls', 'LayoutInflater builds chart views with the (Context, AttributeSet) constructor only, and nothing in the app calls the one-argument constructor (no new ChartView in the source root and no subclass of ChartView)', 'com/ichi2/anki/stats/ChartView.java:40-43; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615; res/layout/fragment_anki_stats.xml:5', 'SOURCE')

UNREACHABLE['ChartView.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'The three-argument constructor runs only when a subclass calls it through super or when code calls new ChartView with a style; the layout inflater uses the two-argument constructor, the two-argument ChartView constructor calls super(context, attrs) (ChartView.java:46), and the source root has no new ChartView and no subclass of ChartView', 'com/ichi2/anki/stats/ChartView.java:45-53; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615', 'SOURCE')

# ---- part 067 (2026-10-28)
# AnkiDroid batch 067 (LABEL helper). 39 methods: HttpFetcher, DeckAdapter (and its ViewHolder), DeckDropDownAdapter
# (and its ViewHolder), FabBehavior, PopupMenuWithIcons.<init>, ActivityTransitionAnimation.<init>, ViewAnimation.
# The full row list is in graphs/AnkiDroid/parts/label_067.md.
#
# Route ownership:
# - Automatic CALL edges (auto_calls.json) are not written here, for example HttpFetcher -> LoadPronounciationActivity,
#   DeckPicker.onCreate -> DeckAdapter setters, DeckAdapter.buildDeckList -> processNodes, FabBehavior.onDependentViewChanged
#   -> getFabTranslationYForSnackbar, and AbstractFlashcardViewer -> ViewAnimation.fade.
# - Edges written here: page-sourced framework dispatch (S_DECKPICKER, S_STATISTICS, S_CARDBROWSER) into methods of this batch.
#   Support library dispatch (RecyclerView, CoordinatorLayout) is INFERRED, source not read.
#
# Gates: STATE_CARDS on the congrats or no-cards Snackbar path (FabBehavior.onDependentViewChanged). No MISSING GATE edge
# is written; the subdeck guard of DeckAdapter.setDeckExpander is MG612, described in the .md row only.

# --- Home screen deck list (S_DECKPICKER): RecyclerView adapter callbacks.
e('S_DECKPICKER', 'DeckAdapter.onCreateViewHolder', 'FRAMEWORK',
  'the home screen deck list asks the adapter for a new row view',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-388; com/ichi2/anki/widgets/DeckAdapter.java:154-158; RecyclerView dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'DeckAdapter.onBindViewHolder', 'FRAMEWORK',
  'the home screen deck list binds the data of each visible row',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-388; com/ichi2/anki/widgets/DeckAdapter.java:161-217; RecyclerView dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'DeckAdapter.getItemCount', 'FRAMEWORK',
  'the RecyclerView asks the number of decks for its layout',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-388; com/ichi2/anki/widgets/DeckAdapter.java:220-222; RecyclerView dispatch is support library, INFERRED, source not read')

# --- Home screen FAB behavior (S_DECKPICKER): CoordinatorLayout behavior callbacks.
e('S_DECKPICKER', 'FabBehavior.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the support library creates the FAB behavior from layout_behavior when the home screen is inflated',
  env=None,
  needs_state=None,
  cls='non_standard',
  via='CoordinatorLayout behavior from layout_behavior (support library, not in the dataset)',
  evidence='SRC res/layout-v14/floating_add_button.xml:16; res/layout/deck_picker.xml:2-3, 36; res/layout/homescreen.xml:7; com/ichi2/anki/widgets/FabBehavior.java:42-44; CoordinatorLayout dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'FabBehavior.layoutDependsOn', 'FRAMEWORK',
  'the CoordinatorLayout asks the FAB behavior whether it depends on each sibling view during layout',
  env=None,
  needs_state=None,
  evidence='SRC res/layout/deck_picker.xml:2-3, 36; com/ichi2/anki/widgets/FabBehavior.java:62-64; CoordinatorLayout dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'FabBehavior.onDependentViewChanged', 'FRAMEWORK',
  'a Snackbar on the home screen root changes the dependency and the FAB behavior is told',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/widgets/FabBehavior.java:67-77; com/ichi2/anki/UIUtils.java:33-35; com/ichi2/anki/DeckPicker.java:656-664; CoordinatorLayout dispatch is support library, INFERRED, source not read',
  note='Gate STATE_CARDS: the congrats or no-cards-due Snackbar follows a study session with RESULT_NO_MORE_CARDS (DeckPicker.java:656-664).')

# --- Toolbar deck spinner of the Statistics screen (S_STATISTICS): framework Spinner calls into DeckDropDownAdapter.
e('S_STATISTICS', 'DeckDropDownAdapter.getCount', 'FRAMEWORK',
  'the toolbar deck spinner measures its content and reads the count of decks',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:601-606, 831-847; com/ichi2/anki/Statistics.java:100')

e('S_STATISTICS', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the closed toolbar deck spinner draws its selected deck',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:660, 698-712; com/ichi2/anki/Statistics.java:100')

e('S_STATISTICS', 'DeckDropDownAdapter.getDropDownView', 'GUI',
  'the user opens the toolbar deck spinner and each row of its list is drawn',
  env=None,
  needs_state=None,
  gui=['the user opens the toolbar deck spinner and each row of its list is drawn'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2365; FW-SRC core/java/android/widget/Spinner.java:989-994; com/ichi2/anki/Statistics.java:100-101')

e('S_STATISTICS', 'DeckDropDownAdapter.getItemId', 'GUI',
  'the user taps a row of the open toolbar deck list',
  env=None,
  needs_state=None,
  gui=['the user taps a row of the open toolbar deck list'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3108-3127; FW-SRC core/java/android/widget/Spinner.java:985-987; com/ichi2/anki/Statistics.java:100-101')

# --- Toolbar deck spinner of the card browser (S_CARDBROWSER): same framework paths, CardBrowser.java:372-385.
e('S_CARDBROWSER', 'DeckDropDownAdapter.getCount', 'FRAMEWORK',
  'the toolbar deck spinner of the card browser measures its content and reads the count of decks',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:601-606, 831-847; com/ichi2/anki/CardBrowser.java:372-373')

e('S_CARDBROWSER', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the closed toolbar deck spinner of the card browser draws its selected deck',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:660, 698-712; com/ichi2/anki/CardBrowser.java:372-373')

e('S_CARDBROWSER', 'DeckDropDownAdapter.getDropDownView', 'GUI',
  'the user opens the card browser toolbar deck spinner and each row of its list is drawn',
  env=None,
  needs_state=None,
  gui=['the user opens the card browser toolbar deck spinner and each row of its list is drawn'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2365; FW-SRC core/java/android/widget/Spinner.java:989-994; com/ichi2/anki/CardBrowser.java:372-373')

e('S_CARDBROWSER', 'DeckDropDownAdapter.getItemId', 'GUI',
  'the user taps a row of the open card browser toolbar deck list',
  env=None,
  needs_state=None,
  gui=['the user taps a row of the open card browser toolbar deck list'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3108-3127; FW-SRC core/java/android/widget/Spinner.java:985-987; com/ichi2/anki/CardBrowser.java:372-373')

# --- UNREACHABLE entries (one per method with no route).
UNREACHABLE['HttpFetcher.<init>'] = ('no_trigger_in_app',
  'HttpFetcher declares no constructor and no code creates an instance; every caller uses the static methods',
  'com/ichi2/anki/web/HttpFetcher.java:47; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:212, 252; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:182',
  'SOURCE')

UNREACHABLE['ActivityTransitionAnimation.<init>'] = ('no_trigger_in_app',
  'ActivityTransitionAnimation declares no constructor and no code creates an instance; only the static slide method is used',
  'com/ichi2/anim/ActivityTransitionAnimation.java:9-20; com/ichi2/anki/AnkiActivity.java:232, 249',
  'SOURCE')

UNREACHABLE['ViewAnimation.<init>'] = ('no_trigger_in_app',
  'ViewAnimation declares no constructor and no code creates an instance; callers use the static fade method',
  'com/ichi2/anim/ViewAnimation.java:10-21; com/ichi2/anki/AbstractFlashcardViewer.java:1221, 1224, 1233',
  'SOURCE')

UNREACHABLE['ViewAnimation.slide'] = ('no_trigger_in_app',
  'no caller: the only class that uses ViewAnimation calls fade, and no code calls ViewAnimation.slide',
  'com/ichi2/anim/ViewAnimation.java:23-62; com/ichi2/anki/AbstractFlashcardViewer.java:76, 1221, 1224, 1233',
  'SOURCE')

UNREACHABLE['DeckDropDownAdapter.getItem'] = ('framework_never_calls',
  'the framework reaches the spinner getItem only through getSelectedItem or getItemAtPosition, and neither is called for this spinner; AbsSpinner.java not read',
  'FW-SRC core/java/android/widget/AdapterView.java:590-594, 796-798; FW-SRC core/java/android/widget/Spinner.java:981-983; FW-SRC core/java/android/preference/PreferenceFragment.java:452; com/ichi2/anki/Statistics.java:99-101, 112; com/ichi2/anki/CardBrowser.java:372-374, 385',
  'INFERRED')

UNREACHABLE['FabBehavior.<init>()'] = ('no_trigger_in_app',
  'no code calls new FabBehavior(); the support library uses the (Context, AttributeSet) constructor from layout_behavior (INFERRED, source not read)',
  'com/ichi2/anki/widgets/FabBehavior.java:38-40; res/layout-v14/floating_add_button.xml:16',
  'SOURCE')

# ---- part 071 (2026-10-28)
UNREACHABLE['DeckTask$TaskData.getType'] = ('no_trigger_in_app', 'No caller passes a DeckTask.TaskData receiver to getType(). The only definition is DeckTask.java:1538-1540. A grep for getType() over the source root gives 45 matches, all on other receivers (EFieldType field getters, Card, AdvancedStatistics, Intent). No trigger in the app reaches this accessor.', 'com/ichi2/async/DeckTask.java:1538-1540', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.setCards'] = ('no_trigger_in_app', 'The only setCards( occurrence in the source root is the definition at DeckTask.java:1493-1495 (the other grep hit, resetCards, is a different method). No caller sets mCards on a TaskData, so no trigger in the app reaches it.', 'com/ichi2/async/DeckTask.java:1493-1495', 'SOURCE')

# ---- part 069 (2026-10-28)
# AnkiDroid batch 069 (LABEL helper). DeckTask part 1: 40 methods, all REACHABLE (no UNREACHABLE entries).
# The full row list is in graphs/AnkiDroid/parts/label_069.md.
#
# Route ownership:
# - The launch edges into the DeckTask bodies (for example StudyOptionsFragment, DeckPicker, CardBrowser) belong to the
#   launch-site batches. The CALL edges (cancelTask(int) -> cancelTask(), ProgressCallback -> doProgress, the getCard callers,
#   Finder -> getInstance) come from auto_calls.json and are not written here.
# - Written here: doInBackground -> DeckTask.onPostExecute (the AsyncTask result hop), and each task body that calls
#   publishProgress -> DeckTask.onProgressUpdate, plus doProgress -> DeckTask.onProgressUpdate. The line of each publishProgress
#   is in the EDGE row of label_069.md.
# - No gate is needed in this batch (MG632-MG641 are not used).

e('DeckTask.doInBackground', 'DeckTask.onPostExecute', 'ASYNC',
  'the worker result is delivered to DeckTask.onPostExecute on the UI thread (AsyncTask finish)',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:203-228, 360-365',
  note='DeckTask.onPostExecute forwards to mListener.onPostExecute (DeckTask.java:362). The AsyncTask finish dispatch is framework code and was not read in this batch. No gate of its own.')

e('DeckTask.doInBackgroundAddNote', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the added note to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:378-381, 352-355',
  note='publishProgress is at DeckTask.java:380, inside the transaction. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundUpdateNote', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the updated card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:418-423, 352-355',
  note='publishProgress is at DeckTask.java:420 and 422 (one per branch). onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundAnswerCard', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the answered card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:455-458, 352-355',
  note='publishProgress is at DeckTask.java:457. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundDismissNote', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the dismissed card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:563-566, 352-355',
  note='publishProgress is at DeckTask.java:565. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundUndo', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the undone card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:599-602, 352-355',
  note='publishProgress is at DeckTask.java:601. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundSearchCards', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the search results to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:629-634, 352-355',
  note='publishProgress is at DeckTask.java:633, in the else branch of the isCancelled check (line 629). onProgressUpdate forwards to the listener (DeckTask.java:354).')

e('DeckTask.doInBackgroundRenderBrowserQA', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the render progress to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:657-660, 352-355',
  note='publishProgress is at DeckTask.java:659. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundImportReplace', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the import progress messages to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:805-810, 855-860, 352-355',
  note='publishProgress is at DeckTask.java:809 (before the collection import) and 859 (in the media loop). onProgressUpdate forwards to the listener (DeckTask.java:354).')

e('DeckTask.doProgress', 'DeckTask.onProgressUpdate', 'ASYNC',
  'doProgress publishes the importer progress, which reaches onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:1348-1350, 352-355',
  note='doProgress calls publishProgress (DeckTask.java:1349), the AsyncTask method. The importer path is ProgressCallback.publishProgress (DeckTask.java:1340-1344), created in doInBackgroundImportAdd (DeckTask.java:750).')

# ---- part 068 (2026-10-28)
# AnkiDroid batch 068 (LABEL helper). BaseAsyncTask (5 methods), CollectionLoader (6), Connection (20),
# Connection$CancelCallback (3) and Connection$Payload (4). The full row list is in
# graphs/AnkiDroid/parts/label_068.md.
#
# Route ownership:
# - The ASYNC framework-dispatch edges from Connection.launchConnectionTask, Connection.cancel, the three
#   Connection.publishProgress overloads and the CollectionLoader callbacks are written here.
# - Auto CALL edges (super calls, call sites) come from auto_calls.json and are not repeated here.
# - The DeckPicker key listener into Connection.cancel is owned by the DeckPicker part.
#
# Gates: MG622 (batch range MG622-MG631). The CollectionLoader onStartLoading -> loadInBackground edge uses MG622.

# --- Connection.launchConnectionTask: the AsyncTask framework dispatch (Connection.java:97-100).
e('Connection.launchConnectionTask', 'Connection.onPreExecute', 'ASYNC',
  'AsyncTask.execute runs onPreExecute on the calling thread before the worker starts',
  evidence='SRC com/ichi2/async/Connection.java:81-102, 124-131; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-650',
  note='Framework dispatch (FW-SRC line 648). ASYNC follows the AsyncTask convention in label_019.py.')

e('Connection.launchConnectionTask', 'Connection.doInBackground', 'ASYNC',
  'execute starts the AsyncTask worker, which calls doInBackground on the background thread',
  evidence='SRC com/ichi2/async/Connection.java:81-102, 173-179; FW-SRC core/java/android/os/AsyncTask.java:326-340, 594-596',
  note='Framework dispatch: the worker calls doInBackground (FW-SRC line 333). The executor step is not printed (INFERRED).')

e('Connection.launchConnectionTask', 'Connection.onPostExecute', 'ASYNC',
  'finish calls onPostExecute on the main thread when the task was not cancelled',
  evidence='SRC com/ichi2/async/Connection.java:81-102, 138-145; FW-SRC core/java/android/os/AsyncTask.java:691-697',
  note='Framework dispatch (FW-SRC line 695). ASYNC follows the AsyncTask convention in label_019.py.')

# --- Connection.publishProgress overloads: posted progress is delivered to onProgressUpdate (FW-SRC 684-718).
e('Connection.publishProgress(int)', 'Connection.onProgressUpdate', 'ASYNC',
  'publishProgress posts a progress message that handleMessage delivers to onProgressUpdate on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:461-463, 152-157; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718',
  note='Framework dispatch: publishProgress (FW-SRC 684-689), then handleMessage calls onProgressUpdate (FW-SRC 706-718, line 715).')

e('Connection.publishProgress(int,long,long)', 'Connection.onProgressUpdate', 'ASYNC',
  'publishProgress posts a progress message that handleMessage delivers to onProgressUpdate on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:471-473, 152-157; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718',
  note='Framework dispatch, as for publishProgress(int) (FW-SRC 684-689, 706-718).')

e('Connection.publishProgress(String)', 'Connection.onProgressUpdate', 'ASYNC',
  'publishProgress posts a progress message that handleMessage delivers to onProgressUpdate on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:466-468, 152-157; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718',
  note='Framework dispatch, as for publishProgress(int) (FW-SRC 684-689, 706-718).')

# --- Connection.cancel: cancel(true) reaches onCancelled through the framework (Connection.java:539-543).
e('Connection.cancel', 'Connection.onCancelled', 'ASYNC',
  'cancel(true) makes the framework call onCancelled(result) on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:539-543, 109-117; FW-SRC core/java/android/os/AsyncTask.java:345-358, 462-464, 525-528, 691-697',
  note='Framework cancel path: cancel(true) (FW-SRC 525-528), the future done step (FW-SRC 345-358), then finish calls onCancelled(result) (FW-SRC 691-697, 462-464). The DeckPicker route into cancel is owned by the DeckPicker part.')

# --- CollectionLoader: the start and the background load (CollectionLoader.java:47-55, 19-29).
e('CollectionLoader.onStartLoading', 'CollectionLoader.loadInBackground', 'ASYNC',
  'forceLoad runs loadInBackground on a background thread when the collection is not locked',
  evidence='SRC com/ichi2/async/CollectionLoader.java:47-55, 19-29; com/ichi2/async/Connection.java:277-279, 452-456',
  note='MISSING GATE MG622: the collection is not locked when the load starts (CollectionLoader.java:49-52). Connection.java:279 locks the collection during a sync and Connection.java:456 unlocks it. No predefined ENV or STATE constant fits, so env and needs_state are unset. The support-library forceLoad step is INFERRED, source not read.')

e('CollectionLoader.loadInBackground', 'CollectionLoader.deliverResult', 'ASYNC',
  'the support-library AsyncTaskLoader delivers the loadInBackground result to deliverResult',
  evidence='SRC com/ichi2/async/CollectionLoader.java:19-29, 31-44',
  note='The support-library AsyncTaskLoader delivers the result after loadInBackground returns (INFERRED, source not read). deliverResult forwards the value when the loader is started (line 41).')

# --- UNREACHABLE: Connection$CancelCallback is never constructed in the source root (Connection.java:549-566).
UNREACHABLE['Connection$CancelCallback.<init>'] = ('no_trigger_in_app', 'No code in the source root creates a CancelCallback. The class has only the implicit constructor. Its references are the parameter type (HttpSyncer.java:152-153) and a call on a parameter (HttpSyncer.java:231), which create no instance.', 'SRC com/ichi2/async/Connection.java:549-551; com/ichi2/libanki/sync/HttpSyncer.java:152-153, 230-232', 'SOURCE')

UNREACHABLE['Connection$CancelCallback.cancelAllConnections'] = ('no_trigger_in_app', 'No call site in the source root. The method is reached only through a CancelCallback object, and none is created in the source root.', 'SRC com/ichi2/async/Connection.java:558-566', 'SOURCE')

UNREACHABLE['Connection$CancelCallback.setConnectionManager'] = ('branch_never_taken', 'The only call is inside if (cancelCallback != null) (HttpSyncer.java:230-232). The only 5-argument req call in the source root is HttpSyncer.java:148, which passes the literal null, and the other req calls have at most four arguments. So cancelCallback is always null and the branch is never taken.', 'SRC com/ichi2/async/Connection.java:553-555; com/ichi2/libanki/sync/HttpSyncer.java:143-155, 230-232; com/ichi2/libanki/sync/RemoteMediaServer.java:94-100, 113-120, 143-148', 'SOURCE')

# --- UNREACHABLE: the zero-, two- and three-argument Connection$Payload constructors have no call site (Connection.java:514-536).
UNREACHABLE['Connection$Payload.<init>()'] = ('no_trigger_in_app', 'No call with zero arguments in the source root. The grep of Payload( finds the declaration (Connection.java:514) and only the one-argument constructions (MyAccount.java:140, DeckPicker.java:1285).', 'SRC com/ichi2/async/Connection.java:514-517; com/ichi2/anki/MyAccount.java:139-143; com/ichi2/anki/DeckPicker.java:1284-1286', 'SOURCE')

UNREACHABLE['Connection$Payload.<init>(int,Object[])'] = ('no_trigger_in_app', 'No call with two arguments in the source root. The grep of Payload( finds the declaration (Connection.java:526) and only the one-argument constructions (MyAccount.java:140, DeckPicker.java:1285). login and sync set taskType themselves (Connection.java:161, 167).', 'SRC com/ichi2/async/Connection.java:526-530, 160-169; com/ichi2/anki/MyAccount.java:139-143; com/ichi2/anki/DeckPicker.java:1284-1286', 'SOURCE')

UNREACHABLE['Connection$Payload.<init>(int,Object[],String)'] = ('no_trigger_in_app', 'No call with three arguments in the source root. The grep of Payload( finds the declaration (Connection.java:532) and only the one-argument constructions. The path argument is not stored in the body (lines 533-535).', 'SRC com/ichi2/async/Connection.java:532-536', 'SOURCE')

# ---- sup for part 068 (2026-10-28): the only 5-argument req() call passes null and no CancelCallback is constructed, so line 231 never runs.
sup(('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'Connection$CancelCallback.setConnectionManager'))
sup(('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)@FullSyncer', 'Connection$CancelCallback.setConnectionManager'))
sup(('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)@RemoteMediaServer', 'Connection$CancelCallback.setConnectionManager'))

# ---- part 070 (2026-10-28)
e('DeckTask$ProgressCallback.publishProgress', 'DeckTask.onProgressUpdate', 'ASYNC',
  'worker progress: ProgressCallback.publishProgress forwards to DeckTask.doProgress, which calls AsyncTask.publishProgress; the framework handler then calls onProgressUpdate on the main thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:1340-1344, 1348-1350, 352-355; FW-SRC core/java/android/os/AsyncTask.java:684-689, 712-716',
  note='The route goes through the framework handler, not a direct call in the app source, so it is not a bytecode CALL. The import task doInBackgroundImportAdd is the one that publishes this progress. No MG gate is needed.')

UNREACHABLE['DeckTask$ProgressCallback.getResources'] = ('no_trigger_in_app', 'no caller: the only ProgressCallback is held in the importer field mProgress, and the importer calls only mProgress.publishProgress (Anki2Importer.publishProgress, line 762); the getResources( calls in files that mention ProgressCallback are only the app Context calls in the DeckTask class at lines 746 and 760', 'SRC com/ichi2/async/DeckTask.java:1335-1337, 746, 760; SRC com/ichi2/libanki/importer/Importer.java:44, 80-81; SRC com/ichi2/libanki/importer/Anki2Importer.java:761-762', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(int,Card)'] = ('no_trigger_in_app', 'No call passes an int first with a Card second. Card-first calls use the (Card,int), (Card,String) or (Card,boolean) forms (lines 422, 565, 601, and the viewer and reviewer launches). The three-argument int calls take a long or an Object[] second (lines 682, 1119).', 'SRC com/ichi2/async/DeckTask.java:1378, 422, 565, 601, 682, 1119; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1077, 1085, 1093; SRC com/ichi2/anki/Reviewer.java:111', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(int,String)'] = ('no_trigger_in_app', 'No call passes an int first with a String second. The String calls are the one-argument TaskData(String) (Anki2Importer lines 761-762) and the two-argument TaskData(String,boolean) (importAdd, lines 1579-1581, and the removeTemplateFailed return at line 1057).', 'SRC com/ichi2/async/DeckTask.java:1475, 1057; SRC com/ichi2/anki/DeckPicker.java:1579-1581; SRC com/ichi2/libanki/importer/Anki2Importer.java:761-762', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(int,boolean)'] = ('no_trigger_in_app', 'No call passes an int first with a boolean second. Boolean-only calls use TaskData(boolean) (line 390). Two-argument boolean calls take a Card first (CardBrowser line 698, AbstractFlashcardViewer line 1085) or a String first (importAdd, lines 1579-1581).', 'SRC com/ichi2/async/DeckTask.java:1443, 390; SRC com/ichi2/anki/CardBrowser.java:698; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1085; SRC com/ichi2/anki/DeckPicker.java:1579-1581', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(long,boolean)'] = ('no_trigger_in_app', 'No call passes a long first with a boolean second. The only long-argument launches pass a single long (deleteDeck at line 2067, deleteModel at lines 578-580).', 'SRC com/ichi2/async/DeckTask.java:1437; SRC com/ichi2/anki/DeckPicker.java:2067; SRC com/ichi2/anki/ModelBrowser.java:578-580', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(Context,int,int)'] = ('no_trigger_in_app', 'No call passes a Context. Every three-argument call starts with an int (0 or -2), as at lines 682, 782 and 1119.', 'SRC com/ichi2/async/DeckTask.java:1408, 682, 782, 1119', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(String,long,boolean)'] = ('no_trigger_in_app', 'No call passes a String first with a long second. The three-argument calls start with an int (0 or -2), as at lines 682, 782 and 1119.', 'SRC com/ichi2/async/DeckTask.java:1481, 682, 782, 1119', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(List,Comparator)'] = ('no_trigger_in_app', 'No call passes a List and a Comparator. The List calls (lines 633 and 663) take one argument, and the Comparator getter has no caller (getComparator, line 1498).', 'SRC com/ichi2/async/DeckTask.java:1420, 633, 663, 1498', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.getComparator'] = ('no_trigger_in_app', 'No caller. No TaskData carries a Comparator, since the List,Comparator constructor has no caller, and a grep for .getComparator( in the files that mention TaskData finds no call.', 'SRC com/ichi2/async/DeckTask.java:1420, 1498', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.getContext'] = ('no_trigger_in_app', 'No caller on a TaskData. The grep of getContext() in the files that mention TaskData shows only Activity, fragment and dialog calls (ModelBrowser line 661, DeckPicker line 1345, StudyOptionsFragment line 675); the Context constructor has no caller either.', 'SRC com/ichi2/async/DeckTask.java:1408, 1533; SRC com/ichi2/anki/ModelBrowser.java:661; SRC com/ichi2/anki/DeckPicker.java:1345; SRC com/ichi2/anki/StudyOptionsFragment.java:675', 'SOURCE')

# ---- part 072 (2026-10-28)
# AnkiDroid batch 072 (LABEL helper). CompatHelper static methods, CompatV10 base bodies and its anonymous classes,
# CompatV11, CompatV15 ($1 listener), CompatV16 and CompatV17: 36 methods. The full row list is in
# graphs/AnkiDroid/parts/label_072.md.
#
# Route ownership: the three e() calls are the TTS listener edges from CompatV15.setTtsOnUtteranceProgressListener
# (CompatV15.java:13-30). The other CALL edges come from auto_calls.json and are not written here.
# Gates: ENV_TTS and STATE_SETTINGS (the TTS preference, as in label_053). No MISSING GATE is needed.
# UNREACHABLE: isNook (no caller) and 18 closed members on the standard API 27 path (12 CompatV10 base bodies that a
# CompatV11..CompatV21 class overrides, and 6 members of their anonymous classes).

e('CompatV15.setTtsOnUtteranceProgressListener', 'CompatV15$1.onDone', 'FRAMEWORK',
  'the TTS engine reports that an utterance finished and the listener speaks the next queued text',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/compat/CompatV15.java:13-22; SRC com/ichi2/anki/ReadText.java:195',
  note='The TTS engine dispatch is not in fw_src (android/speech not read): INFERRED. The body runs only when ReadText.sTextQueue is not empty.')

e('CompatV15.setTtsOnUtteranceProgressListener', 'CompatV15$1.onError', 'FRAMEWORK',
  'the TTS engine reports an error for an utterance',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/compat/CompatV15.java:13-25; SRC com/ichi2/anki/ReadText.java:195',
  note='The TTS engine dispatch is not in fw_src (android/speech not read): INFERRED. The body is empty.')

e('CompatV15.setTtsOnUtteranceProgressListener', 'CompatV15$1.onStart', 'FRAMEWORK',
  'the TTS engine reports that an utterance started',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/compat/CompatV15.java:13-28; SRC com/ichi2/anki/ReadText.java:195',
  note='The TTS engine dispatch is not in fw_src (android/speech not read): INFERRED. The body is empty.')

UNREACHABLE['CompatHelper.isNook'] = ('no_trigger_in_app',
  'No caller in the app source. The constructor uses the private isNookHdOrHdPlus (CompatHelper.java:33), not this method. A grep over src/main/java finds no other reference.',
  'com/ichi2/compat/CompatHelper.java:33, 101-103', 'SOURCE')

UNREACHABLE['CompatV10.detagged'] = ('closed_by_api_level',
  'CompatV16 overrides it (Html.escapeHtml). The base body runs only on API 10 to 15, not on the standard API 27 path.',
  'com/ichi2/compat/CompatV10.java:49-55; com/ichi2/compat/CompatV16.java:34-37; com/ichi2/compat/CompatHelper.java:35-36', 'SOURCE')

UNREACHABLE['CompatV10.flushWebViewCookies'] = ('closed_by_api_level',
  'CompatV21 overrides it (CookieManager.flush). The base body (CookieSyncManager.sync) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:88-90; com/ichi2/compat/CompatV21.java:31-34; com/ichi2/compat/CompatHelper.java:35-36', 'SOURCE')

UNREACHABLE['CompatV10.getPreferenceSubscreenIntent'] = ('closed_by_api_level',
  'CompatV11 overrides it. The base body (legacy headers, action only) does not run on API 11 and up, including API 27.',
  'com/ichi2/compat/CompatV10.java:183-188; com/ichi2/compat/CompatV11.java:40-49; com/ichi2/compat/CompatHelper.java:45-46', 'SOURCE')

UNREACHABLE['CompatV10.isImmersiveSystemUiVisible'] = ('closed_by_api_level',
  'CompatV19 overrides it (SYSTEM_UI_FLAG_HIDE_NAVIGATION check). The base body (always false) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:196-198; com/ichi2/compat/CompatV19.java:90-93', 'SOURCE')

UNREACHABLE['CompatV10.openUrl'] = ('closed_by_api_level',
  'CompatV16 overrides it (Custom Tabs). The base body (CustomTabsFallback.openUri) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:132-134; com/ichi2/compat/CompatV16.java:76-87; com/ichi2/anki/AnkiActivity.java:322-323', 'SOURCE')

UNREACHABLE['CompatV10.restartActivityInvalidateBackstack'] = ('closed_by_api_level',
  'CompatV11 overrides it (TaskStackBuilder restart). The base body runs only on API 10, below the CompatV11 threshold.',
  'com/ichi2/compat/CompatV10.java:105-111; com/ichi2/compat/CompatV11.java:24-32; com/ichi2/compat/CompatHelper.java:45-46', 'SOURCE')

UNREACHABLE['CompatV10.setFullScreen'] = ('closed_by_api_level',
  'CompatV19 overrides it (sticky immersive flags, no super call). The base body does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:113-120; com/ichi2/compat/CompatV19.java:25-26', 'SOURCE')

UNREACHABLE['CompatV10.setHTML5MediaAutoPlay'] = ('closed_by_api_level',
  'CompatV17 overrides it (setMediaPlaybackRequiresUserGesture). The empty base body does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:93-95; com/ichi2/compat/CompatV17.java:13-16', 'SOURCE')

UNREACHABLE['CompatV10.setSelectableBackground'] = ('closed_by_api_level',
  'CompatV21 overrides it (ripple effect). The base body (colorBackground) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:123-130; com/ichi2/compat/CompatV21.java:14-21', 'SOURCE')

UNREACHABLE['CompatV10.setStatusBarColor'] = ('closed_by_api_level',
  'CompatV21 overrides it (window.setStatusBarColor). The empty base body does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:191-193; com/ichi2/compat/CompatV21.java:36-39', 'SOURCE')

UNREACHABLE['CompatV10.setTtsOnUtteranceProgressListener'] = ('closed_by_api_level',
  'CompatV15 overrides it (UtteranceProgressListener). The API 27 route into the TTS init callback reaches CompatV15 (ReadText.java:195). The base body (deprecated OnUtteranceCompletedListener) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:57-67; com/ichi2/compat/CompatV15.java:13-30; com/ichi2/anki/ReadText.java:195', 'SOURCE')

UNREACHABLE['CompatV10.supportAddContentMenu'] = ('closed_by_api_level',
  'Called only from the DeckPicker fallback, which runs only when the add_content_menu view is absent. That id is in the layout-v14 resource only, so API 27 does not take the fallback.',
  'com/ichi2/compat/CompatV10.java:141-180; com/ichi2/anki/DeckPicker.java:391-404; res/layout-v14/floating_add_button.xml:7; res/layout/floating_add_button.xml:1-14', 'SOURCE')

UNREACHABLE['CompatV10$1.<init>'] = ('closed_by_api_level',
  'Created only inside CompatV10.setTtsOnUtteranceProgressListener, which CompatV15 overrides on API 27.',
  'com/ichi2/compat/CompatV10.java:57-67', 'SOURCE')

UNREACHABLE['CompatV10$1.onUtteranceCompleted'] = ('closed_by_api_level',
  'Body of the deprecated listener above. Never registered on API 27.',
  'com/ichi2/compat/CompatV10.java:58-66', 'SOURCE')

UNREACHABLE['CompatV10$2.<init>'] = ('closed_by_api_level',
  'Created only inside supportAddContentMenu, which is closed on API 27.',
  'com/ichi2/compat/CompatV10.java:147-178', 'SOURCE')

UNREACHABLE['CompatV10$2.onSelection'] = ('closed_by_api_level',
  'Runs only from the dialog opened by supportAddContentMenu. Closed with it.',
  'com/ichi2/compat/CompatV10.java:147-178', 'SOURCE')

UNREACHABLE['CompatV10$2$1.<init>'] = ('closed_by_api_level',
  'Created by the case 2 branch of onSelection. Closed with supportAddContentMenu.',
  'com/ichi2/compat/CompatV10.java:161-175', 'SOURCE')

UNREACHABLE['CompatV10$2$1.onClick'] = ('closed_by_api_level',
  'onPositive callback of the new-deck dialog. Reachable only through supportAddContentMenu, closed on API 27.',
  'com/ichi2/compat/CompatV10.java:165-173', 'SOURCE')

# ---- sup for part 072 (2026-10-28): on API 27 CompatHelper.java:35-36 selects CompatV21, whose chain (CompatV19, V17, V16, V15, V12, V11) overrides each CompatV10 member listed here; supportAddContentMenu is reached only by the DeckPicker fallback, which API 27 does not take (DeckPicker.java:391-404).
sup(('CompatV19.setFullScreen', 'CompatV10.setStatusBarColor'))
sup(('CompatV10$2.onSelection', 'CompatV10$2$1.<init>'))
sup(('CompatV10.setTtsOnUtteranceProgressListener', 'CompatV10$1.<init>'))
sup(('CompatV10.supportAddContentMenu', 'CompatV10$2.<init>'))
sup(('AbstractFlashcardViewer$21.handleMessage', 'CompatV10.setFullScreen'))
sup(('AbstractFlashcardViewer.onPause', 'CompatV10.flushWebViewCookies'))
sup(('AbstractFlashcardViewer.fillFlashcard', 'CompatV10.setHTML5MediaAutoPlay'))
sup(('AbstractFlashcardViewer.fillFlashcard@Previewer', 'CompatV10.setHTML5MediaAutoPlay'))
sup(('DeckPicker.onCreate', 'CompatV10.getPreferenceSubscreenIntent'))
sup(('Preferences$7.onPreferenceClick', 'CompatV10.getPreferenceSubscreenIntent'))
sup(('Preferences$3.onPreferenceClick', 'CompatV10.getPreferenceSubscreenIntent'))
sup(('Preferences$6.onPreferenceClick', 'CompatV10.getPreferenceSubscreenIntent'))
sup(('Reviewer$1.onTouch', 'CompatV10.isImmersiveSystemUiVisible'))
sup(('AbstractFlashcardViewer$MyGestureDetector.onFling', 'CompatV10.isImmersiveSystemUiVisible'))
sup(('AbstractFlashcardViewer$MyGestureDetector.onSingleTapConfirmed', 'CompatV10.isImmersiveSystemUiVisible'))
sup(('ReadText$3.onInit', 'CompatV10.setTtsOnUtteranceProgressListener'))
sup(('AnkiActivity.openUrl', 'CompatV10.openUrl'))
sup(('Reviewer.onCollectionLoaded', 'CompatV10.setFullScreen'))
sup(('DeckPicker$8.onClick', 'CompatV10.supportAddContentMenu'))
sup(('NavigationDrawerActivity$2.onCheckedChanged', 'CompatV10.restartActivityInvalidateBackstack'))
sup(('NavigationDrawerActivity.onActivityResult', 'CompatV10.restartActivityInvalidateBackstack'))
sup(('DeckAdapter.onBindViewHolder', 'CompatV10.setSelectableBackground'))
sup(('DiffEngine.wrapBad', 'CompatV10.detagged'))
sup(('DiffEngine.wrapGood', 'CompatV10.detagged'))
sup(('DiffEngine.wrapMissing', 'CompatV10.detagged'))

# ---- part 074 (2026-10-28)
# AnkiDroid batch 074 (LABEL helper). StepsPreference (9 methods), HtmlColors (4), StyledProgressDialog (9),
# Themes (7), DividerItemDecoration (2). The full row list is in graphs/AnkiDroid/parts/label_074.md.
#
# Route ownership:
# - Auto CALL edges (bytecode builder, auto_calls.json) are not written here: StepsPreference internal calls,
#   the convertFromJSON and convertToJSON callers, HtmlColors.invertColors and nameToHex, the StyledProgressDialog
#   four-argument to five-argument delegation, the Themes overload calls, and DividerItemDecoration.<init> from DeckPicker.onCreate.
# - No MG ids are used. Gates are the predefined constants STATE_SETTINGS (invertedColors preference) and STATE_DECK.

# --- StepsPreference: inflated from XML by the framework preference inflater (GenericInflater reflection on the
# --- (Context, AttributeSet) constructor). Both screens that show the steps tags.
e('S_DECKOPTIONS', 'StepsPreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'DeckOptions shows deck_options.xml, whose StepsPreference tags (newSteps, lapSteps) are inflated by the framework preference inflater through the (Context, AttributeSet) constructor, found by reflection',
  env=None,
  cls='non_standard',
  via=['PreferenceInflater reflection (GenericInflater constructor lookup)'],
  evidence='SRC res/xml/deck_options.xml:66-69, 138-141; SRC com/ichi2/anki/DeckOptions.java:499-500, 523; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  note='Non-standard (XML instantiation). The destination is a method of this batch, so the edge belongs here. No gate.')

e('S_FILTEREDDECKOPTIONS', 'StepsPreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'FilteredDeckOptions shows cram_deck_options.xml for a filtered deck (else branch), whose StepsPreference tag (steps) is inflated through the (Context, AttributeSet) constructor by reflection',
  env=None,
  cls='non_standard',
  via=['PreferenceInflater reflection (GenericInflater constructor lookup)'],
  evidence='SRC res/xml/cram_deck_options.xml:50-54; SRC com/ichi2/anki/FilteredDeckOptions.java:369-378; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  note='Non-standard (XML instantiation). The else branch runs only when the deck is a filtered deck, FilteredDeckOptions.java:370-374. No gate constant covers this; env and needs_state unset.')

# --- StepsPreference.onDialogClosed: framework dispatch from DialogPreference.onDismiss (no app call site).
e('S_DECKOPTIONS', 'StepsPreference.onDialogClosed', 'FRAMEWORK',
  'the user taps a steps preference and the dialog closes; DialogPreference.onDismiss calls onDialogClosed',
  env=None,
  evidence='SRC com/ichi2/preferences/StepsPreference.java:69-82; SRC com/ichi2/anki/DeckOptions.java:499-523; FW-SRC core/java/android/preference/DialogPreference.java:274-278, 318, 390-395',
  note='The dialog is shown by DialogPreference.onClick (showDialog at line 277). The dismiss listener is set at line 318. The dispatch to onDialogClosed is at line 395, a framework call with no app call site. No gate.')

e('S_FILTEREDDECKOPTIONS', 'StepsPreference.onDialogClosed', 'FRAMEWORK',
  'the same steps dialog on the filtered-deck options screen closes; DialogPreference.onDismiss calls onDialogClosed',
  env=None,
  evidence='SRC com/ichi2/preferences/StepsPreference.java:69-82; SRC com/ichi2/anki/FilteredDeckOptions.java:370-378; FW-SRC core/java/android/preference/DialogPreference.java:274-278, 318, 390-395',
  note='Same framework dispatch as the DeckOptions edge. No gate.')

# --- HtmlColors static initialiser: runs at the invokestatic of HtmlColors.invertColors in AbstractFlashcardViewer.updateCard.
e('S_REVIEWER', 'HtmlColors.<clinit>', 'FRAMEWORK',
  'the first night-mode card display initialises the HtmlColors class, which runs its static initialiser before invertColors',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1722, 2112-2118; SRC com/ichi2/themes/HtmlColors.java:10-16, 84-85; JVM class-initialisation rule is not in fw_src: INFERRED, source not read',
  note='Gate STATE_SETTINGS: the invertedColors preference (AbstractFlashcardViewer.java:1722) is needed for mNightMode (line 2112). The initialisation happens at the invokestatic in updateCard (line 2118), so the source is the reviewer page. INFERRED.')

# --- DividerItemDecoration.onDrawOver: support-library RecyclerView dispatch (not in fw_src).
e('S_DECKPICKER', 'DividerItemDecoration.onDrawOver', 'FRAMEWORK',
  'the deck list RecyclerView draws the item decoration over its rows',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-376; SRC com/ichi2/ui/DividerItemDecoration.java:28-44; support-library RecyclerView dispatch is not in fw_src: INFERRED, source not read',
  note='Gate STATE_DECK: decks (rows) are on screen, so onDrawOver has children to draw dividers under. INFERRED.')

# --- UNREACHABLE entries.
UNREACHABLE['StepsPreference.<init>(Context)'] = ('framework_never_calls',
  'No app caller; the framework inflater looks up only the (Context, AttributeSet) constructor',
  'com/ichi2/preferences/StepsPreference.java:51-55; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  'SOURCE')

UNREACHABLE['StepsPreference.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
  'No app caller; the framework inflater uses only the (Context, AttributeSet) constructor',
  'com/ichi2/preferences/StepsPreference.java:37-41; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  'SOURCE')

UNREACHABLE['HtmlColors.<init>'] = ('no_trigger_in_app',
  'HtmlColors has only static members; no code creates an instance',
  'com/ichi2/themes/HtmlColors.java:9-30; com/ichi2/anki/AbstractFlashcardViewer.java:88, 2118',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.<init>'] = ('no_trigger_in_app',
  'The constructor runs only from new StyledProgressDialog(...), which does not occur in the source root; the static show overloads return MaterialDialog',
  'com/ichi2/themes/StyledProgressDialog.java:31-39, 53-73; com/ichi2/anki/DeckPicker.java:253-254',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.animationEnabled'] = ('no_trigger_in_app',
  'Private static helper with no caller in the source root',
  'com/ichi2/themes/StyledProgressDialog.java:43-73, 76-82; com/ichi2/anki/AnkiActivity.java:119',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.setMax'] = ('no_trigger_in_app',
  'No-op setter with no instance of StyledProgressDialog; the setMax callers are on SeekBar',
  'com/ichi2/themes/StyledProgressDialog.java:84-86; com/ichi2/ui/SeekBarPreference.java:70, 82',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.setProgress'] = ('no_trigger_in_app',
  'No-op setter with no instance of StyledProgressDialog; the setProgress callers are on SeekBar',
  'com/ichi2/themes/StyledProgressDialog.java:89-91; com/ichi2/ui/SeekBarPreference.java:71, 83',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.setProgressStyle'] = ('no_trigger_in_app',
  'No-op setter with no caller in the source root and no instance',
  'com/ichi2/themes/StyledProgressDialog.java:94-96',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.show()'] = ('no_trigger_in_app',
  'Instance override of Dialog.show; no StyledProgressDialog instance is created, and the app uses the static show overloads',
  'com/ichi2/themes/StyledProgressDialog.java:42-50; com/ichi2/anki/DeckPicker.java:253-254',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.show(Context,CharSequence,CharSequence)'] = ('no_trigger_in_app',
  'Three-argument overload; every app call site passes four arguments, so nothing calls it',
  'com/ichi2/themes/StyledProgressDialog.java:53-55; com/ichi2/anki/DeckPicker.java:253-254, 294-296, 316-317; com/ichi2/anki/StudyOptionsFragment.java:316-317',
  'SOURCE')

UNREACHABLE['Themes.<init>'] = ('no_trigger_in_app',
  'Themes has only static members; no code creates an instance',
  'com/ichi2/themes/Themes.java:30-41; com/ichi2/anki/NoteEditor.java:1110',
  'SOURCE')

UNREACHABLE['Themes.getResFromAttr(Context,int)'] = ('no_trigger_in_app',
  'Single-attribute overload; both app call sites pass an int array and resolve to the array overload',
  'com/ichi2/themes/Themes.java:94-97; com/ichi2/anki/NoteEditor.java:1110; com/ichi2/anki/AbstractFlashcardViewer.java:1580',
  'SOURCE')

# ---- part 075 (2026-10-28)
# AnkiDroid batch 075 (LABEL helper). SeekBarPreference (10 methods) and SlidingTabLayout with its inner classes
# InternalViewPagerListener (4) and TabClickListener (2): 29 methods in total. The full row list is in
# graphs/AnkiDroid/parts/label_075.md.
#
# Route ownership:
# - Automatic CALL edges (the SlidingTabLayout constructor chain, setViewPager to populateTabStrip, the listener
#   constructors, scrollToTab, createDefaultTabView) come from the builder and are not written here.
# - Page edges from S_PREFERENCES, S_CARDTEMPLATEEDITOR and S_STATISTICS into methods of this batch are written here,
#   because the destination is in the batch.
# - One edge with a source in this batch: SeekBarPreference.onStopTrackingTouch -> Preferences$SettingsFragment.onSharedPreferenceChanged.
# - Gates: STATE_COLLECTION (the dayOffset row is enabled only with an open collection; the tabs exist only after
#   onCollectionLoaded); STATE_SETTINGS (a later open, after dayOffset has been stored). No MG ids are needed here.
# - The support ViewPager is not in the dataset, so the pager dispatch edges are INFERRED (source not read).

# --- SeekBarPreference: page edges and the persist edge.
e('S_PREFERENCES', 'SeekBarPreference.<init>', 'FRAMEWORK',
  'Opening the reviewing settings screen inflates the day-offset SeekBarPreference.',
  env=None,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:34-43; SRC res/xml/preferences_reviewing.xml:36-39; FW-SRC core/java/android/preference/GenericInflater.java:376-385',
  note='Inflated when the reviewing subscreen is built (Preferences.java:242-243, 788). No gate: the screen opens without a collection.')

e('S_PREFERENCES', 'SeekBarPreference.onBindDialogView', 'FRAMEWORK',
  'Tap on the day-offset row; the framework calls the dialog binder after the view is built.',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:80-84; FW-SRC core/java/android/preference/DialogPreference.java:287-300; FW-SRC core/java/android/preference/Preference.java:1129-1135',
  note='Gate: the row is disabled when the collection is closed (Preferences.java:434-436), and Preference.performClick returns early when disabled (Preference.java:1131-1132).')

e('S_PREFERENCES', 'SeekBarPreference.onCreateDialogView', 'GUI',
  'Tap on the day-offset row opens the dialog.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Tap on the day-offset row opens the dialog.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:47-76; FW-SRC core/java/android/preference/PreferenceScreen.java:240-249',
  note='Gate: open collection (see onBindDialogView).')

e('S_PREFERENCES', 'SeekBarPreference.onPrepareDialogBuilder', 'FRAMEWORK',
  'Tap on the day-offset row; the framework calls the builder hook on the same tap.',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:135-140; FW-SRC core/java/android/preference/DialogPreference.java:287-306',
  note='Gate: open collection (see onBindDialogView).')

e('S_PREFERENCES', 'SeekBarPreference.onProgressChanged', 'GUI',
  'Drag the thumb or tap the bar in the open dialog.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Drag the thumb or tap the bar in the open dialog.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:99-105; FW-SRC core/java/android/widget/SeekBar.java:91-96',
  note='Gate: open collection (the dialog exists only on an enabled row). The fromTouch branch (lines 100-104) is taken.')

e('S_PREFERENCES', 'SeekBarPreference.onSetInitialValue', 'FRAMEWORK',
  'A later open of the screen, after dayOffset has been stored; the restore branch runs.',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:88-96, 116-119; FW-SRC core/java/android/preference/Preference.java:1547-1561',
  note='Gate: STATE_SETTINGS (dayOffset must have been stored by a prior setValue, which needs the collection: Preferences.java:400-402, 424-428).')

e('S_PREFERENCES', 'SeekBarPreference.onStartTrackingTouch', 'GUI',
  'Press the thumb of the open dialog SeekBar.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Press the thumb of the open dialog SeekBar.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:121-122; FW-SRC core/java/android/widget/SeekBar.java:112-117',
  note='Gate: open collection (see onBindDialogView). The body is empty.')

e('S_PREFERENCES', 'SeekBarPreference.onStopTrackingTouch', 'GUI',
  'Lift the finger after a drag; the dialog closes.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Lift the finger after a drag; the dialog closes.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:125-131; FW-SRC core/java/android/widget/SeekBar.java:119-125',
  note='Gate: open collection (see onBindDialogView). The body persists the value and dismisses the dialog (lines 127-130).')

e('SeekBarPreference.onStopTrackingTouch', 'Preferences$SettingsFragment.onSharedPreferenceChanged', 'FRAMEWORK',
  'persistInt commits the new value to SharedPreferences, which notifies the listener registered in SettingsFragment.onResume.',
  env=None,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:125-131; SRC com/ichi2/anki/Preferences.java:796, 811-812; FW-SRC core/java/android/preference/Preference.java:1716-1735, 1587-1595; FW-SRC core/java/android/app/SharedPreferencesImpl.java:547, 551-563',
  note='The notify is skipped when the stored value is unchanged (Preference.java:1721-1724). No gate beyond the open dialog.')

# --- SlidingTabLayout: page edges (card template editor and statistics) into the batch methods.
e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'Opening the card template editor inflates the tab strip from its layout.',
  env=None,
  evidence='SRC res/layout/card_template_editor_activity.xml:21-24; SRC com/ichi2/anki/CardTemplateEditor.java:127-130; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
  note='No gate: setContentView in onCreate (line 130) runs before the collection loads.')

e('S_STATISTICS', 'SlidingTabLayout.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'Opening the statistics screen inflates the tab strip from its layout.',
  env=None,
  evidence='SRC res/layout/activity_anki_stats.xml:18-21; SRC com/ichi2/anki/Statistics.java:84-88; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
  note='No gate: setContentView in onCreate (line 86) runs before the collection loads.')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout.onAttachedToWindow', 'FRAMEWORK',
  'The window attaches the card template editor layout, which runs onAttachedToWindow.',
  env=None,
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:229-236; FW-SRC core/java/android/view/View.java:17420, 17445',
  note='No gate. scrollToTab runs only when mViewPager is set (line 233).')

e('S_STATISTICS', 'SlidingTabLayout.onAttachedToWindow', 'FRAMEWORK',
  'The window attaches the statistics layout, which runs onAttachedToWindow.',
  env=None,
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:229-236; FW-SRC core/java/android/view/View.java:17420, 17445',
  note='No gate. scrollToTab runs only when mViewPager is set (line 233).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$TabClickListener.onClick', 'GUI',
  'Tap a tab title in the card template editor.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Tap a tab title in the card template editor.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:223, 304-314; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: the tabs exist only after onCollectionLoaded (setViewPager at line 232).')

e('S_STATISTICS', 'SlidingTabLayout$TabClickListener.onClick', 'GUI',
  'Tap a tab title on the statistics screen.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Tap a tab title on the statistics screen.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:223, 304-314; SRC com/ichi2/anki/Statistics.java:92, 125-126',
  note='Gate: the tabs exist only after onCollectionLoaded (setViewPager at line 126).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$InternalViewPagerListener.onPageScrollStateChanged', 'GUI',
  'Swipe between the card template pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the card template pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:282-288; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$InternalViewPagerListener.onPageScrolled', 'GUI',
  'Swipe between the card template pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the card template pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:261-279; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$InternalViewPagerListener.onPageSelected', 'GUI',
  'Swipe to another template page, or tap a tab.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe to another template page, or tap a tab.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:291-300, 309; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_STATISTICS', 'SlidingTabLayout$InternalViewPagerListener.onPageScrollStateChanged', 'GUI',
  'Swipe between the statistics pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the statistics pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:282-288; SRC com/ichi2/anki/Statistics.java:125-126',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_STATISTICS', 'SlidingTabLayout$InternalViewPagerListener.onPageScrolled', 'GUI',
  'Swipe between the statistics pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the statistics pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:261-279; SRC com/ichi2/anki/Statistics.java:125-126',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_STATISTICS', 'SlidingTabLayout$InternalViewPagerListener.onPageSelected', 'GUI',
  'Swipe to another statistics page, or tap a tab.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe to another statistics page, or tap a tab.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:291-300, 309; SRC com/ichi2/anki/Statistics.java:125-126',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

# --- UNREACHABLE: no trigger in the app (every call site was grepped over src/main/java).
UNREACHABLE['SlidingTabLayout.<init>(Context)'] = ('no_trigger_in_app',
    'No new SlidingTabLayout(...) with one argument exists in the source root (grep finds no call site). LayoutInflater builds XML views with the (Context, AttributeSet) constructor only, so the one-argument form has no trigger.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:83-85; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setCustomTabColorizer'] = ('no_trigger_in_app',
    'No call site in the source root. The matches are its declaration and SlidingTabStrip.setCustomTabColorizer, a different method on a different class.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:112-114; SRC com/ichi2/ui/SlidingTabStrip.java:90-93',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setCustomTabView'] = ('no_trigger_in_app',
    'No call site in the source root. Without it mTabViewLayoutId stays 0, so the custom-view branch is never taken and createDefaultTabView is always used.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:149-152, 207-212',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setDividerColors'] = ('no_trigger_in_app',
    'No call site in the source root. The matches are its declaration and SlidingTabStrip.setDividerColors, a different method; the SlidingTabStrip calls at lines 75 and 105 are made inside SlidingTabStrip itself.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:128-130; SRC com/ichi2/ui/SlidingTabStrip.java:73-76, 102-106',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setOnPageChangeListener'] = ('no_trigger_in_app',
    'No call site in the source root, so mViewPagerPageChangeListener stays null and the forwarding branches in InternalViewPagerListener are never taken.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:139-141, 275-278, 285-287, 297-299',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setSelectedIndicatorColors'] = ('no_trigger_in_app',
    'No call site in the source root. The only other match is SlidingTabStrip.setSelectedIndicatorColors, a different method.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:120-122; SRC com/ichi2/ui/SlidingTabStrip.java:95-100',
    'SOURCE')

# ---- part 073 (2026-10-28)
# AnkiDroid batch 073 (LABEL helper). CompatV19 and CompatV21 display paths, the CompatV16 openUrl route into the
# Custom Tabs helper, the Custom Tabs service callbacks, CustomDialogPreference and NumberRangePreference: 38 methods.
# The full row list is in graphs/AnkiDroid/parts/label_073.md.
#
# Route ownership:
# - The automatic CALL edges (auto_calls.json) are not written here. The rows name them.
# - Page edges (S_DECKOPTIONS, S_PREFERENCES, S_FILTEREDDECKOPTIONS) into methods of this batch are written here.
# - Edges into CustomTabActivityHelper.bindCustomTabsService (CustomTabActivityHelper.java:96-104) belong to the batch
#   that holds AnkiActivity.onStart. The support-library callbacks therefore have no inbound edge in this part.
# - Preferences.initPreference line 413 calls NumberRangePreference.setValue with no automatic edge. That edge belongs
#   to the batch that holds Preferences.initPreference and is not written here.
# - MG672 is the only MISSING GATE written on an edge here. MG673 to MG675 (Custom Tabs) appear in the rows only.

e('CompatV19$1.<init>', 'CompatV19$1.onSystemUiVisibilityChange', 'REGISTER',
  'decor view listener registered in setFullScreen; the framework calls it when the system UI visibility changes',
  evidence='SRC com/ichi2/compat/CompatV19.java:42-43; FW-SRC core/java/android/view/View.java:22684-22700; FW-SRC core/java/android/view/ViewRootImpl.java:5990-6007',
  note='MISSING GATE MG672: the callback fires when the system bars show or hide (a system or touch event). The app does not drive it and no constant fits, so env and needs_state are unset.')

e('CompatV19$2.<init>', 'CompatV19$2.onAnimationEnd', 'REGISTER',
  'AnimatorListenerAdapter set on the hide animation; the animator calls onAnimationEnd when the fade-out ends',
  evidence='SRC com/ichi2/compat/CompatV19.java:78-88; FW-SRC core/java/android/view/ViewPropertyAnimator.java:375-378, 1112-1122',
  note='setListener (CompatV19.java:82) stores the listener and ViewPropertyAnimator dispatches onAnimationEnd to it (1121-1122). No gate: the animation starts in hideViewWithAnimation.')

e('S_DECKOPTIONS', 'CustomDialogPreference.<init>', 'FRAMEWORK',
  'deck options screen inflates deck_options.xml, which holds the CustomDialogPreference entries',
  evidence='SRC com/ichi2/anki/DeckOptions.java:521-524; SRC res/xml/deck_options.xml:34-55; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at DeckOptions.java:523 inflates the XML. The inflater uses the (Context, AttributeSet) constructor (GenericInflater.java:56-57). No gate.')

e('S_PREFERENCES', 'CustomDialogPreference.<init>', 'FRAMEWORK',
  'advanced preferences subscreen inflates preferences_advanced.xml, which holds the Reset Languages CustomDialogPreference',
  evidence='SRC com/ichi2/anki/Preferences.java:307-309; SRC res/xml/preferences_advanced.xml:106; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at Preferences.java:308. No gate.')

e('S_DECKOPTIONS', 'CustomDialogPreference.onClick', 'GUI',
  'tap a deck option group preference (reset, remove, set subdecks) and then OK on its dialog',
  evidence='SRC com/ichi2/preferences/CustomDialogPreference.java:40-66; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-388',
  gui=['tap a deck option group preference (reset, remove, set subdecks) and then OK on its dialog'],
  note='The preference opens its dialog through DialogPreference.onClick() (274-277) and showDialog (287-296). The positive button calls CustomDialogPreference.onClick (40). The preference title picks the branch (lines 42-56).')

e('S_PREFERENCES', 'CustomDialogPreference.onClick', 'GUI',
  'tap Reset Languages on the advanced preferences screen and then OK on its dialog',
  evidence='SRC com/ichi2/preferences/CustomDialogPreference.java:40-66; SRC res/xml/preferences_advanced.xml:106; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-388',
  gui=['tap Reset Languages on the advanced preferences screen and then OK on its dialog'],
  note='Same dialog path as the deck options edge. Reset Languages takes the else branch (MetaDB.resetLanguages, CustomDialogPreference.java:59).')

e('S_PREFERENCES', 'NumberRangePreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'reviewing preferences subscreen inflates preferences_reviewing.xml, which holds NumberRangePreference entries',
  evidence='SRC com/ichi2/anki/Preferences.java:241-244; SRC res/xml/preferences_reviewing.xml:43-49; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at Preferences.java:243. No gate.')

e('S_DECKOPTIONS', 'NumberRangePreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'deck options screen inflates deck_options.xml, which holds NumberRangePreference entries (lines 76-167)',
  evidence='SRC com/ichi2/anki/DeckOptions.java:521-524; SRC res/xml/deck_options.xml:76-167; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at DeckOptions.java:523. No gate.')

e('S_FILTEREDDECKOPTIONS', 'NumberRangePreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'filtered deck options screen inflates cram_deck_options.xml, which holds one NumberRangePreference (line 26)',
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:376-379; SRC res/xml/cram_deck_options.xml:26; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at FilteredDeckOptions.java:378. No gate.')

e('S_PREFERENCES', 'NumberRangePreference.getPersistedString', 'FRAMEWORK',
  'the screen reads the stored number preference value on load (Preference.dispatchSetInitialValue, then EditTextPreference.onSetInitialValue)',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/Preferences.java:241-244; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; FW-SRC core/java/android/preference/Preference.java:1547-1562; FW-SRC core/java/android/preference/EditTextPreference.java:158-161',
  note='Runs only when the key is stored (Preference.java:1555-1560). If a preference data store is set (1548-1549) the call runs without a stored value; whether DeckOptions sets a data store was not checked.')

e('S_DECKOPTIONS', 'NumberRangePreference.getPersistedString', 'FRAMEWORK',
  'the deck options screen reads the stored number preference value on load',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckOptions.java:521-524; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; FW-SRC core/java/android/preference/Preference.java:1547-1562; FW-SRC core/java/android/preference/EditTextPreference.java:158-161',
  note='Same route as the reviewing screen. The key must be stored (Preference.java:1555-1560). The data-store branch (1548-1549) is not checked.')

e('S_FILTEREDDECKOPTIONS', 'NumberRangePreference.getPersistedString', 'FRAMEWORK',
  'the filtered deck options screen reads the stored number preference value on load',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:376-379; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; FW-SRC core/java/android/preference/Preference.java:1547-1562; FW-SRC core/java/android/preference/EditTextPreference.java:158-161',
  note='Same route as the reviewing screen. The key must be stored (Preference.java:1555-1560). The data-store branch (1548-1549) is not checked.')

e('S_PREFERENCES', 'NumberRangePreference.onDialogClosed', 'GUI',
  'tap a number preference on the reviewing screen, then OK on its dialog',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:58-64; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-396',
  gui=['tap a number preference on the reviewing screen, then OK on its dialog'],
  note='DialogPreference.onDismiss calls onDialogClosed with the positive result (FW-SRC 395). showDialog sets up the dialog (287-296). Lines 61-62 call getValidatedRangeFromString and setValue (automatic edges).')

e('S_DECKOPTIONS', 'NumberRangePreference.onDialogClosed', 'GUI',
  'tap a number on the deck options screen, then OK on its dialog',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:58-64; SRC com/ichi2/anki/DeckOptions.java:521-524; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-396',
  gui=['tap a number on the deck options screen, then OK on its dialog'],
  note='Same dialog path as the reviewing screen (FW-SRC 395 calls onDialogClosed).')

e('S_FILTEREDDECKOPTIONS', 'NumberRangePreference.onDialogClosed', 'GUI',
  'tap a number on the filtered deck options screen, then OK on its dialog',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:58-64; SRC com/ichi2/anki/FilteredDeckOptions.java:376-379; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-396',
  gui=['tap a number on the filtered deck options screen, then OK on its dialog'],
  note='Same dialog path as the reviewing screen (FW-SRC 395 calls onDialogClosed).')

e('NumberRangePreference.setValue', 'NumberRangePreference.persistString', 'FRAMEWORK',
  'setValue writes the value through setText, which persists the text',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:179-183; FW-SRC core/java/android/preference/EditTextPreference.java:88-94',
  note='setValue calls setText (181). EditTextPreference.setText calls persistString (FW-SRC 94), which dispatches to the override at NumberRangePreference.java:81-82 (persistInt). No gate.')

e('CustomTabActivityHelper.onServiceConnected', 'CustomTabActivityHelper.getSession', 'CALL',
  'the Custom Tabs service connected: onServiceConnected calls getSession to create a session',
  evidence='SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:120-125, 83-90',
  note='Direct call at line 124. Not in auto_calls.json: the exact-match inbound query for getSession lists only CompatV16.openUrl (line 79). Gate MG673 applies to the callback, not to this call.')

# UNREACHABLE entries. Source references are printed lines in the .md rows.
UNREACHABLE['CustomTabsHelper.<init>'] = ('no_trigger_in_app', 'private empty constructor; no caller in the source root (grep for "new CustomTabsHelper" and "CustomTabsHelper()" finds only the declaration)', 'com/ichi2/compat/customtabs/CustomTabsHelper.java:47', 'SOURCE')
UNREACHABLE['CustomTabsHelper.getPackages'] = ('no_trigger_in_app', 'no caller in the source root (grep for CustomTabsHelper.getPackages finds only the declaration at line 144)', 'com/ichi2/compat/customtabs/CustomTabsHelper.java:144-146', 'SOURCE')
UNREACHABLE['NumberRangePreference.<init>(Context)'] = ('framework_never_calls', 'the inflater selects constructors with the (Context, AttributeSet) signature only (GenericInflater.java:56-57); no app code calls new NumberRangePreference(context)', 'com/ichi2/preferences/NumberRangePreference.java:50-55; core/java/android/preference/GenericInflater.java:56-57', 'SOURCE')
UNREACHABLE['NumberRangePreference.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'the inflater uses the (Context, AttributeSet) signature only (GenericInflater.java:56-57); the (Context, AttributeSet) constructor calls super(context, attrs) and does not chain to this one; no app caller', 'com/ichi2/preferences/NumberRangePreference.java:34-39; core/java/android/preference/GenericInflater.java:56-57', 'SOURCE')

# ---- part 078 (2026-10-28)
UNREACHABLE['Base64$OutputStream.suspendEncoding'] = ('no_trigger_in_app', 'No code under src/ calls suspendEncoding(); the only hits are the method itself and the boolean field of the same name. The stream class is created only inside the public static methods of com.ichi2.utils.Base64 (encodeObject, encodeBytesToBytes, encodeToFile, decodeToFile), and none of those has a caller under src/ (the name Base64 is referenced in no file under src/ except Base64.java).', 'SRC com/ichi2/utils/Base64.java:466-468, 499-500, 513-514, 680-681, 703-706, 730-731, 757-761, 1232-1241, 1268-1273, 1676-1680, 1860-1881', 'SOURCE')
UNREACHABLE['Base64$OutputStream.write(int)'] = ('no_trigger_in_app', 'The only call of write(int) under src/ is inside write(byte[],int,int) (the loop at com/ichi2/utils/Base64.java:1814). write(byte[],int,int) is used only by the stream writes at Base64.java:761 (gzos.write, the GZIP stream over this stream), 1241 and 1273 (bos.write on this stream), which sit in encodeBytesToBytes, encodeToFile and decodeToFile. Those public static methods have no caller under src/ (the name Base64 is referenced in no file under src/ except Base64.java).', 'SRC com/ichi2/utils/Base64.java:1754-1758, 1806-1816, 757-761, 1232-1241, 1268-1273', 'SOURCE')
UNREACHABLE['Base64$OutputStream.write(byte[],int,int)'] = ('no_trigger_in_app', 'No instance of the stream is created anywhere in the app. It is created only at com/ichi2/utils/Base64.java:514, 758, 1240 and 1272, inside encodeObject, encodeBytesToBytes, encodeToFile and decodeToFile, and none of those public static methods has a caller under src/ (the name Base64 is referenced in no file under src/ except Base64.java). The writes on this stream under src/ are only Base64.java:761 (through the GZIP stream), 1241 and 1273, all inside those methods.', 'SRC com/ichi2/utils/Base64.java:513-514, 757-761, 1232-1241, 1268-1273, 1806-1816', 'SOURCE')

# ---- sup for part 078 (2026-10-28): write(byte[],int,int) is itself UNREACHABLE (its stream is created only in closed Base64 static methods), so its loop call at Base64.java:1814 cannot make write(int) reachable.
sup(('Base64$OutputStream.write(byte[],int,int)', 'Base64$OutputStream.write(int)'))

# ---- part 076 (2026-10-28)
e('S_STATISTICS', 'SlidingTabStrip.onDraw', 'FRAMEWORK',
  'the statistics screen draws its sliding tab strip (the tab underline, bottom border and dividers)',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:86, 125-126; res/layout/activity_anki_stats.xml:18-21 (src/main); SRC com/ichi2/ui/SlidingTabLayout.java:101-102; SRC com/ichi2/ui/SlidingTabStrip.java:62, 115-118; FW-SRC core/java/android/view/ViewGroup.java:4235-4236; FW-SRC core/java/android/view/View.java:9807-9809, 13438-13449, 18833, 19056-19063, 19163, 19188-19192',
  note='The strip is a child of SlidingTabLayout (added at SlidingTabLayout.java:102). The view tree draws it through ViewGroup.drawChild (ViewGroup.java:4235-4236). onDraw runs because setWillNotDraw(false) (SlidingTabStrip.java:62) clears the skip-draw flag (View.java:13438-13449). No gate: the strip draws whenever the statistics screen is shown.')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabStrip.onDraw', 'FRAMEWORK',
  'the card template editor draws its sliding tab strip (the tab underline, bottom border and dividers)',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:130, 231-232; res/layout/card_template_editor_activity.xml:21-24 (src/main); SRC com/ichi2/ui/SlidingTabLayout.java:101-102; SRC com/ichi2/ui/SlidingTabStrip.java:62, 115-118; FW-SRC core/java/android/view/ViewGroup.java:4235-4236; FW-SRC core/java/android/view/View.java:9807-9809, 13438-13449, 18833, 19056-19063, 19163, 19188-19192',
  note='The strip is a child of SlidingTabLayout (added at SlidingTabLayout.java:102). The view tree draws it through ViewGroup.drawChild (ViewGroup.java:4235-4236). onDraw runs because setWillNotDraw(false) (SlidingTabStrip.java:62) clears the skip-draw flag (View.java:13438-13449). No gate: the strip draws whenever the card template editor is shown.')

UNREACHABLE['SlidingTabStrip.blendColors'] = ('branch_never_taken',
  'The only call is at SlidingTabStrip.java:134, inside the branch where color != nextColor (line 133). Both colours come from the same colorizer, and its indicator array has one element: it is set once at line 74 to DEFAULT_SELECTED_INDICATOR_COLOR (line 33). getIndicatorColor returns mIndicatorColors[position % length] (lines 190-192), so nextColor always equals color. mCustomTabColorizer becomes non-null only at line 91, in setCustomTabColorizer, which has no caller. The other writer of the indicator array, setSelectedIndicatorColors, has no caller either.',
  'com/ichi2/ui/SlidingTabStrip.java:33, 74, 90-98, 129-134, 190-192; com/ichi2/ui/SlidingTabLayout.java:112-114, 120-122 (no callers)',
  'SOURCE')

UNREACHABLE['SlidingTabStrip.setCustomTabColorizer'] = ('no_trigger_in_app',
  'The only caller is SlidingTabLayout.setCustomTabColorizer (SlidingTabLayout.java:113). That public method has no caller in the source root: its definition is at line 112, and its own javadoc (lines 105-111) is text, not a call. The layout files name the view only (activity_anki_stats.xml:18-21; card_template_editor_activity.xml:21-24).',
  'com/ichi2/ui/SlidingTabStrip.java:90-93; com/ichi2/ui/SlidingTabLayout.java:105-114; res/layout/activity_anki_stats.xml:18-21 (src/main); res/layout/card_template_editor_activity.xml:21-24 (src/main)',
  'SOURCE')

UNREACHABLE['SlidingTabStrip.setDividerColors'] = ('no_trigger_in_app',
  'The only caller is SlidingTabLayout.setDividerColors (SlidingTabLayout.java:129), which has no caller in the source root: its definition is at line 128, and a link to it at line 109 is javadoc text, not a call.',
  'com/ichi2/ui/SlidingTabStrip.java:102-107; com/ichi2/ui/SlidingTabLayout.java:109, 128-130',
  'SOURCE')

UNREACHABLE['SlidingTabStrip.setSelectedIndicatorColors'] = ('no_trigger_in_app',
  'The only caller is SlidingTabLayout.setSelectedIndicatorColors (SlidingTabLayout.java:121), which has no caller in the source root: its definition is at line 120, and its own javadoc (lines 116-119) and a link at line 109 are text, not calls.',
  'com/ichi2/ui/SlidingTabStrip.java:95-100; com/ichi2/ui/SlidingTabLayout.java:109, 116-122',
  'SOURCE')

UNREACHABLE['Upgrade.<init>'] = ('no_trigger_in_app',
  'Upgrade declares no constructor, so only the implicit default one exists, and no code creates an instance. The class holds only the static method upgradeJSONIfNecessary (Upgrade.java:11). In the source root the class is referenced only by its declaration (Upgrade.java:9), the import (CardBrowser.java:70) and the static call (CardBrowser.java:399).',
  'com/ichi2/upgrade/Upgrade.java:9-11; com/ichi2/anki/CardBrowser.java:70, 399',
  'SOURCE')

# ---- sup for part 076 (2026-10-28): each destination is UNREACHABLE; the call sites are in a branch never taken or in a setter with no caller.
sup(('SlidingTabStrip.onDraw', 'SlidingTabStrip.blendColors'))
sup(('SlidingTabLayout.setCustomTabColorizer', 'SlidingTabStrip.setCustomTabColorizer'))
sup(('SlidingTabLayout.setDividerColors', 'SlidingTabStrip.setDividerColors'))
sup(('SlidingTabLayout.setSelectedIndicatorColors', 'SlidingTabStrip.setSelectedIndicatorColors'))

# ---- part 077 (2026-10-28)
UNREACHABLE['Base64.<clinit>'] = ('no_trigger_in_app', 'Static initializer of Base64 (constants and lookup tables). It runs only when the class is first used, which needs a static member access or an instance from app code. No app source file other than Base64.java names the class.', 'com/ichi2/utils/Base64.java:50-273', 'SOURCE')
UNREACHABLE['Base64.<init>'] = ('no_trigger_in_app', 'Private constructor (defeats instantiation). No code creates an instance: the file has no new Base64(...) and no other file names the class.', 'com/ichi2/utils/Base64.java:311-312', 'SOURCE')
UNREACHABLE['Base64.decode(String)'] = ('no_trigger_in_app', 'No call site. The name occurs only as its declaration and in javadoc, and the class has no caller outside the file.', 'com/ichi2/utils/Base64.java:1049-1051', 'SOURCE')
UNREACHABLE['Base64.decode(String,int)'] = ('no_trigger_in_app', 'Called from decode(String) (line 1050) and from decodeToObject(String,int,ClassLoader) (line 1167). Both callers have no route (see their rows).', 'com/ichi2/utils/Base64.java:1064-1131; call sites 1050, 1167', 'SOURCE')
UNREACHABLE['Base64.decode(byte[])'] = ('no_trigger_in_app', 'No call site. The name occurs only as its declaration, and the class has no caller outside the file.', 'com/ichi2/utils/Base64.java:949-957', 'SOURCE')
UNREACHABLE['Base64.decode(byte[],int,int,int)'] = ('no_trigger_in_app', 'Called from decode(byte[]) (line 952) and from decode(String,int) (line 1080). Both callers have no route.', 'com/ichi2/utils/Base64.java:974-1038; call sites 952, 1080', 'SOURCE')
UNREACHABLE['Base64.decode4to3'] = ('no_trigger_in_app', 'Called from decode(byte[],int,int,int) (line 1018), from Base64$InputStream.read() (line 1589) and from Base64$OutputStream.write(int) (line 1785). read() and write(int) run only on Base64.InputStream and Base64.OutputStream instances, and those are created only in methods with no route (see their rows).', 'com/ichi2/utils/Base64.java:867-936; call sites 1018, 1589, 1785', 'SOURCE')
UNREACHABLE['Base64.decodeFileToFile'] = ('no_trigger_in_app', 'No call site.', 'com/ichi2/utils/Base64.java:1439-1456', 'SOURCE')
UNREACHABLE['Base64.decodeFromFile'] = ('no_trigger_in_app', 'Called only from decodeFileToFile (line 1441), which has no call site.', 'com/ichi2/utils/Base64.java:1300-1343; call site 1441', 'SOURCE')
UNREACHABLE['Base64.decodeToFile'] = ('no_trigger_in_app', 'No call site.', 'com/ichi2/utils/Base64.java:1268-1285', 'SOURCE')
UNREACHABLE['Base64.decodeToObject(String)'] = ('no_trigger_in_app', 'No call site. Its body (line 1146) calls the three-argument overload.', 'com/ichi2/utils/Base64.java:1144-1147; call site 1146', 'SOURCE')
UNREACHABLE['Base64.decodeToObject(String,int,ClassLoader)'] = ('no_trigger_in_app', 'Called only from decodeToObject(String) (line 1146), which has no call site. It also creates the anonymous ObjectInputStream subclass Base64$1 (line 1184).', 'com/ichi2/utils/Base64.java:1163-1216; call site 1146', 'SOURCE')
UNREACHABLE['Base64.encode(ByteBuffer,ByteBuffer)'] = ('no_trigger_in_app', 'No call site.', 'com/ichi2/utils/Base64.java:414-424', 'SOURCE')
UNREACHABLE['Base64.encode(ByteBuffer,CharBuffer)'] = ('no_trigger_in_app', 'No call site.', 'com/ichi2/utils/Base64.java:436-448', 'SOURCE')
UNREACHABLE['Base64.encode3to4(byte[],int,int,byte[],int,int)'] = ('no_trigger_in_app', 'Called from encode3to4(byte[],byte[],int,int) (line 330), from encodeBytesToBytes(byte[],int,int,int) (lines 812 and 823), and from Base64$InputStream.read() (line 1561). Those callers have no route (see their rows).', 'com/ichi2/utils/Base64.java:356-402; call sites 330, 812, 823, 1561', 'SOURCE')
UNREACHABLE['Base64.encode3to4(byte[],byte[],int,int)'] = ('no_trigger_in_app', 'Called from encode(ByteBuffer,ByteBuffer) (line 421), from encode(ByteBuffer,CharBuffer) (line 443), from Base64$OutputStream.write(int) (line 1766) and from flushBase64 (line 1828). The two ByteBuffer methods have no call site, and the two OutputStream methods run only on instances that no route creates.', 'com/ichi2/utils/Base64.java:329-332; call sites 421, 443, 1766, 1828', 'SOURCE')
UNREACHABLE['Base64.encodeBytes(byte[])'] = ('no_trigger_in_app', 'No call site. Its body (line 575) calls the four-argument overload.', 'com/ichi2/utils/Base64.java:569-581; call site 575', 'SOURCE')
UNREACHABLE['Base64.encodeBytes(byte[],int)'] = ('no_trigger_in_app', 'No call site. Its body (line 614) calls the four-argument overload.', 'com/ichi2/utils/Base64.java:613-615; call site 614', 'SOURCE')
UNREACHABLE['Base64.encodeBytes(byte[],int,int)'] = ('no_trigger_in_app', 'No call site. Its body (line 639) calls the four-argument overload.', 'com/ichi2/utils/Base64.java:633-645; call site 639', 'SOURCE')
UNREACHABLE['Base64.encodeBytes(byte[],int,int,int)'] = ('no_trigger_in_app', 'Called from the one-, two- and three-argument encodeBytes overloads (lines 575, 614, 639). Those have no call site.', 'com/ichi2/utils/Base64.java:680-691; call sites 575, 614, 639', 'SOURCE')
UNREACHABLE['Base64.encodeBytesToBytes(byte[])'] = ('no_trigger_in_app', 'No call site. Its body (line 706) calls the four-argument overload.', 'com/ichi2/utils/Base64.java:703-711; call site 706', 'SOURCE')
UNREACHABLE['Base64.encodeBytesToBytes(byte[],int,int,int)'] = ('no_trigger_in_app', 'Called from encodeBytes(byte[],int,int,int) (line 681) and from encodeBytesToBytes(byte[]) (line 706). Both callers have no route.', 'com/ichi2/utils/Base64.java:730-841; call sites 681, 706', 'SOURCE')
UNREACHABLE['Base64.encodeFileToFile'] = ('no_trigger_in_app', 'No call site. Its body (line 1413) calls encodeFromFile.', 'com/ichi2/utils/Base64.java:1411-1428; call site 1413', 'SOURCE')
UNREACHABLE['Base64.encodeFromFile'] = ('no_trigger_in_app', 'Called only from encodeFileToFile (line 1413), which has no call site.', 'com/ichi2/utils/Base64.java:1358-1400; call site 1413', 'SOURCE')
UNREACHABLE['Base64.encodeObject(Serializable)'] = ('no_trigger_in_app', 'No call site. Its body (line 467) calls the two-argument overload.', 'com/ichi2/utils/Base64.java:466-468; call site 467', 'SOURCE')
UNREACHABLE['Base64.encodeObject(Serializable,int)'] = ('no_trigger_in_app', 'Called only from encodeObject(Serializable) (line 467), which has no call site.', 'com/ichi2/utils/Base64.java:499-558; call sites 467, 514, 540', 'SOURCE')
UNREACHABLE['Base64.encodeToFile'] = ('no_trigger_in_app', 'No call site. Its body creates Base64.OutputStream at line 1240.', 'com/ichi2/utils/Base64.java:1232-1253; call site 1240', 'SOURCE')
UNREACHABLE['Base64.getAlphabet'] = ('no_trigger_in_app', 'Private helper. Called only from encode3to4 with six arguments (line 359), which is reached only through encode3to4 with four arguments, which has no route.', 'com/ichi2/utils/Base64.java:283-291; call site 359', 'SOURCE')
UNREACHABLE['Base64.getDecodabet'] = ('no_trigger_in_app', 'Private helper. Called from decode4to3 (line 887), from decode(byte[],int,int,int) (line 993), and from the InputStream and OutputStream two-argument constructors (lines 1529 and 1741). Those callers have no route.', 'com/ichi2/utils/Base64.java:299-307; call sites 887, 993, 1529, 1741', 'SOURCE')
UNREACHABLE['Base64$1.<init>'] = ('no_trigger_in_app', 'Implicit constructor of the anonymous ObjectInputStream subclass, created at line 1184 inside decodeToObject(String,int,ClassLoader). That method is reached only from decodeToObject(String), which has no call site.', 'com/ichi2/utils/Base64.java:1184-1195; call site 1184', 'SOURCE')
UNREACHABLE['Base64$1.resolveClass'] = ('no_trigger_in_app', 'Override in the anonymous ObjectInputStream subclass. Only an instance created at line 1184 can call it, and that code has no route.', 'com/ichi2/utils/Base64.java:1186-1194', 'SOURCE')
UNREACHABLE['Base64$InputStream.<init>(InputStream)'] = ('no_trigger_in_app', 'No call site. The file creates Base64.InputStream only with the two-argument constructor (lines 1319 and 1377).', 'com/ichi2/utils/Base64.java:1494-1496', 'SOURCE')
UNREACHABLE['Base64$InputStream.<init>(InputStream,int)'] = ('no_trigger_in_app', 'Called from decodeFromFile (line 1319) and encodeFromFile (line 1377). Those are reached only from decodeFileToFile (line 1441) and encodeFileToFile (line 1413), which have no call site.', 'com/ichi2/utils/Base64.java:1519-1530; call sites 1319, 1377', 'SOURCE')
UNREACHABLE['Base64$InputStream.read()'] = ('no_trigger_in_app', 'Called from read(byte[],int,int) (line 1652). Instances are created only at lines 1319 and 1377, in methods with no route (see Base64$InputStream.<init>(InputStream,int)).', 'com/ichi2/utils/Base64.java:1540-1634; call site 1652', 'SOURCE')
UNREACHABLE['Base64$InputStream.read(byte[],int,int)'] = ('no_trigger_in_app', 'Called from decodeFromFile (line 1323) and encodeFromFile (line 1381), which have no route.', 'com/ichi2/utils/Base64.java:1648-1663; call sites 1323, 1381', 'SOURCE')
UNREACHABLE['Base64$OutputStream.<init>(OutputStream)'] = ('no_trigger_in_app', 'No call site. The file creates Base64.OutputStream only with the two-argument constructor (lines 514, 758, 1240, 1272).', 'com/ichi2/utils/Base64.java:1705-1707', 'SOURCE')
UNREACHABLE['Base64$OutputStream.<init>(OutputStream,int)'] = ('no_trigger_in_app', 'Called from encodeObject(Serializable,int) (line 514), encodeBytesToBytes(byte[],int,int,int) (line 758), encodeToFile (line 1240) and decodeToFile (line 1272). Those methods have no route.', 'com/ichi2/utils/Base64.java:1730-1742; call sites 514, 758, 1240, 1272', 'SOURCE')
UNREACHABLE['Base64$OutputStream.close'] = ('no_trigger_in_app', 'Called from encodeObject(Serializable,int) (line 540), encodeBytesToBytes(byte[],int,int,int) (line 775), encodeToFile (line 1248) and decodeToFile (line 1280). Those callers have no route.', 'com/ichi2/utils/Base64.java:1845-1855; call sites 540, 775, 1248, 1280', 'SOURCE')
UNREACHABLE['Base64$OutputStream.flushBase64'] = ('no_trigger_in_app', 'Called from close() (line 1847) and suspendEncoding() (line 1866). Both are instance methods of Base64.OutputStream, and no route creates such an instance.', 'com/ichi2/utils/Base64.java:1825-1836; call sites 1847, 1866', 'SOURCE')
UNREACHABLE['Base64$OutputStream.resumeEncoding'] = ('no_trigger_in_app', 'No call site in the file. It is an instance method that only a Base64.OutputStream instance could call, and no route creates one.', 'com/ichi2/utils/Base64.java:1877-1879', 'SOURCE')

# ---- sup for part 077 (2026-10-28): every Base64 method is UNREACHABLE (no app file names Base64), so these bytecode calls between them create no route.
sup(('Base64$OutputStream.<init>(OutputStream,int)', 'Base64.<clinit>'))
sup(('Base64$OutputStream.write(int)', 'Base64.<clinit>'))
sup(('Base64$OutputStream.flushBase64', 'Base64.<clinit>'))
sup(('Base64$InputStream.<init>(InputStream,int)', 'Base64.<clinit>'))
sup(('Base64$InputStream.read()', 'Base64.<clinit>'))
sup(('Base64.decode(String)', 'Base64.decode(String,int)'))
sup(('Base64.decodeToObject(String,int,ClassLoader)', 'Base64.decode(String,int)'))
sup(('Base64.decode(byte[])', 'Base64.decode(byte[],int,int,int)'))
sup(('Base64.decode(String,int)', 'Base64.decode(byte[],int,int,int)'))
sup(('Base64$OutputStream.write(int)', 'Base64.decode4to3'))
sup(('Base64$InputStream.read()', 'Base64.decode4to3'))
sup(('Base64.decode(byte[],int,int,int)', 'Base64.decode4to3'))
sup(('Base64.decodeFileToFile', 'Base64.decodeFromFile'))
sup(('Base64.decodeToObject(String)', 'Base64.decodeToObject(String,int,ClassLoader)'))
sup(('Base64$InputStream.read()', 'Base64.encode3to4(byte[],int,int,byte[],int,int)'))
sup(('Base64.encode3to4(byte[],byte[],int,int)', 'Base64.encode3to4(byte[],int,int,byte[],int,int)'))
sup(('Base64.encodeBytesToBytes(byte[],int,int,int)', 'Base64.encode3to4(byte[],int,int,byte[],int,int)'))
sup(('Base64$OutputStream.write(int)', 'Base64.encode3to4(byte[],byte[],int,int)'))
sup(('Base64$OutputStream.flushBase64', 'Base64.encode3to4(byte[],byte[],int,int)'))
sup(('Base64.encode(ByteBuffer,ByteBuffer)', 'Base64.encode3to4(byte[],byte[],int,int)'))
sup(('Base64.encode(ByteBuffer,CharBuffer)', 'Base64.encode3to4(byte[],byte[],int,int)'))
sup(('Base64.encodeBytes(byte[])', 'Base64.encodeBytes(byte[],int,int,int)'))
sup(('Base64.encodeBytes(byte[],int)', 'Base64.encodeBytes(byte[],int,int,int)'))
sup(('Base64.encodeBytes(byte[],int,int)', 'Base64.encodeBytes(byte[],int,int,int)'))
sup(('Base64.encodeBytes(byte[],int,int,int)', 'Base64.encodeBytesToBytes(byte[],int,int,int)'))
sup(('Base64.encodeBytesToBytes(byte[])', 'Base64.encodeBytesToBytes(byte[],int,int,int)'))
sup(('Base64.encodeFileToFile', 'Base64.encodeFromFile'))
sup(('Base64.encodeObject(Serializable)', 'Base64.encodeObject(Serializable,int)'))
sup(('Base64.encode3to4(byte[],int,int,byte[],int,int)', 'Base64.getAlphabet'))
sup(('Base64$OutputStream.<init>(OutputStream,int)', 'Base64.getDecodabet'))
sup(('Base64$InputStream.<init>(InputStream,int)', 'Base64.getDecodabet'))
sup(('Base64.decode4to3', 'Base64.getDecodabet'))
sup(('Base64.decode(byte[],int,int,int)', 'Base64.getDecodabet'))
sup(('Base64.decodeToObject(String,int,ClassLoader)', 'Base64$1.<init>'))
sup(('Base64$InputStream.<init>(InputStream)', 'Base64$InputStream.<init>(InputStream,int)'))
sup(('Base64.decodeFromFile', 'Base64$InputStream.<init>(InputStream,int)'))
sup(('Base64.encodeFromFile', 'Base64$InputStream.<init>(InputStream,int)'))
sup(('Base64$InputStream.read(byte[],int,int)', 'Base64$InputStream.read()'))
sup(('Base64.decodeFromFile', 'Base64$InputStream.read(byte[],int,int)'))
sup(('Base64.encodeFromFile', 'Base64$InputStream.read(byte[],int,int)'))
sup(('Base64$OutputStream.<init>(OutputStream)', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.encodeObject(Serializable,int)', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.encodeBytesToBytes(byte[],int,int,int)', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.encodeToFile', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.decodeToFile', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.encodeBytesToBytes(byte[],int,int,int)', 'Base64$OutputStream.close'))
sup(('Base64.encodeToFile', 'Base64$OutputStream.close'))
sup(('Base64.decodeToFile', 'Base64$OutputStream.close'))
sup(('Base64$OutputStream.close', 'Base64$OutputStream.flushBase64'))
sup(('Base64$OutputStream.suspendEncoding', 'Base64$OutputStream.flushBase64'))

# ---- part 079 (2026-10-28)
# AnkiDroid batch 079 (LABEL helper). 38 methods; the full row list is in graphs/AnkiDroid/parts/label_079.md.
# This part writes only UNREACHABLE entries (8, all no_trigger_in_app) and no e() edges (0).
# Source paths are relative to final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java.
# Text is repeated inline; no module-level names are defined.

UNREACHABLE['BitmapUtil.<init>'] = ('no_trigger_in_app', 'BitmapUtil has only static methods and no explicit constructor. A grep for new BitmapUtil under the source root finds no call site, so the default constructor is never invoked.', 'SRC com/ichi2/utils/BitmapUtil.java:35-93', 'SOURCE')

UNREACHABLE['ExifUtil.<init>'] = ('no_trigger_in_app', 'ExifUtil has only the static method rotateFromCamera and no explicit constructor. A grep for new ExifUtil under the source root finds no call site.', 'SRC com/ichi2/utils/ExifUtil.java:29-55', 'SOURCE')

UNREACHABLE['HttpUtility.<init>'] = ('no_trigger_in_app', 'HttpUtility has only the static method postReport and no explicit constructor. A grep for new HttpUtility under the source root finds no call site.', 'SRC com/ichi2/utils/HttpUtility.java:18-43', 'SOURCE')

UNREACHABLE['HttpUtility.postReport'] = ('no_trigger_in_app', 'postReport posts feedback reports with DefaultHttpClient. A grep for postReport under the source root finds no call site, so no in-app trigger reaches it.', 'SRC com/ichi2/utils/HttpUtility.java:19-42', 'SOURCE')

UNREACHABLE['LanguageUtil.<init>'] = ('no_trigger_in_app', 'LanguageUtil has only static members and no explicit constructor. A grep for new LanguageUtil under the source root finds no call site.', 'SRC com/ichi2/utils/LanguageUtil.java:27-67', 'SOURCE')

UNREACHABLE['LanguageUtil.getLocale()'] = ('no_trigger_in_app', 'The only caller under the source root is Utils.fmtPercentage(Double,int) at line 229. That method is called only from fmtPercentage(Double) at Utils.java:224, and no code under the source root calls fmtPercentage(Double), so the chain has no in-app trigger.', 'SRC com/ichi2/utils/LanguageUtil.java:41-43; SRC com/ichi2/libanki/Utils.java:223-232', 'SOURCE')

UNREACHABLE['DiffEngine$DiffAction.equals'] = ('no_trigger_in_app', 'The equals override runs only when a DiffAction is compared with equals, or through a collection contains, remove or indexOf. A grep under the source root finds no such comparison: the contains and remove calls act on Long sets and iterators, and DiffAction objects are compared by reference only.', 'SRC com/ichi2/utils/DiffEngine.java:1158-1164', 'SOURCE')

UNREACHABLE['DiffEngine$DiffAction.toString'] = ('no_trigger_in_app', 'The toString override runs only when a DiffAction is converted to a String implicitly (string concatenation, String.valueOf, print or log). A grep under the source root finds no such conversion; the diff results are read through the operation and text fields only.', 'SRC com/ichi2/utils/DiffEngine.java:1145-1148', 'SOURCE')

# ---- sup for part 079 (2026-10-28): Utils.fmtPercentage(Double,int) has no caller (its only caller fmtPercentage(Double) has none), so its call to getLocale is not on any route.
sup(('libanki.Utils.fmtPercentage(Double,int)', 'LanguageUtil.getLocale()'))

# ---- part 080 (2026-10-28)
# AnkiDroid batch 080 (LABEL helper). MethodLogger, Threads, VersionUtils, WidgetStatus (with UpdateDeckStatusAsyncTask),
# AnkiExporter and AnkiPackageExporter (APKG export). 34 methods; the full row list is in graphs/AnkiDroid/parts/label_080.md.
#
# Route ownership: the two INTENT edges from WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute are written here (the source
# is in this batch). The ASYNC edge into onPostExecute is written by the batch that contains WidgetStatus.update. Automatic CALL
# edges come from auto_calls.json and are not written here. Gate: STATE_SETTINGS (widget and notification preferences).
# No MG id is needed.

e('WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute', 'AnkiDroidWidgetSmall$UpdateService.<init>', 'INTENT',
  'the status task starts the small widget service when the widget preference is enabled',
  guard='sSmallWidgetEnabled is true (set in WidgetStatus.update from widgetSmallEnabled, WidgetStatus.java:55); the start is at WidgetStatus.java:106-110',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/widget/WidgetStatus.java:55, 106-110; SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:77',
  note='Explicit intent start (WidgetStatus.java:108-109). The framework creates the service through its constructor; the next hop UpdateService.onStart is the LIFECYCLE edge in label_018.py. Gate STATE_SETTINGS (widget preference). env None: the start needs no outside event.')

e('WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute', 'NotificationService.<init>', 'INTENT',
  'the status task starts the notification service when the notification preference is enabled',
  guard='sNotificationEnabled is true (set in WidgetStatus.update from minimumCardsDueForNotification, WidgetStatus.java:56); the start is at WidgetStatus.java:111-115',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/widget/WidgetStatus.java:56, 111-115; SRC com/ichi2/anki/services/NotificationService.java:37',
  note='Explicit intent start (WidgetStatus.java:113-114). The framework creates the service through its constructor; the next hops NotificationService.onCreate and onStartCommand are the FRAMEWORK edge in label_049.py. Gate STATE_SETTINGS (notification preference). env None: the start needs no outside event.')

UNREACHABLE['MethodLogger.<init>'] = ('no_trigger_in_app', 'Private constructor of a static utility class. grep for new MethodLogger over the source root finds nothing.', 'SRC com/ichi2/utils/MethodLogger.java:42-45', 'SOURCE')

UNREACHABLE['MethodLogger.log()'] = ('branch_never_taken', 'The seven callers in BaseAsyncTask are MethodLogger.log() calls inside if (DEBUG) blocks. DEBUG is the constant false, so the calls never run and javac emits no bytecode for them. No other caller exists in the source root.', 'SRC com/ichi2/async/BaseAsyncTask.java:27, 39-40, 47-48, 56-57, 66-67, 76-77, 86-87, 96-97; SRC com/ichi2/utils/MethodLogger.java:61-63', 'SOURCE')

UNREACHABLE['MethodLogger.log(String)'] = ('no_trigger_in_app', 'No call site. The source root has no call to log(String). MethodLogger.java:36 is a javadoc example, not code, and the BaseAsyncTask calls use log() with no argument.', 'SRC com/ichi2/utils/MethodLogger.java:36, 53-55; SRC com/ichi2/async/BaseAsyncTask.java:40', 'SOURCE')

UNREACHABLE['MethodLogger.logInternal'] = ('no_trigger_in_app', 'Private helper. Its callers are log(String), which has no call site, and log(), which is reached only under the constant-false DEBUG branch. No trigger in the app reaches it.', 'SRC com/ichi2/utils/MethodLogger.java:54, 62, 73-107', 'SOURCE')

UNREACHABLE['Threads.<init>'] = ('no_trigger_in_app', 'Private constructor of a static utility class. grep for new Threads over the source root finds nothing.', 'SRC com/ichi2/utils/Threads.java:26-27', 'SOURCE')

UNREACHABLE['Threads.newCurrentThreadChecker'] = ('no_trigger_in_app', 'Factory with no caller in the source root. grep for newCurrentThreadChecker finds only its declaration.', 'SRC com/ichi2/utils/Threads.java:59-60', 'SOURCE')

UNREACHABLE['Threads.newLazySingleThreadChecker'] = ('no_trigger_in_app', 'Factory with no caller in the source root. grep for newLazySingleThreadChecker finds only its declaration.', 'SRC com/ichi2/utils/Threads.java:69-70', 'SOURCE')

UNREACHABLE['Threads.newSingleThreadChecker'] = ('no_trigger_in_app', 'Factory with no caller in the source root. grep for newSingleThreadChecker and SingleThreadChecker finds only Threads.java.', 'SRC com/ichi2/utils/Threads.java:48-52', 'SOURCE')

UNREACHABLE['Threads$SingleThreadChecker.<init>'] = ('no_trigger_in_app', 'Private constructor. Its only callers are the three factories above (Threads.java:52, 60, 70), and none of those factories has a caller.', 'SRC com/ichi2/utils/Threads.java:52, 60, 70, 123-124', 'SOURCE')

UNREACHABLE['Threads$SingleThreadChecker.checkThread'] = ('no_trigger_in_app', 'No call site in the source root (grep for checkThread finds only Threads.java). The checker object is built only by the unreached factories.', 'SRC com/ichi2/utils/Threads.java:129-136', 'SOURCE')

UNREACHABLE['VersionUtils.<init>'] = ('no_trigger_in_app', 'No explicit constructor (VersionUtils.java:14 is the class line; the implicit constructor is never used). grep for new VersionUtils finds nothing, and every caller uses a static method.', 'SRC com/ichi2/utils/VersionUtils.java:14', 'SOURCE')

UNREACHABLE['WidgetStatus.<init>'] = ('no_trigger_in_app', 'Private constructor ("This class should not be instantiated"). grep for new WidgetStatus finds nothing.', 'SRC com/ichi2/widget/WidgetStatus.java:46-47', 'SOURCE')

# ---- sup for part 080 (2026-10-28): each source is UNREACHABLE (MethodLogger.log/log(String) have no live caller; the Threads factories have no caller), so these bytecode calls are not on any route.
sup(('MethodLogger.log(String)', 'MethodLogger.logInternal'))
sup(('MethodLogger.log()', 'MethodLogger.logInternal'))
sup(('Threads.newSingleThreadChecker', 'Threads$SingleThreadChecker.<init>'))
sup(('Threads.newCurrentThreadChecker', 'Threads$SingleThreadChecker.<init>'))
sup(('Threads.newLazySingleThreadChecker', 'Threads$SingleThreadChecker.<init>'))

# ---- part 081 (2026-10-28)
# AnkiDroid batch 081 (LABEL helper). libanki Card, part 1 of 2: 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_081.md. This part writes one UNREACHABLE entry (Card.getCol). The other 39 methods
# are REACHABLE through builder CALL edges (not written here). No e() edges are written in this part.

UNREACHABLE['Card.getCol'] = ('no_trigger_in_app',
  "Card.getCol() has no caller in src/main with a Card receiver. Its comment says Needed for tests. "
  "All 13 call sites of getCol() in src/main are on activity receivers, not on a Card: "
  "CompatV10.java:170; CardTemplateEditor.java:386, 451, 601, 609, 641, 662, 676, 697, 698; "
  "DialogHandler.java:94; CustomStudyDialog.java:148, 330. No class extends Card, so no app trigger reaches it.",
  'SRC com/ichi2/libanki/Card.java:604-607; SRC com/ichi2/compat/CompatV10.java:168-171; '
  'SRC com/ichi2/anki/CardTemplateEditor.java:384-387, 449-452, 599-610, 639-642, 660-663, 674-677, 695-699; '
  'SRC com/ichi2/anki/dialogs/DialogHandler.java:92-95; SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:146-149, 328-331',
  'SOURCE')

# ---- part 082 (2026-10-28)
# AnkiDroid batch 082 (LABEL helper): libanki Card methods, part 2 of 2 (27 methods).
# The row list is in graphs/AnkiDroid/parts/label_082.md.
# No e() edges: the setters and the other Card methods own no outgoing edges except automatic CALL edges,
# and the edges into them come from callers owned by other batches (Sched, DeckTask, AbstractFlashcardViewer,
# CardContentProvider, NoteEditor, Collection, CardBrowser).

UNREACHABLE['Card.setCol'] = ('no_trigger_in_app',
  'Only the declaration exists in the source root. The method is marked "Needed for tests", so its only caller would be test code, which is not in the app. A grep for setCol over the source root finds no other call.',
  'com/ichi2/libanki/Card.java:610-613', 'SOURCE')

UNREACHABLE['Card.shouldShowTimer'] = ('no_trigger_in_app',
  'Declared at Card.java 365-372. No call site exists in the source root (grep for the call finds none). The viewer asks showTimer instead (AbstractFlashcardViewer.java 1885).',
  'com/ichi2/libanki/Card.java:365-372; com/ichi2/anki/AbstractFlashcardViewer.java:1883-1886', 'SOURCE')

UNREACHABLE['Card.toString'] = ('no_trigger_in_app',
  'Overrides Object.toString. No explicit call and no implicit string conversion of a libanki Card was found in the source root. The one Card concatenation (AdvancedStatistics.java 1499) uses the inner class Card of AdvancedStatistics, which has its own toString. Confidence is moderate.',
  'com/ichi2/libanki/Card.java:634-648; com/ichi2/libanki/hooks/AdvancedStatistics.java:1497-1500', 'SOURCE')

# ---- part 083 (2026-10-28)
# AnkiDroid batch 083 (LABEL helper). CardStats (com/ichi2/libanki/CardStats.java; the batch file says com.ichi2.anki).
# Methods: CardStats.<init> and CardStats.report. Both are UNREACHABLE (no_trigger_in_app). No e() edges in this part.
# Gates: none (no MG ids used). The outgoing calls of report are the builder's automatic CALL edges and are not repeated here.

# --- CardStats.<init>: the class declares no constructor; no code creates an instance (grep over src/main/java).
UNREACHABLE['CardStats.<init>'] = ('no_trigger_in_app',
  "CardStats declares no constructor, so its only constructor is the implicit default one. No code creates an instance: "
  "grep -rn CardStats over the source root (src/main/java) returns only the class declaration at CardStats.java:12, and no other "
  "file in the app folder names the class (the build output holds only its own compiled class). The class has only the static "
  "method report, which has no caller either (see CardStats.report). So the constructor is never run.",
  "SRC com/ichi2/libanki/CardStats.java:12; SRC com/ichi2/libanki/CardStats.java:14-123",
  'SOURCE')

# --- CardStats.report: the only method of the class (static, lines 14-123). No call site in the source root.
UNREACHABLE['CardStats.report'] = ('no_trigger_in_app',
  "report is the only method of CardStats and it is static. No call site exists: grep -rn CardStats over the source root "
  "returns only the class declaration at CardStats.java:12. A call from another class has to name CardStats (a qualified "
  "call, a static import or a subclass), and no such reference exists. The build output holds only the class's own compiled "
  "file. Nothing in the app reaches report from an entry point, so it never runs.",
  "SRC com/ichi2/libanki/CardStats.java:12; SRC com/ichi2/libanki/CardStats.java:14-123",
  'SOURCE')

# ---- part 086 (2026-10-28)
# AnkiDroid batch 086 (LABEL helper): libanki Consts and DB, 4 methods. Rows are in graphs/AnkiDroid/parts/label_086.md.
# No e() edges in this part. Outgoing calls are automatic CALL edges (builder). Incoming edges belong to other batches.
# MISSING GATE MG802 (for the FRAMEWORK edge DB.<init> -> DB$MyDbErrorHandler.onCorruption, owned by the batch that holds DB.<init>):
#   the collection file is damaged, so SQLite reports corruption and calls DatabaseErrorHandler.onCorruption.

UNREACHABLE['Consts.<init>'] = ('no_trigger_in_app', "Consts only declares static final fields and has no constructor, so Consts.<init> is the implicit default constructor. No code creates an instance: a grep over the source root for new Consts, Consts() and extends Consts finds nothing, and the other references are imports or Consts.NAME static reads.", 'SRC com/ichi2/libanki/Consts.java:19-71', 'SOURCE')
UNREACHABLE['DB.getPath'] = ('no_trigger_in_app', "DB.getPath has no call site in the app. The only getPath() calls inside DB are mDatabase.getPath() on the SQLiteDatabase (DB.java:100, 353), which are not DB.getPath. The other getPath() call sites in the source root are listed in the source reference (printed): none of their receivers is a DB, since a grep for getDb().getPath, db.getPath, mDb.getPath, tempDb.getPath and DB::getPath finds nothing.", 'SRC com/ichi2/libanki/DB.java:352-354, 100; com/ichi2/libanki/Collection.java:1635-1637; com/ichi2/anki/Preferences.java:757; com/ichi2/async/DeckTask.java:763; com/ichi2/anki/BackupManager.java:171, 223, 242, 346; com/ichi2/anki/DeckPicker.java:807, 1595, 1619; com/ichi2/anki/IntentHandler.java:95; com/ichi2/anki/AnkiFont.java:143; com/ichi2/anki/CustomExceptionHandler.java:67, 76; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:121; com/ichi2/anki/provider/CardContentProvider.java:1298; com/ichi2/anki/dialogs/DatabaseErrorDialog.java:259; com/ichi2/utils/ExifUtil.java:33; com/ichi2/libanki/Sound.java:286; com/ichi2/libanki/AnkiPackageExporter.java:325, 337, 364; com/ichi2/libanki/importer/AnkiPackageImporter.java:51; com/ichi2/libanki/sync/FullSyncer.java:93, 155; com/ichi2/libanki/sync/RemoteMediaServer.java:117; com/ichi2/libanki/Media.java:121, 801', 'SOURCE')

# ---- part 084 (2026-10-28)
# AnkiDroid batch 084 (LABEL helper): libanki Collection methods, part 1 of 2 (40 methods).
# The row list is in graphs/AnkiDroid/parts/label_084.md.
# No e() edges: none of the 40 methods owns a source-side gate; they are callees of other owners' methods.
# The 13 UNREACHABLE entries are below; each reason is repeated inline.

UNREACHABLE['Collection.<init>(Context,DB,String)'] = ('no_trigger_in_app',
  'The body only calls this(context, db, path, false). The source root has no call with three arguments: the one constructor call is Storage.java line 63, which passes five arguments. No other constructor calls this one.',
  'com/ichi2/libanki/Collection.java:129-131; com/ichi2/libanki/Storage.java:63', 'SOURCE')

UNREACHABLE['Collection.<init>(Context,DB,String,boolean)'] = ('no_trigger_in_app',
  'The body calls this(context, db, path, false, false), so the server argument is dropped (passed as false). The only caller of this constructor is the three-argument constructor, which has no caller itself. Storage uses the five-argument form.',
  'com/ichi2/libanki/Collection.java:133-135; com/ichi2/libanki/Collection.java:129-131; com/ichi2/libanki/Storage.java:63', 'SOURCE')

UNREACHABLE['Collection._qaData()'] = ('no_trigger_in_app',
  'No caller in the source root. The one-argument _qaData(String) is called from this method (Collection.java:1030) and from renderQA(int[],String) (Collection.java:951). renderQA() (Collection.java:932) and renderQA(int[],String) have no caller in the source root, so no entry point reaches either.',
  'com/ichi2/libanki/Collection.java:1029-1031; com/ichi2/libanki/Collection.java:930-938; com/ichi2/libanki/Collection.java:951', 'SOURCE')

UNREACHABLE['Collection._qaData(String)'] = ('no_trigger_in_app',
  'Called only from _qaData() (Collection.java:1030) and from renderQA(int[],String) (Collection.java:951). Neither caller is reached from an entry point (see _qaData() and renderQA above).',
  'com/ichi2/libanki/Collection.java:1034-1036; com/ichi2/libanki/Collection.java:1030; com/ichi2/libanki/Collection.java:951', 'SOURCE')

UNREACHABLE['Collection.emptyCardReport'] = ('no_trigger_in_app',
  'Declared at Collection.java:868. No call exists in the source root (grep for emptyCardReport finds only the declaration). The find-empty-cards task calls emptyCids (DeckTask.java:1230) and not this method.',
  'com/ichi2/libanki/Collection.java:868-870; com/ichi2/async/DeckTask.java:1226-1234', 'SOURCE')

UNREACHABLE['Collection.findCards(String)'] = ('no_trigger_in_app',
  'No caller in the source root. The one Collection.findCards call site found is Sched.java:1569, which passes two arguments (search, orderlimit) and so uses findCards(String,String). No call uses the one-argument form.',
  'com/ichi2/libanki/Collection.java:1059-1061; com/ichi2/libanki/Sched.java:1569', 'SOURCE')

UNREACHABLE['Collection.findDupes(String)'] = ('no_trigger_in_app',
  'No caller in the source root. The grep for findDupes finds only the declarations in Collection.java and the Finder helpers, which are called only from the Collection overloads.',
  'com/ichi2/libanki/Collection.java:1101-1103; com/ichi2/libanki/Finder.java:955-957', 'SOURCE')

UNREACHABLE['Collection.findDupes(String,String)'] = ('no_trigger_in_app',
  'No caller in the source root. The one-argument overload calls Finder.findDupes directly (Collection.java:1102), not this overload. Finder.findDupes(Collection,String,String) is called only from Collection.',
  'com/ichi2/libanki/Collection.java:1106-1108; com/ichi2/libanki/Collection.java:1102; com/ichi2/libanki/Finder.java:963', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String)'] = ('no_trigger_in_app',
  'No caller in the source root. The Finder static overloads are called only from the Collection overloads, and none of those has a caller.',
  'com/ichi2/libanki/Collection.java:1081-1083; com/ichi2/libanki/Finder.java:806-810', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String,String)'] = ('no_trigger_in_app',
  'No call site in the source root. The Finder overload with a field argument (Finder.java:818-820) is called only from this Collection overload.',
  'com/ichi2/libanki/Collection.java:1091-1093; com/ichi2/libanki/Finder.java:818-820', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String,boolean)'] = ('no_trigger_in_app',
  'No call site in the source root. The Finder overload with a regex flag (Finder.java:813-815) is called only from this Collection overload.',
  'com/ichi2/libanki/Collection.java:1086-1088; com/ichi2/libanki/Finder.java:813-815', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String,boolean,String,boolean)'] = ('no_trigger_in_app',
  'No call site in the source root. The full Finder.findReplace (Finder.java:823-826) is called only from the Collection overloads.',
  'com/ichi2/libanki/Collection.java:1096-1098; com/ichi2/libanki/Finder.java:823-826', 'SOURCE')

UNREACHABLE['Collection.getTimeLimit'] = ('no_trigger_in_app',
  'Declared at Collection.java:1131; it reads the timeLim configuration value. No call exists in the source root (grep for getTimeLimit finds only the declaration).',
  'com/ichi2/libanki/Collection.java:1131-1139', 'SOURCE')

# ---- part 085 (2026-10-28)
# AnkiDroid batch 085 (LABEL helper): libanki Collection methods, part 2 (33 methods; 10 UNREACHABLE here).
# The row list is in graphs/AnkiDroid/parts/label_085.md.
# No e() edges: none of these methods is the source of a GUI, ASYNC, INTENT, RESULT or framework edge.
# The routes into the REACHABLE methods are automatic CALL edges from app code (not repeated) or belong to other batches.

UNREACHABLE['Collection.name'] = ('no_trigger_in_app',
  'Declared at Collection.java 169-172 (returns the file name without the .anki2 extension). The grep for .name() over the source root finds no call on a Collection. The only matches are Enum.name() calls on mChartType in AnkiStatsTaskHandler.java 101 and 104, which are a different method.',
  'com/ichi2/libanki/Collection.java:169-172; com/ichi2/anki/stats/AnkiStatsTaskHandler.java:101-104', 'SOURCE')

UNREACHABLE['Collection.noteCount'] = ('no_trigger_in_app',
  'Declared at Collection.java 478-480. The grep for noteCount over the source root finds only this declaration, so nothing calls it.',
  'com/ichi2/libanki/Collection.java:478-480', 'SOURCE')

UNREACHABLE['Collection.setTimeLimit'] = ('no_trigger_in_app',
  'Declared at Collection.java 1122-1124 (writes timeLim to the collection config). The grep for setTimeLimit over the source root finds only this declaration.',
  'com/ichi2/libanki/Collection.java:1122-1124', 'SOURCE')

UNREACHABLE['Collection.save(long)'] = ('no_trigger_in_app',
  'Declared at Collection.java 252-254; it calls save(null, mod) at 253. No caller passes a single long to Collection.save. The calls to save() with no argument (Collection.java 248, 299, 1347) go to the no-argument overload. The only two-argument call on a Collection is Syncer.java 432, which is save(String, long). The grep for save with an argument over the source root finds no other match.',
  'com/ichi2/libanki/Collection.java:247-254; com/ichi2/libanki/sync/Syncer.java:432', 'SOURCE')

UNREACHABLE['Collection.renderQA()'] = ('no_trigger_in_app',
  'Declared at Collection.java 932-934; it calls renderQA(null, card) at 933. The grep for renderQA over the source root finds no call of renderQA() with no arguments. The other matches are _renderQA in Card.java 303-308 and Models.java 1081-1114, which are different methods.',
  'com/ichi2/libanki/Collection.java:932-934; com/ichi2/libanki/Card.java:303-308; com/ichi2/libanki/Models.java:1081-1114', 'SOURCE')

UNREACHABLE['Collection.renderQA(int[],String)'] = ('no_trigger_in_app',
  'Declared at Collection.java 937-959. Its only call is renderQA(null, card) at 933, inside renderQA(), which has no caller. The grep for renderQA finds no other call of this overload.',
  'com/ichi2/libanki/Collection.java:933-959', 'SOURCE')

UNREACHABLE['Collection.previewCards(Note)'] = ('no_trigger_in_app',
  'Declared at Collection.java 746-748; it calls previewCards(note, 0) at 747. The grep for previewCards over the source root finds only the two declarations (717 and 746) and the call at 747. No caller exists.',
  'com/ichi2/libanki/Collection.java:746-748', 'SOURCE')

UNREACHABLE['Collection.previewCards(Note,int)'] = ('no_trigger_in_app',
  'Declared at Collection.java 717-745. Its only call is previewCards(note, 0) at 747, inside previewCards(Note), which has no caller.',
  'com/ichi2/libanki/Collection.java:717-747', 'SOURCE')

UNREACHABLE['Collection.newNote()'] = ('no_trigger_in_app',
  'Declared at Collection.java 486-488; it calls newNote(true) at 487. The grep for newNote over the source root finds no call with no arguments. The only call of a newNote overload outside Collection is CardTemplateEditor.java 530, which passes a model (newNote(JSONObject)).',
  'com/ichi2/libanki/Collection.java:486-488; com/ichi2/anki/CardTemplateEditor.java:530', 'SOURCE')

UNREACHABLE['Collection.newNote(boolean)'] = ('no_trigger_in_app',
  'Declared at Collection.java 496-498. Its only caller is newNote() at 487, which has no caller, so this overload is never reached. The grep finds no other call with a boolean argument.',
  'com/ichi2/libanki/Collection.java:487; com/ichi2/libanki/Collection.java:496-498', 'SOURCE')
