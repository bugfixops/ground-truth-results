#!/usr/bin/env python3
"""
Direct merge of parts into graph_def.py with UNREACHABLE dict conversion.
"""
import sys
import re

def main():
    part_name = sys.argv[1] if len(sys.argv) > 1 else 'label_b002'
    
    base = '/Users/darshan/Desktop/yang/work'
    part_file = f'{base}/graphs/AmazeFileManager/parts/{part_name}.py'
    graph_def_file = f'{base}/graphs/AmazeFileManager/graph_def.py'
    
    # Read part
    with open(part_file) as f:
        part_content = f.read()
    
    # Convert UNREACHABLE_BNNN dicts to individual assignments
    converted_lines = []
    
    # Find the UNREACHABLE_B002 = { ... } block
    match = re.search(r'UNREACHABLE_B\d+\s*=\s*\{(.*?)\n\}', part_content, re.DOTALL)
    if match:
        dict_body = match.group(1)
        
        # Parse each entry: 'method': (tuple)
        for line in dict_body.split('\n'):
            line = line.strip()
            if not line or line == ',':
                continue
            
            # Match: 'Method.name': (kind, reason, ref, confirmed)
            entry_match = re.match(r"'([^']+)':\s*\((.+)\),?$", line)
            if entry_match:
                method = entry_match.group(1)
                tuple_content = entry_match.group(2)
                converted_lines.append(f"UNREACHABLE['{method}'] = ({tuple_content})")
        
        # Remove the dict from part_content
        part_content = part_content[:match.start()] + part_content[match.end():]
    
    # Append to graph_def
    with open(graph_def_file, 'a') as f:
        f.write(f'\n\n# ---- part {part_name} (manual merge) ----\n')
        f.write(part_content)
        if converted_lines:
            f.write('\n# Converted UNREACHABLE assignments:\n')
            for line in converted_lines:
                f.write(line + '\n')
    
    print(f"Merged {part_name}: {len(converted_lines)} UNREACHABLE methods converted")

if __name__ == '__main__':
    main()
