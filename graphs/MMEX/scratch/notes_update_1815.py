NOTES = 'graphs/MMEX/AGENT_NOTES.md'
s = open(NOTES).read()

current = """## Current step
Run started 18:12:47 by the convert runner (handoff/resume_convert.log). At session start the notes were behind graph_def.py: parts 080 and 084 were already merged (see the 18:15 entries). Part 083 was checked, spot-checked and merged at 18:15 (build_p083). Merged parts: 001 to 084. Not merged: 085 to 145. Helpers running (background, started 18:16): 085 (new helper; the helper of 15:40 stopped with no output after 15:46), 086, 087, 088. Next: for each helper that reports, run check_part.py NNN, spot-check about 1 in 5 cited lines with sed -n (source root final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java), merge_part.py NNN, python3 -I -m py_compile graphs/MMEX/graph_def.py, build to scratch/build_pNNN.txt, add a C7 line, update the batch table row. Then start the next batch in table order (089 onward) in a free slot (up to 4 helpers).

"""
i = s.index('## Current step\n')
j = s.index('## Facts checked\n')
s = s[:i] + current + s[j:]

progress = """- 18:15 notes catch-up: parts 084 and 080 were already in graph_def.py when this run resumed (merge order 084, then 080; graph_def.py last written 15:45:16). They had no C7 line. scratch/build_p080.txt (15:44: edges 7794, REACHABLE 1858, UNRESOLVED 1972, errors 1974, warnings 8) may predate the 080 merge, so it is not the record for them.
- 18:15 build_p083 (scratch/build_p083.txt): merged part 083 (38 rows: 32 REACHABLE, 6 UNREACHABLE; 12 edges; check_part no problems; cited lines spot-checked at home/MainActivity.java:179, 182, 240, 411-413, 1294-1297; home/RecentDatabaseEntryComparator.java:24-25, 47-49; home/MyActionBarDrawerToggle.java:32-40). Counts: edges 7801, REACHABLE 1881, UNREACHABLE 450, UNRESOLVED 1939, errors 1950, warnings 8. Errors did not rise (1974 to 1950). Build exit status is 1 while UNRESOLVED is above 0; this is the tool's normal exit code, not a failure.
- 18:16 helpers started (background): 085 (new helper, replacing the stuck helper of 15:40), 086, 087, 088. Each writes parts/label_NNN.py, label_NNN.md and label_NNN.grep.txt; the orchestrator then runs check_part, spot-checks, merges and builds each batch in turn.

"""
k = s.index('## Batch table (C3)\n')
s = s[:k] + progress + s[k:]

rows = {
    '080': (None, 'merged before 18:13 (see the 18:15 entries)'),
    '083': (None, 'merged 18:15 (build_p083; 32 REACHABLE, 6 UNREACHABLE; 12 edges)'),
    '084': (None, 'merged before 18:13 (see the 18:15 entries)'),
    '085': ('18:16 new helper (background; replaces the stuck helper of 15:40)', 'running'),
    '086': ('18:16 (background)', 'running'),
    '087': ('18:16 (background)', 'running'),
    '088': ('18:16 (background)', 'running'),
}
lines = s.split('\n')
for n, (helper, status) in rows.items():
    hits = [idx for idx, l in enumerate(lines) if l.startswith('| %s |' % n)]
    assert len(hits) == 1, (n, hits)
    cells = lines[hits[0]].split('|')
    if helper:
        cells[4] = ' %s ' % helper
    cells[5] = ' %s ' % status
    lines[hits[0]] = '|'.join(cells)
s = '\n'.join(lines)
open(NOTES, 'w').write(s)
print('notes updated', len(s))
