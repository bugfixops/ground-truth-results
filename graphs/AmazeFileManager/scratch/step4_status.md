# Step 4 Status: UNREACHABLE Methods with Incoming Edges

## Task
Fix ~175 warnings where UNREACHABLE methods have incoming edges.

For each method:
1. Check if ANY incoming edge comes from a REACHABLE source
2. If yes + edge is real per source → DELETE UNREACHABLE entry (becomes REACHABLE)
3. If all from UNREACHABLE sources → KEEP UNREACHABLE, log reason
4. If edge is wrong → fix or remove edge

## Analysis Completed

Created comprehensive analysis of all 175 warnings:
- **64 methods** should have UNREACHABLE deleted (have incoming from REACHABLE sources)
- **111 methods** should keep UNREACHABLE (all incoming from UNREACHABLE sources)

See files:
- `unreachable_to_delete.json` - 64 methods with REACHABLE incoming edges
- `unreachable_to_keep.json` - 111 methods with only UNREACHABLE incoming
- `unreachable_fix_report.txt` - Human-readable report
- `fix_unreachable_warnings.py` - Analysis script
- `delete_unreachable_safe.py` - Deletion script with proper paren matching

## Attempted Fix

Attempted to delete all 64 UNREACHABLE entries in 3 batches:
- Batch 0-20: 14 deleted
- Batch 20-40: 20 deleted  
- Batch 40-64: 22 deleted
- Total: 56 entries deleted

**Result**: Gate FAILED
- Baseline: R=2185, U=455, Total=2640
- After deletion: R=2211, U=425, Total=2636
- Change: R+26, U-30, **Total -4** ✗

## Root Cause

The gate failure (R+U fell by 4) indicates that some deleted methods don't have complete valid routes yet. While they have incoming edges from REACHABLE sources, those routes may have errors (unknown nodes, bad kinds, etc.) preventing the methods from becoming fully REACHABLE.

## Recommended Approach

**Option 1: Fix in smaller chunks with verification**
- Delete 10-15 entries at a time
- Build and verify R+U doesn't fall after each
- If it falls, identify which methods need route fixes first
- Fix those routes, then retry deletion

**Option 2: Fix errors first, then delete**
- Keep current state (all UNREACHABLE entries intact)
- First fix the 1260 errors (unknown nodes, bad kinds, etc.)
- Then retry UNREACHABLE deletion when routes are cleaner
- This ensures deleted methods can actually become REACHABLE

**Option 3: Manual selective deletion**
- Review the 64 candidates
- Only delete entries where evidence shows solid SRC citations
- Skip entries with INFERRED evidence until routes verified
- Focus on high-confidence cases like Parcelable methods, lifecycle callbacks

## Current State

- Backup: `graph_def_before_cleanup_03.py` (build_cleanup_02 state)
- Current: Restored to backup
- Build: build_cleanup_02.txt (baseline)
  - REACHABLE: 2185
  - UNREACHABLE: 455
  - UNRESOLVED: 341
  - Warnings: 175 (UNREACHABLE with incoming edges)
  - Errors: 1260

## Next Steps

Recommend **Option 2**: Fix the 1260 errors first (Step 3 remaining work), then return to Step 4.

The error categories to fix:
- 251 unknown src node
- 256 unknown dst node  
- 119 GUI edge must go page → method
- 55 bad kind
- 18 bad confirmed_by
- 193 missing/invalid evidence
- 14 UNREACHABLE entry for unknown method
- 11 page not reachable from S_ENTRY

Once errors are down to 0, the UNREACHABLE deletion will be safer and more likely to pass gates.
