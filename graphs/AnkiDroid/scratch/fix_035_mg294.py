import sys

BASE = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/parts/label_035'
EDITS = {
    '.md': [
        ('MG294 (login reply of 1024 bytes or more before the progress callback, no constant)',
         'MG294 (request or reply of 1024 bytes or more before the progress callback, no constant)'),
        ('The publish runs only when bytesReceived reaches the 1024 threshold (HttpSyncer.java:93-94, 312): MISSING GATE MG294, because a short login reply never publishes.',
         'The publish runs only when bytesReceived or bytesSent reaches the 1024 threshold (HttpSyncer.java:93-94, 312); the request-body writer also publishes (HttpSyncer.java:400): MISSING GATE MG294. A standard login (short JSON request, short reply) never publishes.'),
        ('SRC com/ichi2/libanki/sync/HttpSyncer.java:286-319 (printed 286-325)',
         'SRC com/ichi2/libanki/sync/HttpSyncer.java:286-319, 393-402 (printed 286-325, 386-402)'),
        ('MG294 (reply of at least 1024 bytes) in note.',
         'MG294 (request or reply of at least 1024 bytes) in note.'),
    ],
    '.py': [
        ('MG294 (login reply of at least 1024 bytes before the progress callback)',
         'MG294 (request or reply of at least 1024 bytes before the progress callback)'),
        ('MISSING GATE MG294: the progress publish runs only when bytesReceived reaches 1024 (HttpSyncer.java:93-94, 300-301, 312), so a login reply shorter than 1024 bytes never reaches this callback.',
         'MISSING GATE MG294: the progress publish runs only when bytesReceived or bytesSent reaches 1024 (HttpSyncer.java:93-94, 312; the request-body writer calls publishProgress at HttpSyncer.java:400), so a login whose request and reply are both under 1024 bytes never reaches this callback.'),
        ('SRC com/ichi2/libanki/sync/HttpSyncer.java:291-319; SRC com/ichi2/async/Connection.java:196-225, 471-472',
         'SRC com/ichi2/libanki/sync/HttpSyncer.java:291-319, 393-402; SRC com/ichi2/async/Connection.java:196-225, 471-472'),
    ],
}

for ext, pairs in EDITS.items():
    path = BASE + ext
    text = open(path, encoding='utf-8').read()
    for old, new in pairs:
        n = text.count(old)
        if n != 1:
            print('NOT UNIQUE/FOUND (%d) in %s: %s' % (n, path, old[:70]))
            sys.exit(1)
        text = text.replace(old, new)
    open(path, 'w', encoding='utf-8').write(text)
    print('applied %d edits to %s' % (len(pairs), path))
