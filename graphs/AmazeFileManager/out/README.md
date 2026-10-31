# Amaze File Manager 3.4.2: page-jump and method-call graph (generated)

A map of how every method of the open-source Android app **AmazeFileManager** (tingsu/AmazeFileManager@instrumented-version-3.2.1, source commit `5d25735a`, package `com.amaze.filemanager.debug`, APK sha256 `9269b957…bfe9e86b`) can be triggered: from which page, by which user gesture or system event, through which framework callback or call. It is the build in `final_java_only/AmazeFileManager`.

**How this one differs from Currency, hash-checker, openlauncher and Omni-Notes:** those graphs were written by hand from reading the source. This one was **generated** by `tools/gen_edges.py` from the bytecode, `AndroidManifest.xml` and `res/` XML, and then checked against the baseline coverage and reviewed (see "How much to trust it"). Every number below is recomputed from the files in this folder.

## What is in this folder

| File | What it is |
|---|---|
| `amaze_trigger_graph.json` | The graph: pages, methods, verdicts, edges. Every edge has an `evidence` label; an edge may carry `env` (needs something outside the app) and `needs_state` (needs an earlier action or setting). |
| `methods.csv` | One row per method: verdict, steps from launch, the user taps on the best path, the path, number of incoming edges, note. Extra columns: `jvm_descriptor`, `monkey_hit`, `ape_hit` (1-hour API 27 baseline runs; empty = JaCoCo does not report the method), and for methods the baseline never ran `frontier_from`, `frontier_first_unrun`, `frontier_edge_kind`, `frontier_edge_evidence`, `steps_after_frontier` (where the chain from code that ran first enters code that never ran). |
| `amaze_trigger_graph.html` | The same data in the viewer from the Currency example. Optional. |
| `build_report.txt` | Output of the validation script (0 errors, 0 warnings, baseline cross-check, the list of reachable methods the baseline never ran). |

## Numbers

- **2981 methods** (the app's own code, aligned with what JaCoCo reports), **37 pages** (4 of them `S_NEW_<Class>` anchors: a class whose empty default constructor is not in the JaCoCo method universe is constructed through such a node), **7745 edges**: 3813 from the bytecode call extractor, 3932 added by the generator or by hand.
- Edge kinds: ASYNC 198, CALL 5185, ENTERS 23, ENTRY 8, FRAMEWORK 991, GUI 26, INTENT 49, LIFECYCLE 1217, RESULT 7, SYSTEM 41.
- Verdicts: **2062 reachable**, **700 reachable after setup**, **219 dead**, 0 framework-only.
- 561 edges are gated by an outside environment, 848 need an earlier action or setting; 338 methods are reached only through an environment gate, 700 only after setup. Average route length: 9.5 edges.
- Evidence labels: 2539 `FW-MEMORY`, 124 `INFERRED`, 5082 `SRC`.
- Largest dead groups (auto-classified, see limits): `SevenZOutputFile` (34 of 34), `GlideApp` (12 of 13), `FileUtil$MediaFile` (9 of 9), `SevenZArchiveEntry` (9 of 46), `ScrimInsetsRelativeLayout` (9 of 9), `SevenZFile` (8 of 42), `SevenZOutputFile$OutputStreamWrapper` (6 of 6), `Coders$DeflateDecoder$DeflateDecoderOutputStream` (5 of 5), `LZMA2Decoder` (5 of 9), `FileUtil` (4 of 25), `CLI` (4 of 4), `LZMADecoder` (4 of 8), `SevenZOutputFile$1` (4 of 4), `RootHelper` (3 of 18).

## Comparison with the baseline coverage (APE and Monkey, 1 hour each, API 27)

- 1132 of the 2978 observable methods ran in at least one run (Monkey 760, APE 1123, both 751). **0 dead or framework-only methods ran**, so the coverage contradicts no verdict.
- **1846 methods were run by neither tool.** By the graph: 216 are dead; 338 are reachable only through an outside environment; 484 need an earlier in-app action or setting; **808 are reachable with no modelled setup and no outside help, yet were never run** (the clearest target list for the paper). Classes holding most of them: `GlideOptions` (68), `GlideRequest` (50), `FtpServerFragment` (35), `MainActivity` (21), `ColorPref` (19), `ExtractService` (17), `GeneralDialogCreation` (17), `GlideRequests` (16), `PreferencesActivity` (15), `SearchAsyncTask` (15), `ColorPickerDialog` (15), `PrefFrag` (14), `MainActivityHelper` (14), `HybridFile` (13).
- **Where the baseline stopped (frontier).** For 1624 of the never-run reachable methods the graph gives the edge where the chain from methods that ran first enters code that never ran (`frontier_*` columns of `methods.csv`: `frontier_from` is the source of that edge, a method that ran or a screen entered from one; `frontier_first_unrun` is its target): 988 CALL, 558 FRAMEWORK, 48 LIFECYCLE, 24 ASYNC, 4 SYSTEM, 2 GUI. A `CALL` frontier is a branch inside code that ran and was not taken (a data, setting or error condition); a `FRAMEWORK`, `GUI`, `INTENT` or `SYSTEM` frontier is a callback, tap or start that no tool triggered. The ten frontier nodes that unlock the most never-run methods:
  - `CompressedExplorerFragment.changePath` (219 never-run methods behind it): reached from `BottomBar.lambda$showButtons$1` by a `CALL` edge (SRC BottomBar.java:218 (bytecode))
  - `Drawer.lambda$refreshDrawer$3` (146 never-run methods behind it): reached from `Drawer.refreshDrawer` by a `FRAMEWORK` edge (SRC Drawer.java:435 (bytecode))
  - `MainActivityHelper.extractFile` (85 never-run methods behind it): reached from `ItemPopupMenu.onMenuItemClick` by a `CALL` edge (INFERRED SRC ItemPopupMenu.java:109 (bytecode))
  - `FtpServerFragment.<init>` (69 never-run methods behind it): reached from `MainActivity$1.onPostExecute` by a `CALL` edge (SRC MainActivity.java:403 (bytecode))
  - `SshClientUtils.execute(SshClientSessionTemplate)` (59 never-run methods behind it): reached from `GenerateHashesTask.doInBackground` by a `CALL` edge (SRC GenerateHashesTask.java:69 (bytecode))
  - `Drawer.lambda$refreshDrawer$2` (48 never-run methods behind it): reached from `Drawer.refreshDrawer` by a `FRAMEWORK` edge (SRC Drawer.java:418 (bytecode))
  - `CloudUtil.launchCloud` (43 never-run methods behind it): reached from `MainFragment.onListItemClicked` by a `CALL` edge (SRC MainFragment.java:930 (bytecode))
  - `MainFragment.launchSMB` (40 never-run methods behind it): reached from `MainFragment.onListItemClicked` by a `CALL` edge (SRC MainFragment.java:915 (bytecode))
  - `EncryptDecryptUtils.decryptFile` (37 never-run methods behind it): reached from `ItemPopupMenu.onMenuItemClick` by a `CALL` edge (INFERRED SRC ItemPopupMenu.java:197 (bytecode))
  - `MainActivity.openCompressed` (30 never-run methods behind it): reached from `MainActivity.goToMain` by a `CALL` edge (SRC MainActivity.java:798 (bytecode))
- Harness facts that matter for target selection: `merged.ec` omits the launch dump `00000.ec`, so first-launch code can show `monkey_hit = 0` although it ran; one dump per tool may be unreadable, and a process that dies between 30-second dumps loses its coverage, so "never hit" does not strictly prove "never ran".

## How much to trust it

- **Method.** `gen_edges.py` applies Android framework rules to the compiled classes: process entry (Application, launcher, exported components behind an `env` gate), lifecycle callbacks and one page `S_<Activity|Fragment>` per screen, UI and system callbacks of every constructed class with a framework ancestor, lambdas and method references (creator method -> body, the tap label is read from the source line), `startActivity(new Intent(ctx, X.class))` and custom intent actions, classes named in layout / xml / menu / navigation files and where they are inflated, activity and permission results, `Handler` messages, ButterKnife / EventBus / data binding / Dagger / Glide / Icepick / Parceler / ORMLite / Room glue, static initialisers, and template-method receiver variants (`Base.m@Sub`). Direct calls come from the bytecode (`extract_calls.py`, class-hierarchy analysis for virtual calls). Methods that nothing reaches are reported DEAD (`AUTO_DEAD`).
- **Calibration on the five hand-written apps** (the generator run on the same inputs, compared with the hand-written verdicts; `tools/calibrate.py`): dead-versus-alive agreement 97.2% (Currency), 96.5% (Diary), 98.5% (hash-checker), 92.9% (openlauncher), 93.8% (Omni-Notes); exact verdict agreement 93.8% (Currency), 95.5% (Diary), 71.1% (hash-checker), 76.9% (openlauncher), 63.1% (Omni-Notes). The gap is almost entirely `needs_state`: a human reads "needs a note / a folder / a setting" out of the code, the generator only knows list rows. (openlauncher and Omni-Notes were used while the generator rules were developed; Currency, Diary and hash-checker were not.)
- **Checks done on this app:** the validation script (0 errors, 0 warnings: every method has a route or a DEAD verdict, every page is reachable); the baseline cross-check above (0 contradictions after the generator rules were completed by reading the contradictions one by one); random shortest paths were read for shortcuts.
- **Not checked on a device.** Framework rules are `FW-MEMORY` (recalled, not checked against AOSP source); guesses are `INFERRED`.

## Limits (read before using a verdict)

- **`REACHABLE` means "no modelled setup", not "no setup".** Gates beyond list rows (data that must exist, settings, earlier actions, incoming intents, files on the device) are modelled only where listed in the review notes. Adapter row callbacks, row-based listeners and action modes carry `needs_state` = "the list shows at least one row".
- A callback is reachable as soon as an instance of its class is constructed; the real trigger (a tap on one specific control) is shown in the `gui_steps` column only where the source line names the control. Menu and click handlers that switch on `R.id.x` give one labelled edge per case (`case R.id.x`), found by the nearest preceding case label (`INFERRED`).
- `Handler.handleMessage`, EventBus subscribers and Dagger-provided objects are linked from every send / post / graph-build site (`INFERRED`), so their routes can be shorter than the real ones.
- DEAD is automatic: nothing in the bytecode, manifest, XML or the modelled libraries reaches the method. Entries through reflection, JNI, other generated code or libraries that are not modelled would be missed (the baseline contradiction check found and fixed every such case that the 1-hour runs exercised).
- Calls inside catch blocks, data-dependent branches and feature flags are ordinary calls unless the review notes say otherwise.

## Review notes for this app

What was reviewed by hand (class level, from method names, the manifest, the layouts and the fixtures on the baseline device):

- **Environment gates (edges into these classes, when the baseline never ran the target, carry `env`):** cloud storage (`Cloud*`: a linked Dropbox / Drive / OneDrive / Box account and network); the FTP server service (`FtpService`, `FtpReceiver`, `FtpNotification`: a Wi-Fi / LAN connection, the baseline emulators had none) and its quick-settings tile (`FtpTileService`); SFTP / SSH (`Sftp*`, `SFtp*`, `Ssh*`, `GetSshHost*`: a reachable server); root access (`RootUtils`, `RootHelper`, `MediaStoreHack`: the baseline emulators were not rooted); package broadcasts (`PackageReceiver`); fingerprint (`FingerprintHandler`). SMB browsing (`SmbConnectDialog`, `SmbSearchDialog`) is not gated: the baseline reached it.
- **Content gates (`needs_state`):** 7z / gzip / bzip2 / tar / LZMA archives and the in-archive browser (`SevenZ*`, `Bzip2*`, `Gzip*`, `Lzma*`, `CompressedExplorerFragment`: the baseline Download fixtures hold only `archive.zip`); encryption (`CryptUtil`, `CryptHandler`, `EncryptService`, `DecryptService`, `EncryptedEntry`, `ArchivePasswordCache`: an `.aze` file, or a saved SMB / SFTP connection with a stored password; the app also decrypts saved SMB paths at startup, which is why `CryptUtil` shows routes without taps); the process viewer (`ProcessViewerFragment`: a background copy / extract / compress operation must be running).
- **Branch gates read from the source at the frontier (`CFG['EDGES']`):** `MainActivity$1.onPostExecute` -> `FtpServerFragment` (only for the quick-settings tile preference intent: `env`; the drawer entry is the in-app route), `MainFragment.onListItemClicked` -> `launchSMB` (an SMB list row: `env`), `MainActivity.goToMain` -> `openCompressed` (the launch intent carried an archive path: `env`).
- **Dead code** is mostly the bundled `commons-compress` 7z writer and tools (`SevenZOutputFile` all 34 methods, its stream wrappers, `CLI`, parts of `SevenZFile` and `SevenZArchiveEntry`, `LZMADecoder` / `LZMA2Decoder` encoder methods), `GlideApp` (generated accessor), `FileUtil$MediaFile` (a legacy MediaStore helper), `ScrimInsetsRelativeLayout` (a view no layout uses) and a few helpers (`RootHelper.generateBaseFile`, `FileUtil.copyDummyFile`).
- **Two source sets.** The class files include the `commons_compress_7z` module next to the app (see `class_files.json`); methods of both are in the universe.
- **Glide** (`GlideApp`, `GeneratedAppGlideModuleImpl`, `GlideOptions`, `GlideRequest(s)`, `AmazeFileManagerModule`, `CloudIconModelFactory`, `ApkImageModelLoader*`) is the Glide annotation-processor glue, loaded by name when Glide initialises; `CloudIconModelFactory` carries the cloud `env` gate.
- **Not gated but never run (the target list):** the settings screens (`PreferencesActivity`, `PrefFrag`, `ColorPref`, `ColorPickerDialog`, `FoldersPref`), `GeneralDialogCreation` lambdas (permissions, paths, cloud, archive dialogs), `MainActivity` connection helpers (`addConnection`, `deleteConnection`), `SearchAsyncTask` (regex / glob search) and `MainActivityHelper` dialogs.

## JSON shape (short)

```
{ "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|REACHABLE_AFTER_SETUP|DEAD|FRAMEWORK_ONLY},
  "dead": {method: reason}, "framework_only": {method: reason},
  "edges": [ {id, src, dst, kind, trigger, gui[], guard, reads[], writes[], note, needs_state, evidence, env} ] }
```
`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`, classes that share a simple name get a package prefix) or pages (`S_...`). A suffix `@CONTEXT` is the same method in a specific receiver class (`Base.m@Sub`) or context.
