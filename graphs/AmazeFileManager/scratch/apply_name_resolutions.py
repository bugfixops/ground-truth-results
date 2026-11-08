#!/usr/bin/env python3
"""
Apply name resolutions from resolve_names.py to graph_def.py.

This script:
1. Automatically renames all "resolved" cases
2. Creates an ambiguous_remaining.txt file for manual resolution
3. Uses AST to ensure only top-level e() calls are modified
"""

import ast
import json
import os
import sys

def load_resolutions(resolution_file):
    """Load the resolution JSON"""
    with open(resolution_file) as f:
        return json.load(f)

class EdgeCallRewriter(ast.NodeTransformer):
    """AST transformer that renames node names in e() function calls"""
    
    def __init__(self, rename_map):
        self.rename_map = rename_map  # {bad_name: canonical_name}
        self.changes_made = []
        
    def visit_Call(self, node):
        """Visit function calls and check if it's an e() call"""
        # Only process if it's a call to 'e' function
        if isinstance(node.func, ast.Name) and node.func.id == 'e':
            # e() calls have signature: e(src, dst, kind, evidence, ...)
            # We need to check src (arg 0) and dst (arg 1)
            if len(node.args) >= 2:
                # Check src
                if isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                    old_name = node.args[0].value
                    if old_name in self.rename_map:
                        new_name = self.rename_map[old_name]
                        self.changes_made.append(('src', old_name, new_name))
                        node.args[0] = ast.Constant(value=new_name, kind=None)
                
                # Check dst
                if isinstance(node.args[1], ast.Constant) and isinstance(node.args[1].value, str):
                    old_name = node.args[1].value
                    if old_name in self.rename_map:
                        new_name = self.rename_map[old_name]
                        self.changes_made.append(('dst', old_name, new_name))
                        node.args[1] = ast.Constant(value=new_name, kind=None)
        
        # Continue traversing
        return self.generic_visit(node)

def apply_resolutions(graph_def_path, resolutions_data, output_path=None):
    """Apply resolutions to graph_def.py using AST transformation"""
    
    # Build rename map from resolved cases only
    rename_map = {}
    for bad_name, info in resolutions_data['resolutions'].items():
        if info['classification'] == 'resolved' and info['canonical']:
            rename_map[bad_name] = info['canonical']
    
    print(f'Loaded {len(rename_map)} resolved name mappings')
    
    # Read the graph_def.py file
    with open(graph_def_path, encoding='utf-8') as f:
        source_code = f.read()
    
    # Parse the AST
    try:
        tree = ast.parse(source_code, filename=graph_def_path)
    except SyntaxError as e:
        print(f'ERROR: Failed to parse {graph_def_path}: {e}')
        return None
    
    # Apply transformations
    rewriter = EdgeCallRewriter(rename_map)
    new_tree = rewriter.visit(tree)
    
    # Fix missing locations
    ast.fix_missing_locations(new_tree)
    
    # Convert back to source code
    new_source = ast.unparse(new_tree)
    
    # Write output
    if output_path is None:
        output_path = graph_def_path
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_source)
    
    print(f'Applied {len(rewriter.changes_made)} renamings to {output_path}')
    return rewriter.changes_made

def create_ambiguous_file(resolutions_data, output_path):
    """Create ambiguous_remaining.txt for manual resolution"""
    
    ambiguous = [(name, info) for name, info in resolutions_data['resolutions'].items() 
                 if info['classification'] == 'ambiguous']
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# Ambiguous node names requiring manual resolution\n')
        f.write(f'# Total: {len(ambiguous)} names\n\n')
        
        for bad_name, info in sorted(ambiguous):
            f.write(f'\n## {bad_name}\n')
            f.write(f'Reason: {info["reason"]}\n')
            f.write('Candidates:\n')
            for candidate in info['candidates']:
                f.write(f'  - {candidate}\n')
    
    print(f'Created {output_path} with {len(ambiguous)} ambiguous cases')

def main(argv):
    if len(argv) < 3:
        print('Usage: python3 -I apply_name_resolutions.py <resolution.json> <graph_def.py>')
        return 1
    
    resolution_file = argv[1]
    graph_def_path = argv[2]
    
    # Load resolutions
    resolutions_data = load_resolutions(resolution_file)
    
    # Apply automatic resolutions
    changes = apply_resolutions(graph_def_path, resolutions_data)
    
    if changes is None:
        return 1
    
    # Create ambiguous file
    scratch_dir = os.path.dirname(resolution_file)
    ambiguous_file = os.path.join(scratch_dir, 'ambiguous_remaining.txt')
    create_ambiguous_file(resolutions_data, ambiguous_file)
    
    # Write changes log
    changes_log = os.path.join(scratch_dir, 'name_resolution_changes.txt')
    with open(changes_log, 'w', encoding='utf-8') as f:
        f.write(f'# Name resolution changes applied\n')
        f.write(f'# Total: {len(changes)} renamings\n\n')
        for side, old, new in changes:
            f.write(f'{side}: {old} -> {new}\n')
    
    print(f'Changes logged to {changes_log}')
    print('\nSummary:')
    print(f'  Resolved and applied: {len(changes)}')
    print(f'  Ambiguous (manual work): {len([1 for v in resolutions_data["resolutions"].values() if v["classification"]=="ambiguous"])}')
    print(f'  Not a node (left as is): {len([1 for v in resolutions_data["resolutions"].values() if v["classification"]=="not_a_node"])}')
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
