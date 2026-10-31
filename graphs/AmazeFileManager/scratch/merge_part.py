#!/usr/bin/env python3
"""Per-part self-healing merger with AST parsing."""
import sys
import ast
import re
import shutil
from pathlib import Path

VALID_EDGE_KINDS = {
    'FRAMEWORK', 'EXPLICIT', 'LIFECYCLE', 'SYSTEM', 'INTENT', 
    'RESULT', 'ENTERS', 'CALL', 'ASYNC', 'GUI',
    'ENTRY', 'REGISTER', 'CONSTRUCTED', 'DIRECT', 'INFERRED'  # Also valid
}

def parse_part_file(part_path):
    """Parse a part file and extract valid edges and UNREACHABLE entries."""
    with open(part_path, 'r') as f:
        content = f.read()
    
    valid_edges = []
    valid_unreachable = []
    dropped_edges = []
    dropped_unreachable = []
    
    # Extract e() calls
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('e('):
            # Collect full e() call
            call_lines = [line]
            paren_count = line.count('(') - line.count(')')
            j = i + 1
            while paren_count > 0 and j < len(lines):
                call_lines.append(lines[j])
                paren_count += lines[j].count('(') - lines[j].count(')')
                j += 1
            
            full_call = '\n'.join(call_lines)
            
            # Validate edge
            # Extract kind (3rd argument)
            match = re.search(r"e\('([^']*)',\s*'([^']*)',\s*'([^']*)'", full_call)
            if match:
                src, dst, kind = match.groups()
                
                # Check for invalid conditions
                reasons = []
                if not match.group(0):  # Malformed
                    reasons.append('malformed syntax')
                elif kind not in VALID_EDGE_KINDS:
                    reasons.append(f'invalid kind {kind}')
                elif "evidence=''" in full_call or 'evidence=""' in full_call:
                    reasons.append('empty evidence')
                elif 'evidence=' not in full_call:
                    reasons.append('missing evidence')
                
                if reasons:
                    dropped_edges.append({
                        'src': src,
                        'dst': dst,
                        'kind': kind,
                        'reasons': reasons,
                        'call': full_call[:200]
                    })
                else:
                    valid_edges.append(full_call)
            else:
                # Malformed e() call
                dropped_edges.append({
                    'src': '?',
                    'dst': '?',
                    'kind': '?',
                    'reasons': ['unparseable'],
                    'call': full_call[:200]
                })
            
            i = j
        else:
            i += 1
    
    # Extract UNREACHABLE entries
    for match in re.finditer(r"UNREACHABLE\['([^']+)'\]\s*=\s*\(([^)]+(?:\n[^)]*)*)\)", content, re.MULTILINE | re.DOTALL):
        method = match.group(1)
        tuple_str = '(' + match.group(2).strip() + ')'
        
        # Validate tuple has 4 elements
        try:
            # Quick validation: should have 4 comma-separated strings
            parts = [p.strip() for p in match.group(2).split("',")]
            if len(parts) >= 4:
                valid_unreachable.append(match.group(0))
            else:
                dropped_unreachable.append({
                    'method': method,
                    'reason': f'tuple has {len(parts)} parts, expected 4'
                })
        except:
            dropped_unreachable.append({
                'method': method,
                'reason': 'malformed tuple'
            })
    
    return valid_edges, valid_unreachable, dropped_edges, dropped_unreachable

def merge_part(part_path, graph_def_path, conflicts_path):
    """Merge a single part into graph_def.py with self-healing."""
    part_name = Path(part_path).stem
    
    print(f"\n=== Merging {part_name} ===")
    
    # Parse part
    valid_edges, valid_unreachable, dropped_edges, dropped_unreachable = parse_part_file(part_path)
    
    print(f"Valid: {len(valid_edges)} edges, {len(valid_unreachable)} UNREACHABLE")
    print(f"Dropped: {len(dropped_edges)} edges, {len(dropped_unreachable)} UNREACHABLE")
    
    if not valid_edges and not valid_unreachable:
        print(f"⚠️  No valid content in {part_name}, skipping")
        return False, []
    
    # Backup graph_def.py
    backup_path = f"{graph_def_path}.backup_{part_name}"
    shutil.copy(graph_def_path, backup_path)
    
    # Append valid content
    with open(graph_def_path, 'a') as f:
        f.write(f"\n# ---- part {part_name} (2026-10-27 21:32) ----\n")
        if valid_edges:
            for edge in valid_edges:
                f.write(edge + '\n\n')
        if valid_unreachable:
            for entry in valid_unreachable:
                f.write(entry + '\n\n')
    
    # Test compilation
    try:
        with open(graph_def_path, 'r') as f:
            compile(f.read(), graph_def_path, 'exec')
        print(f"✓ {part_name} merged successfully")
        
        # Log dropped items to conflicts.md
        if dropped_edges or dropped_unreachable:
            with open(conflicts_path, 'a') as f:
                f.write(f"\n## Dropped from {part_name} (2026-10-27)\n\n")
                if dropped_edges:
                    f.write(f"### Dropped edges ({len(dropped_edges)}):\n")
                    for d in dropped_edges:
                        f.write(f"- {d['src']} → {d['dst']}: {', '.join(d['reasons'])}\n")
                if dropped_unreachable:
                    f.write(f"\n### Dropped UNREACHABLE ({len(dropped_unreachable)}):\n")
                    for d in dropped_unreachable:
                        f.write(f"- {d['method']}: {d['reason']}\n")
        
        # Extract methods that need requeuing
        requeue = []
        for d in dropped_edges:
            if d['dst'] != '?':
                requeue.append(d['dst'])
        for d in dropped_unreachable:
            requeue.append(d['method'])
        
        return True, list(set(requeue))
    
    except Exception as e:
        print(f"✗ {part_name} failed compilation: {e}")
        # Revert
        shutil.copy(backup_path, graph_def_path)
        print(f"  Reverted to backup")
        return False, []

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} part.py graph_def.py conflicts.md")
        sys.exit(1)
    
    part_path = sys.argv[1]
    graph_def_path = sys.argv[2]
    conflicts_path = sys.argv[3]
    
    success, requeue = merge_part(part_path, graph_def_path, conflicts_path)
    
    if success:
        print(f"\n✓ Merge successful")
        if requeue:
            print(f"⚠️  {len(requeue)} methods need requeuing: {', '.join(requeue[:5])}{'...' if len(requeue) > 5 else ''}")
    else:
        print(f"\n✗ Merge failed")
    
    sys.exit(0 if success else 1)
