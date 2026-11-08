"""List lines that would break the publishing rule of the 2026-11-03 review: the repository must not name where the
independent sample comes from, or quote results of that work. The terms are stored encoded, so that this file does not
name them itself. Ordinary app text is not flagged: AnkiDroid's and AnyMemo's own screen words ("cards to study",
"the study options screen", "a study session", "the Study menu", ...) are removed before the terms are matched (APP_WORDS).

Usage (from the repo root):
  python3 -I tools_dev/check_terms.py <file> [<file> ...]  # every line of these files
  python3 -I tools_dev/check_terms.py --since <commit>     # only the lines added since <commit> (committed or not),
                                                           # except app sources; older lines were checked when written
  python3 -I tools_dev/check_terms.py --all                # every line of every tracked text file, except app sources
Exit status 0 when nothing is flagged, 1 otherwise.
"""
import base64
import json
import re
import subprocess
import sys

_ENC = 'WyIoP2kpXFxicGFwZXJzP1xcYiIsICJcXGJJQ1NUXFxiIiwgIig/aSlcXGIoPzp0aGV8b3VyfHRoaXN8dGhhdHxhfHRoZWlyfHlvdXIpIHN0dWR5XFxiIiwgIig/aSlcXGJzdHVkaWVzXFxiIl0='
PATTERNS = [re.compile(p) for p in json.loads(base64.b64decode(_ENC).decode())]
SKIP = ('final_java_only/', 'fw_src/')
TEXT = ('.py', '.md', '.txt', '.csv', '.json', '.html', '.yml', '.yaml', '.sh', '.xml', '.cfg', '.toml', '.ini')
APP_WORDS = re.compile(r'(?i)\bstudy[\s_/-]*(?:options?|screen|page|more|session|menu|caller|override|toolbar|'
                       r'activity|fragment|mode|limit|deck|button|queue|time|cards?|reminders?|preview|flow|items?|overflow)\b')


def line_flagged(line):
    line = APP_WORDS.sub(' ', line)
    return any(p.search(line) for p in PATTERNS)


def flagged(text):
    return [i for i, line in enumerate(text.splitlines(), 1) if line_flagged(line)]


def added_lines(commit):
    """(file, line number, text) of every line added since commit, in the working tree, app sources skipped."""
    out = subprocess.run(['git', 'diff', '-U0', '--no-color', '--no-ext-diff', commit, '--'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace')
    if out.returncode != 0:
        sys.exit('git diff failed: ' + out.stderr.strip())
    f, n = None, 0
    for line in out.stdout.splitlines():
        if line.startswith('+++ '):
            f = line[6:] if line.startswith('+++ b/') else None
        elif line.startswith('@@'):
            m = re.match(r'@@ -\S+ \+(\d+)', line)
            n = int(m.group(1)) if m else 0
        elif line.startswith('+') and f and not f.startswith(SKIP):
            yield f, n, line[1:]
            n += 1


def main(argv):
    if len(argv) >= 2 and argv[0] == '--since':
        bad, files = 0, set()
        for f, n, text in added_lines(argv[1]):
            files.add(f)
            if line_flagged(text):
                print('%s:%d: flagged by the publishing rule' % (f, n))
                bad += 1
        print('nothing flagged in the lines added to %d file(s)' % len(files) if not bad else '%d line(s) flagged' % bad)
        return 1 if bad else 0
    if argv[:1] == ['--all']:
        out = subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.split('\n')
        files = [f for f in out if f and not f.startswith(SKIP) and f.lower().endswith(TEXT)]
    else:
        files = argv
    bad = 0
    for f in files:
        try:
            text = open(f, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for n in flagged(text):
            print('%s:%d: flagged by the publishing rule' % (f, n))
            bad += 1
    print('nothing flagged in %d file(s)' % len(files) if not bad else '%d line(s) flagged' % bad)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
