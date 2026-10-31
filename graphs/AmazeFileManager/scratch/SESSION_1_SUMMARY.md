# AmazeFileManager Schema-2 Re-audit - Session 1 Summary

## Status: IN PROGRESS (NOT DONE)

This is a checkpoint for a multi-session task. The app is large (2,981 methods) and requires 10-16 additional hours of careful work.

## What Was Accomplished

### Foundation Built
1. **Entry points complete** (11 components):
   - Application: AppConfig → GlideApplication → LeakCanaryApplication chain
   - MainActivity: 8 intent-filter contexts (MAIN, GET_CONTENT, RINGTONE_PICKER, VIEW_ARCHIVE, SEND, QS_PREF, SCHEME, FOLDER)
   - 4 other activities with lifecycle chains
   - 7 services with onCreate/onStartCommand
   - FtpReceiver with 2 contexts (START/STOP)

2. **Activity hierarchy mapped**:
   - MainActivity → PermissionsActivity → ThemedActivity → PreferenceActivity → BasicActivity → AppCompatActivity
   - Similar for other activities

3. **Key UI path established**:
   - MainActivity.onCreate → AsyncTask → onPostExecute → goToMain → TabFragment → MainFragment
   - MainFragment lifecycle: <init> → onCreate → onCreateView → onActivityCreated
   - RecyclerAdapter reached via AUTO bytecode edges

4. **Build progress**:
   - Build 001: 145 REACHABLE, 2851 errors
   - Build 002: 440 REACHABLE, 2559 errors  
   - Build 003: 638 REACHABLE, 2369 errors
   - **Progress: +493 methods reached, -482 errors**

### Files Created/Modified
- `graphs/AmazeFileManager/graph_def.py` (317 lines, sections A-G started)
- `graphs/AmazeFileManager/AGENT_NOTES.md` (comprehensive progress tracking)
- `graphs/AmazeFileManager/scratch/build_001.txt, build_002.txt, build_003.txt`
- `graphs/AmazeFileManager/scratch/CHECKPOINT_PLAN.md` (detailed strategy)
- `graphs/AmazeFileManager/scratch/SESSION_1_SUMMARY.md` (this file)

### Rules Compliance
- ✅ All edges cite source files (SRC) or framework (FW-SRC, INFERRED)
- ✅ No FW-MEMORY, DYN, or UNVERIFIED used
- ✅ USE_AUTO = True, leveraging bytecode extraction (5,983 of 6,064 edges)
- ✅ STRICT = True in graph_def.py
- ✅ Working from /Users/darshan/Desktop/yang/work, using WORKING_LOCK
- ✅ Committed all progress to disk continuously
- ✅ Removed SMSInstrumentedReceiver (not in APK/method_list.json)

## What Remains (Estimated 10-16 Hours)

### Phase 1: Build to 0 Errors (6-10 hours)
1. **Add more fragments** (~2 hours):
   - ProcessViewerFragment, FtpServerFragment, CloudSheetFragment
   - CompressedExplorerFragment, AppsListFragment
   - Dialog fragments (176 methods in ui/dialogs/)

2. **UNREACHABLE labeling** (~4-6 hours):
   - **Glide (179 methods)**: Read which methods are actually called from reachable code
     - Most are generated library defaults → no_trigger_in_app or framework_never_calls
   - **7z library (252 methods)**: Check if .7z format is supported
     - If not supported → no_trigger_in_app
     - If supported, only entry points reachable, helpers → framework_never_calls
   - **Cloud storage (~100 methods)**: Check if cloud accounts configured in standard setup
     - No accounts in fresh install → closed_by_configuration
   - **Root operations (~30 methods)**: Check root requirements
     - Not rooted + not enabled → closed_by_configuration
   - **SSH/SMB (~90 methods)**: Check if servers configured
     - No servers in standard setup → closed_by_configuration
   - **Remaining adapters/fragments**: If parent fragment/activity not shown → no_trigger_in_app

3. **Build iterations**:
   - After each labeling batch: rebuild, fix any new issues
   - Target: 0 errors, 0 warnings, ~1000-1500 REACHABLE, ~1500-2000 UNREACHABLE

### Phase 2: Route Verification (4-6 hours)
1. **Sample 30 routes** (~15 min):
   ```bash
   python3 -I tools/verify_sample.py AmazeFileManager 30 20261025 > graphs/AmazeFileManager/scratch/sample_30.txt
   ```

2. **Set up route printer** (~30 min):
   - Copy `handoff/examples/route_print_template.py` to `graphs/AmazeFileManager/scratch/route_print.py`
   - Set constants: GDIR, SAMPLE, METHODS_CSV, GRAPH_JSON, OUT_DIR, APP_BASE, APP_MODULE
   - Verify no "AnyMemo" references remain

3. **Print and verify all 30 routes** (~2-3 hours):
   - Run route_print.py to print each route with source lines
   - Read EVERY step against printed source (including if/catch/for conditions)
   - Check against mistakes list (AGENT_BRIEF_V2.md section 5):
     * First-resume shortcut
     * Guard-ignoring best route
     * Early return hiding guard
     * Static flag
     * File URI vs content URI
     * Guard-less bytecode edge
     * Off-by-one line number
     * ENV text not matching code
   - Mark each route: correct / fixed / wrong / unclear
   - Record in scratch/route_check_notes.md

4. **Fix wrong routes** (~1-2 hours):
   - For each wrong route: update graph_def.py, rebuild, reprint
   - Log in `scratch/fix_log.md`: method, step, printed lines, change made
   - After LAST fix: re-sample (final sample must match final graph)

5. **Compute error rate**:
   - Error rate = (fixed + wrong) / (correct + fixed + wrong)
   - Document in final report

### Phase 3: Checks and Documentation (2-3 hours)
1. **Run all 8 section-6 checks**, save output to scratch/:
   ```bash
   python3 -I tools/build_graph.py graphs/AmazeFileManager amazefilemanager
   python3 -I tools/check_citations.py AmazeFileManager
   python3 -I tools/check_routes.py AmazeFileManager
   python3 -I tools/check_bytecode_lines.py AmazeFileManager
   grep -c "DEAD\|FRAMEWORK_ONLY" graphs/AmazeFileManager/graph_def.py
   grep -c "FW-MEMORY" graphs/AmazeFileManager/graph_def.py
   grep -c "PENDING" graphs/AmazeFileManager/graph_def.py
   python3 -I tools/scan_unreachable.py AmazeFileManager --all
   python3 -I tools/scan_unreachable.py AmazeFileManager --callers
   ```
   All must pass (0 errors, 0 warnings, 0 FW-MEMORY, 0 PENDING, etc.)

2. **Generate verification.csv**:
   - Write `graphs/AmazeFileManager/make_verification.py` (on pattern of examples/make_vlog_omni_notes.py)
   - Assert every note against the graph (has_edge)
   - Rows: path (per sampled method), label (per UNREACHABLE and sampled REACHABLE), edge (per corrected edge and FW claim checked)
   - Columns: type, item, result, confirmed_by, ref, edges, note

3. **Write documentation**:
   - `readme_notes.md` with exactly 5 sections (in order):
     1. What the re-audit changed (compared with schema 1 graph)
     2. How the checked paths were chosen
     3. What waits for a device (API 27)
     4. Hazard candidates (from reading code, not reproduced)
     5. Limits
   - Run `python3 -I tools/gen_readme_v2.py AmazeFileManager`
   - `LESSONS.md`: 3-8 short bullets on what found real errors in this app

4. **Final verification**:
   - All section-6 checks pass
   - All section-7 logs exist
   - No "PENDING" anywhere
   - No decisions written in someone else's name
   - No waivers

5. **Update PROGRESS**:
   - Change `handoff/PROGRESS_V2.md` from:
     `- [K] AmazeFileManager (Kiro queue, not started)`
   - To:
     `- [K] AmazeFileManager (Kiro DONE YYYY-MM-DD, awaiting user tick)`
   - Add paragraph to `handoff/KIRO_APPS_STATUS.md`

6. **Write final message**:
   - `graphs/AmazeFileManager/scratch/kiro_final_message.txt` (≤12 lines)
   - App, status, build counts, route table, check results, files changed, blockers

## Key Decisions Made

1. **SMSInstrumentedReceiver**: Removed from graph - not in APK (method_list.json) despite being in manifest
2. **JaCoCo receiver**: Documented in manifest but not built, cannot be modeled
3. **Flavor**: DATASET.txt does not name a flavor, using src/main only (documented in AGENT_NOTES.md)
4. **GlideApplication**: Part of app's Application inheritance chain, but most Glide methods likely unreachable
5. **PreferenceActivity**: In app code (not android.preference.PreferenceActivity)

## Blockers / Issues

**None currently**. Task is straightforward but large. Requires time and careful reading of source code.

## Files to Read for UNREACHABLE Labeling

Critical source files to read (not yet fully read):
1. `MainActivity.java` (1963 lines) - complete onCreate/onResume logic, fragment management
2. `MainFragment.java` - adapter instantiation, when RecyclerAdapter/Glide used
3. `TabFragment.java` - how it creates MainFragments
4. `CloudSheetFragment.java / CloudHandler.java` - cloud account configuration
5. `Archive handling code` - which formats supported (.7z vs .zip vs .rar)
6. `Root/SSH/SMB code` - requirements and configuration
7. `Glide usage sites` - which app classes actually call GlideApp methods

## Next Session Should

1. **Continue from Build 003** (638 REACHABLE, 2369 errors)
2. **Read CHECKPOINT_PLAN.md** for detailed strategy
3. **Either**:
   - Add 2-3 more key fragments (ProcessViewer, FtpServer, CloudSheet), OR
   - Begin UNREACHABLE labeling immediately (Glide, 7z, cloud, root, SSH/SMB)
4. **Build iteratively** to 0 errors
5. **Then proceed to Phase 2** (route verification)

## Time Investment So Far

Approximately 3-4 hours invested in:
- Reading documentation and understanding requirements
- Reading app manifest and key source files (partial)
- Building initial graph_def.py structure
- 3 build iterations with progressive improvements
- Creating comprehensive documentation and checkpoint plan

## Estimated Time to Completion

**10-16 hours** remaining:
- Phase 1 (Build to 0 errors): 6-10 hours
- Phase 2 (Route verification): 4-6 hours
- Phase 3 (Checks and docs): 2-3 hours

**Total estimated**: 13-19 hours for complete, correct re-audit.

## Compliance Notes

- Following all rules strictly
- Not using guesses or shortcuts
- Citing source for every decision
- Working durably (all progress on disk)
- Ready for continuation by another session or human
- No scope reduction requested or taken
