"""Round 1b helper: exact-text replacements on graph_def.py.

Every (old, new) pair must match exactly once in the current file. If any pair fails, nothing is written.
Usage from a script: from r1b_tool import apply, add_before_gate_end, append_log
"""
import sys

GD = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/graph_def.py'
LOG = '/Users/darshan/Desktop/yang/work/graphs/AnyMemo/scratch/fix_round1.md'


def apply(pairs, label=''):
    text = open(GD, encoding='utf-8').read()
    for old, new in pairs:
        n = text.count(old)
        if n != 1:
            print('FAIL (%s): anchor found %d times: %r' % (label, n, old[:140]))
            sys.exit(1)
        text = text.replace(old, new, 1)
    import os
    if os.environ.get('R1B_DRY'):
        print('DRY OK (%s): %d replacements would be written (nothing written)' % (label, len(pairs)))
        return
    open(GD, 'w', encoding='utf-8').write(text)
    print('OK (%s): %d replacements written' % (label, len(pairs)))


def count(old):
    return open(GD, encoding='utf-8').read().count(old)


def add_gate_entries(lines, label=''):
    """Insert GATE entries (each a full python dict line) before the closing brace of the GATE dict."""
    anchor = "\n}\n\n# ---- dead Load-more chain"
    block = '\n'.join(lines) + '\n'
    apply([(anchor, '\n' + block + '}\n\n# ---- dead Load-more chain')], label or 'gate entries')


def append_log(text):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(text)
