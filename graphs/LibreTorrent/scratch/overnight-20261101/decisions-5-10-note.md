# Stream A Phase 1 — decisions note for batches 5–10 (2026-11-01)

**Authorship: these are Muse's own decisions, recorded for user review.
They are NOT made in Yang's name, and nothing here is attributed to Yang.
No tick mark is written anywhere in this note.**

**Scope of this worker: batches 5, 6, 7, 8, 9, 10 ONLY. Labels only.
No device checks. No pushes (pushes held; this worker does not push).
Build: not run. C1: not run. Every edited file remains UNVERIFIED overall;
these labels still need the usual 1-in-5 spot-check before merge.**

## Decision 1 (batches 5–9, coordinator-directed, now executed)

All 200 rows in batches 5–9 (generated base `*Binding` statics: `bind(View)`,
`bind(View,Object)`, and the four `inflate` overloads, 34 classes) are
**UNREACHABLE no_trigger_in_app**, confirmed_by **INFERRED**.

## Decision 2 (batch 10 rows 1–22, Muse's own decision)

**The same evidence standard as batches 5–9 applies to batch 10 rows 1–22.**
All 22 rows (ItemTorrentDownloadableFileBinding rows 1–4,
ItemTorrentListBinding rows 5–10, ItemTrackersListBinding rows 11–16,
TagsListItemBinding rows 17–22) are **UNREACHABLE no_trigger_in_app**,
confirmed_by **INFERRED**. Rows 23–40 of batch 10 are NOT touched by this
worker (another worker's job); their labels are unchanged, including the
4 rows (30, 32, 39, 40) whose citations were already truncated in the
source file.

### Why the same standard applies

1. **Same family, same trigger question.** Batch 10 rows 1–22 are the same
   kind of method as batches 5–9: generated base-class statics whose only
   possible in-app trigger is a direct call (see §"Reason" below). The
   batch 10 file's own note flagged a gap for these rows — its earlier
   Command A pattern ended at ItemTorrentDownloadableFileBinding, so the
   direct-call leg for ItemTorrentListBinding, ItemTrackersListBinding,
   and TagsListItemBinding was audit-carried, not freshly grepped. The
   complete-tree grep in this pass closes that gap: all three classes
   were grepped directly (4 bare-name hits each, 0 direct calls each).
2. **Consistency within a class.** ItemTorrentDownloadableFileBinding
   appears in both batch 9 and batch 10 rows 1–4. Flipping it in batch 9
   but leaving its batch 10 rows OPEN on identical evidence would be
   incoherent; the same evidence must give the same label.
3. **Rule F's two requirements are met for these rows too** (see below),
   with the same saved grep file and the same reason.

## The written rule (rule F)

Branch `work-2026-10-31`, `handoff/KIRO_CONVERT_APPS.md`, line 38
(re-fetched via the GitHub connector in this pass, wording identical to
the local copy):

> Library and generated classes (for example com.bumptech.glide, the
> GlideApp and GlideRequest classes, Dagger and Hilt components, Room
> *_Impl classes, protobuf classes): their label is INFERRED. An
> UNREACHABLE label for such a method needs two things, both written in
> graphs/<App>/scratch/conflicts.md: (1) the output of grep -rn
> "<ClassName>" over the app's source folder, showing every call site
> (file:line); (2) the reason. If the app calls the class, the method is
> reachable through that call and must get a route. "Generated code is
> not called" without the grep output is not a reason.

How the two requirements are met here:

- **(1) Saved grep.** `~/workspace/overnight/stream-A/greps/batch5-9-complete-tree-grep.txt`
  (SHA-256 `110b8badfbdfcfb2a40a3a2f8232ba7039da868814218896330821aa3e243e16`,
  220 lines) lists, per class, every bare-name hit with file:line and
  every direct-call hit (zero everywhere), over the complete tree
  (§"Complete-tree evidence" below), plus the layout supporting evidence.
  The per-row citations in the edited batch files point at this file.
- **(2) The reason.** See §"Reason" below.
- **"If the app calls the class."** Read as: if app code *invokes a
  method of the class*. A field declaration of binding type
  (`private XBinding binding;`), an import, and a `DataBindingUtil`
  request naming a *layout id* do not invoke any `XBinding.inflate/bind`
  static — they invoke `DataBindingUtil` / the mapper, which returns an
  Impl. That reading is what makes the rule operable for generated
  bindings at all; under the alternative reading (any type reference
  counts as "calling"), no generated base static could ever be
  UNREACHABLE, and rule F's UNREACHABLE path for generated classes
  would be dead letter. This interpretation is itself a decision
  recorded here for user review.

## Complete-tree evidence (the re-verification the task required)

Task premise: the 252-file `~/workspace/ruleF-src/` tree allegedly missed
29 Java files. This pass re-verified from the branch:

- Connector directory listing (one fetch at a time, ~30 s pauses, no
  429 encountered) of
  `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
  (branch `work-2026-10-31`) gives **exactly 252 Java files**.
- Compared with `ruleF-src`: **missing = 0, extra = 0** — the path sets
  are identical. So the grep over `ruleF-src` IS a grep over the
  complete main tree by path (contents are the 2026-11-01
  connector-fetched copies, fetch ok=252 fail=0).
- **Discrepancy, reported honestly: no 29-file gap was found under the
  branch paths specified in the task.** The only other Java files in the
  app module are the other source sets, enumerated the same way:
  androidTest (13 Java files) + test (7 Java files) = **20 files**,
  all fetched fresh via the connector in this pass and grepped
  separately. debug/release contain only `res/` subtrees (listed one
  level: drawable/mipmap/values/xml; not descended because a `res/`
  subtree cannot contain app Java code), and `play/` contains only an
  AndroidManifest. Total repo Java found: 252 + 20 = **272 files**.
  If the "29 missing" refers to files outside `final_java_only` (e.g.
  the original source upload), that was outside the tree this task
  specified and was not searched.
- **Grep results (37 classes: 34 from batches 5–9 + 3 new in batch 10):**
  - Direct `XBinding.(inflate|bind)(` calls: **0 in the main tree,
    0 in the 20 test files.** Robustness checks: no split-line call
    (no line ends with a binding class name), no fully-qualified
    `databinding.XBinding.` call, all non-DataBindingUtil `.inflate(`
    hits are LayoutInflater/MenuInflater/view inflation, and all
    non-DataBindingUtil `.bind(` hits are ViewHolder `holder.bind(...)`
    calls — none names a binding class.
  - Bare class-name hits in the main tree: **95 total** — 83 across 32
    of the 34 batches 5–9 classes (reproducing the earlier corrected
    count exactly) + 4 each for ItemTorrentListBinding,
    ItemTrackersListBinding, TagsListItemBinding. The 2 classes with
    zero app-Java references are AddTorrentInfoBinding and
    DetailTorrentAppbarBinding (both `<include>` children; see below).
  - `DataBindingUtil.(inflate|bind|setContentView)(` occurrences in the
    main tree: **35** (32 for batches 5–9 classes: 29 inflate +
    3 setContentView, plus 3 adapter sites for the new batch 10
    classes). Test files: 0.
  - **No class was left OPEN for a direct call: there is no class NOT
    flipped.** Every one of the 37 classes has zero direct calls, so
    every row in scope flipped.
- **Layout supporting evidence** (in the same grep file): 37 layouts
  with a `<layout>` root, exactly matching the 37 classes; no layout
  XML names a `*Binding` class (only the unrelated `BindingAdapterUtils`
  utility is imported, by two layouts). `<include>` targets that are
  binding layouts: only `@layout/add_torrent_info` (in
  `fragment_add_torrent_info.xml:16`) and `@layout/detail_torrent_appbar`
  (in `fragment_detail_torrent.xml:10`); all other includes target
  `toolbar` / `main_drawer_content`, which are not data-binding
  layouts. A layout does not call a base static directly, so this is
  supporting evidence only, as the task states. Layout copies used are
  prior-pass local copies (69 files); they were not re-fetched
  file-by-file in this pass for the reason just given.

## Reason (rule F requirement 2)

Generated base `*Binding` statics are entry points for direct callers
only:

- App code instantiates bindings by layout id through
  `DataBindingUtil.inflate / setContentView / bind`. Those go through
  the generated `DataBinderMapper`, which instantiates the `*Impl`
  class directly (constructor), bypassing the base static. A
  `DataBindingUtil` site selects by layout id, never by overload, so no
  single overload has a distinct trigger — and with zero direct calls,
  no overload has any trigger at all. All 6 overloads per class
  therefore flip together on identical evidence.
- The `<include>`-child case (AddTorrentInfoBinding,
  DetailTorrentAppbarBinding) was the one live doubt: generated parent
  Impl code could in principle call a child binding's `bind`. The
  databinding library's own `ViewDataBinding` binding path answers it:
  for includes, generated code resolves the child through
  `DataBindingUtil.bind(bindingComponent, child, ...)` (the
  `mapBindings` include path), i.e. again through the mapper to the
  Impl — not through `ChildBinding.bind(...)`. So the child `bind`
  overloads have no generated caller either. (Generated Impl bodies
  themselves are absent from `final_java_only`, so this rests on the
  library's published binding path, not on a printed Impl body — hence
  confirmed_by INFERRED, not SOURCE.)
- The base static's own body (which itself delegates to
  `DataBindingUtil`) is not a call *to* the static and does not make it
  reachable.

## Relation to the earlier D4h "stay OPEN" ruling — SUPERSEDED for this family

`~/workspace/overnight/stream-A/DECISIONS.md` §D4h ruled these same
rows stay OPEN ("zero direct calls plus unprinted generated code =
OPEN, never UNREACHABLE"). This pass **supersedes D4h for batches 5–9
and batch 10 rows 1–22 only**, for three stated reasons:

1. D4h was written on the 252-file tree with the generated-dispatch
   question explicitly open; the complete-tree re-verification (272
   files, zero direct calls) plus the layout mapping closes the
   "a direct call could hide in missed files" leg that D4h left open.
2. D4h's generated-parent-Impl-`bind` speculation for the two child
   classes is answered by the library include path above
   (`DataBindingUtil.bind`, not `ChildBinding.bind`).
3. D4h's overload objection ("no single overload could be promoted
   while its siblings stay OPEN on identical evidence") is resolved by
   promoting *all* overloads together on identical evidence, not one.

D4h is otherwise untouched, and this supersession is itself a decision
for user review: if the user (or the coordinator, holding ticked-app
precedent) disagrees with the "calls the class" reading or the library
include-path reasoning, these 222 rows revert to OPEN by restoring the
pre-flip backups in `~/workspace/overnight/stream-A/backup-pre-flip/`.

## Ticked-app precedent

**None cited.** No ticked-app convention file was in this worker's read
set (the same position DECISIONS.md records at lines 41–44), and no
precedent is invented here. The decision rests on rule F's text, the
complete-tree grep, and the reason above. If the coordinator holds
ticked-app precedent contradicting this decision, it should override
this note and the rows should be reverted from backup.

## Why confirmed_by is INFERRED, not SOURCE

The UNREACHABLE conclusion rests on (a) absence of direct calls in
printed app code (the saved grep) and (b) generated/library dispatch
semantics (mapper bypass, library include path), whose bodies are not
printed in this dataset. Under the task's confirmed_by rule, that is
INFERRED (library/generated code, or code not read), never SOURCE.
No row uses DYN, FW-MEMORY, or UNVERIFIED as confirmed_by.

## Before/after counts (mechanically verified from the label column)

- Batch 5: before 40 OPEN → after **40 UNREACHABLE no_trigger_in_app**.
- Batch 6: before 40 OPEN → after **40 UNREACHABLE no_trigger_in_app**.
- Batch 7: before 40 OPEN → after **40 UNREACHABLE no_trigger_in_app**.
- Batch 8: before 40 OPEN → after **40 UNREACHABLE no_trigger_in_app**.
- Batch 9: before 40 OPEN → after **40 UNREACHABLE no_trigger_in_app**.
- Batch 10: before 26 OPEN / 1 REACHABLE proposed / 13 UNREACHABLE
  proposed → after **22 UNREACHABLE no_trigger_in_app (rows 1–22)** /
  13 UNREACHABLE proposed (untouched) / 1 REACHABLE proposed (row 31,
  untouched) / 4 OPEN (rows 30, 32, 39, 40, untouched, truncated
  citations). Total rows per file: 40. Batch 10 changed rows are
  exactly 1–22 (verified by diff against backup); batches 5–9 changed
  rows are exactly 1–40 each.
- Every edited file carries a dated 2026-11-01 revision note listing
  every changed row and why. Build: not run. C1: not run.

## Caveats for the merger / spot-checker

- Generated `*Impl` / mapper bodies remain unprinted. If a future build
  print shows a generated caller of a specific base static, that
  overload re-opens (per-class, per-overload).
- The pre-existing header notes in the batch 5–9 files saying "stay
  OPEN pending the convention decision" are historical notes from the
  earlier pass; the dated 2026-11-01 revision note at the top of each
  file supersedes them for the flipped rows.
- The "29 missing files" discrepancy (§"Complete-tree evidence") should
  be reconciled by the coordinator: either the 29 refers to files
  outside `final_java_only`, or to a different tree, or the earlier
  claim was mistaken. It does not block these flips, because the
  complete branch tree under the specified paths was enumerated fresh
  and contains no un-grepped Java file.
- Nothing here is merged, pushed, or verified for merge. Originals in
  `~/workspace/libretorrent-merge/` were not touched; branch files
  (`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`) were not
  touched.
