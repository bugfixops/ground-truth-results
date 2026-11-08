"""Scratch helper for the 6-route check: for each 'File.java:line' argument print the enclosing method,
the guard conditions (CS.guard_of) and the raw source line. Read-only."""
import sys

sys.path.insert(0, '/Users/darshan/Desktop/yang/work/tools')
import cases  # noqa: E402

CS = cases.Cases('AnyMemo')
for arg in sys.argv[1:]:
    fname, _, ln = arg.rpartition(':')
    line = int(ln)
    try:
        lines, _text = CS._load(fname)
    except KeyError:
        print('%s: NOT FOUND' % arg)
        continue
    try:
        enc = CS.enclosing(fname, line)
    except Exception as ex:  # noqa: BLE001
        enc = 'ERR %s' % ex
    try:
        g = CS.guard_of(fname, line)
    except Exception as ex:  # noqa: BLE001
        g = ['ERR %s' % ex]
    src = lines[line - 1].rstrip()[:150] if 1 <= line <= len(lines) else '(out of range)'
    print('%s | in=%s | guards=%s\n    %5d  %s' % (arg, enc, g, line, src))
