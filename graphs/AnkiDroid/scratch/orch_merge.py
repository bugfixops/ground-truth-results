import datetime
import re
import shutil
import subprocess
import sys

W = '/Users/darshan/Desktop/yang/work'
APP = W + '/graphs/AnkiDroid'
n, b = sys.argv[1], sys.argv[2]
g = APP + '/graph_def.py'
shutil.copy(g, APP + '/scratch/graph_def_before_part%s.py' % n)
body = open(APP + '/parts/label_%s.py' % n, encoding='utf-8').read()
with open(g, 'a', encoding='utf-8') as f:
    f.write('\n# ---- part %s (%s)\n' % (n, datetime.date.today().isoformat()))
    f.write(body if body.endswith('\n') else body + '\n')
compile(open(g, encoding='utf-8').read(), g, 'exec')
r = subprocess.run(['python3', '-I', W + '/tools/build_graph.py', APP, 'ankidroid'],
                   cwd=W, capture_output=True, text=True)
text = r.stdout + r.stderr
open(APP + '/scratch/build_%s.txt' % b, 'w', encoding='utf-8').write(text)
print('merged', n, 'build', b, 'exit', r.returncode)
for line in text.splitlines():
    if re.match(r'^(methods|verdicts|errors|warnings)', line):
        print(line)
