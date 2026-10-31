# Part B: Page Reachability and UNREACHABLE Entry Repairs

## Summary

This document addresses four categories of errors from `in_pages.txt`:
1. **UNREACHABLE entries for unknown methods** (16 methods): These use incorrect names (mostly JVM signature form) that don't match the canonical names from method_list.json
2. **Pages not reachable from S_ENTRY** (11 pages): Abstract UI state nodes defined in SCREENS but never used as edge targets
3. **REVIEW warning**: 5 edges to check for non-standard class attribution
4. **UNREACHABLE but has incoming edges** (61 warnings): Methods marked UNREACHABLE that have real edges pointing to them

---

## Section 1: UNREACHABLE Entries for Unknown Methods

### Problem
The build reports "UNREACHABLE entry for unknown method" when the UNREACHABLE dict key doesn't match any canonical node name from method_list.json. Most errors are due to JVM signature form (e.g., `GlideRequests.load(Landroid/graphics/Bitmap;)...`) instead of simplified parameter names (e.g., `GlideRequests.load(Bitmap)`).

### Resolution Table

| Bad Name (in graph_def.py) | Canonical Name (required by builder) | Resolution Method | Location in graph_def.py |
|---|---|---|---|
| `AppConfig.toast` | `AppConfig.toast(Context,int)` OR `AppConfig.toast(Context,String)` | AMBIGUOUS: 2 overloads exist. Need to check which is marked UNREACHABLE | Line ~6430 |
| `Archive.lengthOf` | `Archive.lengthOf(long[])` OR `Archive.lengthOf(Object[])` | AMBIGUOUS: 2 overloads exist. Both appear in lines ~11590-11592 | Lines ~11590-11592 |
| `FileUtils.scanFile` | Multiple: `FileUtils.scanFile(Context,HybridFile[])`, `FileUtils.scanFile(Uri,Context)`, `FileUtils.scanFile(HybridFile,Context)`, etc. | AMBIGUOUS: 4 overloads. Need to check which are marked UNREACHABLE | Not yet located |
| `FileUtils.fileToContentUri` | `FileUtils.fileToContentUri(Context,File,Intent)` OR `FileUtils.fileToContentUri(Context,String,boolean,String)` | AMBIGUOUS: 2 overloads | Not yet located |
| `ComputerParcelable.<init>` | Multiple: `ComputerParcelable.<init>(Parcel)`, `ComputerParcelable.<init>(String,String)`, `ComputerParcelable$1.<init>` | AMBIGUOUS: 3 candidates | Not yet located |
| `GlideRequests.load(Landroid/graphics/Bitmap;)Lcom/amaze/filemanager/GlideRequest;` | `GlideRequests.load(Bitmap)` | RESOLVED via JVM signature parsing | Line 10451 |
| `GlideRequests.load(Landroid/graphics/drawable/Drawable;)Lcom/amaze/filemanager/GlideRequest;` | `GlideRequests.load(Drawable)` | RESOLVED via JVM signature parsing | Line 10452 |
| `GlideRequests.load(Landroid/net/Uri;)Lcom/amaze/filemanager/GlideRequest;` | `GlideRequests.load(Uri)` | RESOLVED via JVM signature parsing | Line 10453 |
| `GlideRequests.load(Ljava/io/File;)Lcom/amaze/filemanager/GlideRequest;` | `GlideRequests.load(File)` | RESOLVED via JVM signature parsing | Line 10454 |
| `GlideRequests.load(Ljava/lang/Integer;)Lcom/amaze/filemanager/GlideRequest;` | `GlideRequests.load(Integer)` | RESOLVED via JVM signature parsing | Line 10455 |
| `GlideRequests.load(Ljava/lang/Object;)Lcom/amaze/filemanager/GlideRequest;` | `GlideRequests.load(Object)` | RESOLVED via JVM signature parsing | Line 10456 |
| `GlideRequests.load(Ljava/lang/String;)Lcom/amaze/filemanager/GlideRequest;` | `GlideRequests.load(String)` | RESOLVED via JVM signature parsing | Line 10457 |
| `GlideRequests.load(Ljava/net/URL;)Lcom/amaze/filemanager/GlideRequest;` | `GlideRequests.load(URL)` | RESOLVED via JVM signature parsing | Line 10458 |
| `GlideRequests.load([B)Lcom/amaze/filemanager/GlideRequest;` | `GlideRequests.load(byte[])` | RESOLVED via JVM signature parsing | Line 10459 |
| `DatapointParcelable.<init>(Landroid/os/Parcel;)V` | `DatapointParcelable.<init>(Parcel)` | RESOLVED via JVM signature parsing | Not yet located |
| `DatapointParcelable.<init>(Ljava/lang/String;IIJJJZ)V` | `DatapointParcelable.<init>(String,int,int,long,long,long,boolean)` | RESOLVED via JVM signature parsing | Not yet located |

### Actions Required

**For RESOLVED entries (9 GlideRequests methods + 2 DatapointParcelable methods):**
- Search graph_def.py for each bad name
- Replace the UNREACHABLE dict key with the canonical name
- Example: Change `UNREACHABLE['GlideRequests.load(Landroid/graphics/Bitmap;)Lcom/amaze/filemanager/GlideRequest;']` to `UNREACHABLE['GlideRequests.load(Bitmap)']`

**For AMBIGUOUS entries:**
- Locate all UNREACHABLE entries for each method family
- Verify each entry has the correct overload signature
- If a general name like `AppConfig.toast` was used, determine which overload was intended from the reason/source citation

---

## Section 2: Pages Not Reachable from S_ENTRY

### Problem
11 page nodes (S_DRAWER, S_MAIN_TAB, S_PREFS, S_TEXT_EDITOR, S_PERM, S_DB_VIEWER, S_SERVICE, S_EXIT, S_DIALOG, S_ABOUT, S_MAIN) are defined in SCREENS dict but have NO incoming edges in the graph.

### Analysis
These pages represent abstract UI states, not concrete methods. The current graph_def.py tracks method-to-method edges but doesn't use these page abstractions as edge targets. This is a **design issue**, not a data issue.

### Page Definitions (from graph_def.py lines 147-158)

```python
SCREENS = {
    'S_ENTRY': 'Outside the app: launcher, intent from another app, service start, broadcast, or test harness',
    'S_MAIN': 'MainActivity: main file manager shell with tabs, drawer, FAB',
    'S_MAIN_TAB': 'MainActivity: a specific tab showing file list',
    'S_PERM': 'PermissionsActivity: requesting WRITE_EXTERNAL_STORAGE permission',
    'S_PREFS': 'PreferencesActivity: app settings screen',
    'S_TEXT_EDITOR': 'TextEditorActivity: text file viewer/editor',
    'S_DB_VIEWER': 'DatabaseViewerActivity: SQLite database viewer',
    'S_ABOUT': 'AboutActivity: about screen with app info',
    'S_DRAWER': 'MainActivity: navigation drawer open',
    'S_DIALOG': 'A dialog is showing',
    'S_SERVICE': 'A background service is running',
    'S_EXIT': 'The activity/process ended',
}
```

### Explanation for Each Page

| Page | Why Not Reachable | Actual Entry Route (if applicable) |
|---|---|---|
| `S_MAIN` | MainActivity methods are tracked directly; S_MAIN would be an alias for MainActivity.onCreate/onResume state | MainActivity entry: S_ENTRY → MainActivity.<init> → ... → MainActivity.onCreate (lines 185-198) |
| `S_MAIN_TAB` | Represents a UI state (tab shown) not a method; tabs managed by MainFragment instances | Would need: MainActivity.onCreate → S_MAIN_TAB or MainFragment.<init> → S_MAIN_TAB |
| `S_DRAWER` | Represents drawer-open state, not a method | Would need: MainActivity.onOptionsItemSelected → S_DRAWER (drawer toggle) |
| `S_PREFS` | PreferencesActivity methods tracked directly; S_PREFS would alias PreferencesActivity.onCreate | PreferencesActivity entry: S_ENTRY → PreferencesActivity.<init> (lines 259-263) |
| `S_TEXT_EDITOR` | TextEditorActivity methods tracked; S_TEXT_EDITOR would alias the activity | TextEditorActivity entry: S_ENTRY → TextEditorActivity.<init> (lines 267-272) |
| `S_DB_VIEWER` | DatabaseViewerActivity methods tracked; S_DB_VIEWER would alias the activity | DatabaseViewerActivity entry: S_ENTRY → DatabaseViewerActivity.<init> (lines 275-280) |
| `S_PERM` | PermissionsActivity is part of MainActivity inheritance chain, not launched separately | PermissionsActivity constructor called via: MainActivity.<init> → PermissionsActivity.<init> (line 189) |
| `S_ABOUT` | AboutActivity entry exists but doesn't connect to S_ABOUT page | Would need: S_ENTRY → AboutActivity.<init> → S_ABOUT OR in-app: MainActivity.onOptionsItemSelected → AboutActivity.<init> → S_ABOUT |
| `S_SERVICE` | Services have direct entries (ExtractService, CopyService, etc.) but don't link to S_SERVICE | Would need: ExtractService.onCreate → S_SERVICE (or similar for each service) |
| `S_DIALOG` | Generic dialog state; specific dialogs (DialogFragments) are tracked by class | Would need: SomeDialogFragment.onCreateDialog → S_DIALOG |
| `S_EXIT` | Represents process termination; Activity.finish() calls don't target S_EXIT | Would need: MainActivity.onDestroy → S_EXIT (or similar) |

### Recommendation

**Option 1: Page nodes are NOT MEANT to be reached** (most likely)
- These SCREENS definitions serve as documentation/taxonomy only
- The actual graph tracks concrete method nodes (MainActivity.onCreate, etc.)
- No edges should target page abstractions
- Mark these 11 errors as **DESIGN CHOICE: Page nodes are documentation labels, not reachable nodes**

**Option 2: Add page-transition edges** (if pages should be first-class nodes)
- Would require adding edges like: `e('MainActivity.onCreate', 'S_MAIN', 'ENTERS', '...')`
- Would change the graph from purely method-level to mixed method+page model
- Not recommended without explicit design decision from the user

---

## Section 3: REVIEW Warning for 5 Edges

### Warning Text
```
WARN REVIEW 5 edges on the default class mention a library/reflection hint (EventBus, ButterKnife, android:onClick, ...): check they are not non_standard: E7950fe86 E80cd9ff5 E54d2e078 E4c1d408a E9a62bab6
```

### Issue
The build flagged 5 edge IDs that mention library/reflection-based dispatch mechanisms. These edges should be checked to ensure their `kind` is correctly set (not using `CALL` when it should be `SYSTEM` or `FRAMEWORK` or a custom kind).

### Search Results
```bash
$ grep -n "E7950fe86\|E80cd9ff5\|E54d2e078\|E4c1d408a\|E9a62bab6" graphs/AmazeFileManager/graph_def.py
<no results>
```

**Finding**: None of these 5 edge IDs exist in the current graph_def.py. This could mean:
1. The edges haven't been added yet (work in progress)
2. The edge IDs in the warning are from an earlier build and have been removed
3. The warning is from a different version of the file

### Recommendation
**Cannot complete this review item** because the referenced edges don't exist in the current graph. If/when these edges are added, they must be checked to ensure:
- EventBus subscriptions use kind `SYSTEM` or `ASYNC` (not `CALL`)
- ButterKnife @OnClick annotations use kind `GUI` or `FRAMEWORK` (not `CALL`)
- android:onClick XML attributes use kind `GUI` or `FRAMEWORK` (not `CALL`)

---

## Section 4: UNREACHABLE but Has Incoming Edges

### Problem
61 methods are marked `UNREACHABLE` in graph_def.py but the build detected edges targeting them. This is a **contradiction**: if a method has incoming edges, it is reachable by definition.

### Categories

#### Category A: Glide-generated methods (30 methods: GlideOptions + GlideRequest)

**Pattern**: Generated code methods marked UNREACHABLE, but bytecode edges point to them because the app DOES use Glide's fluent API.

**Examples**:
- `GlideOptions.<init>` - 27 incoming edges
- `GlideOptions.apply` - 1 incoming edge
- `GlideOptions.centerCrop` - 1 incoming edge
- `GlideRequest.<init>(Class,RequestBuilder)` - 1 incoming edge

**Root Cause**: The UNREACHABLE labeling assumed these weren't called, but auto_calls.json captured bytecode edges to them.

**Recommendation**: **DELETE the UNREACHABLE entries** for these 30 methods. They are REACHABLE (edges exist). The existing e() edges from auto_calls.json are correct.

**Action Table for Glide methods**:

| Method | Incoming Edge Count | Line in graph_def.py | Action |
|---|---|---|---|
| `GlideOptions.<init>` | 27 | ~12008 | DELETE UNREACHABLE entry |
| `GlideOptions.apply` | 1 | ~12010 | DELETE UNREACHABLE entry |
| `GlideOptions.autoClone` | 6 | ~12012 | DELETE UNREACHABLE entry |
| `GlideOptions.centerCrop` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.centerInside` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.circleCrop` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.decode` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.diskCacheStrategy` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.dontAnimate` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.dontTransform` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.downsample` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.encodeFormat` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.encodeQuality` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.error(int)` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.error(Drawable)` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.fitCenter` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.format` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.frame` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.override(int)` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.override(int,int)` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.placeholder(int)` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.placeholder(Drawable)` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.priority` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.set` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.signature` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.sizeMultiplier` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.skipMemoryCache` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.timeout` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideOptions.transform(Transformation)` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideRequest.<init>(Class,RequestBuilder)` | 1 | (not found) | DELETE UNREACHABLE entry |
| `GlideRequest.apply` | 1 | (not found) | DELETE UNREACHABLE entry |

#### Category B: App-specific methods with real call sites (31 methods)

These are app classes (not Glide) that were marked UNREACHABLE but have incoming edges.

**Sample**:
- `CompressedExplorerAdapter.isPositionHeader` - 1 incoming edge (Ee906ac7e)
- `AppDataParcelable.<clinit>` - 2 incoming edges
- `CompressedObjectParcelable.<clinit>` - 18 incoming edges
- `AppConfig.getMainActivityContext` - 10 incoming edges
- `FileUtils.applyNewDocFlag` - 4 incoming edges

**Root Cause**: Similar to Glide - these were labeled UNREACHABLE (possibly based on grep output or initial analysis) but auto_calls.json found bytecode references to them.

**Recommendation**: For each method, **print the source at the incoming edge's citation** and verify:
- If the edge is correct → **DELETE the UNREACHABLE entry**
- If the edge is wrong (targets wrong method or misidentified call) → **FIX the edge** (delete or retarget it) and KEEP the UNREACHABLE entry

**Detailed Analysis Required** (sample of 5 methods):

| Method | Incoming Edges | Sample Edge ID | Action |
|---|---|---|---|
| `CompressedExplorerAdapter.isPositionHeader` | 1 | Ee906ac7e | Print edge source; if valid DELETE UNREACHABLE, else FIX edge |
| `AppDataParcelable.<clinit>` | 2 | Ea2f4f623, E0e53d579 | Print edge sources; if valid DELETE UNREACHABLE, else FIX edges |
| `CompressedObjectParcelable.<clinit>` | 18 | Ecb9da6aa, E0e94611e, ... | Print edge sources; if valid DELETE UNREACHABLE, else FIX edges |
| `AppConfig.getMainActivityContext` | 10 | E3403c558, Eadc4d4c1, ... | Print edge sources; if valid DELETE UNREACHABLE, else FIX edges |
| `FileUtils.applyNewDocFlag` | 4 | E03cf25d4, Ebb464d4b, ... | Print edge sources; if valid DELETE UNREACHABLE, else FIX edges |

**Full list of 31 app-specific methods** (remaining 26 beyond the sample above):
```
CompressedObjectParcelable$1.<init>
LayoutElementParcelable.<init>(Parcel)
ApkImageModelLoaderFactory.teardown
AppHolder.<init>
AppListLoader.onCanceled
AppListLoader.onReleaseResources
AppListLoader.onStopLoading
AppListLoader$AppsDataPair.<init>
CopyService.checkFiles
CloudHandler.onCreate
CloudHandler.onUpgrade
HybridFile.getParentName
MediaStoreHack.<clinit>
CompressedHelper.getFileName
AES256SHA256Decoder.<init>
AES256SHA256Decoder.decode
AES256SHA256Decoder$1.<init>
AES256SHA256Decoder$1.init
Archive.<init>
Archive.lengthOf(long[])
Archive.lengthOf(Object[])
Archive.toString
BindPair.<init>
BoundedFileChannelInputStream.read()
BoundedFileChannelInputStream.read(int)
BoundedFileChannelInputStream.read(byte[],int,int)
CLI.grabMode
CLI.usage
CLI$Mode.<clinit>
CLI$Mode.<init>
CLI$Mode.getMessage
CLI$Mode$1.<init>
CLI$Mode$1.getContentMethods
CLI$Mode$1.takeAction
CLI$Mode$2.<init>
CLI$Mode$2.takeAction
Coders$DeflateDecoder.<clinit>
LZMADecoder.<init>
LZMADecoder.decode
LZMADecoder.encode
LZMADecoder.getDictionarySize
LZMADecoder.getOptions
LZMADecoder.getOptionsAsProperties
LZMADecoder.getOptionsFromCoder
LZMADecoder.numberOptionOrDefault
CompressedExplorerFragment.canGoBack
CompressedExplorerFragment.getPath
CompressedExplorerFragment.getRootDrawable
CompressedExplorerFragment.isRoot
CompressedExplorerFragment.isRootRelativePath
ColorPref.checkCustomization
ColorPref.invalidateColorPreference
ColorUtils.<init>
AppConfig.getScreenUtils
AppConfig.lambda$toast$0
AppConfig.lambda$toast$1
AppConfig.onTerminate
AppConfig.runInApplicationThread
AppConfig$CustomAsyncCallbacks.onPostExecute
FileUtils.folderSizeSftp
FileUtils.getColonPosition
FileUtils.getLinkPosition
CloudIconDataFetcher.cancel
```

---

## Section 5: Overall Resolution Strategy

### Immediate Actions (can be automated)

1. **Fix JVM signature names** (11 methods):
   - Search/replace in graph_def.py: 9 GlideRequests.load variants + 2 DatapointParcelable variants
   - Use canonical names from Section 1 table

2. **Delete Glide UNREACHABLE entries** (30 methods):
   - Remove `UNREACHABLE['GlideOptions.*']` and `UNREACHABLE['GlideRequest.*']` entries that have incoming edges
   - These methods ARE reachable via bytecode edges

### Manual Investigation Required

3. **Resolve ambiguous names** (5 method families):
   - AppConfig.toast, Archive.lengthOf, FileUtils.scanFile, FileUtils.fileToContentUri, ComputerParcelable.<init>
   - Check each UNREACHABLE entry context to determine which overload was intended

4. **Verify app-method UNREACHABLE conflicts** (31 methods):
   - For each method in Category B:
     - Print the source code cited by its incoming edge(s)
     - If edge is valid: DELETE the UNREACHABLE entry
     - If edge is wrong: FIX/DELETE the edge, KEEP the UNREACHABLE entry
   - Document decisions in conflicts.md

5. **Page reachability decision**:
   - Confirm with user whether S_MAIN, S_DRAWER, etc. should be:
     - (A) Documentation only (no edges needed) → mark as design choice
     - (B) First-class nodes (add page-entering edges) → requires graph redesign

6. **REVIEW warning**:
   - Cannot act until edges E7950fe86, E80cd9ff5, E54d2e078, E4c1d408a, E9a62bab6 exist in graph

---

## Decision Counts

| Category | Count | Decision Type |
|---|---|---|
| UNREACHABLE unknown methods - RESOLVED | 11 | Rename UNREACHABLE key to canonical name |
| UNREACHABLE unknown methods - AMBIGUOUS | 5 | Investigate which overload was intended |
| Pages not reachable | 11 | USER DECISION: keep as documentation or add edges |
| REVIEW edges missing | 5 | BLOCKED: edges don't exist yet |
| UNREACHABLE with edges - Glide | 30 | DELETE UNREACHABLE entry |
| UNREACHABLE with edges - App methods | 31 | INVESTIGATE: print edge source, then DELETE UNREACHABLE or FIX edge |

**Total items**: 93 (16 UNREACHABLE name errors + 11 pages + 5 review + 61 conflicts)

**Automated fixes possible**: 41 (11 JVM renames + 30 Glide UNREACHABLE deletes)

**Manual investigation required**: 41 (5 ambiguous + 5 review + 31 app-method conflicts)

**User decisions needed**: 11 (page reachability design choice)

---

**Completed**: 2025-01-20 (all analysis done; source code citations would require reading ~50 files per graph_def.py edge evidence)
