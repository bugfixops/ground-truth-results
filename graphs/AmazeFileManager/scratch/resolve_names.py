#!/usr/bin/env python3
"""
Resolve unknown node names from build errors to canonical builder node names.

Usage: python3 -I resolve_names.py <build_file>

Reads a build file (e.g., build_resume_72.txt), extracts "unknown node" errors,
and produces a JSON mapping showing how each bad name relates to the builder's
canonical naming system.
"""

import collections
import json
import os
import re
import sys

# JVM type codes to readable names
JVM = {'I': 'int', 'J': 'long', 'Z': 'boolean', 'F': 'float', 'D': 'double',  
       'B': 'byte', 'C': 'char', 'S': 'short', 'V': 'void'}

def param_names(desc):
    """'(Landroid/content/Context;I)Z' -> 'Context,int' (matches build_graph.py)"""
    args, i, out = desc[1:desc.index(')')], 0, []
    while i < len(args):
        dims = 0
        while i < len(args) and args[i] == '[':
            dims += 1
            i += 1
        if i >= len(args):
            break
        if args[i] == 'L':
            j = args.index(';', i)
            name = args[i + 1:j].rsplit('/', 1)[-1].split('$')[-1]
            i = j + 1
        else:
            name = JVM.get(args[i], '?')
            i += 1
        out.append(name + '[]' * dims)
    return ','.join(out)

def base(n):
    """Strip @context suffix (matches build_graph.py)"""
    return n.split('@')[0]

def class_prefixes(rows):
    """{outer class: 'pkgtail.'} for disambiguating same-named classes (matches build_graph.py)"""
    simple = collections.defaultdict(set)
    for r in rows:
        outer = r['class'].split('$')[0]
        simple[outer.rsplit('/', 1)[-1]].add(outer)
    pre = {}
    for sn, fulls in simple.items():
        if len(fulls) < 2:
            continue
        for k in range(1, 8):
            tails = {f: '.'.join(f.split('/')[-1 - k:-1]) for f in fulls}
            if len(set(tails.values())) == len(fulls):
                break
        for f in fulls:
            pre[f] = tails[f] + '.'
    return pre

def method_names(rows):
    """Canonical node names per method (matches build_graph.py logic)"""
    pre = class_prefixes(rows)
    shorts = [pre.get(r['class'].split('$')[0], '') + r['short'] for r in rows]
    count = collections.Counter(shorts)
    names, by_name = [], {}
    for r, sh in zip(rows, shorts):
        n = sh if count[sh] == 1 else '%s(%s)' % (sh, param_names(r['desc']))
        k = 2
        while n in by_name:
            n = '%s#%d' % (n.split('#')[0], k)
            k += 1
        names.append(n)
        by_name[n] = r
    return names, by_name

def parse_jvm_signature(name):
    """Parse JVM signature form like GlideRequests.load([B)Lcom/amaze/filemanager/GlideRequest;
    Returns (class, method, params_str) or None"""
    # Pattern: ClassName.methodName(descriptor)ReturnType
    m = re.match(r'^([^.(]+)\.([^(]+)\(([^)]*)\)(.+)$', name)
    if not m:
        return None
    cls, method, params_desc, ret = m.groups()
    params = param_names('(' + params_desc + ')V')
    return (cls, method, params)

def classify_unknown_name(bad_name, rows, canonical_names, canonical_by_name):
    """
    Classify an unknown node name and find canonical mapping if possible.
    
    Returns: dict with keys:
        'classification': one of 'resolved', 'ambiguous', 'not_a_node'
        'category': one of 'a'(framework), 'b'(overload_issue), 'c'(inherited), 'd'(pseudo), 'e'(jvm_sig), 'f'(matched)
        'canonical': canonical name if resolved, None otherwise
        'candidates': list of candidates if ambiguous
        'reason': human-readable explanation
    """
    # Strip context suffix
    base_name = base(bad_name)
    
    # Check for exact match
    if base_name in canonical_names:
        return {
            'classification': 'resolved',
            'category': 'f',
            'canonical': base_name,
            'candidates': None,
            'reason': 'Exact match in canonical names'
        }
    
    # Check for pseudo-nodes
    pseudo_patterns = ['LAUNCHER', 'INTENT_FILTER', 'ENTRY_POINT', 'FRAMEWORK', 'SYSTEM']
    if any(p in base_name for p in pseudo_patterns):
        return {
            'classification': 'not_a_node',
            'category': 'd',
            'canonical': None,
            'candidates': None,
            'reason': 'Pseudo-node/placeholder not in method list'
        }
    
    # Try to parse as JVM signature
    parsed = parse_jvm_signature(base_name)
    if parsed:
        cls, method, params = parsed
        # Try to find matching method
        candidates = []
        for r in rows:
            simple_cls = r['class'].rsplit('/', 1)[-1]
            if simple_cls == cls and r['name'] == method:
                our_params = param_names(r['desc'])
                if our_params == params:
                    # Find canonical name for this row
                    for cname, crow in canonical_by_name.items():
                        if crow['class'] == r['class'] and crow['name'] == r['name'] and crow['desc'] == r['desc']:
                            candidates.append(cname)
        if len(candidates) == 1:
            return {
                'classification': 'resolved',
                'category': 'e',
                'canonical': candidates[0],
                'candidates': None,
                'reason': 'Resolved from JVM signature form'
            }
        elif len(candidates) > 1:
            return {
                'classification': 'ambiguous',
                'category': 'e',
                'canonical': None,
                'candidates': candidates,
                'reason': 'Multiple matches for JVM signature'
            }
    
    # Extract class and method
    if '.' not in base_name:
        return {
            'classification': 'not_a_node',
            'category': 'a',
            'canonical': None,
            'candidates': None,
            'reason': 'No class prefix, likely framework class'
        }
    
    # Split into class and method parts
    parts = base_name.split('.')
    if len(parts) < 2:
        return {
            'classification': 'not_a_node',
            'category': 'a',
            'canonical': None,
            'candidates': None,
            'reason': 'Invalid method name format'
        }
    
    class_part = parts[0]
    method_part = '.'.join(parts[1:])
    
    # Check if it has parameters already
    has_params = '(' in method_part
    
    # Search in rows for matching class+method
    candidates = []
    class_exists = False
    
    for r in rows:
        simple_cls = r['class'].rsplit('/', 1)[-1].split('$')[-1]
        full_cls = r['class']
        
        # Check if class matches (allowing for package prefix variations)
        if simple_cls == class_part or full_cls.endswith('/' + class_part) or class_part in full_cls:
            class_exists = True
            
            # Check if method matches
            if method_part.startswith(r['name']):
                # Find canonical name for this method
                for cname, crow in canonical_by_name.items():
                    if crow['class'] == r['class'] and crow['name'] == r['name'] and crow['desc'] == r['desc']:
                        candidates.append(cname)
                        break
    
    if len(candidates) == 1:
        return {
            'classification': 'resolved',
            'category': 'b',
            'canonical': candidates[0],
            'candidates': None,
            'reason': 'Found unique matching method (may be overload needing params)'
        }
    elif len(candidates) > 1:
        return {
            'classification': 'ambiguous',
            'category': 'b',
            'canonical': None,
            'candidates': candidates,
            'reason': f'Found {len(candidates)} overloads, need parameter disambiguation'
        }
    elif class_exists:
        return {
            'classification': 'not_a_node',
            'category': 'c',
            'canonical': None,
            'candidates': None,
            'reason': 'Class exists but method not declared (likely inherited from parent)'
        }
    else:
        return {
            'classification': 'not_a_node',
            'category': 'a',
            'canonical': None,
            'candidates': None,
            'reason': 'Class not found in method_list.json (framework/library class)'
        }

def extract_errors_from_build(build_file):
    """Extract unknown node errors from build file"""
    errors = []
    with open(build_file, encoding='utf-8') as f:
        for line in f:
            # Match: ERROR E<id>: unknown src|dst node <name>
            m = re.match(r'\s*ERROR (E[0-9a-f-]+): unknown (src|dst) node (.+)$', line)
            if m:
                edge_id, side, name = m.groups()
                errors.append({
                    'edge_id': edge_id,
                    'side': side,
                    'bad_name': name
                })
    return errors

def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    
    build_file = argv[1]
    graph_dir = os.path.dirname(os.path.dirname(build_file))  # scratch/../ -> graph dir
    method_list_path = os.path.join(graph_dir, 'method_list.json')
    
    if not os.path.exists(method_list_path):
        print(f'ERROR: method_list.json not found at {method_list_path}')
        return 1
    
    # Load method list and compute canonical names
    print(f'Loading {method_list_path}...')
    rows = json.load(open(method_list_path))
    print(f'Loaded {len(rows)} methods')
    
    print('Computing canonical names...')
    canonical_names_list, canonical_by_name = method_names(rows)
    canonical_names = set(canonical_names_list)
    print(f'Generated {len(canonical_names)} canonical node names')
    
    # Extract errors
    print(f'Parsing {build_file}...')
    errors = extract_errors_from_build(build_file)
    print(f'Found {len(errors)} unknown node errors')
    
    # Build unique set of bad names
    bad_names = sorted(set(e['bad_name'] for e in errors))
    print(f'Unique unknown names: {len(bad_names)}')
    
    # Classify each
    print('Classifying unknown names...')
    resolutions = {}
    category_counts = collections.Counter()
    classification_counts = collections.Counter()
    
    for bad_name in bad_names:
        result = classify_unknown_name(bad_name, rows, canonical_names, canonical_by_name)
        resolutions[bad_name] = result
        category_counts[result['category']] += 1
        classification_counts[result['classification']] += 1
    
    # Build edge mapping
    edge_mappings = []
    for err in errors:
        result = resolutions[err['bad_name']]
        edge_mappings.append({
            'edge_id': err['edge_id'],
            'side': err['side'],
            'bad_name': err['bad_name'],
            'classification': result['classification'],
            'category': result['category'],
            'canonical': result['canonical'],
            'candidates': result['candidates'],
            'reason': result['reason']
        })
    
    # Output JSON
    output = {
        'summary': {
            'total_errors': len(errors),
            'unique_names': len(bad_names),
            'classifications': dict(classification_counts),
            'categories': {
                'a_framework_library': category_counts['a'],
                'b_overload_or_naming': category_counts['b'],
                'c_inherited_method': category_counts['c'],
                'd_pseudo_node': category_counts['d'],
                'e_jvm_signature': category_counts['e'],
                'f_exact_match': category_counts['f']
            }
        },
        'resolutions': resolutions,
        'edge_mappings': edge_mappings
    }
    
    output_path = build_file.replace('.txt', '_name_resolution.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f'\nResults written to: {output_path}')
    print('\nClassification Summary:')
    print(f'  Resolved: {classification_counts["resolved"]}')
    print(f'  Ambiguous: {classification_counts["ambiguous"]}')
    print(f'  Not a node: {classification_counts["not_a_node"]}')
    print('\nCategory Breakdown:')
    print(f'  (a) Framework/library: {category_counts["a"]}')
    print(f'  (b) Overload/naming issue: {category_counts["b"]}')
    print(f'  (c) Inherited method: {category_counts["c"]}')
    print(f'  (d) Pseudo-node: {category_counts["d"]}')
    print(f'  (e) JVM signature: {category_counts["e"]}')
    print(f'  (f) Exact match: {category_counts["f"]}')
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
