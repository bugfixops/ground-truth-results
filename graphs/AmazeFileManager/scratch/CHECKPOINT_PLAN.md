# AmazeFileManager Re-audit Checkpoint and Plan

## Current Status (Build 002)
- **Methods total**: 2,981
- **REACHABLE**: 440 (14.8%)
- **UNRESOLVED**: 2,541 (85.2%)
- **Errors**: 2,559
- **Auto edges working**: 5,993 of 6,060 edges from bytecode (USE_AUTO=True)

## What's Been Done

### Entry Points (Complete)
- ✅ Application: AppConfig → GlideApplication → LeakCanaryApplication → MultiDexApplication
- ✅ MainActivity: 8 intent-filter contexts (MAIN/LAUNCHER, GET_CONTENT, RINGTONE_PICKER, VIEW_ARCHIVE, SEND, QS_TILE_PREFERENCES, SCHEME, FOLDER)
- ✅ PreferencesActivity, TextEditorActivity, DatabaseViewerActivity, AboutActivity
- ✅ 7 Services: ExtractService, ZipService, CopyService, EncryptService, DecryptService, FtpService, FtpTileService
- ✅ 2 Receivers: FtpReceiver (START/STOP variants)

### Lifecycle Chains (Partial)
- ✅ Activity hierarchy: MainActivity/etc → PermissionsActivity → ThemedActivity → PreferenceActivity → BasicActivity
- ✅ Service lifecycle: <init> → onCreate → onStartCommand
- ✅ Basic MainActivity: onCreate → initialisePreferences/initialiseViews/initialiseFab → onResume → onCreateOptionsMenu → onOptionsItemSelected

### NOT Done Yet
- ❌ Fragments (226 methods): MainFragment, CloudSheetFragment, FtpServerFragment, CompressedExplorerFragment, AppsListFragment, etc.
- ❌ Adapters (~100+ methods): RecyclerAdapter, AppsAdapter, HiddenAdapter, CompressedExplorerAdapter, etc.
- ❌ Dialogs (176 methods in ui/dialogs/)
- ❌ Detailed MainActivity logic (file operations, drawer, FAB actions, tabs)
- ❌ Cloud storage integrations (Dropbox, Drive, OneDrive, Box)
- ❌ FTP server UI and implementation
- ❌ Archive handling (7z - 252 methods, other formats)
- ❌ SSH/SFTP and SMB filesystem support
- ❌ Text editor and database viewer internals
- ❌ Complete Glide integration (179 methods - needs fragments to be reachable first)

## The Two-Phase Strategy

### Phase 1: Build to Completeness (Target: 0 errors, reasonable coverage)

**Approach A: Add More Paths (Slower, More Complete)**
1. Add MainFragment lifecycle and key methods
2. Add key adapters with onCreate/onCreateViewHolder/onBindViewHolder
3. Add dialog fragments
4. Add drawer and FAB interactions
5. Build iteratively until REACHABLE ~1000-1500 methods
6. Then mark remaining ~1500-2000 as UNREACHABLE

**Approach B: Strategic UNREACHABLE Labeling (Faster)**
1. Add 1-2 more key fragments (MainFragment especially)
2. Begin systematic UNREACHABLE labeling for large groups:
   - **Glide generated code** (179 methods): Most are library defaults not used by app → no_trigger_in_app or framework_never_calls
   - **7z library** (252 methods in sevenz/): Many are internal helpers → framework_never_calls or no_trigger_in_app if .7z archives never opened
   - **Cloud storage** (~100 methods): If no cloud accounts configured in standard setup → closed_by_configuration
   - **Root operations**: If not rooted → closed_by_configuration
   - **Adapters for unused features**: no_trigger_in_app if the fragment/activity never shown
3. Build to 0 errors faster
4. Proceed to route verification

**RECOMMENDED**: Approach B - it's more realistic given scope and follows the rules' intent (label from source, mark what's genuinely unreachable)

### Phase 2: Route Verification and Checks

1. **Sample**: `python3 -I tools/verify_sample.py AmazeFileManager 30 20261025`
2. **Print routes**: Set up route_print.py from template, print all 30 routes
3. **Verify each route**: Read every step against source, check guards, mark correct/fixed/wrong/unclear
4. **Fix wrong routes**: Update graph_def.py, rebuild, re-print, re-verify
5. **Re-sample after last fix**: Final sample must match final graph
6. **Run all 8 checks** (section 6 of rules)
7. **Generate verification.csv** with make_verification.py
8. **Write readme_notes.md** and LESSONS.md
9. **Flip PROGRESS** to DONE

## Detailed UNREACHABLE Labeling Guide

### For Glide Generated Code (179 methods)
**Read**: Check which GlideApp/GlideRequest/GlideOptions methods are actually called from app code
**Reasoning**: Glide generates many convenience methods. Only those called from reachable fragments/activities are REACHABLE.
**Kind**: `no_trigger_in_app` (if never called) or `framework_never_calls` (if it's a library method)
**Source ref**: SRC GlideApp.java:N (if source exists) or "INFERRED Glide generated code not called from reachable app code"

Example:
```python
'GlideOptions.placeholder(int)': ('no_trigger_in_app', 
    'Glide generated convenience method; no app code calls it from a reachable path',
    'SRC GlideOptions.java:123', 'SOURCE'),
```

### For 7z Library (252 methods in sevenz/)
**Read**: Check if app opens .7z files (MainActivity intent-filter for VIEW, check if it handles .7z specifically)
**Reasoning**: If .7z is supported, the main entry points are reachable but many internal helpers may not be. If .7z NOT supported in standard config, all are unreachable.
**Kind**: `no_trigger_in_app` (if .7z not supported) or `framework_never_calls` (internal library helpers)
**Source ref**: Check MainActivity.java for archive handling logic

### For Cloud Storage (~100 methods)
**Read**: Check if cloud accounts are configured in standard setup (check DATASET.txt, _fixtures/, code for default accounts)
**Reasoning**: Cloud features require account linking (Dropbox OAuth, etc.). Standard config = fresh install, no accounts.
**Kind**: `closed_by_configuration` if feature needs account linking
**Source ref**: SRC CloudSheetFragment.java or CloudHandler.java showing account requirement

### For Root Operations (RootHelper, RootUtils, ~30 methods)
**Read**: Check if root is enabled by default
**Reasoning**: Root requires (1) device rooted (2) user enables root mode in settings. Standard config has neither.
**Kind**: `closed_by_configuration`
**Source ref**: SRC showing root permission check or settings check

### For Adapters (RecyclerAdapter, AppsAdapter, etc.)
**Read**: Check if the fragment/activity that uses the adapter is reachable
**Reasoning**: Adapter is only reached if its fragment/activity is shown
**Kind**: `no_trigger_in_app` if the fragment is never shown
**Source ref**: SRC Fragment.java showing adapter is never instantiated from reachable path

## Key Source Files to Read for UNREACHABLE Decisions

1. **MainActivity.java** (1963 lines):
   - onCreate: what features are initialized?
   - checkForExternalIntent: how does it handle different intent types?
   - What fragments does it show by default?

2. **MainFragment.java**:
   - The main file browser - likely always reachable
   - What adapters does it use?

3. **CloudSheetFragment.java / CloudHandler.java**:
   - How are cloud accounts configured?
   - Are any configured by default?

4. **Archive handling**:
   - Which archive types are actually supported?
   - Are there conditionals for .7z vs .zip vs .rar?

5. **Glide usage**:
   - Which fragments actually use GlideApp?
   - AppsListFragment, RecyclerPreloadModelProvider - are these reachable?

6. **Root features**:
   - Where is root checked?
   - What code paths require root?

## Next Concrete Steps

1. **Add MainFragment** (highest priority - likely reaches many adapters):
   ```python
   # In section G
   e('MainActivity.onCreate', 'MainFragment.<init>', 'FRAMEWORK', 'fragment created by MainActivity',
     evidence='SRC MainActivity.java:XXX; ' + FW_FRAG)
   e('MainFragment.<init>', 'MainFragment.onCreate', 'LIFECYCLE', 'Fragment.onCreate',
     evidence=FW_FRAG)
   e('MainFragment.onCreate', 'MainFragment.onCreateView', 'LIFECYCLE', 'Fragment.onCreateView',
     evidence=FW_FRAG)
   # Add adapter instantiation from onCreateView
   ```

2. **Read MainActivity carefully** for fragment transactions:
   - Find where it instantiates fragments
   - Add edges for fragment creation

3. **Begin UNREACHABLE labeling** for clear cases:
   - Start with Glide: check each method, label if not called
   - Then 7z: check if .7z support exists
   - Then cloud: check if accounts configured
   - Then root: check if enabled

4. **Build iteratively**:
   - After adding MainFragment: rebuild, check REACHABLE count
   - After labeling Glide: rebuild, check error count
   - Target: 0 errors

5. **Once 0 errors achieved**:
   - Proceed to Phase 2 (sampling and verification)

## Blockers / Decisions Needed

None currently - rules are clear, just need time to execute.

## Time Estimate

- Phase 1 remaining: 6-10 hours (adding fragments + UNREACHABLE labeling)
- Phase 2: 4-6 hours (sampling 30 routes, verifying, fixing, checks)
- **Total remaining**: 10-16 hours

## Files Modified So Far

- graphs/AmazeFileManager/graph_def.py
- graphs/AmazeFileManager/AGENT_NOTES.md
- graphs/AmazeFileManager/scratch/build_001.txt
- graphs/AmazeFileManager/scratch/build_002.txt
- graphs/AmazeFileManager/scratch/CHECKPOINT_PLAN.md (this file)

## Files to Create

- graphs/AmazeFileManager/scratch/fix_log.md (when fixing routes)
- graphs/AmazeFileManager/scratch/route_print.py (from template)
- graphs/AmazeFileManager/scratch/route_print/* (printed routes)
- graphs/AmazeFileManager/scratch/sample_30.txt (sampled methods)
- graphs/AmazeFileManager/make_verification.py (verification.csv generator)
- graphs/AmazeFileManager/verification.csv
- graphs/AmazeFileManager/readme_notes.md (5 sections)
- graphs/AmazeFileManager/LESSONS.md
- graphs/AmazeFileManager/scratch/kiro_final_message.txt

Then run: `python3 -I tools/gen_readme_v2.py AmazeFileManager` to generate out/README.md
