#!/usr/bin/env python3
"""Helper script to merge repair part files into graph_def.py with proper format conversion"""
import re
import sys

def convert_part_to_graph_format(part_content):
    """Convert part file format (positional evidence arg) to graph_def.py format (evidence= keyword)"""
    # Match e(...) calls that span multiple lines
    # Pattern: e('src', 'dst', 'kind', 'reason',\n  'evidence')
    # Convert to: e('src', 'dst', 'kind', 'reason',\n  evidence='evidence')
    
    def replace_evidence(match):
        full_match = match.group(0)
        # Check if it already has evidence= keyword
        if 'evidence=' in full_match:
            return full_match
        
        # Split by lines
        lines = full_match.split('\n')
        if len(lines) >= 2:
            # The last line (or second line) should be the evidence
            for i in range(1, len(lines)):
                line = lines[i]
                # Check if it starts with spaces and a quote (and is not a comment)
                if re.match(r'^\s+["\']', line) and not line.strip().startswith('#'):
                    # Add evidence= before the quote
                    lines[i] = re.sub(r'^(\s+)(["\'])', r'\1evidence=\2', line)
                    break
        
        return '\n'.join(lines)
    
    # Match e(...) calls that span lines, non-greedy
    pattern = r"e\([^\n)]+\n(?:[^e].*\n?)*?\)"
    result = re.sub(pattern, replace_evidence, part_content, flags=re.MULTILINE)
    
    return result

def append_part_to_graph(graph_path, part_path, part_name, date_str='2025-01-29'):
    """Append a part file to graph_def.py with proper header"""
    with open(part_path, 'r') as f:
        part_content = f.read()
    
    # Convert format
    converted_content = convert_part_to_graph_format(part_content)
    
    # Read current graph
    with open(graph_path, 'r') as f:
        graph_content = f.read()
    
    # Append the new part
    new_part = f"\n\n# ---- part {part_name} ({date_str})\n{converted_content}"
    
    with open(graph_path, 'a') as f:
        f.write(new_part)
    
    print(f"Merged {part_name} into graph_def.py")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: merge_helper.py <graph_def.py> <part_file.py> [part_name]")
        sys.exit(1)
    
    graph_path = sys.argv[1]
    part_path = sys.argv[2]
    part_name = sys.argv[3] if len(sys.argv) > 3 else part_path.split('/')[-1].replace('.py', '')
    
    append_part_to_graph(graph_path, part_path, part_name)
