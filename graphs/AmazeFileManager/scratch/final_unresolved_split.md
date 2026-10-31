# Final Unresolved Methods Split

**Source:** build_cleanup_07.txt (2026-10-28 23:29)

## Summary

Total methods: 2981
- REACHABLE: 2218 (74.4%)
- UNREACHABLE: 422 (14.2%)
- UNRESOLVED: 341 (11.4%)

## Unresolved Split

### (a) Methods with NO incoming edge (truly unlabeled)
**Count: 84 methods**

These methods have no incoming edges at all in the current graph. They need to be labeled from scratch by reading source code.

Batched into 3 files of ≤40 methods each:
- batch_01.txt: methods 1-40
- batch_02.txt: methods 41-80
- batch_03.txt: methods 81-84

See  for batch details.

### (b) Methods chain-blocked by unreachable/unresolved sources
**Count: 257 methods**

These methods have incoming edges, but ALL incoming edges come from UNREACHABLE or UNRESOLVED methods. They are blocked by upstream methods that need to be resolved first.

**Blocker analysis:**
- 147 unique blocker methods identified
- Blockers sorted by number of methods they unblock
- Top blockers: S_PREFS (8 methods), AndroidAnimator.addListener (8 methods), SftpConnectDialog.onCreateDialog (8 methods)

See  for complete blocker → blocked mapping.

## Batch Assignment (Round-Robin)

Batches assigned to 4 slots for parallel processing:
- Slot 1: batch_01.txt (1 batch)
- Slot 2: batch_02.txt (1 batch)
- Slot 3: batch_03.txt (1 batch)
- Slot 4: (empty)

Total: 84 methods in 3 batches across 3 non-empty slots.

## Files Created

-  - Batch 1 methods (≤40)
-  - Batch 2 methods (≤40)
-  - Batch 3 methods (≤40)
-  - Batch index
-  - Slot 1 batch list
-  - Slot 2 batch list
-  - Slot 3 batch list
-  - Slot 4 batch list (empty)
-  - Blocker analysis for chain-blocked methods

## Next Steps

1. Process batches from group (a) using helpers (slots 1-3)
2. After group (a) is labeled, re-build and analyze blockers from group (b)
3. Iteratively resolve blocker chains until UNRESOLVED reaches 0
