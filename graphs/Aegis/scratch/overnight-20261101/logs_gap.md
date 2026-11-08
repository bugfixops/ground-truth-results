# Aegis logs gap analysis — DRAFT ONLY, no final logs yet

Scope: Aegis ONLY, repo bugfixops/ground-truth-results, branch work-2026-10-31.
Status of this file: DRAFT gap analysis + DRAFT texts + row plan + blockers.
Nothing in this file is a final log. No final verification.csv, readme_notes.md,
LESSONS.md, or AGENT_NOTES.md was written, no branch file was edited, no push was
made, and no device work (emulator/adb/APK/new repo) was done.
confirmed_by in any future log is only SOURCE or INFERRED — never DYN,
FW-MEMORY, or UNVERIFIED. No count below is invented: every number is either
quoted from a file actually read this session or marked TO-VERIFY.

## 0. How this was checked

- Local input read: ~/workspace/aegis-wp3-steps6-10-report.md (WP3 steps 6–10
  helper report, connector-only, not pushed, not verified for merge).
- Branch reads used the GitHub connector only, one file at a time, with ~30 s
  pauses between fetches. No 429 was hit during this leaf's fetches, and no
  token was used, waited for, or written anywhere.
- Branch files actually read in full this session:
  graphs/Aegis/readme_notes.md (SHA 24dd171e34df2d037731985a500cd2c5cab713f8),
  graphs/Aegis/review_notes.md (SHA 1062d3b8ebe975ab788b3f42c728083276ec72dd),
  graphs/Aegis/AGENT_NOTES.md (SHA ff62d457ca067aa0153295821a2e985eb471a3e4,
  670 lines), tools/gen_readme_v2.py (SHA 15337a8675cde3a08fe8722b238764a577e8303c,
  140 lines).
- Branch directories listed via connector: graphs/Aegis/, graphs/Aegis/out/,
  graphs/Aegis/scratch/proposals/, tools/.

## 1. Verification of the WP3 report's claims (checked, not trusted blindly)

| WP3 claim | This leaf's finding |
|---|---|
| graphs/Aegis/verification.csv absent | CONFIRMED. It is in neither the graphs/Aegis/ listing nor the graphs/Aegis/out/ listing. |
| make_verification.py absent from the repo | CONFIRMED. tools/ lists 52 files; none is make_verification.py (checked by name over the full listing). |
| readme_notes.md first four headings all "Pending", only Limits written | CONFIRMED verbatim from the file fetched this session. Headings in order: "What the re-audit changed (compared with the schema 1 graph)", "How the checked paths were chosen", "What waits for a device (API 27)", "Hazard candidates (from reading the code, not reproduced)" — each followed by "Pending: this section is written when the Aegis graph reaches 0 errors." Only "Limits" has content (batch-36-era text, see §2 draft note). |
| LESSONS.md absent | CONFIRMED. graphs/Aegis/ listing contains no LESSONS.md. |
| Stage-5 final checks not current | CONFIRMED as a status claim. AGENT_NOTES.md "Final checks" section (lines 574–579) is explicitly for the stage-5 build and ends: "This does not mean the Aegis graph is done. The OPEN items and route redraws above remain." It must not be copied forward as a final check. |
| Only 2 of 25 round-7 route dumps in the repo | NOT re-verified by this leaf. This leaf did not list graphs/Aegis/scratch/route_check_r7/. Treat the "2 of 25" figure as TO-VERIFY in phase 2 (source: WP3 report; AGENT_NOTES.md round-7 section says dumps were in "scratchpad r7/", outside the repo copy). No verdict in this file depends on the exact dump count. |
| Current graph_def.py md5 differs from the stage-5 resume-point md5 | NOT re-verified by this leaf (graph_def.py was not fetched). Source: WP3 report (stage-5 md5 ad6d1fe684f0f1611557692115cd9e5b from AGENT_NOTES.md line 6 and line 579; current md5 5a7591221f153facc574eaad368aabc3 per WP3 report). Current build counts are therefore TO-VERIFY — no current build count is claimed here. |

### 1a. Correction to a possible misreading of the WP3 report

The WP3 report says "gen_readme_v2 has not produced a finished v2 readme from
it." That is NOT the same as the script being missing. Verified this session:
tools/gen_readme_v2.py EXISTS at tools/gen_readme_v2.py (140 lines). The gap
is its missing inputs, not a missing script (see §4). A related caution:
graphs/Aegis/out/README.md already exists (15,314 bytes), but whether it is
gen_readme_v2 output from final inputs is TO-VERIFY — do not assume the
existing out/README.md is the finished v2 readme.

### 1b. Directory listings actually returned (branch work-2026-10-31)

- graphs/Aegis/ contains, among others: AGENT_NOTES.md, auto_calls.json,
  coverage_baseline.json, generated_draft_graph_def.py.txt, graph_def.py,
  method_list.json, out/, readme_notes.md, review_notes.md, scratch/.
  No LESSONS.md, no verification.csv at this level.
- graphs/Aegis/out/ contains exactly: README.md (15,314 bytes),
  aegis_trigger_graph.html, aegis_trigger_graph.json, build_report.txt
  (3,032 bytes), methods.csv, sanity_check.csv. No verification.csv.
- graphs/Aegis/scratch/proposals/ contains exactly one file:
  WP3_steps6-10_report_UNVERIFIED.md (13,362 bytes) — i.e. the WP3 report
  itself is now on the branch under proposals/.
- tools/ contains 52 files, including the ones phase 2 needs:
  tools/build_graph.py, tools/verify_sample.py, tools/show_route.py,
  tools/check_citations.py, tools/check_routes.py,
  tools/check_bytecode_lines.py, tools/scan_unreachable.py,
  tools/gen_readme.py, tools/gen_readme_v2.py.
  Absent: tools/make_verification.py (no such file at any tools/ path found).

### 1c. What gen_readme_v2.py actually needs (read from the script, not guessed)

Docstring (tools/gen_readme_v2.py, lines 1–9): "Write graphs/<App>/out/README.md
for a schema 2 graph from its build outputs. Usage: python3 -I
tools/gen_readme_v2.py <App>. Reads out/*_trigger_graph.json, out/methods.csv,
out/sanity_check.csv, verification.csv (through the JSON), the dataset notes
(final_java_only/<App>/app/DATASET.txt) and the optional hand-written
graphs/<App>/readme_notes.md, whose text is appended under its own headings.
All numbers come from the files, none is typed in."

Consequences for Aegis:
- The v2 readme takes readme_notes.md text as-is and appends it. Four
  "Pending" sections would therefore be published verbatim as "Pending" if
  gen_readme_v2.py were run now. Do not run it for a final readme until §2
  is finalised.
- The script reads verification counts NOT from verification.csv directly but
  from the trigger-graph JSON's `verification` object. If that object is
  absent it prints "No verification log yet: every label is UNCHECKED and
  nothing is claimed beyond what the evidence column says."
  Whether the current graphs/Aegis/out/aegis_trigger_graph.json carries a
  `verification` object is TO-VERIFY in phase 2 (the JSON was not fetched
  this session; it is ~4.9 MB).
- The script's own description of verification.csv (in the "What is in this
  folder" table it generates): "the audit log: one row per label, edge or
  path that was checked, with result, how, and where (file:line)".
  That sentence is the anchor for the row plan in §4.

## 2. DRAFT readme_notes.md content (DRAFT — five headings in order)

Everything below is a DRAFT for phase-2 finalisation. Grounded sentences cite
the file read; every count or claim that could not be verified is marked
TO-VERIFY with its source. Do not publish this draft as readme_notes.md:
the final text must use final-build numbers taken from files, per the
gen_readme_v2.py rule that no number is typed in.

### DRAFT — ## What the re-audit changed (compared with the schema 1 graph)

- DRAFT, grounded: the method universe is method_list.json, 2,995 methods,
  produced with list_methods.py --jacoco (the JaCoCo report filter, which
  drops generated code). Source: AGENT_NOTES.md line 98 and line 159.
  The 117 extra methods from a fresh APK list (Dagger/Hilt injectors,
  BuildConfig, enum values, the JaCoCo receiver) are NOT graph nodes;
  they belong under Limits, one reason per group (AGENT_NOTES.md line 98).
- DRAFT, grounded: at the stage-1 / stage-5 builds the verdict split was
  REACHABLE 2,537 / UNREACHABLE 458 (AGENT_NOTES.md lines 8, 9, 13, and the
  stage-5 build line: 2,995 methods, 5,466 edges, 0 errors, 0 warnings).
  These are NOT final numbers.
- TO-VERIFY (source: final build output, phase 2): the final method/edge
  counts, the final REACHABLE/UNREACHABLE split, and every schema-1 vs
  schema-2 difference. No schema-1 graph numbers were read this session, so
  no schema-1 comparison sentence is drafted as fact. The sentence "the
  Aegis graph reaches 0 errors" must not be reused: the stage-5 build
  already showed 0 errors / 0 warnings and round 7 then found 25 ERROR steps
  over 12 routes (AGENT_NOTES.md line 669), so "0 errors" is a build
  condition, not a done condition.

### DRAFT — ## How the checked paths were chosen

- DRAFT, grounded: the last fully documented sample is the round-7 sample:
  graphs/Aegis/scratch/route_check_r7/sample_r7.txt, seed 20261025, 25 routes
  (AGENT_NOTES.md round-7 section; WP3 report). Round 7 checked those 25
  routes step by step against source, found 25 ERROR steps over 12 routes
  and 13 routes with no ERROR (3 clean, 10 UNCLEAR-only), made no graph
  edit, and round 8 was not run — so round 8 would re-check the same graph
  and give the same verdicts (AGENT_NOTES.md line 669).
- DRAFT, grounded (earlier practice, for the method description only): the
  stage-1 sample was redrawn with verify_sample.py after the last graph
  change, and each route was then read step by step — current route first,
  then the source line, then a graph edit or a rejection with the line cited
  (AGENT_NOTES.md line 9).
- TO-VERIFY (source: phase-2 verify_sample.py run + fresh show_route dumps):
  the FINAL sample (size, seed, route list), the sampling rule it used, and
  the final error rate. The final section must describe the final sample,
  not round 7. Round 7 is history, not the final sample.

### DRAFT — ## What waits for a device (API 27)

DRAFT list, grounded only in code-read evidence already on the branch. None
of these items is claimed as reproduced on a device. confirmed_by for any
future log row about them is INFERRED unless a device run later confirms it.

- ENV-gated methods on the best route, not tested on a device (from the
  existing readme_notes.md Limits text, retained as evidence):
  MainActivity.handleIncomingIntent (ENV_VIEW, ENV_SEND);
  MainActivity.lambda$new$7 (ENV_PICK_IMAGE); ScannerActivity init and
  onCreate (ENV_CAMERA); WelcomeSlide lambdas (ENV_PICKER);
  ImportExportPreferencesFragment.lambda$new$0 and
  IconPacksManagerFragment.lambda$new$0 (ENV_PICKER);
  BackupsPreferencesFragment.lambda$new$0 (ENV_BACKUP_RESULT); export RESULT
  lambdas (ENV_EXPORT_RESULT); BiometricSlotInitializer
  .onAuthenticationSucceeded (ENV_BIOMETRIC).
- Baseline coverage gap (graphs/Aegis/review_notes.md, read in full): the
  1-hour runs got past first-run setup and showed the vault list, but the
  vault stayed empty — EntryAdapter.onBindViewHolder never ran — so nothing
  needing an entry (row binding, copy/edit/delete/group actions, action
  mode, TransferEntriesActivity) was exercised. Only 751 of the 2,995
  methods ran. A device run with a populated vault is still needed to cover
  that region; it is device work and therefore out of this logs phase.
- Gates that only a device can discharge (review_notes.md): AuthActivity
  (password-protected, locked vault — the baseline vault opened without an
  unlock screen); Glide request classes (an entry with a custom icon or icon
  pack — baseline entries used the default letter icon); the other-authenticator
  importers (a backup file of that app; none among the baseline fixtures);
  quick-settings tile classes and biometric classes (emulators had no
  enrolled biometrics); the Android backup agent (entered from S_ENTRY
  through an env edge; the system Backup Manager creates it).
- Import-from-app path (review_notes.md + AGENT_NOTES.md round-7 section):
  ImportEntriesActivity.lambda$startImportApp$5 to readFromApp /
  processImporterState needs a root shell and the other authenticator app
  installed (ImportEntriesActivity.java:149 shows a root error and finishes
  otherwise). Device confirmation needs root + that app installed.
- TO-VERIFY (source: phase-2 device plan, NOT this logs phase): the API 27
  image / emulator choice, and whether any of the above was already covered
  by a later device run not recorded in the files read. Do not mark any of
  these as device-checked in a final log without a device-run record.

### DRAFT — ## Hazard candidates (from reading the code, not reproduced)

DRAFT list. Each item is a code-reading candidate only, explicitly NOT
reproduced. Keep this heading's disclaimer in the final text.

- SwitchPreference.setChecked(boolean) ignores its argument and always sets
  the switch on; the stored value is set through the androidx initial-value
  path (INFERRED, androidx source not read). Hazard candidate for the
  security page. Source: existing readme_notes.md Limits text.
- With android:fullBackupOnly="true" (AndroidManifest.xml:24), onBackup,
  onRestore and onQuotaExceeded are UNREACHABLE (INFERRED: the BackupAgent
  source is not in fw_src). A full-backup run on API 27 should show only
  onFullBackup and onRestoreFile running. Source: existing readme_notes.md
  Limits text.
- DropdownCheckBoxes filter: the framework runs the group filter (getFilter,
  performFiltering, publishResults, predicate lambda) even though typing is
  closed by app:allow_filtering="false" (dialog_export.xml:98, input type 0).
  The app source gives no trigger for that framework run and the
  AutoCompleteTextView source is not held. Open device item: open the export
  dialog's groups field and see whether the popup filters rows as the tap or
  the dialog opening triggers it. Source: existing readme_notes.md Limits
  text; see also LESSONS draft bullet 4.
- Pin-switch visibility vs plain vault: SecurityPreferencesFragment.java:
  259–265 sets the pin switch visible only when the vault is encrypted, so
  routes that show the pin switch on a plain-text vault are suspect
  (AGENT_NOTES.md round-7 section: Slot step 21; detailed-multi step 21).
  Candidate, not a device finding.
- Default search mask: SEARCH_IN_ISSUER | SEARCH_IN_NAME
  (Preferences.java:198); GROUPS is set only by
  BehaviorPreferencesFragment.java:57. A same-run GROUPS search applies only
  after a relaunch, so it is a two-process route. Source: WP3 report Yang
  item 4 (AGENT_NOTES.md line 603 area); this is a Yang decision item, so
  the final hazard text must follow the decision, not pre-empt it.
- TO-VERIFY (source: final graph + Yang decisions): whether each candidate
  above is still a live candidate on the final graph, and whether any new
  hazard candidate surfaced in round 7 / round 8. No new hazard candidate
  is asserted here.

### DRAFT — ## Limits (existing text: KEEP, with a dated addendum — do not rewrite blindly)

- The existing Limits text (batch-36-era) is the only finished section and
  must be preserved, not replaced by this draft. It documents, among other
  things: 67 UNREACHABLE consistency flags plus one REVIEW line after the
  batch-36 build; the GlideOptions/GlideRequest clusters; the protobuf
  accessor flags; ApkSignaturePin / TrustedIntents; EntryAdapter.onItemDismiss;
  the NONSTD_HINT false positives; TextDrawable Builder flags; Dialogs flags;
  NotificationService.serviceMethod; and the ENV-gated / hazard items
  carried into the drafts above.
- DRAFT addendum note (to be finalised in phase 2): the Limits text opens
  with "Warnings after the batch-36 build (96 errors, 68 warnings...)".
  Those counts are batch-36-era and are superseded as build history by the
  stage-5 build (2,995 methods, 5,466 edges, 0 errors, 0 warnings,
  AGENT_NOTES.md line 575) and then by the round-6/round-7 edits. The final
  Limits section needs a dated addendum stating which build the flag list
  was checked against, and re-confirming (by grep on the final graph) that
  every flagged method still has no REACHABLE or UNRESOLVED caller.
  TO-VERIFY (source: final graph_def.py + final build output): the
  re-confirmation grep result. Do not carry the "96 errors" figure forward
  as a current figure.

## 3. DRAFT LESSONS.md (DRAFT — 7 bullets, each grounded in a specific event)

DRAFT only. Each bullet cites the source file and line actually read.
Line numbers are AGENT_NOTES.md lines of the branch file fetched this
session, unless another file is named. No bullet decides a Yang item.

- DRAFT lesson 1 — A state-blind router makes "add the producer edge" a
  non-fix. The router compares env, needs_state count and steps and never
  checks that a state is produced (AGENT_NOTES.md line 10, citing
  tools/build_graph.py:147–175, 436–470), so a producer edge alone never
  puts the producer on the chosen route (AGENT_NOTES.md lines 604, 614:
  "The router stays state-blind and unchanged. Its effect is the main cause
  of the remaining ERROR steps"). Fixes need variant nodes that only the
  producer chain reaches, or a state-aware router — the latter needs Yang's
  approval (AGENT_NOTES.md line 604).
- DRAFT lesson 2 — One shared dialog node cannot serve callers with different
  listeners. The shared text-input relay (edges E41c33149 / E02b5fa3e) and
  the shared error-dialog OK relay (Dialogs.lambda$showErrorDialog$15)
  dispatch every caller's OK to one listener; round 6/7 errors on
  GlideRequests steps 24/27, Slot step 26, and ExportResultListener steps
  24–29 all trace to this (AGENT_NOTES.md lines 626, 635; stage-5 log lines
  464, 488: the @FILE/@APP split was needed because "one dialog node is
  shared by both rows and the router is state-blind"). The partial fix that
  did land — typing before OK in the shared text-input dialog
  (AGENT_NOTES.md lines 634, 643: "OK in the shared text-input dialog needs
  typing first", Dialogs.java:201–205 watcher, 226–229 OK disabled until
  text) — fixed the no-typing errors without fixing the relay itself.
- DRAFT lesson 3 — Cross-run state is UNCLEAR, not ERROR, once the rule is
  stated. Round 7 applied rule D2: cross-run vault or icon-pack states are
  UNCLEAR, not ERROR (AGENT_NOTES.md round-7 section). Slot step 8 and
  EntryAdapter step 8 were reclassified ERROR to UNCLEAR under D2, and the
  round-7 totals (25 ERROR steps over 12 routes, AGENT_NOTES.md line 669)
  already reflect that rule. Stating the classification rule before judging
  steps prevents re-litigating the same steps every round.
- DRAFT lesson 4 — A tool run beats a configuration reading. The first plan
  closed the export-groups filter path with closed_by_configuration because
  allow_filtering=false stops typing; the sanity check then showed getFilter,
  its anonymous Filter, performFiltering and publishResults running in a
  tool run, so the plan was corrected and the four were kept as REACHABLE
  framework routes (INFERRED), with the trigger left as an open device item
  (AGENT_NOTES.md line 27). Configuration text alone does not settle what
  the framework runs.
- DRAFT lesson 5 — Splitting a shared node beats moving its edge. The
  stage-5 import-dialog fix split E72c20578 into @FILE (opened by the file
  import row, OK to lambda$onCreatePreferences$5) and @APP (opened by the app
  import row, OK to lambda$onCreatePreferences$7), because moving a single
  edge would have moved an edge correct for its own branch (AGENT_NOTES.md
  lines 464, 473). When one edge is right for one branch and wrong for
  another, the node — not the edge — is the unit to change.
- DRAFT lesson 6 — A 0-error build is not a done graph. The stage-5 final
  checks read: build 0 errors / 0 warnings, check_citations 22 distinct /
  0 problems, check_bytecode_lines 3,654 checked / 0 mismatches, DEAD /
  FRAMEWORK_ONLY grep 0 (AGENT_NOTES.md lines 574–579) — and the same section
  warns "This does not mean the Aegis graph is done." Round 7 then found
  25 ERROR steps on that graph family (AGENT_NOTES.md line 669). Final
  checks must be re-run on the FINAL build and reported with the sample
  error rate, not inherited from an earlier stage.
- DRAFT lesson 7 — Route dumps must live in the repo, or the check cannot be
  repeated. The WP3 report records that only 2 of the 25 round-7 dumps are
  in the repo under graphs/Aegis/scratch/route_check_r7/ and the other 23
  were in "scratchpad r7/", outside the repo copy — so their steps 6–10
  could not be re-checked from the branch (WP3 report; AGENT_NOTES.md
  round-7 section: "Dumps: scratchpad r7/"). Exact repo count TO-VERIFY
  in phase 2 (see §1). Future samples must save every dump under
  graphs/Aegis/scratch/ before the round is called checked.

## 4. verification.csv row plan (DRAFT — for make_verification.py, which does not exist yet)

### 4a. Exact header (as specified for this project)

```
type,item,result,confirmed_by,ref,edges,note
```

- `confirmed_by` takes only SOURCE or INFERRED in any row this project
  publishes. Never DYN, FW-MEMORY, or UNVERIFIED.
- `ref` is the where: a file:line citation (app source, fw_src, or graph
  edge line), matching gen_readme_v2.py's description of verification.csv
  as "one row per label, edge or path that was checked, with result, how,
  and where (file:line)".
- `edges` carries the edge id(s) for edge and path rows, and is empty for
  pure label rows. TO-VERIFY (source: brief step-7 spec, phase 2): whether
  edge ids in this column use the stable hash ids from the trigger-graph
  JSON (gen_readme_v2.py JSON-shape note: "Edge ids are a hash of the edge
  content, so they stay stable when other edges change").

### 4b. What item types / rows make_verification.py must emit

Derived from gen_readme_v2.py's consumption: it aggregates
`verification[type]` for exactly three types — `label`, `edge`, `path` —
each with `checked`, `correct`, `errors_found`, `unclear` counts, and prints
a table with rows "labels", "edges (framework and other claims read against
source)", "paths (stratified sample, read step by step)". The CSV must
therefore emit rows whose `type` values aggregate exactly to those three
buckets. DRAFT row inventory:

- `label` rows: one row per method label INDIVIDUALLY checked (not one row
  per method in the universe by default). `item` = the method
  (Class.method, overloads as Class.method(Type,Type), per the JSON-shape
  note). `result` = correct / error_found / unclear. A label row may only
  claim `correct` if its best route was read step by step against source;
  a label whose route was not read is not a row at all — the script's
  warning is explicit: "The rows are the items that were individually
  checked, not a random sample of all labels."
- `edge` rows: one row per framework claim or other edge claim read against
  source. `item` = the edge id. This covers FW-SRC citations (e.g. the
  ActivityThread create/start lines behind FW_CREATE), INFERRED library
  edges (e.g. the Glide library path in readme_notes.md Limits, where the
  Glide library source is not read), and any edge whose evidence was
  re-read in the final round. `confirmed_by` = SOURCE where every cited
  line was read; INFERRED where any hop rests on inference.
- `path` rows: one row per sampled route read step by step in the FINAL
  sample (not round 7). `item` = the route's target method + sample id
  (e.g. the final sample file name and seed — TO-VERIFY in phase 2).
  `edges` = the route's edge ids in order. `result` = correct only if
  every step was read and no ERROR step remains; error_found if any step
  is ERROR; unclear if any step is UNCLEAR and none is ERROR.
  TO-VERIFY (source: brief step-7 spec, phase 2): the exact granularity —
  one row per route (proposed here) vs one row per route step. Do not emit
  per-step rows until the spec is confirmed, because the gen_readme_v2.py
  aggregation counts rows per type and the granularity changes the
  published "Rows" figures.
- Summary/count rows: NONE in the CSV under this plan. Counts are derived
  by aggregating the three row types, not by adding extra rows, so that the
  CSV row count and the published table agree. If the brief step-7 spec
  requires explicit check rows (build, citations, routes, bytecode), those
  belong in the build/check outputs and in AGENT_NOTES.md, not as extra
  verification.csv types — TO-VERIFY against the spec in phase 2.

### 4c. What make_verification.py must do besides writing the CSV

Because gen_readme_v2.py reads verification counts from the trigger-graph
JSON (`g.get('verification')`), not from the CSV file, make_verification.py
(or the build step that follows it) must also place a `verification`
object into graphs/Aegis/out/aegis_trigger_graph.json with, per type
(label/edge/path), the fields `checked`, `correct`, `errors_found`,
`unclear` — where `checked` = correct + errors_found + unclear as the
script computes it (`v['checked'] + v['unclear']` is printed as "Rows",
so the JSON `checked` field must already exclude unclear rows, or the
table double-counts — TO-VERIFY against the script's arithmetic in phase 2
before writing the injector).
Until that object exists, gen_readme_v2.py prints "No verification log
yet" even if verification.csv exists. The CSV alone does not finish the
v2 readme.

### 4d. Inputs still missing before a FINAL verification.csv can be produced

- The FINAL graph itself: post-decision, post-fix graph_def.py + a final
  build on a full checkout (build_report.txt for the final build). The
  stage-5 build_report is not final (see §1).
- The FINAL sample: a fresh verify_sample.py draw on the final build, with
  every route dump saved under graphs/Aegis/scratch/ (see lesson 7).
- The FINAL step-by-step route checks: fresh show_route.py output for every
  sampled route, read against app source + fw_src, with ERROR/UNCLEAR
  verdicts per step and per route. Round-7 verdicts are history, not final
  rows, because round 7 made no graph edit and round 8 was not run.
- The eight-check outputs on the final build. Checks grounded in files read
  this session: build (errors/warnings), check_citations.py,
  check_routes.py, check_bytecode_lines.py, scan_unreachable.py,
  verify_sample.py + show_route.py step checks, and the DEAD /
  FRAMEWORK_ONLY grep (AGENT_NOTES.md lines 574–579; WP3 report blockers).
  The complete eight-check inventory was NOT read in any Aegis file this
  session — TO-VERIFY against the handoff brief in phase 2, and do not
  publish an eight-item list until it is confirmed. Any check that cannot
  run on the phase-2 checkout must be named as not run, never marked passed.
- Yang's 7 decisions, or an explicit record that a decision item is left
  UNCLEAR with its route excluded from "correct" rows. An UNCLEAR step
  cannot be a `correct` path row.
- The brief step-7 spec confirmation for §4b granularity (row per route vs
  per step) and for the JSON `verification` injection mechanism (§4c).

## 5. Exact blockers to final logs, in dependency order

1. Yang's 7 decisions (handover D1; verbatim items in the WP3 report, from
   AGENT_NOTES.md lines 379, 479, 599, 603, 609, 636, 659). Aegis cannot be
   reported done until they are made; this leaf makes none of them. The
   related Stage-5 OPEN list (cold-start relaunch edges, shared text-input
   relay, Glide INFERRED edges, E4db374dd) rides on the same decisions.
2. A final graph: fixes for the round-7 ERROR steps that are NOT decision
   items (10 of the 25 are structural: shared relay, state-blind router,
   saveAndFinish sharing, bind producer — AGENT_NOTES.md line 669), applied
   to graph_def.py, then a fresh build. No final log may cite a
   pre-fix build.
3. A full local checkout. This leaf was connector-only by instruction and
   cannot run tools/build_graph.py, verify_sample.py, show_route.py,
   check_citations.py, check_routes.py, check_bytecode_lines.py, or
   scan_unreachable.py. Phase 2 must run them from a checkout; connector
   reads alone cannot produce a final sample or final check outputs.
4. A final sample + step-by-step route checks (round 8 or its successor):
   fresh verify_sample.py draw, fresh show_route dumps saved in the repo
   under graphs/Aegis/scratch/, every sampled route read against source,
   final error rate computed. The round-7 sample (seed 20261025, 25 routes)
   is not a substitute.
5. tools/make_verification.py must be written (Aegis scope; it does not
   exist at any tools/ path). It must emit the §4 header, the three row
   types, and the JSON `verification` object (§4c), with confirmed_by
   restricted to SOURCE / INFERRED.
6. graphs/Aegis/verification.csv itself, produced by (5) from (4)'s rows —
   not hand-typed. Hand-typed counts would violate the gen_readme_v2.py
   rule that all numbers come from files.
7. Final readme_notes.md: the four Pending sections (§2 drafts finalised)
   + the Limits dated addendum (§2), using final-build numbers from files.
   Only then may tools/gen_readme_v2.py be run for a final out/README.md.
8. Final LESSONS.md (§3 drafts finalised after the final round, so the
   lessons describe the final round, not only rounds 5–7) and the final
   eight-check outputs recorded in AGENT_NOTES.md (phase 2; the eight-check
   inventory itself is TO-VERIFY per §4d).
9. Device checks (API 27) remain NOT STARTED and are a separate phase after
   the logs: the §2 device list is the handover for that phase, not a
   claim that any device check passed. Aegis stays unticked until the
   device phase and the user tick.

## 6. What phase 2 should verify first (short list)

- Re-list graphs/Aegis/scratch/route_check_r7/ and confirm the "2 of 25"
  dump figure (§1).
- Confirm the brief step-7 spec: verification.csv granularity (§4b) and the
  JSON `verification` injection (§4c), plus the full eight-check inventory
  (§4d).
- Check whether graphs/Aegis/out/aegis_trigger_graph.json already carries a
  `verification` object, and whether the existing out/README.md is
  gen_readme_v2 output or an older readme.
- Re-run the Limits consistency grep on the final graph before finalising
  §2 Limits.

— End of DRAFT gap analysis. No final log file was created by this leaf. —
