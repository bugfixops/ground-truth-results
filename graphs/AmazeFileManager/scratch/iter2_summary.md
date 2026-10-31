# AmazeFileManager Fix Iteration 2 Summary

**Date**: 2026-10-27  
**Reviewer verdict**: CHANGES_REQUESTED (7 blocking findings)  
**Starting state**: Build errors 2637, UNRESOLVED 1716 (57.6%)  
**Current state**: Build errors 2035, UNRESOLVED 1850 (62.1%)  

## What Was Fixed

### 1. Schema-1 Edge Kinds (Priority 1, partial)
**Problem**: 212 edges used invalid schema-1 kinds (EXPLICIT, DIRECT, CONSTRUCTED, INFERRED, IMPLICIT)  
**Fix**: Created `fix_schema1_kinds.py` that converted all to CALL:
- EXPLICIT → CALL: 154 edges
- DIRECT → CALL: 26 edges  
- CONSTRUCTED → CALL: 28 edges
- INFERRED → CALL: 198 occurrences (includes evidence text)
- IMPLICIT → CALL: 2 edges

**Result**: Eliminated all "bad kind" errors. Build errors reduced by 209.

### 2. Unknown Node Errors (Priority 1, partial)
**Problem**: 2428 errors from 289 methods referenced in edges but never defined  
**Analysis**: 
- 221 methods don't exist in method_list.json (helper mistakes, wrong method names)
- 33 methods DO exist in method_list.json but have no label yet

**Fix**: Created `fix_unknown_nodes_v2.py` that removed 418 complete edge definitions referencing the 221 non-existent methods.

**Result**: Build errors reduced from 2345 to 2035. Remaining 2035 errors are from the 33 methods that exist but need labels.

## What Remains (Blocking)

### Priority 1: Fix Remaining 2035 Build Errors
The 33 methods in `unknown_exists.txt` exist in method_list.json and are referenced in edges, but have no REACHABLE edges or UNREACHABLE[] assignments. Examples:
- AppConfig.toast (4 edge references)
- CompressedObjectParcelable.<init> (referenced but no label)
- BoundedFileChannelInputStream.read (referenced but no label)
- CloudStreamServer.<init>, CloudStreamServer$Response.<init>
- AsyncTaskResult.<init>
- ColorPickerDialog$SavedState.<init>
- CircleGradientDrawable.<init>, CircularColorsView.<init>
- DataUtils.addBook, .contains, .containsServer
- Drawer.addNewItem
- FileUtils.fileToContentUri
- ... and 20 more

Each needs source reading to decide REACHABLE (add routes) or UNREACHABLE (explain why with kind, reason, ref).

### Priority 2: Label 1850 UNRESOLVED Methods
After fixing the 33 methods above, 1817 other methods in method_list.json still have no label. The review requires UNRESOLVED: 0.

### Priority 3: Resolve 2 Contradictions
- FileUtils.getBaseFileSize: marked UNREACHABLE but ran in tools
- FileUtils.isSelfDefault: marked UNREACHABLE but ran in tools

Must read source, print call sites, decide REACHABLE (add routes) or UNREACHABLE (explain why tool run doesn't matter).

### Priority 4: Route Verification (Section 4, untouched)
1. Copy handoff/examples/route_print_template.py to scratch/route_print.py, configure
2. Draw sample: `verify_sample.py AmazeFileManager 30`
3. Print all sampled routes with full source lines
4. Judge every route (correct/fixed/wrong/unclear) against mistakes list
5. Fix wrong routes in graph_def.py, rebuild, re-print
6. Log fixes in fix_log.md
7. Re-draw sample, produce route table with error rate

### Priority 5: Section 6 Checks (missing saved outputs)
Must run and save outputs for:
- check_citations.py (blocked by build errors)
- check_routes.py (blocked by no routes)
- check_bytecode_lines.py
- 3 grep checks (DEAD, FW-MEMORY, PENDING)
- scan_unreachable.py --all and --callers

### Priority 6: Section 7 Deliverables (all missing)
- verification.csv (path/label/edge rows for all sampled and UNREACHABLE methods)
- make_verification.py (script that generates verification.csv and asserts notes)
- readme_notes.md (5 exact headings)
- LESSONS.md (3-8 bullets)
- Run gen_readme_v2.py

### Priority 7: Flip PROGRESS_V2.md, Write Status Paragraph
Only after all above complete.

## Estimated Remaining Effort

**Conservative estimate**: 20-40 agent-hours
- Labeling 1850 methods: ~15-30 hours (reading source, deciding labels, batching/merging)
- Route verification: ~3-5 hours (sample, print, judge, fix, re-check)
- Section 6/7: ~2-5 hours (run checks, generate deliverables)

**Approach options**:
1. **Incremental single-agent**: Continue over 10-20+ sessions, each fixing a batch of ~100-200 methods
2. **Parallel multi-agent**: Launch 4-8 helper agents each labeling a class-based batch (similar to Sonnet waves documented in AGENT_NOTES build 013-048)
3. **Partial completion**: Accept that AmazeFileManager is too large for the conversion recipe timeframe, document findings, move to next app

## Files Created This Session

Scripts:
- `scratch/fix_schema1_kinds.py` - converted 408 schema-1 edge kinds to CALL
- `scratch/check_unknown_nodes.py` - checked which unknown nodes exist in method_list.json
- `scratch/fix_unknown_nodes_v2.py` - removed 418 edges referencing 221 non-existent methods

Outputs:
- `scratch/unknown_nodes.txt` - 254 unique unknown method names from build errors
- `scratch/unknown_exists.txt` - 33 methods that exist, need labels (PRIORITY)
- `scratch/unknown_not_exists.txt` - 221 methods removed
- `scratch/nodes_need_labels.txt` - TODO list for the 33 methods
- `scratch/build_iter2_current.txt` - current build output (2440 lines, 2035 errors)

Backups:
- `graph_def.py.broken_iter2` - the broken state from first fix attempt (indentation error)

## Next Steps (Awaiting User Direction)

**If continuing**: Start with Priority 1 (fix 33 methods in unknown_exists.txt), then continue labeling the remaining 1817 UNRESOLVED methods in batches. Use helper agents if available to parallelize.

**If pivoting**: Document the blockers in graphs/AmazeFileManager/AGENT_NOTES.md under "## Blocked" section and report NOT DONE to user.
