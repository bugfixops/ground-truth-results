#!/usr/bin/env python3
"""G4 check (Kiro): class of each checked case from out/methods.csv against its source class (Appendix B of
handoff/MUSE_REAUDIT_5APPS.md until review/checked_cases.csv exists). Usage, from the repo root:
    python3 -I tools_dev/check_cases.py
A target named without a signature matches its only overload (LibreTorrent-16 is NoFilesSelectedException.<init>())."""
import csv
cases = [l for l in open('handoff/MUSE_REAUDIT_5APPS.md', encoding='utf-8').read().split('## Appendix B')[1].split('## Appendix C')[0].split('\n')
         if l.startswith('| ') and '-' in l.split('|')[1] and 'Case' not in l]
cache, ok = {}, 0
for l in cases:
    c = [x.strip() for x in l.strip('|').split('|')]
    case, target, src = c[0], c[1].strip('`'), c[4]
    app = case.rsplit('-', 1)[0]
    if app not in cache:
        cache[app] = {r['method']: r for r in csv.DictReader(open('graphs/%s/out/methods.csv' % app, encoding='utf-8'))}
    r = cache[app].get(target) or cache[app].get(target + '()')
    if not r:
        print(case, 'MISSING', target); continue
    ek = [k for k in r['env_kinds'].split(';') if k and k != 'permission']
    if r['verdict'] != 'REACHABLE':
        cls = 'config' if r['unreachable_kind'] in ('closed_by_configuration', 'closed_by_api_level') else 'dead'
    else:
        cls = 'env' if ek else 'state' if r['state_kinds'] else 'library' if r['explicit_standard_route'] == 'no' else 'gui'
    good = cls in src
    ok += good
    print('%-22s %-48s full=%-8s source=%-30s %s' % (case, target[:48], cls, src, 'OK' if good else 'MISMATCH'))
print('matching:', ok, 'of', len(cases))
