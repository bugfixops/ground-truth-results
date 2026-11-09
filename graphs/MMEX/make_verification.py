#!/usr/bin/env python3
"""Generate graphs/MMEX/verification.csv (mirror only) from judged routes + built graph.

REFUSES to run unless the built graph exists: it needs graphs/MMEX/out/methods.csv
and graphs/MMEX/out/mmex_trigger_graph.json from a faithful build, plus
graphs/MMEX/scratch/route_table.md (the audited final route table, the
single source of truth for path verdicts) and
graphs/MMEX/scratch/corrected_edges.tsv
(edge_id<TAB>result<TAB>confirmed_by<TAB>ref<TAB>note).

No arguments are required: run from the repo root as
  python3 graphs/MMEX/make_verification.py
and every input defaults to its repo-root-relative location (DEFAULT_*
below). Optional overrides (--sample, --table, --corrected-edges, --out)
change one input each; they are never required. The resolved input paths
and the sample file used are printed on stdout on every run, so a stale
default is visible, not silent. An override that is not an absolute path
is tried as given (repo-root invocation), then repo-root-relative, then
relative to this file's directory. A missing or wrong input is refused,
never silently replaced.

Path verdicts come ONLY from route_table.md headings (see TABLE_HEADING):
there is no second verdict file to drift against. A mechanically-generated
verdict file checked against its own source table would be circular; the
audited table is the single source of truth, so eliminating that file
removes a drift surface. The table records no per-route confirmed_by or
ref field, so path rows use one documented convention: confirmed_by
SOURCE (every heading verdict rests on fresh source reading recorded in
the judging evidence), ref the table path itself, and note the heading
text after the route number (stratum, steps, verdict, qualifier verbatim).

STALENESS TRIPWIRE (replaces the v1 required-argument defense, which
no-argument running removes): the run refuses, writing nothing, if the
table set differs from the sample set, the table has != 30 headings, any
table method is absent from methods.csv, or any path edge is absent from
the trigger JSON edge set. A hardcoded sample default is safe only
because this tripwire refuses any stale combination.

Header is exactly: type,item,result,confirmed_by,ref,edges,note
Rows (written sorted by (type, item)):
  path  - one per sampled method; edges MUST equal the method's current
          route_edge_ids from methods.csv, else the script stops (STALE),
          and every path edge MUST exist in the trigger JSON edge set.
  label - one per UNREACHABLE method in the built labels, and one per sampled
          reachable method; confirmed_by only SOURCE or INFERRED. A label
          note longer than 300 characters is cut at 300 and marked with
          an explicit truncation marker; the truncated count is reported.
  edge  - one per corrected edge, listed in scratch/corrected_edges.tsv.
          The file is REQUIRED: if it is absent the script refuses, so a
          B7 run that should carry edge rows can never silently emit 0.
          Supply an empty (or comment-only) file to record explicitly
          that B7 carries no edge rows.
Sample-size rule (brief B6 step 2, sample command with 30): the sample
must contain exactly 30 path rows, every sampled method must have a
route_table.md verdict, every table verdict must belong to a sampled
method, and the table must contain exactly 30 verdict headings.
No row is written by hand: this script is the only writer of verification.csv.
Exit non-zero (and write nothing) if any assertion fails or any input is missing.
"""
import csv, json, os, re, sys

# This file lives at <repo root>/graphs/MMEX/make_verification.py.
GDIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(GDIR))

# v2 defaults: repo-root-relative locations, resolved against REPO_ROOT.
# No default is an absolute path. In the tree layout GDIR == REPO_ROOT
# + graphs/MMEX, so these resolve to the same files v1 resolved via GDIR.
DEFAULT_SAMPLE = 'graphs/MMEX/scratch/sample_30_final2.txt'
DEFAULT_TABLE = 'graphs/MMEX/scratch/route_table.md'
DEFAULT_CORRECTED_EDGES = 'graphs/MMEX/scratch/corrected_edges.tsv'
DEFAULT_METHODS = 'graphs/MMEX/out/methods.csv'
DEFAULT_GRAPH = 'graphs/MMEX/out/mmex_trigger_graph.json'
DEFAULT_OUT = 'graphs/MMEX/verification.csv'
# D7 (brief section 5.6): DEVICE rows live in graphs/MMEX/device/results.csv
# (written by device/compare.py from a committed device/results/<run>/).
# If that file exists, one DEVICE path row per results row is appended
# AFTER the seeded rows (result correct when reached, else unclear; a
# not-reached route never becomes wrong; no label changes). If it does
# not exist, the output is byte-identical to the seeded rows.
DEFAULT_DEVICE_RESULTS = 'graphs/MMEX/device/results.csv'
# Convention for table-derived path rows (see docstring): the table has
# no per-route confirmed_by or ref field.
TABLE_CONFIRMED_BY = 'SOURCE'

RESULTS = ('correct', 'fixed', 'wrong', 'unclear')
CB_LABEL = ('SOURCE', 'INFERRED')
# Brief B6 step 2: the sample command draws 30 routes; section 4 requires
# one path row per route in the final sample. Any other count is refused.
EXPECTED_SAMPLE_SIZE = 30
LABEL_NOTE_LIMIT = 300
LABEL_TRUNC_MARKER = '…[truncated]'

# Route-table heading: "### N. <method> — <stratum>, N steps — VERDICT"
# with an optional parenthetical qualifier, e.g. "WRONG (drawn prefix only)".
# The verdict word is the row's result; a qualifier is reported
# on stdout but does not change the verdict.
TABLE_HEADING = re.compile(
    r'^###\s+\d+\.\s+(.+?)\s+—\s+.*?,\s*\d+\s+steps\s+—\s+(\w+)'
    r'(?:\s+\((.*)\))?\s*$')


def die(msg):
    print('make_verification: REFUSED: ' + msg, file=sys.stderr)
    sys.exit(1)


def resolve_input(arg, default_rel):
    # Input resolution: default -> REPO_ROOT + repo-relative default;
    # override -> absolute as given, else as given if it exists (repo-root
    # invocation), else repo-root-relative if it exists, else writer-dir
    # relative (v1 fallback).
    if arg is None:
        return os.path.join(REPO_ROOT, default_rel)
    if os.path.isabs(arg):
        return arg
    if os.path.isfile(arg):
        return arg
    cand = os.path.join(REPO_ROOT, arg)
    if os.path.isfile(cand):
        return cand
    cand = os.path.join(GDIR, arg)
    if os.path.isfile(cand):
        return cand
    # None of the candidates exists: echo the argument as given, so the
    # refusal names exactly what was asked for instead of a doubled path.
    return arg


def resolve_output(arg, default_rel):
    if arg is None:
        return os.path.join(REPO_ROOT, default_rel)
    if os.path.isabs(arg):
        return arg
    return os.path.join(os.getcwd(), arg)


def parse_args(argv):
    # v2: every argument is optional. A lone positional is accepted as
    # the sample override (v1 compatibility); the --flags are preferred.
    opts = {'sample': None, 'table': None, 'corrected_edges': None, 'out': None}
    flags = {'--sample': 'sample', '--table': 'table',
             '--corrected-edges': 'corrected_edges', '--out': 'out'}
    i = 0
    positional = []
    while i < len(argv):
        a = argv[i]
        if a in flags:
            if i + 1 >= len(argv):
                print('usage: make_verification.py [--sample FILE] [--table FILE] '
                      '[--corrected-edges FILE] [--out FILE]', file=sys.stderr)
                sys.exit(1)
            opts[flags[a]] = argv[i + 1]
            i += 2
        elif a.startswith('--') and '=' in a and a.split('=', 1)[0] in flags:
            k, v = a.split('=', 1)
            opts[flags[k]] = v
            i += 1
        elif a.startswith('--'):
            print('unknown option: %s' % a, file=sys.stderr)
            sys.exit(1)
        else:
            positional.append(a)
            i += 1
    if len(positional) > 1:
        print('usage: make_verification.py [--sample FILE] [--table FILE] '
              '[--corrected-edges FILE] [--out FILE]', file=sys.stderr)
        sys.exit(1)
    if positional and opts['sample'] is None:
        opts['sample'] = positional[0]
    return opts


def main():
    # v2: no arguments required. Defaults are the repo-root-relative
    # locations above; overrides are optional and never required.
    opts = parse_args(sys.argv[1:])
    sample_txt = resolve_input(opts['sample'], DEFAULT_SAMPLE)
    route_table_md = resolve_input(opts['table'], DEFAULT_TABLE)
    corrected_tsv = resolve_input(opts['corrected_edges'], DEFAULT_CORRECTED_EDGES)
    methods_csv = resolve_input(None, DEFAULT_METHODS)
    graph_json = resolve_input(None, DEFAULT_GRAPH)
    dest = resolve_output(opts['out'], DEFAULT_OUT)
    print('make_verification: inputs:')
    print('  sample: %s' % sample_txt)
    print('  table: %s' % route_table_md)
    print('  corrected_edges: %s' % corrected_tsv)
    print('  methods: %s' % methods_csv)
    print('  graph: %s' % graph_json)
    print('  out: %s' % dest)
    for p in (methods_csv, graph_json, sample_txt, route_table_md):
        if not os.path.isfile(p):
            die('missing input: %s (faithful build + sampler output required; nothing written)' % p)
    # W5: corrected_edges.tsv is REQUIRED. An absent file used to mean a
    # silent 0 edge rows; B7 must account for corrected edges explicitly,
    # so refuse, and let the merger supply an empty file for zero rows.
    if not os.path.isfile(corrected_tsv):
        die('missing input: %s (B7 must account for corrected edges explicitly: '
            'supply an empty file for zero edge rows; nothing written)' % corrected_tsv)
    # The route table is a required input (checked in the loop above);
    # it is also the sole source of path verdicts (parsed below).
    rows = {}
    with open(methods_csv, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            rows[r['method']] = r
    with open(graph_json, encoding='utf-8') as f:
        graph = json.load(f)
    edge_ids = {e['id'] for e in graph['edges']}
    labels = graph['labels']

    # v2: verdicts come ONLY from route_table.md headings, parsed with
    # the v1 TABLE_HEADING regex verbatim. confirmed_by, ref and note
    # follow the documented table convention (see docstring): the table
    # has no per-route confirmed_by or ref field, so no per-route value
    # is invented. Note is the heading text after the route number.
    verdicts = {}
    with open(route_table_md, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line.startswith('### '):
                continue
            m = TABLE_HEADING.match(line)
            if not m:
                die('route_table.md has a malformed verdict heading: %r' % line)
            method, verdict, qualifier = m.group(1), m.group(2).lower(), m.group(3)
            if verdict not in RESULTS:
                die('route_table.md verdict %r for %s is not a valid result' % (verdict, method))
            if method in verdicts:
                die('route_table.md has a duplicate verdict heading for %s' % method)
            note = re.sub(r'^###\s+\d+\.\s+', '', line)
            verdicts[method] = (verdict, TABLE_CONFIRMED_BY, DEFAULT_TABLE, note, qualifier)
    # Staleness tripwire, part 1: exactly 30 table headings, and every
    # table method must exist in the built methods.csv.
    if len(verdicts) != EXPECTED_SAMPLE_SIZE:
        die('route_table.md has %d verdict headings, expected %d (nothing written)'
            % (len(verdicts), EXPECTED_SAMPLE_SIZE))
    not_in_methods = [m for m in verdicts if m not in rows]
    if not_in_methods:
        die('route_table.md methods absent from methods.csv: %s' % ', '.join(sorted(not_in_methods)))

    # Sample file: skip header line, last token of each line is the method name.
    with open(sample_txt, encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f if l.strip()]
    if not lines or not lines[0].startswith('#'):
        die('sample file missing sampler header line')
    sampled = [l.split()[-1] for l in lines[1:]]
    if len(sampled) != len(set(sampled)):
        die('sample file has duplicate methods')
    # W2 (kept) + staleness tripwire, part 2: exactly 30 path rows, and
    # the table verdict set must equal the sample set exactly. In v2
    # there is no second verdict source, so no cross-check is possible
    # or needed: a mismatch here IS the tripwire firing.
    if len(sampled) != EXPECTED_SAMPLE_SIZE:
        die('sample file has %d methods, expected %d (brief B6 sample size; '
            'nothing written)' % (len(sampled), EXPECTED_SAMPLE_SIZE))
    table_missing = [m for m in sampled if m not in verdicts]
    if table_missing:
        die('sampled methods without a route_table.md entry: %s' % ', '.join(table_missing))
    table_extra = [m for m in verdicts if m not in set(sampled)]
    if table_extra:
        die('route_table.md entries for non-sampled methods: %s' % ', '.join(sorted(table_extra)))
    table_qualifiers = ['%s (%s)' % (m, verdicts[m][4]) for m in sampled if verdicts[m][4]]

    out_rows = []
    for m in sampled:
        result, cb, ref, note, _qualifier = verdicts[m]
        current = rows[m]['route_edge_ids'].split() if rows[m]['route_edge_ids'].strip() else []
        if rows[m]['verdict'] != 'REACHABLE':
            die('sampled method is not REACHABLE: %s (%s)' % (m, rows[m]['verdict']))
        # W3: every path edge, copied verbatim from methods.csv, must exist
        # in the trigger JSON edge set (previously only corrected edges
        # were checked, so a methods.csv/JSON build mismatch passed silently).
        absent = [e for e in current if e not in edge_ids]
        if absent:
            die('path edges for %s absent from the trigger JSON edge set: %s'
                % (m, ' '.join(absent)))
        out_rows.append({'type': 'path', 'item': m, 'result': result, 'confirmed_by': cb,
                         'ref': ref, 'edges': ' '.join(current), 'note': note})
        out_rows.append({'type': 'label', 'item': m, 'result': result, 'confirmed_by': cb,
                         'ref': ref, 'edges': '', 'note': note})
    truncated = 0
    for m, lab in sorted(labels.items()):
        if lab.get('unreachable'):
            u = lab['unreachable']
            cb = lab.get('confirmed_by') or 'INFERRED'
            if cb not in CB_LABEL:
                die('unreachable method %s has confirmed_by %r' % (m, cb))
            # W4: never truncate silently; mark every cut note explicitly.
            text = u['text']
            if len(text) > LABEL_NOTE_LIMIT:
                note = text[:LABEL_NOTE_LIMIT] + LABEL_TRUNC_MARKER
                truncated += 1
            else:
                note = text
            out_rows.append({'type': 'label', 'item': m, 'result': 'correct', 'confirmed_by': cb,
                             'ref': u.get('ref') or lab.get('source_ref') or '',
                             'edges': '', 'note': note})
    # W5: corrected_edges.tsv is required (checked above); an empty or
    # comment-only file legitimately yields 0 edge rows.
    with open(corrected_tsv, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) != 5:
                die('bad corrected_edges row: %r' % line)
            eid, result, cb, ref, note = parts
            if eid not in edge_ids:
                die('corrected edge no longer exists (text changed): %s' % eid)
            if result not in RESULTS or cb not in ('SOURCE', 'INFERRED'):
                die('bad corrected edge row: %r' % line)
            out_rows.append({'type': 'edge', 'item': eid, 'result': result, 'confirmed_by': cb,
                             'ref': ref, 'edges': '', 'note': note})
    # W9 reachable audit (Kiro, 2026-11-08): one label row per drawn method from scratch/reaudit/audit_result.csv
    # (note "reachable audit, class <X>"); a method that already has a label row keeps it.
    _w9 = {}
    exec(open(os.path.join(REPO_ROOT, 'tools_dev', 'w9_audit_rows.py'), encoding='utf-8').read(), _w9)
    for _r in _w9['audit_rows'](GDIR, [r['item'] for r in out_rows if r['type'] == 'label']):
        out_rows.append(dict(zip(['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note'], _r)))
    # W6 (merger decision): sort all rows by (type, item) before writing.
    # The old order (sample order, then unreachable labels, then edges in
    # file order) was deterministic but not sorted; the brief section 4
    # phrase "fixed, sorted order" is implemented as this sort.
    out_rows.sort(key=lambda r: (r['type'], r['item']))
    # D7 DEVICE rows (appended after the seeded rows, so the seeded
    # section is byte-identical with or without a results file).
    device_path = os.path.join(REPO_ROOT, DEFAULT_DEVICE_RESULTS)
    n_device = 0
    if os.path.isfile(device_path):
        # Reviewer rule 2026-11-09 (tools_dev/device_rows.py): a reached row is written only when its replayed edge
        # ids equal the method's current best route.
        _dr = {}
        exec(open(os.path.join(REPO_ROOT, 'tools_dev', 'device_rows.py'), encoding='utf-8').read(), _dr)
        dev_rows, dev_dropped = _dr['device_rows'](GDIR, 'MMEX')
        for _d in dev_dropped:
            print('make_verification: DEVICE row dropped: %s %s: %s' % _d)
        for d in dev_rows:
            reached = (d.get('reached') or '').strip()
            result = 'correct' if reached == 'yes' else 'unclear'
            status = (d.get('script_status') or '').strip()
            if result == 'unclear':
                if status == 'unscriptable':
                    reason = 'unscriptable'
                elif status == 'ok':
                    reason = 'not reached'
                else:
                    reason = 'script failed (%s)' % status
                note = 'device script %s; %s' % (status, reason)
            else:
                note = 'device script %s' % status
            out_rows.append({'type': 'path', 'item': d['method'],
                             'result': result, 'confirmed_by': 'DEVICE',
                             'ref': 'device run %s/%s' % (d.get('run'), d.get('script')),
                             'edges': d.get('edges') or '', 'note': note})
            n_device += 1
        print('make_verification: DEVICE rows added: %d' % n_device)
    with open(dest, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['type', 'item', 'result', 'confirmed_by', 'ref', 'edges', 'note'])
        w.writeheader()
        w.writerows(out_rows)
    print('wrote %s: %d rows (%d path, %d label, %d edge)' % (
        dest, len(out_rows),
        sum(1 for r in out_rows if r['type'] == 'path'),
        sum(1 for r in out_rows if r['type'] == 'label'),
        sum(1 for r in out_rows if r['type'] == 'edge')))
    # W4 count: every truncated label note carries the marker above.
    print('make_verification: %d label notes truncated at %d chars (marked %s)'
          % (truncated, LABEL_NOTE_LIMIT, LABEL_TRUNC_MARKER))
    if table_qualifiers:
        print('make_verification: route_table.md verdict qualifiers: %s'
              % '; '.join(table_qualifiers))


if __name__ == '__main__':
    main()
