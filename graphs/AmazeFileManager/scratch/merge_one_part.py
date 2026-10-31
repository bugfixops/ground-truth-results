#!/usr/bin/env python3
"""
Per-part merge script for AmazeFileManager.
Cleans one label part, validates it, merges it into graph_def.py with rollback on failure.
"""
import sys
import ast
import shutil
import subprocess
import re
from pathlib import Path

VALID_EDGE_KINDS = {
    'FRAMEWORK', 'EXPLICIT', 'LIFECYCLE', 'SYSTEM', 'INTENT', 
    'RESULT', 'ENTERS', 'CALL', 'ASYNC', 'GUI', 'CONSTRUCTED',
    'DIRECT', 'ENTRY', 'REGISTER', 'INFERRED'
}

def clean_part(part_path):
    """Parse part file, clean edges, normalize UNREACHABLE dicts."""
    with open(part_path) as f:
        content = f.read()
    
    # Parse with AST to validate Python syntax
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        return None, f"Syntax error: {e}"
    
    cleaned_lines = []
    dropped_edges = []
    dropped_methods = []
    
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Handle REACHABLE lines
        if 'REACHABLE[' in line:
            # Check for valid format
            if '=' in line and ('FRAMEWORK' in line or 'EXPLICIT' in line or 'LIFECYCLE' in line or
                               'CALL' in line or 'ENTRY' in line or 'REGISTER' in line or
                               'CONSTRUCTED' in line or 'DIRECT' in line or 'INFERRED' in line):
                # Validate edge kind
                valid = False
                for kind in VALID_EDGE_KINDS:
                    if f"'{kind}'" in line or f'"{kind}"' in line:
                        valid = True
                        break
                
                if valid and 'SRC ' in line or 'INFERRED' in line or 'FW-SRC' in line:
                    cleaned_lines.append(line)
                else:
                    # Extract method name for requeue
                    match = re.search(r"REACHABLE\['([^']+)'\]", line)
                    if match:
                        dropped_methods.append(match.group(1))
                    dropped_edges.append(f"Invalid edge: {line[:100]}")
            else:
                match = re.search(r"REACHABLE\['([^']+)'\]", line)
                if match:
                    dropped_methods.append(match.group(1))
                dropped_edges.append(f"Malformed edge: {line[:100]}")
        
        # Handle UNREACHABLE dict format -> convert to individual assignments
        elif 'UNREACHABLE_B' in line or 'UNREACHABLE = {' in line:
            # Skip dict-based UNREACHABLE, extract and requeue methods
            if '{' in line:
                # Multi-line dict, find the closing brace
                dict_lines = [line]
                brace_count = line.count('{') - line.count('}')
                i += 1
                while i < len(lines) and brace_count > 0:
                    dict_lines.append(lines[i])
                    brace_count += lines[i].count('{') - lines[i].count('}')
                    i += 1
                
                # Extract method names for requeue
                dict_content = '\n'.join(dict_lines)
                for match in re.finditer(r"'([^']+)':\s*\(", dict_content):
                    dropped_methods.append(match.group(1))
                i -= 1  # Back up one since we'll increment at loop end
        
        # Handle normal UNREACHABLE individual assignments
        elif 'UNREACHABLE[' in line:
            # Validate format: must have kind, reason, ref, confirmed_by
            if '=' in line and '(' in line:
                # Check for at least 4 tuple elements
                if line.count(',') >= 3:
                    cleaned_lines.append(line)
                else:
                    match = re.search(r"UNREACHABLE\['([^']+)'\]", line)
                    if match:
                        dropped_methods.append(match.group(1))
                    dropped_edges.append(f"Incomplete UNREACHABLE: {line[:100]}")
            else:
                match = re.search(r"UNREACHABLE\['([^']+)'\]", line)
                if match:
                    dropped_methods.append(match.group(1))
        
        # Pass through other lines
        elif line.strip() and not line.strip().startswith('#'):
            cleaned_lines.append(line)
        elif line.strip().startswith('#') or not line.strip():
            cleaned_lines.append(line)
        
        i += 1
    
    return '\n'.join(cleaned_lines), dropped_edges, dropped_methods

def main():
    if len(sys.argv) < 2:
        print("Usage: merge_one_part.py <part_name>")
        print("Example: merge_one_part.py label_b002")
        sys.exit(1)
    
    part_name = sys.argv[1]
    if not part_name.endswith('.py'):
        part_name += '.py'
    
    base_dir = Path('/Users/darshan/Desktop/yang/work')
    part_path = base_dir / 'graphs/AmazeFileManager/parts' / part_name
    graph_def = base_dir / 'graphs/AmazeFileManager/graph_def.py'
    backup_path = base_dir / f'graphs/AmazeFileManager/scratch/graph_def_before_{part_name}.bak'
    conflicts_file = base_dir / 'graphs/AmazeFileManager/scratch/conflicts.md'
    requeue_file = base_dir / 'graphs/AmazeFileManager/scratch/reassign_queue.txt'
    
    if not part_path.exists():
        print(f"ERROR: Part file not found: {part_path}")
        sys.exit(1)
    
    print(f"Processing {part_name}...")
    
    # Step 1: Clean the part
    result = clean_part(part_path)
    if result[0] is None:
        print(f"ERROR: {result[1]}")
        sys.exit(1)
    
    cleaned_content, dropped_edges, dropped_methods = result
    
    if dropped_edges:
        print(f"Dropped {len(dropped_edges)} bad edges")
        with open(conflicts_file, 'a') as f:
            f.write(f"\n## {part_name} - Dropped edges\n")
            for edge in dropped_edges[:10]:  # Log first 10
                f.write(f"- {edge}\n")
    
    if dropped_methods:
        print(f"Requeued {len(dropped_methods)} methods")
        with open(requeue_file, 'a') as f:
            for method in dropped_methods:
                f.write(f"{method}\n")
    
    # Step 2: Backup graph_def.py
    shutil.copy(graph_def, backup_path)
    print(f"Backed up graph_def.py to {backup_path.name}")
    
    # Step 3: Append cleaned part
    with open(graph_def, 'a') as f:
        f.write(f"\n\n# ===== MERGED: {part_name} =====\n")
        f.write(cleaned_content)
        f.write(f"\n# ===== END {part_name} =====\n")
    
    # Step 4: Validate Python syntax
    result = subprocess.run(
        ['python3', '-m', 'py_compile', str(graph_def)],
        capture_output=True,
        text=True,
        cwd=base_dir
    )
    
    if result.returncode != 0:
        print(f"ERROR: Python compilation failed")
        print(result.stderr)
        shutil.copy(backup_path, graph_def)
        print("Reverted to backup")
        with open(conflicts_file, 'a') as f:
            f.write(f"\n## {part_name} - Compilation failed\n")
            f.write(f"```\n{result.stderr}\n```\n")
        sys.exit(1)
    
    print("Python syntax OK")
    
    # Step 5: Build graph
    result = subprocess.run(
        ['python3', '-I', 'tools/build_graph.py', 'graphs/AmazeFileManager', 'amazefilemanager'],
        capture_output=True,
        text=True,
        cwd=base_dir
    )
    
    if result.returncode != 0:
        print(f"ERROR: Build failed")
        print(result.stdout)
        print(result.stderr)
        shutil.copy(backup_path, graph_def)
        print("Reverted to backup")
        with open(conflicts_file, 'a') as f:
            f.write(f"\n## {part_name} - Build failed\n")
            f.write(f"```\n{result.stdout}\n{result.stderr}\n```\n")
        sys.exit(1)
    
    # Parse build output
    output = result.stdout
    match = re.search(r'verdicts: REACHABLE (\d+), UNREACHABLE (\d+), UNRESOLVED (\d+)', output)
    if match:
        reachable, unreachable, unresolved = match.groups()
        print(f"Build SUCCESS: REACHABLE {reachable}, UNREACHABLE {unreachable}, UNRESOLVED {unresolved}")
    
    # Check for errors/warnings
    if 'errors ' in output:
        err_match = re.search(r'(\d+) errors', output)
        warn_match = re.search(r'(\d+) warnings', output)
        errors = int(err_match.group(1)) if err_match else 0
        warnings = int(warn_match.group(1)) if warn_match else 0
        print(f"Errors: {errors}, Warnings: {warnings}")
    
    print(f"\n✓ Successfully merged {part_name}")
    
    # Return stats for C7 logging
    if match:
        print(f"\nC7: {reachable},{unreachable},{unresolved}")

if __name__ == '__main__':
    main()
