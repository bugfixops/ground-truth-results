# AmazeFileManager 3.4.2: method-level trigger graph (schema 2)

How every method of **AmazeFileManager** is triggered, in the standard configuration: the instrumented debug build (`tingsu/AmazeFileManager@instrumented-version-3.2.1`, commit `5d25735ae846`, APK sha256 `9269b957...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `amazefilemanager_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, the derived best route (`shortest_path`, `route_edge_ids`), and the full JVM class and descriptor (`jvm_class`, `jvm_descriptor`; the `method` key adds a package prefix only where simple class names clash) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `amazefilemanager_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **2981 methods**, **12 pages** (including pseudo pages), **7318 edges**. Verdicts: **2447 REACHABLE**, **534 UNREACHABLE**.
- UNREACHABLE by reason: branch_never_taken 3, closed_by_api_level 39, framework_never_calls 54, no_trigger_in_app 438.
- ENV gates (methods): hardware 38, network 201, other 26, other_app 314, system_event 9. STATE gates (methods): data 46, file 531, session 154, settings 31. Methods with no gate: 1384.
- Edge classes: explicit 6257, non_standard 36, page 11, standard 1014. Non-standard edges: 36 (EventBus @Subscribe delivery of FtpReceiverActions; EventBus post of FtpReceiverActions to @Subscribe methods; Glide generated code; XML inflation: LayoutInflater or the preference inflater builds this class from its XML tag through the (Context, AttributeSet) constructor (layout or preference XML c).
- 78 reachable methods have a non-standard edge on their best route; 134 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 1316, SOURCE 1665 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

Verification log (`verification.csv`), counts of what was checked and found:

| Checked | Rows | Correct | Errors found (fixed) | Unclear |
|---|---:|---:|---:|---:|
| labels | 622 | 590 | 31 | 1 |
| edges (framework and other claims read against source) | 16 | 6 | 10 | 0 |
| paths (stratified sample, read step by step) | 30 | 4 | 26 | 0 |

Device replay on the emulator (API 27): 0 of 30 routes reached their target method; 0 of these ran the whole script and are `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; see `../device/results.csv`.

Path status over all reachable methods: SOURCE_OK 29, UNCHECKED 2417, WRONG 1.
The rows are the items that were individually checked, not a random sample of all labels; see the notes below for how they were chosen and what the unclear rows wait for.

Edges whose evidence is not a source line (403 of 7318): E9c493cd5 (MainActivity.onResume -> MainActivity.onCreateOptionsMenu); E7a0b9a37 (MainActivity.onCreateOptionsMenu -> MainActivity.onOptionsItemSelected); E745b85ef (MainActivity$1.<init> -> MainActivity$1.doInBackground); Ed18978e9 (MainActivity$1.doInBackground -> MainActivity$1.onPostExecute); Ef643161a (TabFragment.onCreateView -> MainFragment.<init>); E3f533b40 (MainFragment.<init> -> MainFragment.onCreate); Ebd761bbf (MainFragment.onCreate -> MainFragment.onCreateView); E9adbdc5d (MainFragment.onCreateView -> MainFragment.onActivityCreated); E199e866f (RecyclerAdapter.<init> -> RecyclerAdapter.onCreateViewHolder); Ee1989850 (RecyclerAdapter.onCreateViewHolder -> RecyclerAdapter.onBindViewHolder); E6c3cfc3a (RecyclerAdapter.setItems(RecyclerView,ArrayList,boolean) -> RecyclerPreloadModelProvider.getPreloadRequestBuilder); Eacc36ed3 (Drawer.<init> -> Drawer.onNavigationItemSelected) ...

Sanity check against tool coverage (never used to set a label): 1132 methods ran in the 1-hour Monkey / APE runs on API 27; **19** of them are labelled UNREACHABLE.

## What the re-audit changed (compared with the schema 1 graph)

Re-audit of November 2026 (rounds of W2 to W7, see handoff/MUSE_REAUDIT_SUMMARY.md):

- No first-run screen (W2); the text editor and the FTP receiver get in-app starts (W3; exported-entry routes 57 to 5).
- HybridFile templates (W4): the anonymous template classes are renumbered from javap; HybridFile$9 exists only in the uncalled no-arg getInputStream(), so its execute is UNREACHABLE (AmazeFileManager-20).
- Library class (W5): 12 classes built from XML tags are created through non_standard edges.
- Outside data (W6): SSH, SFTP, stream servers, pickers and database upgrades are env (AmazeFileManager-12).
- Guards (W7, round 1): .db and .apk files, USB OTG locations need state or a device (AmazeFileManager-01, -27, -46).

The schema 1 graph was a generated draft; the schema 2 graph was rebuilt from
the AmazeFileManager sources (AmazeFileManager-#1837) with hand-written
edges, each cited to printed lines or marked INFERRED where the source is
generated code or was not read. Counts moved from 2509 REACHABLE / 472
UNREACHABLE (after the B2+B3 check fixes) to 2512 / 469 at the end of B6.

- B1: STRICT was already True; no change.
- B2: citation paths reduced to the basename form the checker resolves
  (the `asynchronous/services/` and `adapters/data/` components were
  stripped from app citations); check 2 went 23 -> 0.
- B3: the EDIT hook was implemented (it had been a no-op): 59 FIX_LINES
  corrections, 3 INFERRED generated-class rewrites (GlideRequests,
  GeneratedAppGlideModuleImpl, GeneratedRequestManagerFactory), and the
  CLI.main -> SevenZFile.close edge rewritten to the INFERRED
  try-with-resources implicit close (CLI.java:127 opens, :132 closes the
  try block). Check 4 went 63 -> 0.
- B4: check 8 went 4 -> 3 with one label flip. AES256SHA256Decoder$1.`<init>`
  flipped to REACHABLE (decode() is REACHABLE via Coders.addDecoder at
  Coders.java:57 registration and :79 dispatch, and unconditionally
  instantiates the anonymous class at AES256SHA256Decoder.java:36). The
  remaining 3 check-8 pairs are explained in scratch/check8_explained.md.
- B6: 30 sampled routes were read step by step (error rate 25/30 = 0.833;
  5 correct, 25 fixed, 0 wrong, 0 unclear in the final draw). Fixes
  included the systematic manifest ENTRY citation shift for all 8 services
  plus the receiver, deletion of 7 bogus ZipService$CompressAsyncTask.execute
  cross-task edges (to PrepareCopyTask, DecryptService, EncryptService and
  MainFragment$6) with valid AsyncTask edges added where the deletions
  required them, deletion of the bogus SMB StreamServer -> CloudStreamSource
  edge with the faithful CloudStreamServer sendResponse -> read edge added,
  rewiring of the INFERRED CompressedExplorerFragment -> Decompressor edge
  to the real onActionItemClicked call site (:329), deletion of 4 false
  BasicActivity superclass edges (TextEditorActivity and
  DatabaseViewerActivity extend ThemedActivity, not BasicActivity), and
  two label flips from printed app source: GlideRequest.listener and
  IconDataParcelable.setImageBroken, both UNREACHABLE -> REACHABLE.

## How the checked paths were chosen

A fixed 30-method sample was drawn from the reachable methods with the
repository tool and a fixed seed (`python3 -I tools/verify_sample.py
AmazeFileManager 30 20261025`), so the draw is reproducible and not
cherry-picked. For each sampled method the best route was read step by
step against the printed source (edge trigger, guard, and ENV / STATE gate
on each hop), judged correct / fixed / wrong / unclear, and every wrong
route was repaired and re-verified. Because the draw is route-sensitive,
each fix batch redrew the sample; the final table covers only the final
draw (30 of 2512 reachable methods, 226 distinct edges), which was stable
across the last redraw, and all 30 final prints were confirmed to reach
their targets. The sample, the prints, the table and the fix record are in
scratch/sample_30.txt, scratch/route_print/, scratch/route_table.md and
scratch/fix_log.md. Routes dropped by redraws were judged and fixed in
their own draws; their fixes are in fix_log.md but they are not in the
final table.

Note on sample timing: the sample was drawn before the log step. The label rows written by the log step change which 30 methods the sampler picks on the final graph, so a fresh draw on the final graph would not necessarily pick the same 30 methods. The judged routes are still current: the final verification run reports 0 STALE warnings, so every judged route still matches the final graph.

## What waits for a device (API 27)

- **Re-audit, last real run 42560435293-1 (2026-11-09, API 27).** The sampled routes were re-verified first (Step 3), and the dry run had 0 FAIL. 0 of 30 routes reached their target (3 scripts ran to the end, 23 stopped, 4 are unscriptable); every route is unclear, never wrong. What is listed below still waits for a device.

- **Device run 41593209101-1 (2026-11-03, Google APIs, API 27, x86).** 0 of 30 routes reached their target method; 0 of them ran the whole script and are now `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; the reason for each route is in `handoff/DEVICE_RUN_SUMMARY.md`. What is listed below still waits for a device.

Device checks are deferred: they run in GitHub CI when the user starts
`.github/workflows/device-replay.yml` by hand; no emulator run has been
started in this run. Device preparation (D1 route list, D3 scripts, D7
DEVICE rows) covers the 30 final-sample routes. The device run should
confirm, in particular: the two Glide virtual dispatches flipped in B6
(GlideRequest.listener via the GlideRequest receiver at
RecyclerAdapter.java:899,:945, and IconDataParcelable.setImageBroken via
the OnImageProcessed method references at RecyclerAdapter.java:596,599,609,
724,733); the ENV-gated routes (another app opening a text file for the
TextEditorActivity routes, manifest :129-144; another app opening a zip/rar
for CompressedExplorerFragment.onDestroyView); and the paste-case routes
(PasteHelper family, which need a pending copy/cut). Nothing in the label
set depends on a device result: no label was set from tool coverage, and a
not-reached device result must never flip a label (per the brief, it
becomes `unclear`, never `wrong`).

## Hazard candidates (from reading the code, not reproduced)

These are open questions from the audit, not reproduced behaviour and not
label changes:

- The wider BasicActivity superclass cluster (e.g. BasicActivity ->
  MainActivity.onCreate, BasicActivity -> PreferencesActivity.onCreate)
  uses the same pattern as the 4 false edges deleted in B6, but MainActivity
  extends PermissionsActivity (MainActivity.java:157) and PreferencesActivity
  extends ThemedActivity (PreferencesActivity.java:58). That cluster needs
  its own audit; it was not changed here because none of its edges is on a
  sampled route.
- GlideRequests.as and the five GlideOptions methods (GlideOptions.`<init>`,
  .apply, .autoClone, .clone, .lock) are UNREACHABLE with no app-source
  call sites on a full-tree grep, but they appear in tool-coverage
  contradiction lists. The generated GlideRequests.java source is not in
  the upload, so the asDrawable() -> as() delegation step could not be
  printed; it was deliberately NOT added as an INFERRED edge.
- SftpConnectDialog lambda numbering ($2 vs $6 for the removeConnection
  callback that creates GetSshHostFingerprintTask at
  SftpConnectDialog.java:178 and executes it at :199) stays OPEN pending
  bytecode/class-file lambda order; the current $2 links are consistent
  with the printed source but the assignment was not independently proven.
- CompressedExplorerFragment.onDestroyView's route requires a zip/rar VIEW
  intent from another app; the edge carries no env field, so a device
  script for it must set up that intent explicitly.

## Limits

- No device run has been performed; all reachability here is from printed
  source and framework lifecycle reasoning, not from execution.
- Generated code (Glide, Dagger/Hilt) is not in the app source upload, so
  edges through it are INFERRED (library/generated code) with the
  mechanism stated, never SOURCE.
- Lambda numbering follows the graph's bytecode-derived mapping and was not
  re-derived; where a lambda body was printed it matched its edge.
- Tool coverage (Monkey, APE, JaCoCo, sanity_check.csv) was never used to
  set or flip a label; the 19 UNREACHABLE-but-ran contradictions in the
  build report were each left to source evidence (one, GlideRequest.listener,
  flipped on printed source; the rest held).
- The 30-route sample covers 30 of 2512 reachable methods; route checks
  judge each sampled method's best route, not every route to it.
- Check 8 still lists 3 of 469 unreachable methods with a bytecode caller
  outside the set; all three are explained in scratch/check8_explained.md
  (B4) and are not label errors.

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
