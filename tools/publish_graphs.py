"""Publish the finished schema 2 work to the branch `graphs` of the public repo bugfixops/work-emulator (a snapshot, not the emulator runs).

Usage (from work/): python3 -I tools/publish_graphs.py [--push] [--workdir <folder>]   (default folder: work/publish_tmp, not copied anywhere)
- takes every app that is ticked "- [x]" in handoff/PROGRESS_V2.md (graph outputs, graph_def.py, verification.csv, readme_notes.md, AGENT_NOTES.md, LESSONS.md);
- adds tools/, the schema, the brief, the recipe, the progress file and the worked examples; leaves out the app sources, backups and draft files;
- scrubs local paths and personal names, then refuses to continue if a personal string is still in the copy;
- clones the repo into <workdir>/clone, replaces the content of branch `graphs` with the copy (history is kept: one new commit), commits with the
  neutral identity bugfixops and pushes only with --push. Never touches `main` or `results`.
"""
import argparse
import glob
import os
import re
import shutil
import subprocess
import sys

WORK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = 'https://github.com/bugfixops/work-emulator.git'
# names are matched exactly, suffixes and prefixes on the file or folder name
TOOLS_SKIP = {'__pycache__', 'auto_resume.sh', 'resume_after_reset.sh', 'rd.sh', 'publish_graphs.py', 'calibration.json'}
TOOLS_SKIP_SUFFIX = ('_backup.py', '_backup.html', '.pyc', '.log')
APP_SKIP = {'__pycache__', '.plan', 'generated_draft_graph_def.py.txt', 'KIRO_WORKLIST.md'}
APP_SKIP_SUFFIX = ('.pyc', '.log')
HANDOFF_FILES = ('SCHEMA_V2.md', 'CONVERSION_RECIPE.md', 'AGENT_BRIEF_V2.md', 'PROGRESS_V2.md', 'HANDOFF_V2.md')
LEAK = re.compile(r'(darshan|khanal|dibya|dibae|[a-z0-9]+@gmail|gmail\.com|uc\.edu|/Users/|claude-501|d045584d)', re.I)
ALLOWED = ('smlnskgmail',)          # a Java package name of hash-checker, not a personal address
SCRUB = [
    (re.compile(r'/private/tmp/claude-501/-Users-darshan-Desktop-yang/d045584d-1ca6-4e30-988a-f2f0a8d6b500'), '<scratchpad>'),
    (re.compile(r'/Users/darshan/Desktop/yang'), '<root>'),
    (re.compile(r'-Users-darshan-Desktop-yang'), '<project>'),
    (re.compile(r'\bDarshan\b'), 'the student'),
    (re.compile(r'\bdarshan\b'), 'user'),
    (re.compile(r'\bYang\b'), 'the reviewer'),
    (re.compile(r'\bKiro\b'), 'a helper agent'),
]


def progress_done():
    lines = open(os.path.join(WORK, 'handoff', 'PROGRESS_V2.md'), encoding='utf-8').read().split('\n')
    return [l[6:].split()[0] for l in lines if l.startswith('- [x] ')]


def copy_tree(src, dst, names, suffixes, prefixes=()):
    for dp, dn, fn in os.walk(src):
        dn[:] = [d for d in dn if d not in names and not d.endswith(suffixes) and not d.startswith(prefixes or ('\0',))]
        for f in fn:
            if f in names or f.endswith(suffixes) or f.startswith(prefixes or ('\0',)):
                continue
            s_ = os.path.join(dp, f)
            d_ = os.path.join(dst, os.path.relpath(s_, src))
            os.makedirs(os.path.dirname(d_), exist_ok=True)
            shutil.copy2(s_, d_)


def scrub_tree(root):
    for dp, dn, fn in os.walk(root):
        for f in fn:
            p = os.path.join(dp, f)
            if not f.endswith(('.py', '.md', '.csv', '.json', '.sh', '.html', '.txt')):
                continue
            try:
                s = open(p, encoding='utf-8').read()
            except UnicodeDecodeError:
                continue
            t = s
            for rx, rep in SCRUB:
                t = rx.sub(rep, t)
            if t != s:
                open(p, 'w', encoding='utf-8').write(t)


def leaks(root):
    out = []
    for dp, dn, fn in os.walk(root):
        for f in fn:
            p = os.path.join(dp, f)
            try:
                s = open(p, encoding='utf-8').read()
            except (UnicodeDecodeError, OSError):
                continue
            for m in LEAK.finditer(s):
                line = s[s.rfind('\n', 0, m.start()) + 1: s.find('\n', m.end()) if s.find('\n', m.end()) >= 0 else len(s)]
                if any(a in line for a in ALLOWED):
                    continue
                out.append('%s: %s' % (os.path.relpath(p, root), line.strip()[:160]))
                break
    return out


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit('command failed: %s\n%s' % (' '.join(cmd), r.stderr or r.stdout))
    return r.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--push', action='store_true')
    ap.add_argument('--workdir', default=None)
    ap.add_argument('--message', default='Update the schema 2 ground-truth graphs (snapshot of the finished apps)')
    a = ap.parse_args()
    apps = progress_done()
    if not apps:
        sys.exit('no app is ticked in handoff/PROGRESS_V2.md')
    tmp = a.workdir or os.path.join(WORK, 'publish_tmp')
    os.makedirs(tmp, exist_ok=True)
    export = os.path.join(tmp, 'export')
    shutil.rmtree(export, ignore_errors=True)
    os.makedirs(export)
    for app in apps:
        src = os.path.join(WORK, 'graphs', app)
        if not os.path.isdir(src):
            sys.exit('missing folder for a ticked app: %s' % app)
        copy_tree(src, os.path.join(export, 'graphs', app), APP_SKIP, APP_SKIP_SUFFIX)
    copy_tree(os.path.join(WORK, 'tools'), os.path.join(export, 'tools'), TOOLS_SKIP, TOOLS_SKIP_SUFFIX, prefixes=('_t_',))
    for f in HANDOFF_FILES:
        p = os.path.join(WORK, 'handoff', f)
        if os.path.exists(p):
            os.makedirs(os.path.join(export, 'handoff'), exist_ok=True)
            shutil.copy2(p, os.path.join(export, 'handoff', f))
    copy_tree(os.path.join(WORK, 'handoff', 'examples'), os.path.join(export, 'handoff', 'examples'), {'__pycache__'}, ('.pyc',))
    scrub_tree(export)
    bad = leaks(export)
    if bad:
        print('personal strings left, nothing pushed:')
        print('\n'.join(bad[:40]))
        sys.exit(1)
    clone = os.path.join(tmp, 'clone')
    shutil.rmtree(clone, ignore_errors=True)
    run(['git', 'clone', '--quiet', REPO, clone])
    branches = run(['git', 'branch', '-r'], cwd=clone)
    if 'origin/graphs' in branches:
        run(['git', 'checkout', '--quiet', '-B', 'graphs', 'origin/graphs'], cwd=clone)
    else:
        run(['git', 'checkout', '--quiet', '--orphan', 'graphs'], cwd=clone)
    for entry in os.listdir(clone):
        if entry == '.git':
            continue
        p = os.path.join(clone, entry)
        shutil.rmtree(p) if os.path.isdir(p) and not os.path.islink(p) else os.remove(p)
    for entry in os.listdir(export):
        s = os.path.join(export, entry)
        d = os.path.join(clone, entry)
        shutil.copytree(s, d) if os.path.isdir(s) else shutil.copy2(s, d)
    run(['git', 'add', '-A'], cwd=clone)
    if not run(['git', 'status', '--porcelain'], cwd=clone):
        print('nothing changed since the last publish')
        return
    msg = a.message + '\n\nApps in this snapshot: ' + ', '.join(apps) + '\n\nCo-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>\n'
    mf = os.path.join(tmp, 'msg.txt')
    open(mf, 'w', encoding='utf-8').write(msg)
    run(['git', '-c', 'user.name=bugfixops', '-c', 'user.email=bugfixops@users.noreply.github.com', 'commit', '-q', '-F', mf], cwd=clone)
    head = run(['git', 'rev-parse', '--short', 'HEAD'], cwd=clone)
    print('commit %s on branch graphs with %d apps: %s' % (head, len(apps), ', '.join(apps)))
    if a.push:
        run(['git', 'push', '--quiet', 'origin', 'graphs'], cwd=clone)
        print('pushed graphs to %s' % REPO)
    else:
        print('dry run: not pushed (clone and export are in %s)' % tmp)


if __name__ == '__main__':
    main()
