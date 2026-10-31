import re, sys

ROOT = '/Users/darshan/Desktop/yang/work/final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/com/ichi2/'
FILES = {
    'AbstractFlashcardViewer': 'anki/AbstractFlashcardViewer.java',
    'LanguagesListerGlosbe': 'anki/multimediacard/language/LanguagesListerGlosbe.java',
    'Meaning': 'anki/multimediacard/glosbe/json/Meaning.java',
    'Phrase': 'anki/multimediacard/glosbe/json/Phrase.java',
    'Response': 'anki/multimediacard/glosbe/json/Response.java',
    'ModelEditorContextMenu': 'anki/dialogs/ModelEditorContextMenu.java',
    'NotificationService': 'anki/services/NotificationService.java',
    'Previewer': 'anki/Previewer.java',
    'Sched': 'libanki/Sched.java',
    'SlidingTabLayout': 'ui/SlidingTabLayout.java',
    'Statistics': 'anki/Statistics.java',
    'VideoPlayer': 'anki/VideoPlayer.java',
    'Utils': 'libanki/Utils.java',
}
PAT = re.compile(sys.argv[1]) if len(sys.argv) > 1 else None
only = sys.argv[2:] if len(sys.argv) > 2 else list(FILES)
for name in only:
    path = ROOT + FILES[name]
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    print('== %s (%s) %d lines' % (name, FILES[name], len(lines)))
    for i, l in enumerate(lines, 1):
        if PAT is None or PAT.search(l):
            print('  %d: %s' % (i, l[:170]))
