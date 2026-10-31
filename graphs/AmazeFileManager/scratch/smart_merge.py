#!/usr/bin/env python3
"""Smart merge script - handles UNREACHABLE dicts and validates edges."""
import sys
import re
import shutil
import subprocess
from pathlib import Path

def convert_unreachable_dict(content):
    """Convert UNREACHABLE_BNNN = {...} to individual UNREACHABLE['method'] = (...) assignments."""
    
    # Find all UNREACHABLE dict definitions
    pattern = r"UNREACHABLE_B\d+\s*=\s*\{([^}]+(?:\}[^}]*)*?)\}"
    
    converted_lines = []
    methods_found = []
    
    for match in re.finditer(pattern, content, re.DOTALL):
        dict_content = match.group(1)
        
        # Parse each key: value pair
        # Format: 'Method.name': ('kind', 'reason', 'ref', 'SOURCE')
        entry_pattern = r"'([^']+)':\s*\(([^)]+)\)"
        
        for entry_match in re.finditer(entry_pattern, dict_content):
            method_name = entry_match.group(1)
            tuple_content = entry_match.group(2)
            
            # Validate tuple has 4 elements
            parts = []
            current = []
            in_quotes = False
            quote_char = None
            depth = 0
            
            for char in tuple_content:
                if char in ('"', "'") and (not in_quotes or char == quote_char):
                    in_quotes = not in_quotes
                    if in_quotes:
                        quote_char = char
                    current.append(char)
                elif char == ',' and not in_quotes and depth == 0:
                    parts.append(''.join(current).strip())
                    current = []
                elif char in '([{':
                    depth += 1
                    current.append(char)
                elif char in ')]}':
                    depth -= 1
                    current.append(char)
                else:
                    current.append(char)
            
            if current:
                parts.append(''.join(current).strip())
            
            if len(parts) >= 4:
                # Reconstruct as individual assignment
                line = f"UNREACHABLE['{method_name}'] = ({', '.join(parts)})"
                converted_lines.append(line)
                methods_found.append(method_name)
    
    # Remove the dict definition from content
    content_without_dicts = re.sub(pattern, '', content, flags=re.DOTALL)
    
    return content_without_dicts, converted_lines, methods_found

def validate_edge_line(line):
    """Check if an edge line is valid."""
    if not line.strip() or line.strip().startswith('#'):
        return True
    
    if 'e(' not in line:
        return True  # Not an edge line
    
    # Check for basic syntax
    if 'evidence=' not in line:
        return False
    
    # Count parentheses
    open_paren = line.count('(')
    close_paren = line.count(')')
    
    # Should be balanced or close on next line (multiline edge)
    if open_paren > close_paren + 2:  # Allow some imbalance for multiline
        return False
    
    return True

def clean_and_merge_part(part_path, graph_def_path):
    """Clean part file and append to graph_def.py."""
    
    with open(part_path) as f:
        content = f.read()
    
    # Step 1: Convert UNREACHABLE dicts
    content_cleaned, unreachable_lines, unreachable_methods = convert_unreachable_dict(content)
    
    # Step 2: Collect edge lines and validate
    lines = content_cleaned.split('\n')
    output_lines = []
    dropped_edges = []
    multiline_edge = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Handle multiline edges
        if multiline_edge or (line.strip().startswith('e(') and line.count('(') > line.count(')')):
            multiline_edge.append(line)
            
            # Check if we've closed all parens
            total_open = sum(l.count('(') for l in multiline_edge)
            total_close = sum(l.count(')') for l in multiline_edge)
            
            if total_open <= total_close:
                # Edge complete
                full_edge = '\n'.join(multiline_edge)
                if 'evidence=' in full_edge and ('SRC ' in full_edge or 'INFERRED' in full_edge or 'FW-SRC' in full_edge):
                    output_lines.extend(multiline_edge)
                else:
                    dropped_edges.append(full_edge[:100])
                multiline_edge = []
        
        # Single-line edge
        elif line.strip().startswith('e('):
            if validate_edge_line(line):
                if 'evidence=' in line and ('SRC ' in line or 'INFERRED' in line or 'FW-SRC' in line):
                    output_lines.append(line)
                else:
                    dropped_edges.append(line[:100])
            else:
                dropped_edges.append(line[:100])
        
        # Comment or blank line
        elif line.strip().startswith('#') or not line.strip():
            output_lines.append(line)
        
        # UNREACHABLE individual assignment (already in source)
        elif line.strip().startswith('UNREACHABLE['):
            output_lines.append(line)
        
        i += 1
    
    # Step 3: Append converted UNREACHABLE lines
    if unreachable_lines:
        output_lines.append('')
        output_lines.append('# Converted UNREACHABLE assignments')
        output_lines.extend(unreachable_lines)
    
    return '\n'.join(output_lines), dropped_edges, len(unreachable_methods)

def main():
    if len(sys.argv) < 2:
        print("Usage: smart_merge.py <part_name>")
        print("Example: smart_merge.py label_b002")
        sys.exit(1)
    
    part_name = sys.argv[1]
    if not part_name.endswith('.py'):
        part_name += '.py'
    
    base_dir = Path('/Users/darshan/Desktop/yang/work')
    part_path = base_dir / 'graphs/AmazeFileManager/parts' / part_name
    graph_def = base_dir / 'graphs/AmazeFileManager/graph_def.py'
    backup_path = base_dir / f'graphs/AmazeFileManager/scratch/backup_before_{part_name}.bak'
    conflicts_file = base_dir / 'graphs/AmazeFileManager/scratch/conflicts.md'
    
    if not part_path.exists():
        print(f"ERROR: {part_path} not found")
        sys.exit(1)
    
    print(f"Processing {part_name}...")
    
    # Clean and convert
    cleaned_content, dropped_edges, unreachable_count = clean_and_merge_part(part_path, graph_def)
    
    if dropped_edges:
        print(f"  Dropped {len(dropped_edges)} malformed edges")
        with open(conflicts_file, 'a') as f:
            f.write(f"\n## {part_name} - Dropped edges ({len(dropped_edges)})\n")
            for edge in dropped_edges[:5]:
                f.write(f"- {edge}\n")
    
    print(f"  Converted {unreachable_count} UNREACHABLE methods")
    
    # Backup
    shutil.copy(graph_def, backup_path)
    
    # Append
    with open(graph_def, 'a') as f:
        f.write(f"\n\n# ---- part {part_name.replace('.py', '')} (merged via smart_merge) ----\n")
        f.write(cleaned_content)
    
    # Test Python syntax
    result = subprocess.run(
        ['python3', '-m', 'py_compile', str(graph_def)],
        capture_output=True, text=True, cwd=base_dir
    )
    
    if result.returncode != 0:
        print(f"  SYNTAX ERROR:")
        print(result.stderr[:500])
        shutil.copy(backup_path, graph_def)
        print("  Reverted to backup")
        sys.exit(1)
    
    print("  Syntax OK")
    
    # Build
    result = subprocess.run(
        ['python3', '-I', 'tools/build_graph.py', 'graphs/AmazeFileManager', 'amazefilemanager'],
        capture_output=True, text=True, cwd=base_dir
    )
    
    # Check for actual errors in output (build_graph.py returns 0 even with errors/warnings)
    output = result.stdout
    has_error_line = 'error:' in output.lower() or 'traceback' in output.lower()
    
    if result.returncode != 0 or has_error_line:
        print(f"  BUILD ERROR:")
        print(result.stdout[:500])
        if result.stderr:
            print(result.stderr[:500])
        shutil.copy(backup_path, graph_def)
        print("  Reverted to backup")
        sys.exit(1)
    
    # Parse build output
    output = result.stdout
    match = re.search(r'verdicts: REACHABLE (\d+), UNREACHABLE (\d+), UNRESOLVED (\d+)', output)
    if match:
        r, u, unres = match.groups()
        print(f"  ✓ Build OK: R={r}, U={u}, UNRES={unres}")
        print(f"\nC7|{part_name}|{r}|{u}|{unres}")
    else:
        print("  ✓ Build OK")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
