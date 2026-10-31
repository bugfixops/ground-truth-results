import datetime

NOTES = 'graphs/MMEX/AGENT_NOTES.md'
s = open(NOTES).read()
table = open('graphs/MMEX/scratch/batch_table.md').read()
now = datetime.datetime.now().strftime('%H:%M')

assert s.count('(not yet split)\n') == 1
s = s.replace('| batch | classes | methods | helper | status |\n|---|---|---|---|---|\n(not yet split)\n', table)

assert s.count('(none yet)\n') == 1
s = s.replace('(none yet)\n',
              '%s build_001 (scratch/build_001.txt): methods 4270, REACHABLE 5, UNREACHABLE 0, UNRESOLVED 4265, '
              'errors 4270, warnings 1. Merged parts: none.\n' % now)

decisions = (
    '## Decisions (conservative, recorded per run rule)\n'
    '- D1 Ownership: a batch writes the edges whose DESTINATION method it owns, and the UNREACHABLE entries of its own methods. '
    'A class split into chunks (C3) therefore never gives duplicate edges.\n'
    '- D2 No new named constants in parts. A part registers gate texts inline with env_text(...) / state_text(...) '
    '(defined in graph_def.py section A).\n'
    '- D3 Classes over 40 methods are split into chunks of at most 40 by method order (C3). This overrides "no class is split" '
    '(section 11), because C3 is stricter.\n'
    '- D4 REACHABLE is decided by the whole-graph build, not by a helper. A helper records the route it found (trigger edge and caller). '
    'An UNRESOLVED or wrong REACHABLE is fixed by the orchestrator in the next round.\n'
    '- D5 Library and generated classes: INFERRED labels. UNREACHABLE only with the grep output saved as parts/label_NNN.grep.txt '
    '(KIRO rule 3).\n\n'
    '## Plan\n')
assert s.count('## Plan\n') == 1
s = s.replace('## Plan\n', decisions)
open(NOTES, 'w').write(s)
print('notes updated', len(s))
