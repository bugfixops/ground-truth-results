# Spot-check leaf summary — LibreTorrent Phase 3b, batches 1–60

Branch work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no branch edits, no token used, no tick marker written. No work file under phase3/work/ was edited; all output is under phase3/spotcheck/ (one file per batch, batch1.md … batch60.md, plus this summary). A sibling leaf's batches 61–120 files already present in the same directory were not touched.

## Scope and method

- Changed-row list derived by this leaf from phase3/verdicts_applied_table.json (entries with new_label different from old_label, plus confirmed_by-only entries with new_label null) and phase3/coordinator_verdicts.json (in-range rows: 3/26, 30/16, 30/17). Union in batches 1–60: **104 rows** (87 label flips + 14 confirmed_by-only + 3 coordinator rows). Coordinator row 3/26 supersedes the L1 table's stays-OPEN entry for the same row.
- 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36) in each batch 1–60: **474 present** (batch 11 has only 9 rows, so 6 sample positions are absent and uncounted). Overlap with changed rows: 13 rows (1/1, 3/26, 4/11, 29/36, 30/6, 30/16, 31/1, 31/6, 33/16, 34/16, 42/31, 47/21, 56/16) — each checked once, under Changed, and counted once.
- Unique rows checked: **565** = 104 changed + 461 sample-only.
- For each changed row: label, kind, and confirmed_by were checked mechanically against the verdict (all 104 match, except that the 4/11 confirmed_by sits in a trailing "INFERRED Kind: …" cell, which a naive exact-match parse misses — it is INFERRED, not missing), and the label was re-derived from the verdict files (phase3/verdicts/L1–L5, R1, R5), the saved greps (phase3/greps/L1–L5, coordinator), and the corpus (phase3/../corpus). Key prints re-verified directly: L1 full-scope greps (grep_all_calls.txt, grep_hash_collections.txt, grep_selectiontracker.txt, grep_log_concat.txt, grep_getstring_formatargs.txt, grep_databinding_text.txt, grep_layout_types.txt); L2 Parcel.java:2894 `getField("CREATOR")`, storage sites (MainFragment:162, DetailTorrentTrackersFragment:183, FeedFragment:142), array greps (0 lines); L3 rebind print (executePendingBindings queries hasPendingBindings(), rendered L686) and zero-hit greps (getters/setVariable/onFieldChange/hasPendingBindings, all 0 lines); L4 D13 greps (grep_D13_newBR.txt 0 lines); L5 greps (grep_4_11_uriconverter.txt, grep_48_07_clearAllTables.txt, grep_48_19_dropAllTables.txt); R5 corpus lines (TorrentInfo.java:125 inside 30/2, :155 inside 30/10; TorrentStateCode.java:71 inside 30/16); D36 coordinator print (Selection backed by LinkedHashSet, Selection_androidx-main.java:67-68, :183-184).
- Verdicts D1–D36 and R1–R5 were NOT re-decided. A FAIL means the application of the verdict is wrong. No decision challenge is raised: no verdict was found wrong on printed evidence.
- FAIL-prose criterion: the work row's evidence prose still affirmatively asserts the pre-flip status — a present-tense "stays/still/kept OPEN" sentence, a "NOT UNREACHABLE" sentence on a row flipped to UNREACHABLE, a present-tense "OPEN under convention … / NOT decided" claim on a decided row, or a dependency parenthetical that is false post-flip where it formed the row's OPEN rationale (34/3). Dated decision history that does NOT assert current OPEN status is not FAIL-prose (e.g. the D4d "REACHABLE -> OPEN" records on 59/5, 59/17, 60/40, and the conditional framing on 48/19 — see the per-batch files for the reasoning). This distinction also governs sample rows: where a sample row's cell ends with an explicit applied decision (Phase 1c D3b/D3c/D4c/D4e/D8, GREPFAMILY FLIP) that supersedes earlier "stays OPEN" history in the same cell, the row is PASS (e.g. 18/1, 31/21, 31/26, 41/11, 51/6, 51/21, 52/11, 60/11, 60/26, 60/36); where a Phase 3 flip appended only a bare "[Phase 3 completion … verdict applied.]" note and left the operative "Stays OPEN" conclusion standing, the row is FAIL-prose. The task's own rule for newly-flipped rows states that stale "stays OPEN" sentences count as FAIL-prose.

## Grand totals

- Checked: **565** (104 changed + 461 sample-only)
- PASS: **494** (34 changed + 460 sample-only)
- FAIL-prose: **70** (all among changed rows; label, kind, and confirmed_by correct in every one)
- FAIL-label: **1** (sample row 28/21; see below)
- FAIL-kind / FAIL-confirmed_by: **0**
- Decision challenges: **0**

## Full FAIL list

### FAIL-label (1)

- **28/21 AbstractInfoParcel.writeToParcel — work label OPEN, correct label REACHABLE.** Work evidence: "Printed super-callers … AdvancedTorrentInfo:103, PeerInfo:152, SessionStats:69, TorrentInfo:151, TrackerInfo:185 — each inside that subclass's own `writeToParcel`, all of which are OPEN (no printed parcel site), so the dependency rule keeps this OPEN." Post-Phase-3, two of those subclass writeToParcel methods are REACHABLE: TorrentInfo.writeToParcel (30/10, REACHABLE INFERRED via L2 D20) unconditionally calls super.writeToParcel(dest, flags) as its first statement (corpus core/model/data/TorrentInfo.java:151, verified), and TrackerInfo.writeToParcel (30/30, REACHABLE INFERRED via L2 D20) calls super.writeToParcel at :185 (verified). TorrentListItem extends TorrentInfo with no CREATOR/parcel lines and TrackerItem extends TrackerInfo with no CREATOR/parcel lines (L2 verification), so the D20 storage dispatch reaches exactly these super-calls. Under the project's D5b positive direction as applied for 30/2, 30/16, and 30/17, this row flips to REACHABLE (confirmed_by SOURCE by the 30/2 precedent — the super-call sites are printed in app source inside REACHABLE methods; INFERRED is defensible as the chain-weakest-link reading, but OPEN is wrong on either reading). The other three super-callers (AdvancedTorrentInfo, PeerInfo, SessionStats writeToParcel) remain OPEN and do not block the flip. This is a missed dependency consequence of the Phase 3 flips, not a disagreement with any D/L verdict. Per-batch detail: batch28.md.

### FAIL-prose (70) — label, kind, confirmed_by all correct; stale prose contradicts the new label

Quoted stale sentence(s) per row are in the per-batch files. Batch/row list:

- Batch 1: 1/1 ("…so the row stays OPEN"; "D8 decides this row stays OPEN for its own reason (field reads prove class loading, not \<init\> invocation)").
- Batch 2: 2/37 ("Still OPEN under convention (x)"; "do not merge as UNREACHABLE on this evidence"; "D8 decides this row stays OPEN…").
- Batch 3: 3/26 ("D6 decides this row stays OPEN (neither delegator REACHABLE…)").
- Batch 4: 4/11 ("DISPUTED row, kept OPEN"; "Do NOT merge this row as UNREACHABLE on the current evidence"; "…so the row stays OPEN"; "D3c decides this row stays OPEN").
- Batch 10: 10/30, 10/32, 10/39, 10/40 (each: "Stays OPEN…" sentences plus "REVISION 2026-11-01 (still OPEN)" / "round 2 (still OPEN…)" and conditional-table H/T "stays OPEN" entries; 10/39 additionally "This is the strongest OPEN row in batch 10, but still OPEN under the strict full-grep rule").
- Batch 20: 20/39 ("row stays OPEN pending the project-wide hashCode rule"; "Phase 1c (D6 printed-trigger rule): stays OPEN…").
- Batch 21: 21/39 ("stays OPEN pending the project-wide hashCode rule"; "Phase 1c (D6…): stays OPEN…"), 21/40 ("stays OPEN pending the project-wide toString rule"; "Phase 1c (D7…): stays OPEN…").
- Batch 22: 22/4 ("stays OPEN under undecided policy (xii)…"; "Phase 1c (D5a trio policy kept): stays OPEN…").
- Batch 28: 28/28 ("…NOT UNREACHABLE."), 28/29 ("…NOT UNREACHABLE.").
- Batch 29: 29/2, 29/3, 29/7, 29/17, 29/18, 29/22, 29/28, 29/35, 29/36, 29/40 (each: "Stays OPEN").
- Batch 30: 30/2, 30/6, 30/8, 30/9, 30/10, 30/12, 30/13, 30/19, 30/24, 30/27, 30/29, 30/30, 30/32, 30/33, 30/37, 30/39 (each: "Stays OPEN"); 30/16 ("Dependency rule: stays OPEN"); 30/17 ("Dependency rule: stays OPEN, standing/falling with rows 10 and 16").
- Batch 31: 31/1, 31/2, 31/5, 31/6, 31/13, 31/14, 31/18, 31/25, 31/29, 31/37, 31/40 (each: "Stays OPEN"); 31/3 ("Parcelable-trio policy: stays OPEN").
- Batch 34: 34/3 ("called only by BencodeFileTree.toString:125, which is itself OPEN (batch 33 row 8)" — 33/8 is now UNREACHABLE; the parenthetical that formed this row's OPEN rationale is false post-flip).
- Batch 47: 47/21 ("stays OPEN IF the merger holds the settings-family caveat that an implicit/framework toString (…").
- Batch 48: 48/7 ("stays OPEN IF the merger holds the Room-family caveat that zero app-tree hits alone never flip a Room row (generated dispatch unprinted)").
- Batch 58: 58/34 ("…so this stays OPEN, not UNREACHABLE, pending the no-variable-layout convention…"), 58/35 ("Stays OPEN"), 58/37 ("**CONVENTION CONFLICT — NOT decided…**" header and "OPEN under the 58/63-64 convention; would flip to REACHABLE INFERRED under the 65-66 `executeBindings`-read convention.").
- Batch 59: 59/2 ("stays OPEN"), 59/8 ("stays OPEN under convention (v-field)"), 59/13 ("stays OPEN"), 59/22 ("stays OPEN under convention (v-field)"), 59/27 ("stays OPEN").
- Batch 60: 60/9 ("stays OPEN"), 60/17 ("stays OPEN"), 60/25 ("stays OPEN"), 60/30 ("stays OPEN under convention (v-field)"), 60/35 ("stays OPEN").

Pattern note: the FAIL-prose rows are exactly the rows whose pre-flip evidence cell ended in an operative "stays OPEN" conclusion (batches 1–4, 10, 20–22, 29–31, 47–48, 58–60) plus the four special cases (28/28, 28/29, 34/3, 58/37). Rows flipped in batches 32, 33, and the confirmed_by-only rows (39, 40, 42, 56, 57) carry neutral prose and pass; 58/32, 59/5, 59/17, 60/40, and 48/19 pass on the criterion above (see per-batch files). The fix for all 70 is prose-only: remove/replace the quoted sentences with the verdict rationale (which is already in the verdict files); no label, kind, or confirmed_by changes are needed for them.

## Per-batch totals

| Batch | Checked | PASS | FAIL-prose | FAIL-label |
|---|---|---|---|---|
| 1 | 8 | 7 | 1 | 0 |
| 2 | 9 | 8 | 1 | 0 |
| 3 | 8 | 7 | 1 | 0 |
| 4 | 8 | 7 | 1 | 0 |
| 5 | 8 | 8 | 0 | 0 |
| 6 | 8 | 8 | 0 | 0 |
| 7 | 8 | 8 | 0 | 0 |
| 8 | 8 | 8 | 0 | 0 |
| 9 | 8 | 8 | 0 | 0 |
| 10 | 12 | 8 | 4 | 0 |
| 11 | 2 | 2 | 0 | 0 |
| 12 | 8 | 8 | 0 | 0 |
| 13 | 8 | 8 | 0 | 0 |
| 14 | 8 | 8 | 0 | 0 |
| 15 | 8 | 8 | 0 | 0 |
| 16 | 8 | 8 | 0 | 0 |
| 17 | 8 | 8 | 0 | 0 |
| 18 | 8 | 8 | 0 | 0 |
| 19 | 8 | 8 | 0 | 0 |
| 20 | 9 | 8 | 1 | 0 |
| 21 | 10 | 8 | 2 | 0 |
| 22 | 9 | 8 | 1 | 0 |
| 23 | 8 | 8 | 0 | 0 |
| 24 | 8 | 8 | 0 | 0 |
| 25 | 8 | 8 | 0 | 0 |
| 26 | 8 | 8 | 0 | 0 |
| 27 | 8 | 8 | 0 | 0 |
| 28 | 11 | 8 | 2 | 1 |
| 29 | 17 | 7 | 10 | 0 |
| 30 | 24 | 6 | 18 | 0 |
| 31 | 18 | 6 | 12 | 0 |
| 32 | 19 | 19 | 0 | 0 |
| 33 | 9 | 9 | 0 | 0 |
| 34 | 9 | 8 | 1 | 0 |
| 35 | 8 | 8 | 0 | 0 |
| 36 | 8 | 8 | 0 | 0 |
| 37 | 8 | 8 | 0 | 0 |
| 38 | 8 | 8 | 0 | 0 |
| 39 | 10 | 10 | 0 | 0 |
| 40 | 9 | 9 | 0 | 0 |
| 41 | 8 | 8 | 0 | 0 |
| 42 | 10 | 10 | 0 | 0 |
| 43 | 8 | 8 | 0 | 0 |
| 44 | 8 | 8 | 0 | 0 |
| 45 | 8 | 8 | 0 | 0 |
| 46 | 8 | 8 | 0 | 0 |
| 47 | 8 | 7 | 1 | 0 |
| 48 | 10 | 9 | 1 | 0 |
| 49 | 8 | 8 | 0 | 0 |
| 50 | 8 | 8 | 0 | 0 |
| 51 | 8 | 8 | 0 | 0 |
| 52 | 8 | 8 | 0 | 0 |
| 53 | 8 | 8 | 0 | 0 |
| 54 | 8 | 8 | 0 | 0 |
| 55 | 8 | 8 | 0 | 0 |
| 56 | 14 | 14 | 0 | 0 |
| 57 | 9 | 9 | 0 | 0 |
| 58 | 12 | 9 | 3 | 0 |
| 59 | 15 | 10 | 5 | 0 |
| 60 | 14 | 9 | 5 | 0 |
| **Total** | **565** | **494** | **70** | **1** |

## Caveats and notes for the parent (not FAILs)

- 58/32 (PASS): L3 D17 applied over L4's hold-OPEN position (overlap report §1.1 CONFLICT). The D17 rebind print was verified to contain the hasPendingBindings() query, but it is the master-branch upstream file, not a pinned androidx databinding-runtime release version (L3's own caveat). If the merger requires the pinned print, 58/32 (and the other D17 hasPendingBindings rows in scope: 59/2, 59/13, 59/27, 60/9, 60/17, 60/25, 60/35 — all FAIL-prose, not FAIL-label) would need that print; this leaf does not re-decide it.
- 48/19 (PASS, borderline): work prose is conditional framing ("CONDITIONAL, not flipped: flips to UNREACHABLE … IF the merger rules…"), not a "stays OPEN" assertion; counted PASS with the reasoning recorded in batch48.md so the parent can re-judge the framing.
- 28/19 (out of scope, NOT counted): AbstractInfoParcel.\<init\>(Parcel) is neither a changed row nor a sample row and was not checked for this leaf. For routing only: its L2 stays-OPEN premise (subclass Parcel ctors all OPEN) is likewise broken by the Phase 3 flips — TorrentInfo Parcel ctor (30/2, REACHABLE SOURCE) calls super(source) at TorrentInfo.java:121 and TrackerInfo Parcel ctor (30/19, REACHABLE SOURCE) calls super(source) at TrackerInfo.java:170 (both verified in corpus) — so 28/19 appears to follow 28/21 to REACHABLE under the same D5b direction. See batch28.md.
- Sample rows marked "proposal" with "grep owed" (notably batches 1–4, 10, 12–17) were passed on their cited printed-file evidence with the owed-grep limitation recorded per row; the limitation is stated in the rows themselves and is not a contradiction of the label.
- Sample rows with carried (not freshly re-fetched) citations state that caveat in the row (e.g. 24/11, 24/21, 24/26, 24/36; 54/26; 57/11, 57/16); passed on the cited lines with the caveat recorded per row.
- Schema note: work files use varying row layouts (kind sometimes in the label cell, confirmed_by sometimes in a trailing cell, an intervening "—" descriptor cell in batches 12–13). A naive first-match parse misreads some confirmed_by cells (e.g. 12/16, 4/11); the per-row verdicts above use the correct cell in each case.
