import re
import sys

MD = '/Users/darshan/Desktop/yang/work/graphs/AnkiDroid/parts/label_035.md'
PATHS = {
    'MyAccount.java': 'com/ichi2/anki/MyAccount.java',
    'DeckPicker.java': 'com/ichi2/anki/DeckPicker.java',
    'Connection.java': 'com/ichi2/async/Connection.java',
    'HttpSyncer.java': 'com/ichi2/libanki/sync/HttpSyncer.java',
}
BARE = re.compile(r'(?<![/\w])(' + '|'.join(re.escape(k) for k in PATHS) + r')(?=:\d)')

lines = open(MD, encoding='utf-8').read().split('\n')
changed = 0
out = []
for line in lines:
    if line.startswith('|'):
        parts = line.split('|')
        if len(parts) == 7:
            new = BARE.sub(lambda m: 'SRC ' + PATHS[m.group(1)], parts[5])
            if new != parts[5]:
                changed += 1 + new.count('SRC ') - parts[5].count('SRC ') - 1
                parts[5] = new
            line = '|'.join(parts)
    out.append(line)
open(MD, 'w', encoding='utf-8').write('\n'.join(out))
print('source cells rewritten: citations changed', changed)
sys.exit(0)
