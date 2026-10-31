# Handover: finish the ground-truth trigger graphs for 13 Android apps

Written 2026-10-31 from the state on disk at about 16:45 EDT. Re-check every number yourself before you rely on it: run the build command and print the output. Do not copy counts from this file.

## 0. Read this first

- **Project.** A paper for ICST 2027 about targeted Android testing tools. For each of 13 apps, every method in `graphs/<App>/method_list.json` gets one label. The graph is the ground truth that the tools are judged against, so it has to be right and independent of the tools.
- **Label types.**
  - REACHABLE: a route exists from an entry point, built from edges you wrote from printed source.
  - UNREACHABLE: exactly one kind (see section 2), a reason, and a source reference.
- **Never use as evidence:** tool coverage (Monkey, APE, `coverage_baseline.json`, `sanity_check.csv`, JaCoCo reports), the old generated graphs, or the build's REACHABLE count. A method with a route must never be UNREACHABLE.
- **Work from the files in this folder.** Read the rules files in full before you start: `handoff/KIRO_CONVERT_APPS.md`, `handoff/KIRO_CORRECTIONS.md`, `handoff/SCHEMA_V2.md`, `handoff/AGENT_BRIEF_V2.md`, `handoff/CONVERSION_RECIPE.md`.

## 1. Where things stand

| App | Status | Build (labels) | Route checks (path rows in verification.csv) | Next |
|---|---|---|---|---|
| Currency | Ticked by user | 145 labelled, 0 errors, 0 warnings | 28 | none |
| Diary | Ticked | 286 labelled, 0/0 | 30 | none |
| hash-checker | Ticked | 529 labelled, 0/0 | 37 | none |
| Omni-Notes | Ticked | 1456 labelled, 0/0 | 33 | none |
| openlauncher | Ticked | 900 labelled, 0/0 | 27 | none |
| Vanilla-Music | Ticked | 1473 labelled, 0/0 | 30 | none |
| Markor | Ticked | 2864 labelled, 0/0 | 30 | none |
| AnyMemo | Ticked | 2207 labelled, 0/0 | 30 | none (see decision D2) |
| Aegis | Not ticked; blocked on decisions for Yang | 2995 labelled, 0/0 (build 2026-10-28) | in progress (route steps 6 to 10 open) | WP3 |
| AmazeFileManager | Labelled overnight 2026-10-30; not route-checked | 2981 labelled (2509 REACHABLE, 472 UNREACHABLE), 0/0 (build 28) | 0 | WP2 |
| AnkiDroid | Labelled overnight 2026-10-30; not route-checked | 4186 labelled (3275 / 911), 0/0 (build 204) | 0 | WP2 |
| MMEX | Labelled overnight 2026-10-31; not route-checked | 4270 labelled (3430 / 840), 0/0 (build p147) | 0 | WP2 |
| LibreTorrent | In the Claude queue from 2026-10-31 16:37; the run may still be on it | Not labelled: 4732 rows; only about 161 supported by hand; build 2026-10-30 10:35: 0 errors, 230 warnings, 2721 placeholder "unclassified" rows | 0 | WP1, then WP4 |
| Device replay | Not started | 0 DEVICE rows anywhere | n/a | WP6, only after the user says go |

Totals: 8 of 13 apps ticked. Labelling is complete for 12 apps; LibreTorrent is not. Route checks are the big gap.

## 2. Rules (copy these into your working notes)

**Labels** (from `handoff/KIRO_CONVERT_APPS.md` section 3):
- Exactly one label per method in `graphs/<App>/method_list.json`.
- UNREACHABLE kinds, and nothing else: `no_trigger_in_app`, `branch_never_taken`, `framework_never_calls`, `closed_by_configuration`, `closed_by_api_level`. Each needs a reason and a source reference.
- `confirmed_by` is `SOURCE` (you printed the lines) or `INFERRED` (library or generated code, or code you did not read). Never write `DYN`, `FW-MEMORY` or `UNVERIFIED`.
- Generated classes (Glide, Dagger/Hilt, Room `*_Impl`, data binding, protobuf): an UNREACHABLE label needs the printed output of a real grep over the source folder, saved in `scratch/`. "method_list.json:1" is not a citation.
- Framework claims cite only printed lines from `fw_src/android-8.1.0_r1/` (write `FW-SRC path:lines`). If the framework file is not there, the claim is INFERRED and says "source not read".

**Edges and gates** (from `handoff/SCHEMA_V2.md` and `graphs/<App>/graph_def.py`):
- Edge classes: `explicit` (app code calls app code); `standard` (the framework calls a callback the app registered: lifecycle, listeners, menu callbacks, AsyncTask, activity results, launcher entry); `non_standard` with a `via` (a library or reflection links it; nothing in app code calls or registers the target).
- A route must exist that uses only `explicit` and `standard` edges where possible. Record which kinds each route uses.
- Gates are ENV kinds (`network`, `tls_chain`, `permission`, `hardware`, `other_app`, `system_event`, `time`, `other`) or STATE kinds (`data`, `settings`, `account`, `file`, `session`). Copy gate text exactly from the code. An ordinary program condition is not a gate.
- ENV gates change which route is chosen. They do not change the verdict.

**Standard configuration:** the debug build (package names from each app's `DATASET.txt`, e.g. `com.amaze.filemanager.debug`), a fresh install, API 27, runtime permissions granted only where a route needs them. For AmazeFileManager, AboutActivity is labelled from `src/fdroid` (decided 2026-10-30; see `handoff/HANDOFF_V2.md`, "Convert run decisions").

**Route checks** (from `handoff/KIRO_CONVERT_APPS.md` section 4):
- Sample 30 methods: `python3 -I tools/verify_sample.py <App> 30 20261025 > graphs/<App>/scratch/sample_30.txt`. If the sampler returns fewer, record the number and why.
- Copy `handoff/examples/route_print_template.py` to `graphs/<App>/scratch/route_print.py`, set its constants for the app, and print every step.
- Judge each step against its printed lines, including the if, catch and for conditions around each call. A step you did not print counts as not checked.
- Verdict per route: `correct`, `fixed` (you fixed `graph_def.py`, rebuilt, and printed the route again), `wrong` (not fixed), or `unclear` (depends on another app, the keyboard, a WebView engine, or code you cannot read).
- Error rate = (fixed + wrong) / (correct + fixed + wrong).
- Check every route against the mistakes list in `handoff/AGENT_BRIEF_V2.md` section 5.
- Log each fix in `graphs/<App>/scratch/fix_log.md`. After the last fix, draw the sample again; the final table covers only the final draw.

**Build and checks** (all must pass before an app is done; save each output in `scratch/`; never write "passed" without the output):
1. `python3 -I tools/build_graph.py graphs/<App> <prefix>`: 0 errors, 0 warnings, no STALE line, `STRICT = True`.
2. `python3 -I tools/check_citations.py <App>`: 0 problems; FW-MEMORY / DYN / UNVERIFIED 0.
3. `python3 -I tools/check_routes.py <App>`: 0 flagged (a flagged route is allowed only if `readme_notes.md` explains it with printed lines).
4. `python3 -I tools/check_bytecode_lines.py <App>`: 0 bad.
5. `grep -c "DEAD\|FRAMEWORK_ONLY" graphs/<App>/graph_def.py`: 0.
6. `grep -c "FW-MEMORY" graphs/<App>/graph_def.py`: 0.
7. `grep -c "PENDING" graphs/<App>/graph_def.py`: 0.
8. `python3 -I tools/scan_unreachable.py <App> --all` and `--callers`: every UNREACHABLE method has a kind, reason and source reference.

**Logs** (all must exist):
- `graphs/<App>/verification.csv`, written by `graphs/<App>/make_verification.py` (never by hand). Header exactly: `type,item,result,confirmed_by,ref,edges,note`.
- `graphs/<App>/readme_notes.md` with these five headings, in order: `## What the re-audit changed (compared with the schema 1 graph)`, `## How the checked paths were chosen`, `## What waits for a device (API 27)`, `## Hazard candidates (from reading the code, not reproduced)`, `## Limits`. Then run `python3 -I tools/gen_readme_v2.py <App>`.
- `graphs/<App>/LESSONS.md`: 3 to 8 short bullets on what found real errors.
- `graphs/<App>/AGENT_NOTES.md`: updated after each step, with the time and the build file name.

**Batching:** at most 40 methods per helper batch. Up to 4 helpers at a time per app. Helpers never edit `graph_def.py`, `out/`, the progress file, the notes file, `tools/`, or another helper's files. A part is merged only after the C1 checks pass.

**Stuck rule:** a helper with no output for 30 minutes gets its batch re-launched once. If that also stalls, record the batch under `## Blocked` in `AGENT_NOTES.md` and carry on.

## 3. Work packages (do them in this order)

### WP1: LibreTorrent labelling (120 batches, 4,732 rows)

- **Before you start:** check `handoff/resume_convert.log`. If a Claude run is on LibreTorrent, create `handoff/STOP_CONVERT`, wait for that session to end, then start. Do not run two agents on LibreTorrent at the same time.
- **Starting point:** `graphs/LibreTorrent/AGENT_NOTES.md`, section "Current status", which says the app is not done. Its status: batches 1 and 2 are rechecked (40 each); batch 3 has 38 supported UNREACHABLE labels, 1 REACHABLE and 1 OPEN; batch 4 has 39 supported UNREACHABLE and 1 OPEN; batches 5 to 9 are open; batch 10 has 3 supported. Its batch log also has lines for batches 118 to 120 that say "OPEN". Treat "Current status" as the authority and re-check any batch you rely on.
- **Plan:** `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (4,732 rows, 120 batches). It is the only source of batch membership. Its status column reads `REACHABLE (generator candidate, no hand route yet)` for 4,323 rows, `UNREACHABLE unclassified` for 329, and `UNREACHABLE no_trigger_in_app` for 80. Those are candidates, not evidence.
- **Brief:** `handoff/CHATGPT_PROMPT_LIBRETORRENT_3.md`. Follow its PART 1 fixes, PART 3 rules A to K, and PART 4 steps. Its PART 2 "definition of done" applies to the whole app, not to one session.
- **Known state:** the generator (`gen_edges`) was removed from `graph_def.py`. The gate decisions are T1 to T4 (see `graphs/LibreTorrent/scratch/gates.md`); T1 is STATE `data` ("The list / adapter shows at least one row"). Verify each one from source.
- **Gate for this work package:** every method in `method_list.json` has one label from printed source; no "unclassified" placeholder rows remain; build `errors 0` and `warnings 0` (currently 230 warnings). Route checks are not part of this package.
- **Done line:** change the app's line in `handoff/PROGRESS_V2.md` to `- [L] LibreTorrent (labelled <date>; route checks not started)`. Do not write "[x]"; the user ticks.

### WP2: route checks for AmazeFileManager, AnkiDroid, MMEX

Each app is already labelled with 0 unresolved, 0 errors and 0 warnings. Route checks have not started. For each app:

1. Run the sampler (30 methods, date seed `20261025`) and save `scratch/sample_30.txt`.
2. Print every route step with the template (section 2). Judge each step.
3. Fix wrong routes in `graph_def.py`, rebuild, print the route again, log the fix in `scratch/fix_log.md`.
4. Write the final sample table. Then run `make_verification.py`, the five-heading `readme_notes.md`, `gen_readme_v2.py`, and `LESSONS.md`.
5. Run all eight checks in section 2. Save each output.
6. If every check passes, change the app's line to `- [K] <App> (route checks DONE <date>, awaiting user tick)`.

Known issues before you start:
- AnkiDroid: `Card.toString` is UNREACHABLE (`no_trigger_in_app`), but one tool run hit it, and its caller is unknown. Resolve it before you assign a route to it. The 2026-10-29 open items (`EasySSLSocketFactory.equals` and `hashCode`, the API level 27 vs target 23 question, the `Hooks.runFilter` pair) were not re-checked after the labelling run. See `graphs/AnkiDroid/AGENT_NOTES.md`.
- MMEX: several UNREACHABLE entries are INFERRED (`getPageTitle`, `AccountBillsWidgetService.onGetViewFactory`, `MmxDatabaseUtils.<clinit>`, generated Dagger and ButterKnife methods). Check each one in route checks. Parts 146 and 147 were written by the orchestrator, not by a helper; see the decisions in `handoff/HANDOFF_V2.md`.
- AmazeFileManager: the Glide UNREACHABLE-but-ran contradictions (`GlideOptions.*`, `GlideRequest.*`) are still open; rule C5 applies. The `E89e2cedd` (`SftpConnectDialog.lambda$null$2`) and `Ee1aeff93` (`CompressedExplorerFragment.<init>` to `Decompressor.decompress`) items are open. See `graphs/AmazeFileManager/AGENT_NOTES.md`.

### WP3: Aegis (finish route steps 6 to 10)

- **Starting point:** `graphs/Aegis/AGENT_NOTES.md`, the last RESUME POINT (2026-10-28 02:42). The build on disk is 0 errors, 0 warnings, 2995 methods, 5466 edges.
- **Known state:** an earlier run found 25 ERROR steps across 12 routes. Ten were structural (shared relay, state-blind router, `saveAndFinish` sharing, bind producer). The rest were a missing in-run producer, a wrong receiver or source, or a default-setting contradiction. Route 1, step 21 and route 4, step 9 are open.
- **Do not decide these yourself:** the open items marked "Decision for Yang" in `graphs/Aegis/AGENT_NOTES.md` (7 lines, at about lines 379, 479, 599, 603, 609, 636 and 659 when last checked). Record each one under "## Open decisions for the user" and stop on that route. Do not write a decision in Yang's name.
- Done when all routes pass the checks in section 2, except the routes that are waiting for Yang's decisions. Those stay open, and the app is not done until Yang decides.

### WP4: LibreTorrent route checks

Only after WP1 has reached `[L]`. Then run WP2's steps for LibreTorrent.

### WP5: no work on the ticked apps

The eight ticked apps are closed unless the user reopens them. Do not change their labels or routes. If you find a real error in one, write it in `handoff/MUSE_NOTES.md` and tell the user; do not edit.

### WP6: device replay (not started; do not start without the user's go)

- Plan: `handoff/NEXT_DEVICE_REPLAY.md`.
- Needs an API 27 emulator and a GitHub Actions workflow. Check the environment variables and secrets it needs, and list them in that plan file before any push. Secrets go only in the GitHub repo settings, never in a file.
- Target repo: `bugfixops/test-13` (public or private: check before pushing). Commit only the workflow, route scripts, APK list and fixtures. No graph notes, no personal data, no tokens. Commit as `bugfixops <bugfixops@users.noreply.github.com>`.
- Start only when the user says go. Routes per app and the permission grant rule are for the user and Yang to decide.

## 4. Decisions only the user or Yang can make

Stop and ask; do not decide these yourself.

- **D1, Aegis:** the open items marked "Decision for Yang" (WP3).
- **D2, AnyMemo storage permission:** is `WRITE_EXTERNAL_STORAGE` pre-granted in the standard configuration, or granted only on the routes that need it? `graphs/AnyMemo/graph_def.py` line 157 (`ENV_STORAGE_PERM`) and the startup gate near line 1765 depend on the answer. AnyMemo is ticked, so this only matters if the user reopens it.
- **D3, device replay:** go or no-go; routes per app; the permission grant rule; whether to delete the repo afterwards.
- **D4, API 27 image:** Yang's examples use Currency v1.33; the dataset copy is v1.58. Which API 27 image (Google APIs or plain, arm64 or x86) Yang uses is unknown.
- **D5, LibreTorrent owner:** the user chose the Claude queue on 2026-10-31. If that changes, the user decides.

## 5. Safety and scope

- **Pushing:** the only push done so far is the results folder to the private repo `bugfixops/ground-truth-results` (2026-10-31, on the user's instruction). Push again only if the user asks. Do not push to any other repo.
- **Secrets and personal data:** do not copy tokens or the user's email address into any file, commit or message. If you see a token, do not reuse it.
- **Other apps:** do not edit the folders of the ticked apps or Aegis unless the work package says so. Do not edit `tools/`, `final_java_only/`, the zip files or the memory folder. Do not edit git repositories.
- **Network and devices:** no adb, emulator, gradle or sudo except in WP6 after the user's go. No network except the AOSP 8.1.0_r1 framework files (`raw.githubusercontent.com`), and only if the environment allows it. Do not download anything else. Do not install packages.
- **Locks:** create `handoff/WORKING_LOCK` before work on an app; remove it when you stop.

## 6. What to report

After each batch and each app:
- The exact build command you ran, and the printed counts (methods, REACHABLE, UNREACHABLE, UNRESOLVED, errors, warnings).
- The status line for the app you changed in `handoff/PROGRESS_V2.md`.
- Blockers, and the decisions you need from the user or Yang (section 4).
- The route table counts (correct, fixed, wrong, unclear, error rate) for any route checks.

Never report a count you did not print in the same session.

## 7. Scope and time

The remaining work is large:
- LibreTorrent labelling: 120 batches of at most 40 methods.
- Route checks: 3 apps (about 30 sampled routes each), then LibreTorrent.
- Aegis: route steps 6 to 10, plus Yang's decisions.
- Device replay: not started, and it needs the user's go.

Plan for several sessions. A full labelling run for one app took several hours, with session limits in between. Finishing everything in one night is unlikely. Work in batches, keep the notes current, and stop at a clean point if a limit is reached.
