#!/usr/bin/env python3
# Remove contradicted UNREACHABLE entries from graph_def.py

contradictions = [
    "GlideRequests.<init>",
    "GlideRequests.as",
    "GlideRequests.asDrawable",
    "GlideRequests.setRequestOptions",
    "CopyService$DoInBackground.onPostExecute",
    "HybridFileParcelable$1.<init>",
    "MainFragment.lambda$reloadListElements$5",
    "BottomBar.areButtonsShowing",
    "ComputerParcelable$1.<init>",
    "AppTheme.<clinit>",
    "AppTheme.<init>"
]

with open('graphs/AmazeFileManager/graph_def.py', 'r') as f:
    lines = f.readlines()

new_lines = []
removed_count = 0

for line in lines:
    # Check if this line is an UNREACHABLE assignment for a contradicted method
    is_contradiction = False
    for method in contradictions:
        if f"'{method}'" in line and ('UNREACHABLE[' in line or "UNREACHABLE_" in line):
            # This might be part of a dict entry - need to check pattern
            if 'UNREACHABLE[' in line and '] =' in line:
                # Single-line UNREACHABLE[...] = ... assignment
                is_contradiction = True
                removed_count += 1
                print(f"REMOVING: {method}")
                break
            elif "': (" in line:
                # Dict entry like 'method': (kind, reason, ...)
                is_contradiction = True
                removed_count += 1
                print(f"REMOVING dict entry: {method}")
                break
    
    if not is_contradiction:
        new_lines.append(line)

print(f"\nRemoved {removed_count} contradicted UNREACHABLE entries")

with open('graphs/AmazeFileManager/graph_def.py', 'w') as f:
    f.writelines(new_lines)

print("DONE")
