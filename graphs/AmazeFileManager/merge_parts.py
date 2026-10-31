#!/usr/bin/env python3
"""Merge multiple parts into graph_def.py, skipping REACHABLE/INCOMPLETE (leave UNRESOLVED)"""

import sys

# Parts to merge: (filename, part_id, description)
PARTS = [
    ('label_b041.md', 'b041', 'empty'),
    ('label_b042.md', 'b042', 'empty'),
    ('label_b043.md', 'b043', 'LoadFolderSpaceDataTask + LruBitmapCache + Lzma'),
    ('label_b045.md', 'b045', 'MainActivity inner + MainActivityHelper'),
]

# Skip UNREACHABLE for these classes (known bytecode edge issues)
SKIP_UNREACHABLE_CLASSES = {'GlideRequests', 'GlideOptions', 'GlideRequest'}

def parse_part(path):
    """Parse markdown table into list of (method, label, kind, reason, source_lines)"""
    rows = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('STATUS:') or line.startswith('|---') or line.startswith('| Method |'):
                continue
            if line.startswith('|'):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 6:
                    method, label, kind, reason, source_lines = parts[1], parts[2], parts[3], parts[4], parts[5]
                    if method and label:
                        rows.append((method, label, kind, reason, source_lines))
    return rows

def escape_string(s):
    """Escape single quotes and backslashes for Python string literals"""
    return s.replace('\\', '\\\\').replace("'", "\\'")

def should_skip_unreachable(method):
    """Check if this UNREACHABLE should be skipped due to known bytecode issues"""
    for cls in SKIP_UNREACHABLE_CLASSES:
        if method.startswith(cls + '.') or method.startswith(cls + '('):
            return True
    return False

def generate_part_text(rows, part_id, description):
    """Generate UNREACHABLE dict only (skip REACHABLE/INCOMPLETE - leave UNRESOLVED)"""
    unreachable = [(m, k, r, s) for m, l, k, r, s in rows 
                   if l == 'UNREACHABLE' and not should_skip_unreachable(m)]
    reachable_count = sum(1 for r in rows if r[1] == 'REACHABLE')
    incomplete_count = sum(1 for r in rows if r[1] == 'INCOMPLETE')
    skipped_unreachable = sum(1 for r in rows if r[1] == 'UNREACHABLE' and should_skip_unreachable(r[0]))
    
    lines = [f'\n# ---- part label_{part_id} (merged from parts/label_{part_id}.md) ----']
    lines.append(f'# {description}')
    if reachable_count:
        lines.append(f'# {reachable_count} REACHABLE (skip - already in graph or will be added by bytecode)')
    if incomplete_count:
        lines.append(f'# {incomplete_count} INCOMPLETE (skip - leave UNRESOLVED per user instruction)')
    if skipped_unreachable:
        lines.append(f'# {skipped_unreachable} UNREACHABLE skipped (Glide bytecode edge issue)')
    
    if not unreachable:
        lines.append('')
        return '\n'.join(lines) + '\n'
    
    lines.append('\nUNREACHABLE = {}')
    
    for method, kind, reason, source_lines in unreachable:
        kind_value = kind if kind else 'no_trigger_in_app'
        method_esc = escape_string(method)
        kind_esc = escape_string(kind_value)
        reason_esc = escape_string(reason)
        source_esc = escape_string(source_lines)
        lines.append(f"UNREACHABLE['{method_esc}'] = ('{kind_esc}', '{reason_esc}', '{source_esc}', 'CALL')")
    
    return '\n'.join(lines) + '\n'

def main():
    graph_path = 'graphs/AmazeFileManager/graph_def.py'
    
    # Read graph_def.py
    with open(graph_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process each part
    parts_text = []
    total_unreachable = 0
    total_reachable_skipped = 0
    total_incomplete_skipped = 0
    total_glide_skipped = 0
    
    for part_file, part_id, description in PARTS:
        part_path = f'graphs/AmazeFileManager/parts/{part_file}'
        print(f'Parsing {part_file}...')
        rows = parse_part(part_path)
        reachable = sum(1 for r in rows if r[1] == 'REACHABLE')
        unreachable = sum(1 for r in rows if r[1] == 'UNREACHABLE')
        incomplete = sum(1 for r in rows if r[1] == 'INCOMPLETE')
        glide_skip = sum(1 for r in rows if r[1] == 'UNREACHABLE' and should_skip_unreachable(r[0]))
        unreachable_kept = unreachable - glide_skip
        
        print(f'  {reachable} REACHABLE (skip), {unreachable_kept} UNREACHABLE (merge), {glide_skip} Glide U (skip), {incomplete} INCOMPLETE (skip)')
        
        parts_text.append(generate_part_text(rows, part_id, description))
        total_unreachable += unreachable_kept
        total_reachable_skipped += reachable
        total_incomplete_skipped += incomplete
        total_glide_skipped += glide_skip
    
    # Append to end of file
    new_content = content + '\n' + ''.join(parts_text)
    
    # Write back
    with open(graph_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'\nSummary:')
    print(f'  Merged {total_unreachable} UNREACHABLE entries from {len(PARTS)} parts')
    print(f'  Skipped {total_reachable_skipped} REACHABLE (leave UNRESOLVED, will get edges later)')
    print(f'  Skipped {total_incomplete_skipped} INCOMPLETE (leave UNRESOLVED per user)')
    print(f'  Skipped {total_glide_skipped} Glide UNREACHABLE (bytecode edge issue)')
    return 0

if __name__ == '__main__':
    sys.exit(main())
