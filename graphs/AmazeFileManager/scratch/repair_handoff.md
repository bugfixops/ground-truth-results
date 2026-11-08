# Phase 2b Repair Handoff - AmazeFileManager

**Date**: 2025-01-20
**Handoff from**: Batch 1-9 completion
**Next writer starts at**: Contraction pass for FRAMEWORK-HOP nodes

---

## 1. Current State: build_repair_09

**Build file**: `graphs/AmazeFileManager/scratch/build_repair_09.txt`

**Counts**:
```
methods 2981, pages 12, edges 7869
verdicts: REACHABLE 1827, UNREACHABLE 272, UNRESOLVED 882
errors: 1694
warnings: 101
```

**Error breakdown** (from orchestrator measurement):
- 692 unknown src/dst node (489 src, 203 dst)
- 139 'bad confirmed_by CALL' → **FIXED** ✓
- 77 'GUI edge must go page -> method'
- 5 bad kind
- 4 missing/invalid evidence
- 6 UNREACHABLE entry for unknown method
- 11 page not reachable
- 882 method has no path (expected; Phase 3 handles)

**Progress vs Baseline** (repair_baseline: 2272 errors, 1826 REACHABLE, 297 UNREACHABLE):
- Errors reduced: 2272 → 1694 (-578, 25% reduction)
- REACHABLE: 1826 → 1827 (+1, maintained)
- UNREACHABLE: 297 → 272 (-25, valid methods becoming UNRESOLVED as labels verified)

---

## 2. Work COMPLETED (Batches 1-9)

### Batch 1-2: Canonical Name Renames (build_repair_02, build_repair_03)
- ✅ **161 full-package-path → canonical renames** (Proposal 1 Group 1)
  - Example: `com.amaze.filemanager.activities.MainActivity.onActivityResult` → `MainActivity.onActivityResult`
  - Script: `scratch/apply_proposals.py`
  - Backup: `scratch/graph_def_before_repair_01.py`

- ✅ **11 JVM signature UNREACHABLE fixes**
  - 9 GlideRequests.load() methods: `GlideRequests.load(Landroid/graphics/Bitmap;)...` → `GlideRequests.load(Bitmap)`
  - 2 DatapointParcelable.<init>() methods
  - Script: `scratch/fix_jvm_signatures.py`
  - Backup: `scratch/graph_def_before_repair_02.py`

### Batch 3-4: Proposal 3 & 4 Retargets (build_repair_04)
- ✅ **28 FRAMEWORK → S_ENTRY retargets** (Proposal 3)
- ✅ **18 DialogPreference → S_PREFS retargets** (Proposal 3)
- ✅ **5 resolved overload renames** (Proposal 4):
  - `HybridFile.exists` → `HybridFile.exists()`
  - `HybridFile.folderSize` → `HybridFile.folderSize()`
  - `CompressedObjectParcelable.<init>` → `CompressedObjectParcelable.<init>()`
  - `CircularColorsView.<init>` → `CircularColorsView.<init>(Context)`
  - `HybridFile.getInputStream` → `HybridFile.getInputStream()`
- Script: `scratch/apply_all_proposals.py`
- Backup: `scratch/graph_def_before_repair_03.py`

### Batch 5-6: Glide UNREACHABLE Conflicts (build_repair_06)
- ✅ **27 Glide UNREACHABLE deletions** (pages.md Category A)
  - Methods like `GlideOptions.centerCrop`, `GlideOptions.diskCacheStrategy`, etc.
  - These had incoming bytecode edges, so they ARE reachable
  - Deleted UNREACHABLE entries to resolve contradictions
- Script: `scratch/delete_glide_unreachable.py`
- Documented in: `scratch/conflicts.md`
- Backup: `scratch/graph_def_before_repair_06.py`

### Batch 7-9: confirmed_by CALL Regression Fix (build_repair_09)
- ✅ **139 'bad confirmed_by CALL' → INFERRED/SOURCE**
  - Earlier edge normalizer incorrectly set confirmed_by field in UNREACHABLE tuples to 'CALL'
  - Fixed with: `sed -i.bak "s/, 'CALL'),/, 'INFERRED'),/g" graph_def.py`
  - All Glide/library entries now use INFERRED, app entries use SOURCE
- Backup: `scratch/graph_def_before_repair_07.py`

### Classification Pass
- ✅ **Classified 276 unique unknown nodes**:
  - **225 FRAMEWORK-HOP**: Framework classes, inherited/undeclared methods, pseudo-nodes
  - **51 APP-AMBIGUOUS**: App methods with ambiguous overloads or missing full signatures
- Script: `scratch/classify_unknown_nodes.py`
- Output files:
  - `scratch/framework_hop_nodes.txt` (225 entries with reasons)
  - `scratch/app_ambiguous_nodes.txt` (51 entries with reasons)

---

## 3. Key File Paths

### Build Outputs
- Latest: `graphs/AmazeFileManager/scratch/build_repair_09.txt`
- Baseline: `graphs/AmazeFileManager/scratch/repair_baseline.txt`
- Build sequence: build_repair_02, 03, 04, 06, 07, 08, 09 (10 was test that was rolled back)

### Backups (in graphs/AmazeFileManager/scratch/)
- `graph_def_before_repair_01.py` through `graph_def_before_repair_10.py`
- **Current active**: Restored to state before failed deletion attempt

### Classification Files
- `framework_hop_nodes.txt` - 225 FRAMEWORK-HOP nodes to contract
  - Format: `NodeName<TAB>Reason`
  - Example: `Application.onCreate	framework class Application not in method_list`
  
- `app_ambiguous_nodes.txt` - 51 APP-AMBIGUOUS nodes to resolve
  - Format: `NodeName<TAB>Reason`
  - Example: `FileUtils.openFile	ambiguous: 2 overloads exist`

### Requeue File
- `requeue_from_repair.txt` - 179 edges queued for Phase 3
  - Format: `EdgeID<TAB>Src<TAB>Dst<TAB>Kind<TAB>Evidence`
  - Edges with unknown endpoints that will be re-routed with canonical names

### Log Files
- `repair_log.md` - Spot checks and batch notes
- `repair_verification.md` - Build counts and regression checks
- `conflicts.md` - UNREACHABLE conflict resolutions
- `AGENT_NOTES.md` - C7 build tracking table (in /Users/darshan/Desktop/yang/work/)

### Scripts (in graphs/AmazeFileManager/scratch/)
- `classify_unknown_nodes.py` - Classify unknown nodes (already run)
  - Usage: `python3 -I scratch/classify_unknown_nodes.py`
  
- `delete_unknown_edges_ast.py` - AST-based edge deletion (DO NOT USE - failed invariant)
  - This approach was abandoned; use contraction instead

- `apply_proposals.py`, `fix_jvm_signatures.py`, etc. - Completed batch scripts

### Method List
- `graphs/AmazeFileManager/method_list.json` - Canonical method names
  - Format: List of dicts with 'short', 'class', 'name' fields

### Auto Calls (for APP-AMBIGUOUS resolution)
- `graphs/AmazeFileManager/auto_calls.json` - Bytecode call sites with full signatures

---

## 4. NEXT ACTION: Contraction Pass for FRAMEWORK-HOP Nodes

**Objective**: Contract all 225 FRAMEWORK-HOP nodes while preserving REACHABLE exactly.

### Contraction Specification

For each FRAMEWORK-HOP node **U** from `scratch/framework_hop_nodes.txt`:

#### 4.1 Create Bridging Edges
For every pair of edges **A→U** and **U→B**:

1. **Add a new edge A→B** with:
   - **Kind**: 
     - If A is a page (S_ENTRY, S_MAIN, etc.): Use the A→U kind (respects GUI/ENTERS/LIFECYCLE page rules)
     - Otherwise: Use the U→B kind (usually FRAMEWORK, LIFECYCLE, or CALL)
   
   - **Guards/env/needs_state**: Combined from both edges
     - Keep every guard from both
     - Union the env sets
     - Union the needs_state sets
   
   - **Evidence**: Join both evidence strings with `; `, then append:
     ```
     ; INFERRED framework dispatch through <U> (not an app method)
     ```
     The evidence MUST still begin with a valid label (SRC/FW-SRC/INFERRED)
     Example: If A→U has evidence "SRC Foo.java:42" and U→B has "FRAMEWORK Activity lifecycle", result is:
     ```
     SRC Foo.java:42; FRAMEWORK Activity lifecycle; INFERRED framework dispatch through Application.onCreate (not an app method)
     ```

2. **Remove all edges that touch U** (both A→U and U→B)

#### 4.2 Handle Special Cases

**Fake roots** (U has outgoing edges but NO incoming edges):
- Check if U is a real app entry from source (e.g., `Application.onCreate` - framework instantiates the Application subclass at process start)
- If YES: Replace U with the correct entry page (S_ENTRY, S_PREFS, etc.)
  - Change `Application.onCreate → AppConfig.<init>` to `S_ENTRY → AppConfig.<init>`
- If NO: Delete U's edges and append to `requeue_from_repair.txt`

**Sinks** (U has incoming edges only, no outgoing):
- Simply delete the incoming edges (safe - they lead nowhere)

#### 4.3 Logging Requirements
- Log every contraction to `scratch/repair_log.md`:
  - Node U contracted
  - Number of A→U edges, number of U→B edges, number of A→B bridges created
  - Any fake root replacements or sink deletions
  
- Append every deleted edge to `scratch/requeue_from_repair.txt`:
  ```
  EdgeID<TAB>Src<TAB>Dst<TAB>Kind<TAB>Evidence
  ```

#### 4.4 Implementation Approach

**Use AST parsing** for precision:
- Parse `graph_def.py` with Python's `ast` module
- Find all `e()` Call nodes
- Build edge index: {src: [(dst, edge_info), ...], dst: [(src, edge_info), ...]}
- For each U in framework_hop_nodes.txt:
  - Find all A where edge A→U exists
  - Find all B where edge U→B exists
  - Generate bridge edges A→B
  - Mark all A→U and U→B for deletion
  - Delete marked edges by line range (lineno to end_lineno)
  - Insert bridge edges at appropriate location (after last e() call in module)

**Backup before running**:
```bash
cp graph_def.py scratch/graph_def_before_contraction.py
```

#### 4.5 Invariant Checks (CRITICAL)

**Before rebuilding**, compare with pre-contraction file:
- ✓ UNREACHABLE[' occurrence count is IDENTICAL
- ✓ `grep -n '^UNREACHABLE *='` output is identical
- ✓ Number of non-e() top-level statements is identical
- ✓ File parses with `ast.parse()`

**After rebuilding**:
- ✓ **REACHABLE is UNCHANGED EXACTLY** (must be 1827)
- ✓ **UNREACHABLE is unchanged EXACTLY** (must be 272)
- ✓ Unknown-node errors drop by approximately the number of contracted nodes
- ✓ Total edge count changes as expected (deletions - additions)

**If ANY invariant fails**: Restore `scratch/graph_def_before_contraction.py` and debug the script.

#### 4.6 Testing Strategy

**Phase 1**: Test on ~20 FRAMEWORK-HOP nodes
- Pick simple cases: bare framework classes, clear inherited methods
- Avoid: fake roots, complex chaining
- Run contraction script
- Verify all invariants
- If successful, proceed to Phase 2

**Phase 2**: Run full contraction on all 225 nodes
- Back up again
- Run contraction
- Verify all invariants
- Build and verify REACHABLE=1827, UNREACHABLE=272

**Phase 3**: Update C7 line in AGENT_NOTES.md with new build counts

---

## 5. Steps Remaining After Contraction

### Step A: Resolve APP-AMBIGUOUS Nodes (51 nodes)

For each node in `scratch/app_ambiguous_nodes.txt`:

**For dst side (callee)**:
- Match (src_method, file, line) against `auto_calls.json`
- auto_calls.json records the full callee signature from bytecode
- Replace ambiguous name with the full signature

**For src side (caller)**:
- Print the source at the evidence line
- Check the method signature enclosing that line
- Pick the overload whose declared parameters match
- Replace ambiguous name with the matched overload

**Undecidable cases**:
- LEAVE THE EDGE AS-IS for now
- List in `scratch/ambiguous_remaining.txt`
- Phase 3 will handle these

**Verification**: Unknown-node errors for APP-AMBIGUOUS names should drop to ~0 (except undecidables)

### Step B: Fix 77 GUI Edge Errors

Error: "GUI edge must go page -> method"

**Cause**: Edge has kind=GUI but doesn't follow page→method pattern

**Fix approach**:
- Print the edge evidence to understand intent
- If src is not a page: Change kind to CALL or FRAMEWORK (based on evidence)
- If dst is not a method: Fix the endpoint or delete/requeue

**Script**: Create `scratch/fix_gui_edges.py` using AST to find GUI edges, print evidence, apply fixes

### Step C: Fix 5 Bad-Kind Edges + 4 Missing-Evidence Edges

**Bad kind**: Use full schema-2 kinds (CALL, FRAMEWORK, LIFECYCLE, GUI, etc.)
- Find edges with invalid kind values
- Replace with correct schema-2 kind based on edge semantics

**Missing evidence**: Every edge must have evidence
- Find edges with empty or missing evidence field
- Add evidence from source citation, or delete/requeue if source unclear

### Step D: Fix 6 UNREACHABLE Unknown-Method Entries

From build_repair_09 errors:
- AppConfig.toast
- Archive.lengthOf  
- ComputerParcelable.<init>
- DatapointParcelable.<init>(Landroid/os/Parcel;)V
- FileUtils.fileToContentUri
- FileUtils.scanFile

**Approach**:
- Run `tools/resolve_names.py` on these to find canonical names
- If found: Rename UNREACHABLE key to canonical
- If not found (method doesn't exist): Delete UNREACHABLE entry and log in repair_log.md

### Step E: Handle pages.md Conflicts and Unreachable Pages

**UNREACHABLE but has incoming edges** (~30 remaining app-specific methods from pages.md Category B):
- For each: Print edge source
- If edge is valid: DELETE the UNREACHABLE entry
- If edge is wrong: Fix or remove the edge
- Document each in `scratch/conflicts.md`

**11 pages not reachable from S_ENTRY**:
- S_DRAWER, S_MAIN_TAB, S_PREFS, S_TEXT_EDITOR, S_PERM, S_DB_VIEWER, S_SERVICE, S_EXIT, S_DIALOG, S_ABOUT, S_MAIN
- Per pages.md analysis: These are documentation labels, not meant to be reachable nodes
- **Decision needed**: Confirm with source whether these should have entry edges or remain as abstract page definitions

---

## 6. Known Pitfalls & Rules

### AST Edge Deletion Rules
- ❌ **NEVER** delete e() calls inside `for` loops, `while` loops, comprehensions, or `def` bodies
- ✓ **ONLY** delete top-level e() calls or those in top-level `if` blocks that contain only e() calls
- ❌ **NEVER** delete e() calls whose arguments are variables, f-strings, or expressions
- ✓ **ONLY** delete e() calls with string literal arguments

### UNREACHABLE Dict Rules
- ❌ **NEVER** touch UNREACHABLE tuple fields when normalizing edge kinds
- ✓ Edge normalization applies to `e()` calls only, not UNREACHABLE entries
- ✓ UNREACHABLE dict must have exactly ONE definition: `UNREACHABLE = {`
- ✓ Count of `UNREACHABLE['` must never change during edge operations

### Regression Rules
- **REACHABLE must not fall** - Any drop means reachability was broken
- **UNREACHABLE must be unchanged exactly** - Any change means UNREACHABLE dict was corrupted
- **On ANY invariant failure**: Restore backup immediately, fix script, re-run

### Evidence Rules
- All evidence must begin with valid label: SRC, FW-SRC, INFERRED, DYN, UNVERIFIED
- When joining evidence: Preserve the first label from the first evidence string
- Never create evidence that starts with semicolon or has no label

---

## 7. Verification Checklist for Next Writer

Before moving to next step:
- [ ] All invariant checks passed
- [ ] REACHABLE = 1827 (unchanged)
- [ ] UNREACHABLE = 272 (unchanged)
- [ ] `grep -n '^UNREACHABLE *=' graph_def.py` shows single definition
- [ ] `python3 -I -m py_compile graph_def.py` passes
- [ ] Unknown-node error count dropped by ~contracted node count
- [ ] C7 line added to AGENT_NOTES.md
- [ ] New backup created before next batch

---

## 8. Final Target for Phase 2b

**Goal**: All error categories at 0 EXCEPT 'method has no path' (882, expected for Phase 3)

**Expected final state**:
- Unknown node errors: 0
- GUI edge errors: 0
- Bad kind/evidence errors: 0
- UNREACHABLE unknown method errors: 0
- Page reachability: Resolved or documented as design choice
- REACHABLE: 1827 (maintained)
- UNREACHABLE: ~270-280 (may shift slightly as labels verified)

**Then**: Hand off to reviewer for approval to proceed to Phase 3 (path analysis and UNRESOLVED labeling)

---

**Handoff prepared**: 2025-01-20
**Next writer**: Begin with contraction pass, test on 20 nodes first, then full 225-node pass
