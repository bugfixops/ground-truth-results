#!/usr/bin/env python3
"""
Process blocker files: parse, filter already-resolved methods, sort by count,
and distribute into 4 balanced groups.
"""

import sys
import re
from pathlib import Path

def parse_blockers(filepath):
    """Parse blocker file into dict: {blocker: [list of blocked methods]}"""
    blockers = {}
    current_blocker = None
    current_count = 0
    current_methods = []
    
    with open(filepath) as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#'):
                continue
            
            # Check if this is a blocker line (format: "blocker -> N methods")
            match = re.match(r'^(.+?)\s+->\s+(\d+)\s+methods?\s*$', line)
            if match:
                # Save previous blocker if exists
                if current_blocker:
                    blockers[current_blocker] = (current_count, current_methods)
                
                # Start new blocker
                current_blocker = match.group(1)
                current_count = int(match.group(2))
                current_methods = []
            elif line.startswith('  '):
                # This is a blocked method (indented)
                method = line.strip()
                if method:
                    current_methods.append(method)
        
        # Save last blocker
        if current_blocker:
            blockers[current_blocker] = (current_count, current_methods)
    
    return blockers

def parse_build_status(filepath):
    """Parse build file to get set of UNRESOLVED methods"""
    unresolved = set()
    
    with open(filepath) as f:
        for line in f:
            # Look for the verdict line
            if line.startswith('verdicts:'):
                # Just return early - we'll use the unresolved_blockers.txt instead
                break
    
    return unresolved

def filter_resolved_methods(blockers, unresolved_file):
    """Filter out methods that are no longer unresolved"""
    # Parse the unresolved blockers to get current state
    current_blockers = parse_blockers(unresolved_file)
    
    # Build set of all unresolved methods
    unresolved_set = set()
    for blocker, (count, methods) in current_blockers.items():
        unresolved_set.add(blocker)
        unresolved_set.update(methods)
    
    # Filter: keep only blockers and dependents that are still unresolved
    filtered = {}
    for blocker, (orig_count, methods) in blockers.items():
        if blocker not in unresolved_set:
            continue
        
        # Filter the dependent methods
        still_blocked = [m for m in methods if m in unresolved_set]
        
        if still_blocked:
            filtered[blocker] = (len(still_blocked), still_blocked)
    
    return filtered

def sort_blockers(blockers):
    """Sort blockers by count (descending), return list of (blocker, count, methods)"""
    items = [(blocker, count, methods) for blocker, (count, methods) in blockers.items()]
    items.sort(key=lambda x: x[1], reverse=True)
    return items

def distribute_round_robin(sorted_blockers, num_groups=4):
    """Distribute blockers into groups using round-robin, balanced by total blocked count"""
    groups = [[] for _ in range(num_groups)]
    group_totals = [0] * num_groups
    
    # Round-robin assignment: largest first
    for i, (blocker, count, methods) in enumerate(sorted_blockers):
        # Find group with smallest total so far (greedy balancing)
        min_idx = group_totals.index(min(group_totals))
        groups[min_idx].append((blocker, count, methods))
        group_totals[min_idx] += count
    
    return groups, group_totals

def write_blocker_order(sorted_blockers, output_path):
    """Write sorted list of all blockers"""
    with open(output_path, 'w') as f:
        f.write("# Blockers sorted by number of blocked methods (descending)\n")
        f.write("# Format: blocker_method -> blocked_count\n\n")
        
        for blocker, count, methods in sorted_blockers:
            f.write(f"{blocker} -> {count}\n")

def write_group(group, output_path):
    """Write a single group file"""
    with open(output_path, 'w') as f:
        f.write("# Blocker group\n")
        f.write("# Format: blocker_method -> count\n")
        f.write("#   dependent_method_1\n")
        f.write("#   dependent_method_2\n")
        f.write("#   ...\n\n")
        
        for blocker, count, methods in group:
            f.write(f"{blocker} -> {count}\n")
            for method in methods:
                f.write(f"  {method}\n")
            f.write("\n")

def main():
    base_dir = Path("/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/final_label")
    scratch_dir = Path("/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch")
    
    blockers_file = base_dir / "blockers.txt"
    unresolved_file = scratch_dir / "unresolved_blockers.txt"
    
    # Parse original blockers
    print("Reading blockers.txt...", file=sys.stderr)
    blockers = parse_blockers(blockers_file)
    print(f"Found {len(blockers)} blockers", file=sys.stderr)
    
    # Filter based on current unresolved state
    print("Filtering resolved methods...", file=sys.stderr)
    blockers = filter_resolved_methods(blockers, unresolved_file)
    print(f"After filtering: {len(blockers)} blockers still unresolved", file=sys.stderr)
    
    # Sort by blocked count
    sorted_blockers = sort_blockers(blockers)
    
    # Calculate total blocked methods
    total_blocked = sum(count for _, count, _ in sorted_blockers)
    
    # Write blocker order
    order_file = base_dir / "blocker_order.txt"
    write_blocker_order(sorted_blockers, order_file)
    print(f"Wrote {order_file}", file=sys.stderr)
    
    # Distribute into 4 groups
    groups, group_totals = distribute_round_robin(sorted_blockers, 4)
    
    # Write each group
    for i, group in enumerate(groups, 1):
        group_file = base_dir / f"blocker_group_{i}.txt"
        write_group(group, group_file)
        print(f"Wrote {group_file} ({len(group)} blockers, {group_totals[i-1]} blocked methods)", file=sys.stderr)
    
    # Final summary
    print(f"\nSummary:", file=sys.stderr)
    print(f"  Total blockers: {len(sorted_blockers)}", file=sys.stderr)
    print(f"  Total blocked methods: {total_blocked}", file=sys.stderr)
    print(f"  Group sizes (by blocked method count): {group_totals}", file=sys.stderr)
    
    # Output for workflow (counts only)
    print(f"{len(sorted_blockers)} {total_blocked} {group_totals[0]} {group_totals[1]} {group_totals[2]} {group_totals[3]}")

if __name__ == "__main__":
    main()
