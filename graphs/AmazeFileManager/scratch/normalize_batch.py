#!/usr/bin/env python3
"""Robust batch normalizer using AST parsing for multi-line strings."""
import sys
import re
import ast
import json

def load_method_list_mapping(method_list_path):
    """Load mapping of full package paths to short Class.method names."""
    with open(method_list_path, 'r') as f:
        methods = json.load(f)
    
    # Create mapping from full name to short name
    mapping = {}
    for m in methods:
        full = m.get('full', '')
        short = m.get('short', '')
        if full and short:
            mapping[full] = short
    return mapping

def normalize_method_name(method, method_mapping):
    """Normalize full package path to short Class.method form."""
    # Already short form?
    if '/' not in method and method.count('.') <= 2:
        return method
    
    # Try direct mapping
    if method in method_mapping:
        return method_mapping[method]
    
    # Try with com/amaze/filemanager prefix removed
    if method.startswith('com/amaze/filemanager/'):
        short_path = method[len('com/amaze/filemanager/'):]
        # Convert path to Class.method format
        parts = short_path.split('/')
        if len(parts) >= 2:
            class_part = parts[-1]  # Last part is Class.method
            return class_part
    
    # Return as-is if can't normalize
    return method

def parse_unreachable_dict(content, dict_name):
    """Parse UNREACHABLE_BNNN dict using AST, handling multi-line strings."""
    # Find the dict definition
    pattern = rf'{dict_name}\s*=\s*\{{'
    match = re.search(pattern, content)
    if not match:
        return None, []
    
    start_pos = match.end() - 1  # Position of opening brace
    
    # Find matching closing brace by counting
    brace_count = 0
    pos = start_pos
    while pos < len(content):
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
            if brace_count == 0:
                dict_str = content[start_pos:pos+1]
                break
        pos += 1
    else:
        return None, []
    
    # Parse as Python dict literal
    try:
        parsed_dict = ast.literal_eval(dict_str)
        entries = []
        for method, value_tuple in parsed_dict.items():
            if len(value_tuple) == 4:
                kind, reason, source_ref, confirmed = value_tuple
                entries.append({
                    'method': method,
                    'kind': kind,
                    'reason': reason,
                    'source_ref': source_ref,
                    'confirmed': confirmed
                })
        return (match.start(), pos+1), entries
    except Exception as e:
        print(f"Warning: Failed to parse {dict_name}: {e}")
        return None, []

def normalize_edge_kind(kind, src, dst, evidence):
    """Normalize edge kind to valid builder kinds."""
    # Valid kinds: CALL, CONSTRUCTED, DIRECT, ENTRY, EXPLICIT, FRAMEWORK, INFERRED, LIFECYCLE
    # Plus from original schema: SYSTEM, INTENT, RESULT, ENTERS, ASYNC, GUI
    
    kind_map = {
        'FW': 'FRAMEWORK',
        'UI': 'EXPLICIT',
        'LC': 'LIFECYCLE',
        'DIRECT': 'CALL',
        'ENT': 'ENTRY',
        'ENTRY_POINT': None,  # Need to determine from context
    }
    
    if kind in kind_map:
        mapped = kind_map[kind]
        if mapped is None:
            # ENTRY_POINT needs context - check evidence
            if 'public static method' in evidence or 'called from' in evidence.lower():
                return 'CALL'
            elif 'framework' in evidence.lower():
                return 'FRAMEWORK'
            else:
                # Ambiguous - return None to signal need for manual review
                return None
        return mapped
    
    # Already a valid kind
    valid_kinds = {'CALL', 'CONSTRUCTED', 'DIRECT', 'ENTRY', 'EXPLICIT', 'FRAMEWORK', 
                   'INFERRED', 'LIFECYCLE', 'SYSTEM', 'INTENT', 'RESULT', 'ENTERS', 
                   'ASYNC', 'GUI'}
    if kind in valid_kinds:
        return kind
    
    return None  # Unknown kind

def normalize_batch(input_path, output_path, method_mapping):
    """Normalize a batch part file."""
    with open(input_path, 'r') as f:
        content = f.read()
    
    changes = []
    dropped_edges = []
    
    # Step 1: Normalize edge kinds in e() calls
    lines = content.split('\n')
    normalized_lines = []
    
    for i, line in enumerate(lines, 1):
        # Match e('src', 'dst', 'KIND', ...)
        match = re.match(r"^e\('([^']*)', '([^']*)', '([^']*)'", line)
        if match:
            src, dst, kind = match.groups()
            # Extract evidence if on same line
            evidence = ''
            ev_match = re.search(r"evidence='([^']*)'", line)
            if ev_match:
                evidence = ev_match.group(1)
            
            new_kind = normalize_edge_kind(kind, src, dst, evidence)
            if new_kind is None:
                changes.append(f"Line {i}: Dropped edge {src}→{dst} (ambiguous kind '{kind}')")
                dropped_edges.append((src, dst, kind))
                # Comment out the edge
                normalized_lines.append('# ' + line + '  # DROPPED: ambiguous kind')
                continue
            elif new_kind != kind:
                line = line.replace(f"'{kind}'", f"'{new_kind}'", 1)
                changes.append(f"Line {i}: {kind}→{new_kind} in {src}→{dst}")
        
        normalized_lines.append(line)
    
    content = '\n'.join(normalized_lines)
    
    # Step 2: Parse and convert UNREACHABLE dict
    batch_num = re.search(r'label_b(\d+)', input_path)
    if batch_num:
        dict_name = f'UNREACHABLE_B{batch_num.group(1)}'
        dict_range, entries = parse_unreachable_dict(content, dict_name)
        
        if dict_range and entries:
            # Normalize method names in entries
            normalized_entries = []
            for entry in entries:
                orig_method = entry['method']
                norm_method = normalize_method_name(orig_method, method_mapping)
                if norm_method != orig_method:
                    changes.append(f"Method name: {orig_method} → {norm_method}")
                entry['method'] = norm_method
                normalized_entries.append(entry)
            
            # Generate individual UNREACHABLE[] assignments
            unreachable_lines = []
            for entry in normalized_entries:
                # Format as multi-line for readability
                unreachable_lines.append(
                    f"UNREACHABLE['{entry['method']}'] = (\n"
                    f"    '{entry['kind']}',\n"
                    f"    '{entry['reason']}',\n"
                    f"    '{entry['source_ref']}',\n"
                    f"    '{entry['confirmed']}'\n"
                    f")"
                )
            
            # Replace dict with individual assignments
            start, end = dict_range
            new_section = '\n'.join(unreachable_lines)
            content = content[:start] + new_section + content[end:]
            
            changes.append(f"Converted {dict_name} → {len(entries)} UNREACHABLE[] assignments")
    
    # Write normalized content
    with open(output_path, 'w') as f:
        f.write(content)
    
    return changes, dropped_edges

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} input.py output.py method_list.json")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    method_list_path = sys.argv[3]
    
    # Load method name mapping
    method_mapping = load_method_list_mapping(method_list_path)
    print(f"Loaded {len(method_mapping)} method mappings")
    
    # Normalize
    changes, dropped = normalize_batch(input_path, output_path, method_mapping)
    
    print(f"\nNormalized {input_path} → {output_path}")
    print(f"Changes: {len(changes)}")
    for change in changes[:20]:  # Show first 20
        print(f"  {change}")
    if len(changes) > 20:
        print(f"  ... and {len(changes) - 20} more")
    
    if dropped:
        print(f"\nDropped {len(dropped)} edges (ambiguous kinds):")
        for src, dst, kind in dropped:
            print(f"  {src} → {dst} (kind: {kind})")
