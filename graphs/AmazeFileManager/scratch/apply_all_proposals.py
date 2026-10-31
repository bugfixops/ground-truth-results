#!/usr/bin/env python3
"""
Apply all repair proposals systematically:
1. Apply decidable fixes (renames, retargets to S_ENTRY/S_PREFS, resolved overloads)
2. Delete edges with unknown endpoints and requeue them
3. Never delete edges where both endpoints are known
"""

import re
import sys

# Track all changes
changes_log = []
requeue_log = []
spot_checks = []

def log_change(change_type, details):
    changes_log.append(f"{change_type}: {details}")

def requeue_edge(edge_id, src, dst, kind, evidence):
    """Add edge to requeue file"""
    requeue_log.append(f"{edge_id}\t{src}\t{dst}\t{kind}\t{evidence}")

def find_edge_in_text(text, edge_id):
    """Find an edge by ID and return its text and position"""
    # Try to find the edge definition
    pattern = rf"e\(['\"]({re.escape(edge_id)})['\"]"
    match = re.search(pattern, text)
    if match:
        return match.start()
    return None

def extract_edge_info(text, start_pos):
    """Extract edge info starting from a position"""
    # Find the complete e(...) call
    paren_count = 0
    in_edge = False
    edge_start = start_pos
    
    # Back up to find the start of e(
    while edge_start > 0 and text[edge_start] != '\n':
        if text[edge_start:edge_start+2] == 'e(':
            break
        edge_start -= 1
    
    # Now find the end
    i = edge_start
    while i < len(text):
        if text[i] == '(':
            paren_count += 1
            in_edge = True
        elif text[i] == ')':
            paren_count -= 1
            if in_edge and paren_count == 0:
                return text[edge_start:i+1]
        i += 1
    return None

def delete_edge(text, edge_text):
    """Delete an edge from the text"""
    # Find the complete line(s) including newlines
    start = text.find(edge_text)
    if start == -1:
        return text, False
    
    # Find the start of the line
    line_start = start
    while line_start > 0 and text[line_start-1] != '\n':
        line_start -= 1
    
    # Find the end (after the closing paren and newline)
    line_end = start + len(edge_text)
    while line_end < len(text) and text[line_end] != '\n':
        line_end += 1
    if line_end < len(text):
        line_end += 1  # Include the newline
    
    new_text = text[:line_start] + text[line_end:]
    return new_text, True

def apply_proposal_3_renames(text):
    """Apply Proposal 3 decidable fixes: FRAMEWORK->S_ENTRY, DialogPreference->S_PREFS"""
    changes = 0
    
    # Replace FRAMEWORK with S_ENTRY in e() calls (28 edges)
    # Be careful to only replace in src position
    text = re.sub(r"e\('FRAMEWORK'", "e('S_ENTRY'", text)
    framework_count = len(re.findall(r"e\('S_ENTRY',", text))
    
    # Replace DialogPreference with S_PREFS (18 edges from proposal 3)
    text = re.sub(r"e\('DialogPreference'", "e('S_PREFS'", text)
    
    log_change("Proposal 3", f"Replaced FRAMEWORK→S_ENTRY and DialogPreference→S_PREFS")
    return text

def apply_proposal_4_resolved_overloads(text):
    """Apply Proposal 4 resolved overloads (the ones helper marked as decidable)"""
    # From proposal 4, these were resolved:
    renames = {
        'HybridFile.exists': 'HybridFile.exists()',
        'HybridFile.folderSize': 'HybridFile.folderSize()',
        'CompressedObjectParcelable.<init>': 'CompressedObjectParcelable.<init>()',
        'CircularColorsView.<init>': 'CircularColorsView.<init>(Context)',
        'HybridFile.getInputStream': 'HybridFile.getInputStream()',
    }
    
    for old_name, new_name in renames.items():
        if old_name in text:
            text = re.sub(
                r"(['\"])" + re.escape(old_name) + r"(['\"])",
                r"\1" + new_name + r"\2",
                text
            )
            log_change("Proposal 4 overload", f"{old_name} → {new_name}")
    
    return text

def delete_framework_edges(text):
    """Delete edges to/from framework classes per Proposal 1 REMOVE group"""
    framework_classes = [
        'ActionMode.Callback.<init>',
        'AndroidAsyncTask.execute',
        'AndroidAsyncTask.onPostExecute',
        'AppCompatActivity.startSupportActionMode',
        'Context.bindService',
        'Context.sendBroadcast',
        'Context.startService',
        'Context.stopService',
        'Drawable',
        'DrawerLayout.setDrawerListener',
        'EventBus.register',
        'InflaterInputStream.close',
        'InflaterInputStream.read',
        'LayoutInflater.inflate',
        'MediaScannerConnection.connect',
        'MediaScannerConnection.scanFile',
        'Parcelable.Creator',
        'RecyclerView.draw',
        'RecyclerView.measureChild',
        'RecyclerView.setAdapter',
        'ScheduledExecutorService.scheduleWithFixedDelay',
        'ViewTreeObserver.addOnGlobalLayoutListener',
        'BaseSavedState',
        'BroadcastReceiver.<init>',
        'DeflaterOutputStream.close',
        'DeflaterOutputStream.write',
        'GridLayoutManager.SpanSizeLookup.<init>',
        'ImageLoader.get',
        'JVM',
        'MainActivity',  # bare className, no method
        'Thread.<init>',
        'Thread.run',
        'Thread.start',
        'android.view.LayoutInflater.inflate',
        'CloudStreamServer',
        'CloudStreamer',
        'SevenMethodConfiguration.setContentMethods',
        'SubnetScanner$ScanNodeTask.call',
        'SmbFile',
        'GlideListPreloader.onScroll',
    ]
    
    deleted_count = 0
    for fw_class in framework_classes:
        # Find all edges that reference this framework class
        pattern = rf"e\([^,]*['\"]({re.escape(fw_class)})['\"][^)]*\)"
        matches = list(re.finditer(pattern, text))
        for match in reversed(matches):  # Delete from end to preserve positions
            edge_text = match.group(0)
            # Extract basic info for requeue
            parts = edge_text.split("'")
            if len(parts) >= 6:
                src = parts[1]
                dst = parts[3]
                kind = parts[5] if len(parts) > 5 else 'CALL'
                evidence = 'Framework class edge - requeueing'
                
                # Find edge ID if present
                edge_id = "AUTO"
                if edge_text.startswith("e('") and len(parts) > 0:
                    edge_id = parts[1]
                
                requeue_edge(edge_id, src, dst, kind, evidence)
                
            text, success = delete_edge(text, edge_text)
            if success:
                deleted_count += 1
    
    log_change("Framework edges deleted", str(deleted_count))
    return text

def main():
    graph_path = '/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/graph_def.py'
    
    print("Reading graph_def.py...")
    with open(graph_path, 'r') as f:
        text = f.read()
    
    original_length = len(text)
    
    print("\n=== Applying Proposal 3 renames ===")
    text = apply_proposal_3_renames(text)
    
    print("\n=== Applying Proposal 4 resolved overloads ===")
    text = apply_proposal_4_resolved_overloads(text)
    
    print("\n=== Deleting framework class edges ===")
    # Commenting this out for now - too risky to do in bulk
    # text = delete_framework_edges(text)
    
    print(f"\n=== Writing updated graph_def.py ===")
    with open(graph_path, 'w') as f:
        f.write(text)
    
    print(f"Original length: {original_length}, New length: {len(text)}")
    
    print("\n=== Change Summary ===")
    for change in changes_log:
        print(f"  {change}")
    
    if requeue_log:
        print(f"\n=== Writing requeue file ({len(requeue_log)} edges) ===")
        with open('/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/requeue_from_repair.txt', 'a') as f:
            for line in requeue_log:
                f.write(line + '\n')
    
    print("\nDone!")

if __name__ == '__main__':
    main()
