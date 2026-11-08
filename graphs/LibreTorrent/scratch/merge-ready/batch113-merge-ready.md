**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 113 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 113 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, from printed source. The prior batch-113 proposal (`~/workspace/libretorrent-batch113-proposal.md`) was used as an INPUT, not a result; every row below was checked against printed source in this pass, and one change was made from it (rows 10 and 15, see below).

## Membership — verified, not guessed

Exactly the 40 rows for batch 113 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy). All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan (candidates, not evidence), in plan order:
DrawerExpandableAdapter (+ holders) rows 1-9, DrawerGroup rows 10-14, DrawerGroupItem row 15, EmptyTagItem rows 16-18, NoTagsItem rows 19-21, drawer.TagItem rows 22-24, drawer.TagsAdapter (+ holders, $1) rows 25-40.
Membership was re-checked mechanically in this pass against the plan copy: 40 rows, sequence 1-40 intact, method names identical to the plan list.

## Printed source used in this pass

Path prefix for all (unless stated): `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
- Prior-session printed copies, re-read in full in this pass, saved under `~/workspace/b113-114-src/`:
  - `ui/main/drawer/DrawerExpandableAdapter.java` (250 lines)
  - `ui/main/drawer/DrawerGroup.java` (69 lines)
  - `ui/main/drawer/DrawerGroupItem.java` (38 lines)
  - `ui/main/drawer/EmptyTagItem.java` (35 lines)
  - `ui/main/drawer/NoTagsItem.java` (32 lines)
  - `ui/main/drawer/TagItem.java` (61 lines) — this is `ui/main/drawer/TagItem`, NOT the `ui/tag/TagItem` of batches 119-120; different class, different equals, must not be conflated.
  - `ui/main/drawer/TagsAdapter.java` (316 lines)
  - `ui/main/MainActivity.java` (811 lines)
  - `ui/main/MainFragment.java` (637 lines; checked — contains no drawer/tags construction, only TorrentListAdapter; the drawer lives in MainActivity, not MainFragment)
  - `ui/main/drawer/AbstractTagItem.java` (26 lines, abstract isSame/equals declarations only; not a batch row)
- Fresh connector fetch in THIS pass, branch `work-2026-10-31`, one file at a time, no HTTP 429 hit:
  - `core/utils/Utils.java`, saved to `~/workspace/b113-114-src-fresh/Utils.java` (44,368 bytes). `getNavigationDrawerItems` at :720; `new DrawerGroup(...)` sites (status/sorting/dateAdded) and `status.items.add(new DrawerGroupItem(...))` etc. immediately following. This fresh print is what upgrades rows 10 and 15 below from the prior proposal's INFERRED to SOURCE.

## Shared routes (printed steps, cited once and reused by row)

All file references below are to the prefix above unless stated otherwise. DEA = `ui/main/drawer/DrawerExpandableAdapter.java`, DG = `ui/main/drawer/DrawerGroup.java`, DGI = `ui/main/drawer/DrawerGroupItem.java`, ET = `ui/main/drawer/EmptyTagItem.java`, NT = `ui/main/drawer/NoTagsItem.java`, TI = `ui/main/drawer/TagItem.java`, TA = `ui/main/drawer/TagsAdapter.java`, MA = `ui/main/MainActivity.java`.

**R-DRAWER — MainActivity drawer.** MA.initLayout -> initDrawer :230-293. initDrawer :248-250: `Utils.getNavigationDrawerItems(this, ...)` -> `new DrawerExpandableAdapter(groups, drawerItemManager, this::onDrawerItemSelected)` :250 -> `drawerItemManager.createWrappedAdapter(drawerAdapter)` :251 -> onDrawerGroupsCreated() :252 -> drawerItemsList.setAdapter(wrappedDrawerAdapter) :255 -> drawerItemManager.attachRecyclerView(drawerItemsList) :259. The wrapped adapter / manager / RecyclerView then dispatch the expandable-adapter callbacks (library dispatch, INFERRED, not printed from library source).

**R-TAGS — MainActivity tags list.** Same initDrawer :270-272: tagsList.setLayoutManager, `tagsAdapter = new TagsAdapter(tagsClickListener)` :271, tagsList.setAdapter(tagsAdapter) :272. subscribeTags :470-486: `Flowable.just(new EmptyTagItem())` :475, `Flowable.just(new NoTagsItem())` :476, `Flowable.fromIterable(list).map(TagItem::new)` :477, then `tagsAdapter.submitList(items)` :485 (ListAdapter/DiffUtil dispatch, INFERRED). setInitSelection :490-525 calls tagsAdapter.setSelectedItem with a new EmptyTagItem :498/:509, a new NoTagsItem :501, or a matched TagItem :519. MainActivity:331 calls tagsAdapter.getSelectedItem() inside the tag-menu handler; :334 calls setSelectedItem(emptyItem).

**R-DIFF — TagsAdapter DiffUtil callback (the batch-113 special item).** TagsAdapter:130-147 defines static `diffCallback` (anonymous class $1): areContentsTheSame :133-138 `return oldItem.equals(newItem);`, areItemsTheSame :141-146 `return oldItem.isSame(newItem);`. DiffUtil runs this callback when submitList is called (R-TAGS :485) — library dispatch, INFERRED. This is the printed route for drawer.TagItem.equals: TagItem.equals is NOT no_trigger_in_app. It is REACHABLE proposed, INFERRED, on this route. The same callback is the second route for every AbstractTagItem subclass's equals/isSame. This contradicts the out/methods.csv UNREACHABLE-unclassified entry for this method; the plan's TODO_CANDIDATE_REACHABLE is the correct direction on this evidence.

**Confirmed_by convention used here.** SOURCE = the method's own call site is printed in app code (explicit `new`, method call, or `super(...)` in a printed constructor, or a printed call inside the same file). INFERRED = the only step into the method is a framework/library dispatch (RecyclerView, ListAdapter/DiffUtil, View click, PopupMenu, JVM class initialisation) or a call inside an unprinted method body. A row whose upstream callback is INFERRED but whose own call site is a printed explicit call is marked SOURCE, with the upstream caveat noted — e.g. holder constructors and typed bind overloads. Under a whole-route INFERRED convention, the SOURCE rows whose upstream dispatch is library/framework would flip to INFERRED; labels are unaffected, only confirmed_by would change at merge.

## Counts — proposed, not verified (mechanically verified: 40 rows, sequence 1-40 intact)

- REACHABLE proposed: 40 / 40 (SOURCE 24, INFERRED 16)
- UNREACHABLE proposed: 0
- OPEN: 0
- Verified for merge: 0

Change from the prior proposal (the only change): rows 10 and 15 move INFERRED -> SOURCE, because Utils.getNavigationDrawerItems was freshly printed in this pass (see above); prior SOURCE 22 / INFERRED 18 becomes SOURCE 24 / INFERRED 16. Labels unchanged.

## Per-method table (all 40 rows, in plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|
| 1 | DrawerExpandableAdapter.onBindChildViewHolder | REACHABLE proposed | INFERRED | R-DRAWER: adapter set on RecyclerView MA:255, manager attached MA:259; library dispatches to DEA:105-124 (binds holder, :115 holder.bind(group, item), :116-123 click listener). Body printed, dispatch library, hence INFERRED. |
| 2 | DrawerExpandableAdapter.onBindGroupViewHolder | REACHABLE proposed | INFERRED | R-DRAWER as row 1; DEA:94-102 (:101 holder.bind(group)). Dispatch library, hence INFERRED. |
| 3 | DrawerExpandableAdapter.onCheckCanExpandOrCollapseGroup | REACHABLE proposed | INFERRED | R-DRAWER as row 1; DEA:186-190, called by the expandable-item manager on user expand/collapse (library dispatch, unprinted). |
| 4 | DrawerExpandableAdapter.onCreateChildViewHolder | REACHABLE proposed | INFERRED | R-DRAWER as row 1; DEA:85-91 (:90 new ItemViewHolder(v)). Dispatch library, hence INFERRED. |
| 5 | DrawerExpandableAdapter.onCreateGroupViewHolder | REACHABLE proposed | INFERRED | R-DRAWER as row 1; DEA:75-81 (:80 new GroupViewHolder(v)). Dispatch library, hence INFERRED. |
| 6 | DrawerExpandableAdapter$GroupViewHolder.<init> | REACHABLE proposed | SOURCE | Explicit printed construction DEA:80 `return new GroupViewHolder(v);` inside onCreateGroupViewHolder (row 5, upstream INFERRED). Definition DEA:196-201. |
| 7 | DrawerExpandableAdapter$GroupViewHolder.bind | REACHABLE proposed | SOURCE | Explicit printed call DEA:101 `holder.bind(group);` inside onBindGroupViewHolder (row 2). Definition DEA:203-210 (:205 setText(group.name), :207-209 expand state). |
| 8 | DrawerExpandableAdapter$ItemViewHolder.<init> | REACHABLE proposed | SOURCE | Explicit printed construction DEA:90 `return new ItemViewHolder(v);` inside onCreateChildViewHolder (row 4). Definition DEA:218-224. |
| 9 | DrawerExpandableAdapter$ItemViewHolder.bind | REACHABLE proposed | SOURCE | Explicit printed call DEA:115 `holder.bind(group, item);` inside onBindChildViewHolder (row 1). Definition DEA:226-243 (:238 group.isItemSelected(item.id) — also row 13's route). |
| 10 | DrawerGroup.<init> | REACHABLE proposed | SOURCE | UPGRADED in this pass (was INFERRED in prior proposal): explicit printed constructions in freshly fetched Utils.getNavigationDrawerItems (Utils.java:720ff — `new DrawerGroup(...)` for status, sorting, and dateAdded groups), called from MA:248-250. Definition DG:39-44 (3-arg ctor). Under a whole-route convention this would be INFERRED; label unaffected. |
| 11 | DrawerGroup.getDefaultExpandState | REACHABLE proposed | SOURCE | Explicit printed call MA:604 `if (group.getDefaultExpandState())` in applyExpandState, called from onDrawerGroupsCreated MA:599, called from initDrawer MA:252. Definition DG:65-68. |
| 12 | DrawerGroup.getSelectedItemId | REACHABLE proposed | SOURCE | Explicit printed calls MA:591, :594, :596 in onDrawerGroupsCreated (status/sorting/date-added filters). Definition DG:56-59. |
| 13 | DrawerGroup.isItemSelected | REACHABLE proposed | SOURCE | Explicit printed calls DEA:117 (click listener guard) and DEA:238 (ItemViewHolder.bind colour index). Definition DG:51-54. |
| 14 | DrawerGroup.selectItem | REACHABLE proposed | SOURCE | Explicit printed call DEA:119 `group.selectItem(item.id);` in the child click listener (DEA:116-123). Definition DG:46-49. |
| 15 | DrawerGroupItem.<init> | REACHABLE proposed | SOURCE | UPGRADED in this pass (was INFERRED in prior proposal): explicit printed constructions in freshly fetched Utils.getNavigationDrawerItems (Utils.java:720ff — `status.items.add(new DrawerGroupItem(...))` and the sorting/dateAdded equivalents), called from MA:248-250. Definition DGI:32-37 (3-arg ctor id/iconResId/name, matching the call sites). Under a whole-route convention this would be INFERRED; label unaffected. |
| 16 | EmptyTagItem.<init> | REACHABLE proposed | SOURCE | Explicit printed constructions MA:475 (Flowable.just), :498 and :509 (setInitSelection). No explicit ctor declared in ET (implicit default ctor); the `new` sites are printed, hence SOURCE. |
| 17 | EmptyTagItem.equals | REACHABLE proposed | INFERRED | R-DIFF: TA:137 `oldItem.equals(newItem)` in areContentsTheSame, run on submitList MA:485 (library DiffUtil dispatch, unprinted). Definition ET:32-34 (`this == o`). Second INFERRED trigger: TA:119 `getCurrentList().indexOf(item)` in setSelectedItem (library List.indexOf uses equals). |
| 18 | EmptyTagItem.isSame | REACHABLE proposed | SOURCE | Explicit printed call TA:262 `item.isSame(selectedItem)` in EmptyItemViewHolder.bind (row 38's method). Also R-DIFF TA:145. Definition ET:27-29 (`o instanceof EmptyTagItem`). SOURCE on the bind route. |
| 19 | NoTagsItem.<init> | REACHABLE proposed | SOURCE | Explicit printed constructions MA:476 (Flowable.just) and :501 (setInitSelection). Implicit default ctor (no ctor declared in NT), `new` sites printed, hence SOURCE. |
| 20 | NoTagsItem.equals | REACHABLE proposed | INFERRED | R-DIFF TA:137, as row 17. Definition NT:29-31 (`this == o`). Second trigger TA:119 indexOf, as row 17. |
| 21 | NoTagsItem.isSame | REACHABLE proposed | SOURCE | Explicit printed call TA:308 `item.isSame(selectedItem)` in NoTagsItemViewHolder.bind (batch 114 row 8's method). Also R-DIFF TA:145. Definition NT:24-26 (`o instanceof NoTagsItem`). |
| 22 | drawer.TagItem.<init> | REACHABLE proposed | SOURCE | Explicit printed constructor reference MA:477 `.map(TagItem::new)` in subscribeTags, and TagItem items matched at MA:515-516 / :521. Definition TI:30-32 (TagInfo ctor, field `info` TI:28). This is ui/main/drawer/TagItem, not ui/tag/TagItem. |
| 23 | drawer.TagItem.equals | REACHABLE proposed | INFERRED | **Batch-113 special item — resolved, NOT UNREACHABLE, NOT no_trigger_in_app.** R-DIFF TA:137 `oldItem.equals(newItem)` on submitList MA:485; TagItem is in the submitted list (MA:477). Definition TI:40-47 (identity, then info.equals). Second trigger TA:119 indexOf. Dispatch is library DiffUtil, hence INFERRED. Do NOT copy the ui/tag TagItem verdict from batches 119-120 — different class. |
| 24 | drawer.TagItem.isSame | REACHABLE proposed | SOURCE | Explicit printed call TA:216 `item.isSame(selectedItem)` in ItemViewHolder.bind(TagItem) (batch 114 row 2's method). Also R-DIFF TA:145 and MA:331 `item.isSame(tagsAdapter.getSelectedItem())`. Definition TI:35-37 (instanceof TagItem and info.id equality). |
| 25 | drawer.TagsAdapter.<clinit> | REACHABLE proposed | INFERRED | Static field `diffCallback` TA:130-147 is initialised at class initialisation; first printed use of the class is MA:271 `new TagsAdapter(...)`. Class-init timing is the unprinted JVM rule, hence INFERRED (same convention as other batches' <clinit> rows). |
| 26 | drawer.TagsAdapter.<init> | REACHABLE proposed | SOURCE | Explicit printed construction MA:271 `tagsAdapter = new TagsAdapter(tagsClickListener);` in initDrawer. Definition TA:52-56 (`super(diffCallback)` :53, listener field :55). |
| 27 | drawer.TagsAdapter.getItemViewType | REACHABLE proposed | INFERRED | R-TAGS: adapter set MA:272, list submitted MA:485; RecyclerView/ListAdapter dispatch to TA:104-115 (instanceof TagItem/EmptyTagItem/NoTagsItem -> TYPE constants). Dispatch library, hence INFERRED. |
| 28 | drawer.TagsAdapter.getSelectedItem | REACHABLE proposed | SOURCE | Explicit printed call MA:331 `tagsAdapter.getSelectedItem()` in the tag-menu handler. Definition TA:126-128. |
| 29 | drawer.TagsAdapter.onBindViewHolder | REACHABLE proposed | INFERRED | R-TAGS as row 27; TA:96-101 (:97 getItem(position), :99 holder.bind(item, listener)). Dispatch library, hence INFERRED. |
| 30 | drawer.TagsAdapter.onCreateViewHolder | REACHABLE proposed | INFERRED | R-TAGS as row 27; TA:60-93 (TYPE_EMPTY -> :70 new EmptyItemViewHolder, TYPE_TAG_ITEM -> :79 new ItemViewHolder, TYPE_NO_TAGS_ITEM -> :88 new NoTagsItemViewHolder). Dispatch library, hence INFERRED. |
| 31 | drawer.TagsAdapter.setSelectedItem | REACHABLE proposed | SOURCE | Explicit printed calls MA:334, :498, :501, :509, :519, and internal holder click lambdas TA:193, :250, :296. Definition TA:117-124 (:119 indexOf — also the equals trigger for rows 17/20/23). |
| 32 | drawer.TagsAdapter$1.<init> | REACHABLE proposed | INFERRED | Anonymous DiffUtil.ItemCallback subclass TA:130-147, created by the static-field initializer `diffCallback = new DiffUtil.ItemCallback...` (:130-131); it is the only anonymous class in TagsAdapter.java, so $1 = this callback (numbering by source order, NOT bytecode-verified — merger must confirm). Instantiation timing is class initialisation (row 25), hence INFERRED. |
| 33 | drawer.TagsAdapter$1.areContentsTheSame | REACHABLE proposed | INFERRED | R-DIFF: TA:133-138, called by DiffUtil on submitList MA:485 (library dispatch, unprinted). Body calls oldItem.equals (rows 17/20/23). |
| 34 | drawer.TagsAdapter$1.areItemsTheSame | REACHABLE proposed | INFERRED | R-DIFF: TA:141-146, called by DiffUtil on submitList MA:485 (library dispatch, unprinted). Body calls oldItem.isSame (rows 18/21/24). |
| 35 | drawer.TagsAdapter$AbstractViewHolder.<init> | REACHABLE proposed | SOURCE | Explicit printed `super(...)` calls in every subclass ctor: TA:171 (ItemViewHolder, super(binding.getRoot())), :230 (EmptyItemViewHolder), :275 (NoTagsItemViewHolder). Definition TA:156-158. |
| 36 | drawer.TagsAdapter$EmptyItemViewHolder.<init> | REACHABLE proposed | SOURCE | Explicit printed construction TA:70 `return new EmptyItemViewHolder(binding);` inside onCreateViewHolder (row 30, upstream INFERRED). Definition TA:229-233. |
| 37 | drawer.TagsAdapter$EmptyItemViewHolder.bind(AbstractTagItem,OnClickListener) | REACHABLE proposed | SOURCE | Explicit printed call TA:99 `holder.bind(item, listener);` in onBindViewHolder (row 29), virtual dispatch to this overload for empty items; body TA:236-243 checks `instanceof EmptyTagItem` then calls row 38's overload at :241. |
| 38 | drawer.TagsAdapter$EmptyItemViewHolder.bind(EmptyTagItem,OnClickListener) | REACHABLE proposed | SOURCE | Explicit printed call TA:241 `bind((EmptyTagItem) item, listener);` inside row 37's method. Definition TA:247-268 (:249 click listener, :262 isSame — row 18's SOURCE route). |
| 39 | drawer.TagsAdapter$EmptyItemViewHolder.lambda$bind$0 | REACHABLE proposed | INFERRED | Click-listener lambda TA:249-254 (`binding.getRoot().setOnClickListener((v) -> {...})`, body :250 setSelectedItem, :252 listener.onTagSelected). Registered in printed code but invoked by framework View click dispatch (unprinted), hence INFERRED. Lambda numbering by source order (first lambda in EmptyItemViewHolder.bind), NOT bytecode-verified. |
| 40 | drawer.TagsAdapter$ItemViewHolder.<init> | REACHABLE proposed | SOURCE | Explicit printed construction TA:79 `return new ItemViewHolder(binding);` inside onCreateViewHolder (row 30, upstream INFERRED). Definition TA:170-174. |

## OPEN rows and what would resolve them

None in this batch on the printed evidence above. The two formerly INFERRED construction rows (rows 10, 15) are now SOURCE on the fresh Utils print. All other INFERRED rows rest on standard library/framework dispatch (RecyclerView, ListAdapter/DiffUtil, View click, JVM class init) from a printed anchor (MainActivity.initDrawer / submitList), not on absence of evidence.

## Caveats restated (merger must see)

1. Strict-entry caveat: the LAUNCHER -> MainActivity step (AndroidManifest) was NOT freshly re-printed in this pass (it is cited by sibling MainActivity batches). Under a strict rule requiring every step printed, all 40 rows revert to OPEN until the manifest + MainActivity.onCreate -> initLayout chain is re-printed at merge. MainActivity.onCreate itself calls initLayout at :188 (printed in the prior copy), and initLayout calls initDrawer at :226 (printed).
2. No row is verified for merge: no build, sampler, grep, or C1 check was run (no local checkout). A merge step must re-derive every row from a full checkout, run the C1 checks, confirm anonymous/lambda numbering ($1, lambda$bind$0) against bytecode, and spot-check at least 1 in 5 citations. Build/C1: not run (Mac after push).
3. TagItem.hashCode and TagItem.toString are NOT in batch 113 and are not judged here; their absence from this file is not a verdict.
4. Undecided conventions recorded, not decided: per-row SOURCE vs whole-route INFERRED (see convention note above); strict-entry rule (caveat 1). Labels are unaffected by the confirmed_by choice.
5. No connector search_code result was used as evidence of absence. No fresh HTTP 429 was hit in this pass (the single fresh fetch, Utils.java, succeeded).
