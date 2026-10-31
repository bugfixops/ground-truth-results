from pathlib import Path
import csv
import re

PLAN = Path('/Users/darshan/Desktop/yang/work/handoff/LIBRETORRENT_BATCH_PLAN.tsv')
HELPER = Path('/Users/darshan/Desktop/yang/work/graphs/LibreTorrent/scratch/batch_003_helper.md')
SOURCE = Path('/Users/darshan/Desktop/yang/work/final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent')

with PLAN.open() as f:
    methods = [row['method'] for row in csv.DictReader(f, delimiter='\t') if row['batch'] == '3']
helper_rows = {}
for line in HELPER.read_text().splitlines():
    if not line.startswith('| ') or line.startswith('| method') or line.startswith('|---'):
        continue
    columns = [x.strip() for x in line.strip('|').split('|')]
    if len(columns) == 5:
        helper_rows[columns[0]] = columns

print('COMMAND: python3 -I graphs/LibreTorrent/scratch/print_batch3.py')
print(f'PLAN: {PLAN}; selected rows: batch == 3; count: {len(methods)}')
for method in methods:
    row = helper_rows.get(method)
    if not row:
        print(f'### {method} | no citation index in helper; OPEN')
        continue
    print(f'### {method}')
    refs = re.findall(r'`([^`]+\.java):([0-9,-]+)`', row[4])
    if not refs:
        print('No source reference; OPEN')
        continue
    for relative, spec in refs:
        path = SOURCE / relative
        if not path.exists():
            print(f'SOURCE FILE NOT FOUND: {relative}:{spec}')
            continue
        lines = path.read_text(errors='replace').splitlines()
        wanted = set()
        for part in spec.split(','):
            if '-' in part:
                first, last = map(int, part.split('-', 1))
                wanted.update(range(first, last + 1))
            else:
                wanted.add(int(part))
        print(f'--- {relative}:{spec} ---')
        for number in sorted(wanted):
            if 1 <= number <= len(lines):
                print(f'{number}: {lines[number - 1]}')
