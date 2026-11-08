#!/bin/bash
# Watch for new label parts and merge them automatically

PARTS_DIR="/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/parts"
WORK_DIR="/Users/darshan/Desktop/yang/work"
MERGED_LOG="/Users/darshan/Desktop/yang/work/graphs/AmazeFileManager/scratch/auto_merged.log"

cd "$WORK_DIR"

echo "Watching for new parts (batch 013+)..." | tee -a "$MERGED_LOG"

while true; do
    # Check for new .py files (batch 013 onwards that aren't merged yet)
    for part in "$PARTS_DIR"/label_b0{13..20}.py; do
        if [ -f "$part" ]; then
            basename=$(basename "$part" .py)
            
            # Check if already merged
            if grep -q "# ---- part $basename" graphs/AmazeFileManager/graph_def.py 2>/dev/null; then
                continue
            fi
            
            echo "=== Found new part: $basename ===" | tee -a "$MERGED_LOG"
            date | tee -a "$MERGED_LOG"
            
            # Backup
            cp graphs/AmazeFileManager/graph_def.py "graphs/AmazeFileManager/scratch/backup_before_${basename}.bak"
            
            # Merge
            python3 -I graphs/AmazeFileManager/scratch/do_merge.py "$basename" 2>&1 | tee -a "$MERGED_LOG"
            
            # Build and capture stats
            echo "Building..." | tee -a "$MERGED_LOG"
            touch handoff/WORKING_LOCK
            python3 -I tools/build_graph.py graphs/AmazeFileManager amazefilemanager 2>&1 | head -20 | tee -a "$MERGED_LOG"
            
            echo "---" | tee -a "$MERGED_LOG"
        fi
    done
    
    # Sleep and repeat
    sleep 30
done
