from pathlib import Path
import re

PLAN = Path('/Users/darshan/Desktop/yang/work/handoff/LIBRETORRENT_BATCH_PLAN.tsv')
GRAPH = Path('/Users/darshan/Desktop/yang/work/graphs/LibreTorrent/graph_def.py')
SOURCE = Path('/Users/darshan/Desktop/yang/work/final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java')
GREP = Path('/Users/darshan/Desktop/yang/work/graphs/LibreTorrent/scratch/generated_class_grep.txt')

refs = {}
for line in GRAPH.read_text().splitlines():
    m = re.match(r"\s*'([^']+)': \([^\n]*?'((?:SRC|INFERRED) [^']+)'", line)
    if m:
        refs[m.group(1)] = m.group(2)

rows = [line.rstrip('\n').split('\t') for line in PLAN.read_text().splitlines()[1:]]
methods = [row[2] for row in rows if row[1] == 'DONE_RECHECK']
print('COMMAND: python3 -I graphs/LibreTorrent/scratch/print_recheck.py')
for method in methods:
    ref = refs.get(method)
    if not ref:
        print(f'### {method} | NO CITATION IN GRAPH')
        continue
    print(f'### {method} | {ref}')
    if ref.startswith('SRC '):
        path_line = ref[4:]
        filename, line_number = path_line.rsplit(':', 1)
        candidates = list(SOURCE.rglob(Path(filename).name))
        if not candidates:
            print('SOURCE FILE NOT FOUND')
            continue
        source_file = candidates[0]
        source_lines = source_file.read_text(errors='replace').splitlines()
        line_number = int(line_number)
        for number in range(max(1, line_number - 1), min(len(source_lines), line_number + 2) + 1):
            print(f'{number}: {source_lines[number - 1]}')
    else:
        for number, text in enumerate(GREP.read_text().splitlines(), 1):
            print(f'grep:{number}: {text}')
