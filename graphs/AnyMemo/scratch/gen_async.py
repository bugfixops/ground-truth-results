# Generates ASYNC edges for AsyncTask subclasses from the execute / cancel sites in auto_calls.json (framework_calls).
# Each generated line carries the source line of the execute() call and of the callback it reaches.
import json, os, re, subprocess
G = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/'
SRCROOT = '/Users/darshan/Desktop/yang/final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/java/org/liberty/android/fantastischmemo/'
A = json.load(open(G + 'auto_calls.json'))
M = json.load(open(G + 'method_list.json'))
names = set()
for r in M:
    names.add(r['short'])
gd = open(G + 'graph_def.py', encoding='utf-8').read()
def file_of(outer):
    out = subprocess.run(['find', SRCROOT, '-name', outer + '.java'], capture_output=True, text=True).stdout.split()
    return out[0] if len(out) == 1 else None
def rel(p):
    return os.path.relpath(p, SRCROOT) if p else None
def find_line(path, pattern, after=None):
    if not path:
        return None
    lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
    start = 0
    if after:
        for i, l in enumerate(lines):
            if re.search(after, l):
                start = i
                break
    for i in range(start, len(lines)):
        if re.search(pattern, lines[i]):
            return i + 1
    return None
def task_outer(t):
    return t.split('$')[0] if '$' in t else t.split('.')[0]
sites, cancels = [], []
for m, calls in A['framework_calls'].items():
    for x in calls:
        if x.endswith('.execute') or x.endswith('.executeOnExecutor'):
            t = x.rsplit('.', 1)[0]
            if t + '.doInBackground' in names or t + '.onPreExecute' in names:
                sites.append((m, t))
        if x.endswith('.cancel'):
            t = x.rsplit('.', 1)[0]
            if t + '.onCancelled' in names or t + '.doInBackground' in names:
                cancels.append((m, t))
sites = sorted(set(sites)); cancels = sorted(set(cancels))
print('execute sites', len(sites), 'cancel sites', len(cancels))
out = []
def pair_in_graph(s, d):
    return ("'%s', '%s'" % (s, d)) in gd
for m, t in sites:
    mo = m.split('.')[0]
    mfile = file_of(task_outer(mo))
    tsimple = t.split('$')[-1]
    exec_line = find_line(mfile, r'%s\(\)\s*\.execute|\.execute\(|%s\b.*execute' % (tsimple, tsimple)) if mfile else None
    tfile = mfile if '$' in t and task_outer(t) == task_outer(mo) else file_of(task_outer(t))
    tfile = tfile if tfile else None
    dib = find_line(tfile, r'doInBackground\(', after=r'class %s\b' % tsimple) if tfile else None
    ope = find_line(tfile, r'void onPreExecute\(', after=r'class %s\b' % tsimple) if tfile else None
    ope_post = find_line(tfile, r'void onPostExecute\(', after=r'class %s\b' % tsimple) if tfile else None
    ocan = find_line(tfile, r'void onCancelled\(', after=r'class %s\b' % tsimple) if tfile else None
    es = 'SRC %s:%s' % (rel(mfile), exec_line) if mfile and exec_line else 'SRC (execute site in %s)' % m
    FW_PRE = "FW-SRC core/java/android/os/AsyncTask.java:645-650"
    FW_WORK = "FW-SRC core/java/android/os/AsyncTask.java:333"
    FW_POST = "FW-SRC core/java/android/os/AsyncTask.java:691-696"
    if ope and ('%s.onPreExecute' % t) in names and not pair_in_graph(m, t + '.onPreExecute'):
        out.append((m, t + '.onPreExecute', 'ASYNC', 'new %s().execute(): onPreExecute runs on the calling (main) thread first' % tsimple,
                    "%s; %s; SRC %s:%d" % (FW_PRE, es, rel(tfile), ope)))
    if dib and ('%s.doInBackground' % t) in names and not pair_in_graph(m, t + '.doInBackground'):
        out.append((m, t + '.doInBackground', 'ASYNC', 'the worker thread runs doInBackground of %s' % tsimple,
                    "%s; %s; SRC %s:%d" % (FW_WORK, es, rel(tfile), dib)))
    if dib and ope_post and ('%s.onPostExecute' % t) in names and not pair_in_graph(t + '.doInBackground', t + '.onPostExecute'):
        out.append((t + '.doInBackground', t + '.onPostExecute', 'ASYNC', 'the result is delivered to onPostExecute on the main thread',
                    "%s; SRC %s:%d" % (FW_POST, rel(tfile), ope_post)))
for m, t in cancels:
    mo = m.split('.')[0]
    tsimple = t.split('$')[-1]
    tfile = file_of(task_outer(t))
    ocan = find_line(tfile, r'void onCancelled\(', after=r'class %s\b' % tsimple) if tfile else None
    if ocan and ('%s.onCancelled' % t) in names and not pair_in_graph(m, t + '.onCancelled'):
        mfile = file_of(task_outer(m.split('.')[0]))
        cl = find_line(mfile, r'\.cancel\(', after=None)
        out.append((m, t + '.onCancelled', 'ASYNC', 'cancel() was called on %s; onCancelled runs on the main thread after the worker finishes' % tsimple,
                    "FW-SRC core/java/android/os/AsyncTask.java:525-526,691-696; SRC %s:%s; SRC %s:%d" % (rel(mfile), cl, rel(tfile), ocan)))
print('generated', len(out))
lines = []
for s, d, k, text, ev in out:
    lines.append("e(%r, %r, %r, %r, evidence=%r)" % (s, d, k, text, ev))
open(G + 'scratch/async_lines.py', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
for l in lines[:6]: print(l[:260])
