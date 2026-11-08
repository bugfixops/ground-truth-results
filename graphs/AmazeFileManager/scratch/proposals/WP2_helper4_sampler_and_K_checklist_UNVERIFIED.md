# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# WP2 AmazeFileManager — Helper 4 of 4: folded fixes, sampler reconstruction, [K] checklist

**Status: UNVERIFIED, NOT MERGED, NOT PUSHED.** This helper pushed nothing;
the parent pushes. Repo `bugfixops/ground-truth-results`, branch
`work-2026-10-31` only. No token, no git clone, no edit to `graph_def.py`,
`out/`, `progress/`, or `tools/` in the repo. No APK, zip, secret, or token
in any file produced here.

## (a) Folded merge-ready file

`WP2_Amaze_merge_ready_fixes_FOLDED_UNVERIFIED.py` (same directory as this
report; parent to commit under
`graphs/AmazeFileManager/scratch/proposals/`).

What it folds, with nothing added beyond the four source reports
(first set, second set, non-Glide report, Glide report):

| # | Item | Delete / remove | Add | Guard / evidence | Status |
|---|---|---|---|---|---|
| 1 | E89e2cedd | Delete edge E89e2cedd (snapshot line 11617, confirm on checkout) | `SftpConnectDialog.lambda$null$5 -> GetSshHostFingerprintTask.execute` | Guard `!isEmpty(sshHostKey)` (:175); evidence `SftpConnectDialog.java:178,199` | Proposed |
| 2 | Ee1aeff93 | Delete `<init> -> Decompressor.decompress` ONLY if confirmed present (edge_lines snapshot: absent, `None`) | `CompressedExplorerFragment$1.onActionItemClicked -> Decompressor.decompress(String,String[])` | Guard `item.getItemId() == R.id.ex` (:307,:321); decompressor assigned :215/:243; evidence `:329` | Proposed (add); delete conditional |
| 3 | GlideRequest.listener | Remove UNREACHABLE (snapshot line 11004, confirm) | `showThumbnailWithBackground -> listener` (:899), `showRoundedThumbnail -> listener` (:945) | `PREFERENCE_SHOW_THUMB` (:593,:607,:719,:732) | Proposed |
| 4 | GlideRequest.clone | Remove UNREACHABLE ONLY if checkout confirms current label is UNREACHABLE (absent from 363-entry snapshot — proves nothing) | `AppsAdapterPreloadModel.getPreloadRequestBuilder -> GlideRequest.clone` (:44) | Receiver `GlideRequest<Drawable>` (:24,:28) | Proposed (add); removal conditional |
| 5 | IconDataParcelable.setImageBroken | Remove UNREACHABLE (snapshot line 14064, confirm) | `showThumbnailWithBackground -> setImageBroken` (:864,883,895), `showRoundedThumbnail -> setImageBroken` (:912,930,941), plus `onBindViewHolder -> show*` method-reference edges (:595-596,598-599,608-609 / :724,733) | `PREFERENCE_SHOW_THUMB` at callers | Proposed |
| 6 | LayoutElementParcelable.writeToParcel | Remove UNREACHABLE (snapshot line 11155, confirm) | `MainFragment.onSaveInstanceState -> writeToParcel` (FRAMEWORK; CALL acceptable if merger convention differs, marshalling still INFERRED) | `listView != null` (:402); evidence `:397,402,415`, `LIST_ELEMENTS` :153 | Proposed |
| 7 | RoundedImageView.setBackgroundColor | Remove UNREACHABLE (snapshot line 13206, confirm) | `onBindViewHolder -> setBackgroundColor` (:716,742,744), `showRoundedThumbnail -> setBackgroundColor` (:905,908,916,925,940) | **Grid branch only + `PREFERENCE_USE_CIRCULAR_IMAGES` true**; :723 `imageView1` deliberately NOT cited; non-circular `iconLayout` branch NOT this override | Proposed |
| 8 | SimpleTextWatcher.beforeTextChanged | Remove UNREACHABLE (snapshot lines 14477-14479, confirm) | `RenameBookmark.onCreateDialog -> beforeTextChanged` (FRAMEWORK) | Evidence `RenameBookmark.java:86-93,112-119`; TextView dispatch INFERRED | Proposed |
| 9 | SimpleTextWatcher.onTextChanged | Remove UNREACHABLE (snapshot lines 14481-14483, confirm) | `RenameBookmark.onCreateDialog -> onTextChanged` (FRAMEWORK) | Same sites as #8 | Proposed |
| 10 | GlideRequests.as | Remove UNREACHABLE (snapshot line 11014, confirm) | `GlideRequests.asDrawable -> GlideRequests.as` | Anchors `RecyclerPreloadModelProvider.java:30`, `AppsAdapterPreloadModel.java:28` | Proposed **INFERRED only — HOLD-FOR-SOURCE if merger requires SOURCE-only** (resolver: print build-generated `GlideRequests.java`, confirm `asDrawable() { return as(Drawable.class); }`) |
| S | Supporting edges (deduplicated, once each) | — | `setItems -> RecyclerPreloadModelProvider.<init>` (:388); `RecyclerPreloadModelProvider.<init> -> GlideRequests.asDrawable` (:30); `AppsAdapterPreloadModel.<init> -> GlideRequests.asDrawable` (:28) | Add only if missing | Proposed |

Supporting-edge deduplication note: the `onBindViewHolder -> show*`
edges appear once, as code in FIX 5, and are cross-referenced (not
repeated) from FIX 3, so the merger must not add them twice. Total in
the folded file: 18 `e(...)` calls (15 in FIX 1-10 + 3 supporting),
10 removal proposals (2 conditional), 1 hold-flagged INFERRED fix.

Deliberately NOT in the folded file (no fix exists in any report for
them): the 13 Glide OPEN methods, `SimpleTextWatcher.afterTextChanged`,
`TextEditorActivity.<init>`, and the Sftp `$2` vs `$6` assignment — all
carried as OPEN items with their resolvers inside the folded file, and
listed again in the [K] checklist below. Also not added: any edge for
`GlideOptions.clone` from `AppsAdapterPreloadModel.getPreloadRequestBuilder`
(that site is `GlideRequest.clone`, FIX 4).

Local syntax check only: `python3 -m py_compile` on the folded file
passes (it is `e(...)` fragments in `graph_def.py` style, not a runnable
script — `e` is defined by `graph_def.py`, not by this file). That check
proves syntax only; it is NOT a build, sampler, grep, or C1 check, and
no such check is claimed for any folded item.

## (b) Sampler reconstruction attempt — FAILED for all three files, plainly

Attempt method (this helper, spaced single-file connector fetches only,
no burst): (i) listed `graphs/AmazeFileManager/out/` via
`get_file_contents` on the directory; (ii) inspected the live
`get_file_contents` tool schema via `list-tools`; (iii) attempted one
`get_file_contents` fetch of `out/methods.csv` itself. No `git clone`,
no token, no download-URL use (see barrier below). `parts/` files were
considered and rejected as a reconstruction source (see §3).

### Per-file result

| File | Size (bytes) | Reconstructed? | Exact barrier |
|---|---|---|---|
| `graphs/AmazeFileManager/out/methods.csv` | 1,179,770 (confirmed by this helper: directory listing + fetch attempt on branch `work-2026-10-31`) | **NO** | Connector reply, verbatim in substance: "File graphs/AmazeFileManager/out/methods.csv is too large to display (1179770 bytes). Use the download URL to fetch the content: https://raw.githubusercontent.com/…/methods.csv?token=<redacted> (SHA: 22e201cda35c422ffd3061dfc4931ae587208f9c)". The token is redacted in tool output and must not be unwrapped or used (second-set report rule, followed here). No content was returned. |
| `graphs/AmazeFileManager/graph_def.py` | 1,058,622 (per first/second-set reports; not re-fetched this session, to keep fetches spaced and single — see §2) | **NO** | Same tool, same barrier class: file exceeds the connector's display limit, and the tool offers no chunk/range parameters (see §2). No content obtainable connector-only. |
| `graphs/AmazeFileManager/out/auto_calls.json` (path as named in the second-set report; the build input alongside `graph_def.py`) | 1,839,161 (per second-set report; not re-fetched this session, same reason) | **NO** | Same barrier as `graph_def.py`. No content obtainable connector-only. |

### 1. No chunk/range mechanism exists in the connector actually offered

The live `get_file_contents` input schema (from `list-tools` in this
session) accepts only: `owner`, `repo`, `path`, `ref`, `sha`, and
`fields` (directory listings only — a subset of entry fields to reduce
listing size). There is **no** start/end/offset/limit/range/line-range
parameter, no blob/range tool, and no partial-read tool in the reviewed
read set (`get_file_contents`, `search_code`, etc.). `fields` does not
help for a single file: the schema states it is "Ignored when the path
is a single file." `search_code` was already shown broken for this repo
(returns 0 / incomplete for terms definitely present, e.g.
`setImageBroken`, `SimpleTextWatcher`, `GlideOptions`, `E89e2cedd`) and
cannot reconstruct file contents row by row. Directory listings return
names/types/sizes only — they confirm a file exists and its size, never
its rows.

### 2. Why the two large files were not re-fetched this session

Re-fetching `graph_def.py` and `auto_calls.json` would each predictably
return the same "too large to display" refusal already established by
the first and second sets, at the cost of two more large-file connector
calls. They were therefore cited from those reports (sizes above) rather
than re-proved, and the single fresh fetch spent this session was the
one that matters most for the sampler: `methods.csv`. If the parent
wants all three refusals re-confirmed in one session, that is three
spaced single fetches, not a burst — but the outcome is already
determined by the tool schema in §1, which has no range parameter to
exploit.

### 3. Why `parts/` files cannot reconstruct what the sampler needs

`tools/verify_sample.py` (local scratch copy read for this report)
reads exactly one input: `graphs/<App>/out/methods.csv`, filters rows
to `verdict == 'REACHABLE'`, and needs per-row fields the parts files do
not contain: `env_kinds`, `state_kinds`, `route_edge_classes`,
`confirmed_by`, `steps_from_launch`, `route_edge_ids`, and `method`.
Its strata quotas for N=30 are NONSTD 4, INFERRED 4, STATE 3, ENV 6,
LONG 6, PLAIN 7 (scaled by N/30), with a seed-shuffled, max-new-edges
greedy pick (default seed 20261025). Parts files (`parts/*.py`, e.g.
`label_1.py`, `label_b014.py`, `repair_rp02.py`) are graph-definition
fragments — edge lists and label reasons — not the built `methods.csv`
route table, and they carry no `route_edge_ids` / strata fields. Even a
complete parts listing therefore cannot reproduce the sampler's input,
its shuffled order, or its picked 30. Reconstructing `methods.csv` from
parts would also require running the build, which itself needs the
unfetchable `graph_def.py` + `auto_calls.json` — circular.

### 4. What is therefore NOT claimed

No `sample_30.txt`, no sampled-route table, no error rate (neither the
WP2 sample rate nor the issue-first 5/5 and 3/3 fractions from the
earlier sets, which must not be quoted as the app's rate), no
`verification.csv`, and no check result of any kind (build, sampler,
grep, C1) is produced or implied by this helper. The earlier sets'
"5/5" and "3/3" fractions describe deliberately issue-first judged items
only.

### 5. What a full local checkout would need to run (exact list)

In dependency order at merge time (see checklist §(c) for the order):

1. `python3 -I tools/verify_sample.py AmazeFileManager 30 20261025`
   (needs `graphs/AmazeFileManager/out/methods.csv` locally).
2. `tools/build_graph.py` (rebuild after applying folded fixes; needs
   `graphs/AmazeFileManager/graph_def.py` + `auto_calls.json` locally).
3. `check_citations` (citation check — exact tool/script name as used in
   the handover's eight checks; confirm against `tools/` on checkout).
4. `check_routes` (route check).
5. `check_bytecode_lines` (bytecode-line check; also the resolver for
   the Sftp `$2` vs `$6` assignment — needs class files, not source).
6. `scan_unreachable --all` and `scan_unreachable --callers`
   (unreachable scan, both modes).
7. `make_verification.py` (writes `verification.csv` — never by hand).
8. `gen_readme_v2.py` (regenerates the app README from the verified
   table + notes).

Plus, for the OPEN resolvers (not the eight checks, but merge gates):
receiver-typed full-tree grep for the Glide group (see folded file
R-tree), build-generated `GlideRequests.java` / `GlideRequest.java`
prints (R-as, R-setRequestOptions, R-options-init, R-request), Glide
library source for the app's Glide version (R-lib), `graph_def.py`
edge prints + manifest + `FileUtils.openFile`/`openunknown` for the
`TextEditorActivity.<init>` ENV gate, and a full-repo
`SimpleTextWatcher` registration hunt for `afterTextChanged`.

## (c) [K] checklist — what is done, what is blocked, merge-time order

`[K]` here means: route checks DONE, awaiting user tick. It is **NOT**
`[x]` (verified/complete), and this helper does **not** claim `[K]` is
reached — the blocked items below prevent it honestly. The parent
decides the PROGRESS_V2 line; it must read `[K]`, never `[x]`, and only
after the merge-time steps below are actually run on a checkout.

### Done (proposals only — route-judging complete, verification not done)

- Baseline re-checked: 2981 methods, 2509 REACHABLE / 472 UNREACHABLE,
  errors 0, warnings 0, no `verification.csv` on `work-2026-10-31`
  (out/ listing this session confirms: no `verification.csv` present;
  `methods.csv` 1,179,770 bytes present).
- 25 unique methods judged across first + second sets (per the
  21:27 EDT stage record): 2 wrong edges (E89e2cedd, Ee1aeff93),
  8 REACHABLE proposed (`GlideRequest.listener`, `GlideRequest.clone`,
  `IconDataParcelable.setImageBroken`, `LayoutElementParcelable.writeToParcel`,
  `RoundedImageView.setBackgroundColor`, `SimpleTextWatcher.beforeTextChanged`,
  `SimpleTextWatcher.onTextChanged`, `GlideRequests.as` INFERRED),
  15 OPEN (13 Glide + `afterTextChanged` + `TextEditorActivity.<init>`).
- All fix fragments folded into one file (§(a) above), each annotated
  with edge id, delete/add, evidence file:line, guard, and status.
- Sampler reconstruction attempted and documented as failed (§(b) above).

### Blocked (each blocks [K] until resolved on a full checkout)

- **B1 — Sampler / sample table.** `methods.csv` unfetchable
  connector-only (§(b)). No reproducible 30-route sample, no sample
  error rate, no `verification.csv` until a checkout runs
  `verify_sample.py AmazeFileManager 30 20261025` and every sampled
  route is judged step by step from printed source.
- **B2 — Build / C1.** `graph_def.py` + `auto_calls.json` unfetchable
  connector-only. No rebuild, citation, route, bytecode-line, or
  `scan_unreachable --all/--callers` check can be run or claimed.
- **B3 — Glide OPEN (13).** Needs generated-source prints (R-as,
  R-setRequestOptions, R-options-init, R-request), a receiver-typed
  full-tree grep (R-tree), and Glide library source (R-lib). Until
  then: no flip, no edge, no UNREACHABLE confirmation for any of the 13.
- **B4 — `SimpleTextWatcher.afterTextChanged` OPEN.** Needs the
  full-repo registration / override-set hunt. The RenameBookmark
  evidence cuts against the base method for those two instances (no
  `super` call); coverage alone must not flip it.
- **B5 — `TextEditorActivity.<init>` ENV gate OPEN.** Needs the
  `graph_def.py` ENV edge text + manifest + `FileUtils` launch path,
  and a check of whether the ENV condition held in the tool run.
- **B6 — Sftp `$2` vs `$6` OPEN.** Needs bytecode / class-file lambda
  order. Do not assign by source order (source order ≠ `$null$`
  numbering for nested lambdas). This blocks only that assignment, not
  FIX 1's delete + `lambda$null$5` add — but the merger must not
  silently resolve it while applying FIX 1.
- **B7 — GlideRequests.as SOURCE status.** Under a SOURCE-only rule,
  FIX 10 stays held until generated `GlideRequests.java` confirms the
  `asDrawable() -> as(...)` delegation. Under an INFERRED-accepted rule
  it may be applied with the INFERRED flag recorded.
- **B8 — Conditional items.** Ee1aeff93 existence and
  `GlideRequest.clone`'s current label must both be printed from the
  checkout before their removals are applied (snapshot pointers:
  Ee1 absent from `edge_lines.json`; clone absent from the 363-entry
  `unreach_lines.json` — neither absence proves the current state).

### Exact order of steps at merge time (checkout only, in this order)

1. **Print current `graph_def.py` lines** for every delete / removal in
   the folded file (E89e2cedd ~11617; listener ~11004; as ~11014;
   setImageBroken ~14064; writeToParcel ~11155; setBackgroundColor
   ~13206; beforeTextChanged ~14477-14479; onTextChanged ~14481-14483;
   plus Ee1aeff93 existence search and `GlideRequest.clone` label
   lookup). Confirm each edge/entry still exists at that line; if any
   text differs, stop for that item and re-derive it — do not apply
   blindly.
2. **Apply the folded fixes** (FIX 1-10 + SUPPORTING, respecting every
   conditional and the FIX 10 hold flag; leave every OPEN item untouched).
3. **Rebuild**: `python3 -I tools/build_graph.py graphs/AmazeFileManager`
   (confirm exact invocation against `tools/` on checkout); save the
   build report; confirm counts move only as the fixes predict and
   errors/warnings stay 0.
4. **Re-print** every route touched by the fixes from the rebuilt graph
   and confirm each proposed route now resolves (including the
   `lambda$null$5` route head and the Glide receiver chains).
5. **Redraw the sample**: `python3 -I tools/verify_sample.py
   AmazeFileManager 30 20261025`; print every sampled route step;
   judge each step from source (SOURCE only where lines were printed,
   otherwise INFERRED, never DYN / FW-MEMORY / UNVERIFIED); record
   correct / fixed / wrong / unclear per the route-check rule.
6. **Resolve or explicitly carry the OPEN items**: run resolvers R-as,
   R-setRequestOptions, R-options-init, R-request, R-tree, R-lib (Glide);
   the `SimpleTextWatcher` registration hunt; the `TextEditorActivity`
   ENV-edge + manifest + `FileUtils` check; the Sftp `$2`/`$6` bytecode
   check. Anything still unresolved stays OPEN in the table with its
   resolver named — it is not silently dropped or flipped.
7. **Final table**: write the WP2 table (sample of 30, error rate on
   judged non-unclear items only, with the issue-first fractions from
   earlier sets kept separate and never quoted as the sample rate).
8. **`verification.csv` via `make_verification.py` only** (never by hand).
9. **Five-heading `readme_notes.md`** (headings per the handover's WP2
   readme convention; confirm on checkout) + run `gen_readme_v2.py`.
10. **`LESSONS.md`** entry (what the Sftp lambda, method-reference, and
    Glide receiver-type errors teach for the remaining apps).
11. **Eight checks**: build, citations, routes, bytecode lines,
    `scan_unreachable --all`, `scan_unreachable --callers`, sampler
    reproducibility (re-run with seed 20261025, same 30), and the
    verification.csv / README consistency check — each recorded with
    its printed output, none claimed without a run.
12. **PROGRESS_V2 line to `[K]` (awaiting user tick, never `[x]`)**,
    only after steps 1-11 are all actually run and recorded. If any
    step cannot run, the line stays below `[K]` and the blocker is
    named — a `[K]` line must never be written on proposals alone.

### What the parent still needs to do (this helper did not)

- Push the folded file + this report to `work-2026-10-31` under
  `graphs/AmazeFileManager/scratch/proposals/` (this helper was told
  not to push; nothing was pushed by this helper).
- Arrange the full local checkout that unblocks B1/B2, or an authorised
  file transfer the parent arranges — the connector cannot supply
  `methods.csv`, `graph_def.py`, or `auto_calls.json` in usable form.
- Confirm whether the merger's edge rule is SOURCE-only (then FIX 10
  holds) or INFERRED-accepted with flagging (then FIX 10 may apply
  flagged).
