from pathlib import Path
import subprocess

ROOT = Path('/Users/darshan/Desktop/yang/work/final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java')
SEARCHES = [
    r'IPFilterParser\s*\(',
    r'addTorrent\s*\(',
    r'new\s+FileTree\s*\(|super\s*\(\s*index\s*,',
    r'PriorityConverter\.convert\s*\(',
    r'getTorrentId\s*\(',
    r'new\s+FileNode\.Type\s*\(|new\s+Type\s*\(',
]

print('COMMAND: python3 -I graphs/LibreTorrent/scratch/print_batch3_search.py')
for pattern in SEARCHES:
    cmd = ['rg', '-n', '-e', pattern, str(ROOT)]
    result = subprocess.run(cmd, text=True, capture_output=True)
    print('SEARCH:', ' '.join(cmd))
    print('EXIT:', result.returncode)
    if result.stdout:
        print(result.stdout, end='')
    if result.stderr:
        print(result.stderr, end='')
