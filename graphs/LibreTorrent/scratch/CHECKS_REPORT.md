# LibreTorrent logs-step CHECKS report — fresh eight-check suite (LOCAL ONLY)

Scope: measurement only, on a fresh build in `logs/checks/tree/` copied from
the B6 tree. NOTHING pushed, no branch file edited, no `tools/` file edited,
no DECISIONS entry written, no tick markers written, no label changed, no B6
fix direction applied. The writer helper's `logs/tree/` was not built in or
touched; this helper built only in its own `logs/checks/tree/` copy.

Inputs: B6 tree `work/LibreTorrent/b6/tree/` (read-only source);
expected values from the D7 gate evidence (`work/LibreTorrent/d7/D7_REPORT.md`,
independent audit PASS); B6 final sample
`b6/tree/graphs/LibreTorrent/scratch/sample_30.txt`, B6 final table
`b6/route_table.md` (27 routes), B6 caveat list `b6/caveats/unresolved_86.txt`,
and the 59/32 edge `Ea751b47d`.

## 0. Headline — NO deviation from D7 expected values

Every measured value matches the D7 expected values exactly. In addition,
the fresh build outputs are byte-identical to the B6 copy, and eight fresh
check outputs are byte-identical to the D7 scratch outputs:

- Fresh `out/` md5s = B6 copy md5s: `build_report.txt e7bf0a37…`,
  `libretorrent_trigger_graph.json de7d1c87…`, `methods.csv ad3a8fc3…`,
  `sanity_check.csv f5d4eeb6…` (full hashes in `build_pre_hashes.txt`).
- Byte-identical to D7 scratch: `check2.txt`, `check2_full.txt`,
  `check3_routes.txt`, `check4_default.txt`, `check4_all.txt`,
  `check8_default.txt`, `check8_all.txt`, `check8_callers.txt`.
- Raw outputs are in this directory, one file per check, never
  summarised-only. Commands + exit codes: `commands_and_exits.txt`.
  Exit-code reading (important, not crashes):
  - Build exit 1 and check-2 exit 1 and check-4 exit 1 are each the tool's
    own "return 1 if problems/errors else 0" behaviour with complete
    outputs, NOT crashes.
  - Checks 5/6/7 grep exit 1 is grep's "no matches" exit, i.e. the
    0-count result, not a failure.

## 1. Check 1 — build (counts, errors, warnings, STRICT)

- Copy: B6 tree copied to `logs/checks/tree/` (`graphs/` real copy,
  `tools/` / `final_java_only/` / `fw_src/` as the same symlinks the B6
  tree uses, pointing through the merger tree to the clone tree).
  `__pycache__` excluded. Zero 0-byte files under the copied `graphs/`.
  Copied `graph_def.py` is 572,861 B, byte-identical to the B6 source,
  `git hash-object 564da867e63a1ccdd7835f2007cb8b26b0a5e16e` — the
  expected branch-base blob.
- Command (from `logs/checks/tree/`):
  `python3 -I tools/build_graph.py graphs/LibreTorrent libretorrent`
  → exit 1. **Build exit 1 with errors 86 is the tool's normal errors
  behaviour (outputs complete), NOT a crash** (`return 1 if errors else 0`;
  stderr empty apart from the recorded exit line; all four `out/` files
  written, non-empty, md5-identical to the B6 copy).
- Full log: `build.log` (123,559 B); `build_report.txt` is the fresh
  `out/build_report.txt` (123,546 B, md5 `e7bf0a37…`, identical to D7's
  audited build report).
- Measured: methods **4732**, pages 1, edges **7293**;
  verdicts **REACHABLE 3882 / UNREACHABLE 764 / UNRESOLVED 86**;
  unreachable by kind: branch_never_taken 12, closed_by_api_level 24,
  closed_by_configuration 1, framework_never_calls 13,
  no_trigger_in_app 714 (sums to 764);
  edge kinds: CALL 5970, ENTRY 22, FRAMEWORK 748, INTENT 51,
  LIFECYCLE 176, REGISTER 294, RESULT 32 (sums to 7293);
  labels confirmed by: **INFERRED 4112, SOURCE 620** (sums to 4732);
  **errors 86, warnings 16, STRICT True** (exactly one
  `STRICT = True` line, `graph_def.py:8`).
- The 86 build ERROR lines are exactly the 86 fresh `methods.csv`
  UNRESOLVED methods (verified by set comparison, not by count alone).
  See §9: errors 86 = the 86 UNRESOLVED methods, a technical blocker
  for F1, not closed here.

## 2. Check 2 — citations (`tools/check_citations.py LibreTorrent`, exit 1)

- Raw: `check2.txt` (tool output, 41 lines: header + first 40 problems);
  `check2_full.txt` (full 131-problem list, 131 lines) plus the
  re-enumeration script `check2_full.py` (adapted from D7's script: same
  ROOT/TAG styles, same `resolve()` against the same caches, same
  "file not held" rule; only its output path changed to this directory)
  and its stdout `check2_full_stdout.txt`.
- Measured: **191 distinct, 131 problems; library citations (not
  checked) 0; evidence with FW-MEMORY / DYN / UNVERIFIED 0.**
  The tool's printed first 40 problems were verified to be exactly the
  first 40 lines of the full list.
- Full-list composition (fresh recount, sums to 131; all 131 are
  "file not held", zero line-range problems):
  `core/settings/SettingsRepositoryImpl.java` 51,
  `core/FeedParser.java` 33, `core/model/TorrentEngine.java` 21,
  `core/model/session/TorrentSessionImpl.java` 11,
  `core/utils/Utils.java` 4, `core/model/stream/TorrentStreamServer.java` 4,
  `core/system/FileSystemFacadeImpl.java` 3,
  `core/system/SystemFacadeHelper.java` 2,
  `core/model/TorrentInfoProvider.java` 1, `core/RepositoryHelper.java` 1.
- Explanation (D7/D5 evidence, not a fresh re-derivation of the
  mechanism): the 131 = checker-scope mechanism. `check_citations.py`
  checks FRAMEWORK citations only — its caches are `fw_src` dirs, never
  the app tree — but it matches every `core/...` citation in any
  evidence text with ROOT_STYLE. The 131 are APP citations in
  `core/...` short form (e.g. edge `E07451abf` evidence
  `SRC core/model/TorrentEngine.java:117-125`); the files DO exist in
  `final_java_only` (D7 confirmed `SettingsRepositoryImpl.java` present).
  This is ruling-owed R8 (see §9): explained checker-scope artifact vs
  citation-form rewrite vs checker exemption — NOT silently explained
  away to zero. The 131 are reported here as measured, unchanged.

## 3. Check 3 — routes (`tools/check_routes.py LibreTorrent`, exit 0)

- Raw: `check3_routes.txt` — the tool's full output, which is exactly:
  `# LibreTorrent: 0 routes flagged`.
- What this does and does not mean (stated plainly, because the logs
  step now HAS a final table): `check_routes.py` does NOT read
  `route_table.md` or any judged B6 table. It walks the graph's best
  routes (`methods.csv route_edge_ids`) for every REACHABLE method and
  applies a guard/ENV-contradiction heuristic (RESULT_CANCELED→RESULT_OK,
  histMap null→non-null, network off→on). So "0 routes flagged" is a
  statement about the graph's best routes under that heuristic, NOT a
  judgment on the 27 B6 judged routes (which stand at CORRECT 19 /
  WRONG 8 in `b6/route_table.md`, unchanged by this check).
- Corroboration that the tool actually walked routes rather than
  skipping: an extra `--all` run (`check3_routes_all.txt`, exit 0,
  3,883 lines = 3,882 REACHABLE method lines + the same
  `# LibreTorrent: 0 routes flagged` summary). This extra file is beyond
  the D7 set; the default-mode result is identical to D7's.
- Note for the logs step: LibreTorrent had no checked path rows at D7
  gate time; the B6 table now exists, but it is not an input to this
  tool, so no "checked path rows" effect on this check is expected or
  claimed. Nothing flagged; no deviation from D7 (0 flagged).

## 4. Check 4 — bytecode lines (`tools/check_bytecode_lines.py`, both modes)

- Raw: `check4_default.txt` (exit 1, 60 bad lines printed — a print cap,
  not a different result) and `check4_all.txt` (exit 1, all 141 bad
  lines). Both byte-identical to D7's outputs.
- Shared header, both modes (identical):
  `LibreTorrent: 1673 bytecode-cited edges checked, 583 skipped
  (lambda / clinit / anonymous), 56 implicit (super / enum / Dagger),
  141 where the cited line does not show the callee`.
- Partition, freshly counted on `check4_all.txt`, sums exactly:
  **file-not-found 134 + name-not-within-2 7 = 141 bad**; zero
  "name on line" rows among the bad lines (those are fixes, not bad).
- The 7 name-not-within-2 rows (all `FileDescriptorWrapperImpl.close`,
  fresh, matching D7's audited post-fix list exactly):
  `FeedRepositoryImpl.java:155`, `FileSystemFacadeImpl.java:236`,
  `TorrentEngine.java:380`, `TorrentSessionImpl.java:296`,
  `TorrentSessionImpl.java:360`, `IPFilterParser.java:72`,
  `SaveLogWorker.java:89`.
- Explanation (D7/D5 evidence): the 141 = D5 Class A 134 + Class B 7.
  Class A = generated-code file-not-found (fresh token check: 108 of
  the 134 file-not-found lines mention `Binding`/`Binder`, matching
  D7's data-binding 108; the remaining 26 are the D5 Class A Room set
  per D7 — this helper did not independently re-classify those 26).
  Class B = the 7 `FileDescriptorWrapperImpl.close` edges above.
  D7 records the `E02ee8cda` correction as already applied via D5;
  this helper did not re-derive that correction identifier (it is not
  an edge id in the fresh graph JSON, nor does it appear in fresh
  check-4 output) — the fresh Class B evidence is the 7 rows above,
  whose cited lines match D7's audited post-fix state.
- Counting nuance (D7, confirmed by the tool's semantics): `checked`
  increments ONLY after a source file is found, so a `file not found`
  line lands in `bad` WITHOUT incrementing `checked` — bad is NOT a
  subset of checked, and the 134 file-not-found lines sit outside the
  1673 checked figure.
- Ruling-owed (see §9): check-4's 141 is exactly R2 (Class A route) +
  R3 (Class B handling). Reported as measured, never forced to 0.

## 5. Check 5 — DEAD / FRAMEWORK_ONLY grep (exit: grep 1 = no matches)

- Command: `grep -rn -E 'DEAD|FRAMEWORK_ONLY'
  graphs/LibreTorrent/graph_def.py graphs/LibreTorrent/parts/*.py`
- Raw: `check5_grep.txt` — **0 lines, 0 bytes**. No file has a count > 0.
- Measured: **0**. Matches D7.

## 6. Check 6 — FW-MEMORY grep (exit: grep 1 = no matches)

- Command: `grep -rn -E 'FW-MEMORY'
  graphs/LibreTorrent/graph_def.py graphs/LibreTorrent/parts/*.py`
- Raw: `check6_grep.txt` — **0 lines, 0 bytes**.
- Measured: **0**. Matches D7. (Consistent with check-2's
  "evidence with FW-MEMORY / DYN / UNVERIFIED: 0".)

## 7. Check 7 — PENDING grep (exit: grep 1 = no matches)

- Command: `grep -rn -E 'PENDING'
  graphs/LibreTorrent/graph_def.py graphs/LibreTorrent/parts/*.py`
- Raw: `check7_grep.txt` — **0 lines, 0 bytes**.
- Measured: **0**. Matches D7.

## 8. Check 8a — unreachable mentions (`tools/scan_unreachable.py`)

- Raw: `check8_default.txt` (exit 0) and `check8_all.txt` (exit 0),
  both byte-identical to D7's outputs.
- Default mode (the substantive figure):
  **606 methods with other mentions shown; 158 with no other mention**
  (606 + 158 = 764).
- `--all` mode: **764 methods with other mentions shown; 0 with no
  other mention**. The `--all` 0 is **0 by construction, NOT the
  substantive figure**: the tool appends to the quiet ("no other
  mention") list only when `--all` is NOT passed, so `--all` forces
  every method into the shown set. Do NOT present `--all` 0 as the
  result; the result is the default split 606/158.

## 9. Check 8b — unreachable methods with bytecode callers (`--callers`)

- Raw: `check8_callers.txt` (exit 0), byte-identical to D7's file,
  which D7 verified byte-identical to the D5D6 post-D3 output.
- Measured: **33 data rows + summary line:
  "33 of 764 unreachable methods have a bytecode caller outside the set".**
  Row set verified against D7's `check8_callers.txt` by byte comparison
  (identical file, so the row set matches exactly, not just the count).
- Explanation (D7/D5 evidence): the 33 = the existing explained set
  (rows listed in `check8_callers.txt`; no new unexplained row appears
  on this fresh build). It is reported as measured, not reduced to 0.

## 10. Warnings 16 — composition (from the fresh build log)

Fresh `build.log` WARN lines = 16, composition matching D7:
8 Parcel constructors (`AdvancedTorrentInfo`, `MagnetInfo`, `PeerInfo`,
`SessionStats`, `FeedItem`, `Torrent`, `BencodeFileItem`,
`TorrentMetaInfo`) + `FileItem.toString` (`Ea94d2a26`) +
`PercentEncoder.pow` (`Ea6713c2e`) + `PermissionManager.lambda$new$0`
(`Eacdbd1c4`) + `notifySound` (`E673d2ce0`, `notifySound(String)`) +
3 Appearance legacy-notify (`E9d220da3`, `E9f932f66`, `E17cd04e4`) +
1 REVIEW line (95 edges) = 15 method WARNs + 1 REVIEW = 16.

## 11. Caveat screens — recomputed on the FRESH build (mechanical)

Script: `caveat_screen.py` (read-only; run from `logs/checks/tree/`);
output: `caveat_screen.txt`. Method, in full:

1. Sampled methods = the 27 names parsed from the B6 sampler file
   (`tree/graphs/LibreTorrent/scratch/sample_30.txt`, last token per
   data line), cross-checked against `b6/route_table.md` table rows:
   the two lists agree exactly, same order, 27 rows.
2. Drawn steps = sum of `len(route_edge_ids)` over those 27 rows in
   the FRESH `methods.csv`; distinct edges = union of those
   `route_edge_ids`. Per-route fresh step counts match the sampler
   header AND the route-table steps for all 27 routes; all 27 sampled
   methods are present in the fresh `methods.csv`, all REACHABLE.
3. 59/32 edge = count of `Ea751b47d` in those 27 drawn routes.
4. Unresolved touches = every drawn edge id resolved in the FRESH
   graph JSON; its `src` and `dst` intersected with BOTH
   (a) `b6/caveats/unresolved_86.txt` and (b) the fresh `methods.csv`
   UNRESOLVED set. The two unresolved sets are identical (86 entries,
   set-equal), so both intersections are the same test run twice.

Results (all as expected):

| Screen | Expected | Fresh recomputation |
|---|---|---|
| Total drawn steps | 407 | **407** |
| Distinct edges on the 27 routes | 294 | **294** |
| 59/32 edge `Ea751b47d` in sampled routes | 0 | **0** (also absent from the 294-edge union) |
| Drawn-step src/dst touches of `unresolved_86.txt` | 0 | **0** (and 0 against the fresh UNRESOLVED set) |

Additional fresh facts: no drawn edge id is missing from the fresh
graph JSON. The 59/32 edge DOES exist in the fresh graph
(`FragmentAddTorrentInfoBindingImpl.executeBindings` →
`AddTorrentInfoBindingImpl.setVariable`, kind CALL, INFERRED generated
included-layout variable propagation) — it is simply drawn in zero
sampled routes, so it is never claimed as a verified route here either.
Scope limit, stated plainly: this screen covers DRAWN steps only
(`route_edge_ids`). It does NOT erase B6's route-2 (havePiece)
caveat-2 premise-history disclosure: the shutdown-first premise chain
(`SchedulerReceiver.*`, `TorrentService.*`,
`Utils.lambda$startServiceBackground$0`, all in `unresolved_86.txt`)
is setup history verified from source, not a drawn step, and B6's
ruling (i) — the caveat attaches only to drawn steps — is what makes
0 touches consistent with that disclosure. That disclosure still stands
as written in `b6/route_table.md`; this screen neither re-judges it
nor removes it.

## 12. What is NOT closed here (stated plainly)

- **Errors 86 = the 86 UNRESOLVED methods: a technical blocker for F1,
  not closed here.** The build errors are exactly one per UNRESOLVED
  method ("method has no path and no UNREACHABLE entry"), all INFERRED.
  On a literal CI SUMMARY errors-0 bar, they block F1 until labeled (or
  until a ruling disposes of them — none granted by this helper). This
  helper reclassifies nothing; T1 execution remains the path that
  addresses them, and it is blocked on user decisions D1/D2/D3, which
  are outside this task.
- **Checks 2 and 4 non-zero are ruling-owed, not silently explained
  away:** check-2's 131 is R8 (checker-scope disposition); check-4's
  141 is R2 (Class A route) + R3 (Class B handling). The explanations
  in §2 and §4 describe the mechanism and the D5/D7 evidence; they do
  not grant the rulings. No value in this report was forced to 0.
- Checks 3, 5, 6, 7 are 0 as measured (with the §3 scope note for
  check 3); check-8's 33 and warnings 16 are measured and dispositioned
  through the existing explanation sets, not new findings.

## 13. Deviation log vs D7 expected values

**No deviation.** Every D7 expected value reproduced exactly:
4732 / 7293 / R3882 / U764 / UNRES86, errors 86, warnings 16,
STRICT True, SOURCE 620, check 2: 191 distinct / 131 problems,
check 3: 0 flagged, check 4: 1673 / 583 / 56 / 141 (134 + 7),
checks 5/6/7: 0 / 0 / 0, check 8a default 606 / 158 (764 total),
`--all` 764 / 0 by construction, check 8b: 33 of 764.
Caveat screens: 407 / 294 / 0 / 0, all as expected.
The only additions beyond the D7 set are the extra `--all` check-3 run
(§3, corroboration only) and the fresh-file verification counts in §4
and §11; neither changes any measured value.

## 14. Files in this directory

- `tree/` — private fresh build (B6 copy + fresh `out/`; NOT
  `logs/tree/`, which the writer helper owns).
- `build.log`, `build.err`, `build_report.txt`, `build_pre_hashes.txt`
  — Check 1.
- `check2.txt`, `check2_full.txt`, `check2_full.py`,
  `check2_full_stdout.txt`, `check2_full.err`, `check2.err` — Check 2.
- `check3_routes.txt`, `check3_routes_all.txt`, `check3_routes.err`,
  `check3_routes_all.err` — Check 3.
- `check4_default.txt`, `check4_all.txt`, `check4_default.err`,
  `check4_all.err` — Check 4.
- `check5_grep.txt`, `check6_grep.txt`, `check7_grep.txt` (+ `.err`,
  all empty) — Checks 5/6/7.
- `check8_default.txt`, `check8_all.txt`, `check8_callers.txt`
  (+ `.err`, all empty) — Checks 8a/8b.
- `commands_and_exits.txt` — every check command with its exit code (helper-script invocations check2_full.py / caveat_screen.py are recorded via their own stdout/err files listed above).
- `caveat_screen.py`, `caveat_screen.txt`, `caveat_screen.err` — §11.
- `CHECKS_REPORT.md` — this report.
- Nothing in this directory was pushed, and no branch file, tools
  file, DECISIONS entry, or tick marker was written by this helper.
