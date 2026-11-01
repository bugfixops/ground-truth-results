# Stream A Phase 2 spot-check — batch 113

Source re-derived from already-fetched local copies only
(`~/workspace/b113-114-src/` and `~/workspace/b113-114-src-fresh/Utils.java`);
no connector fetch was needed, no 429 hit. The merge-ready file was NOT
edited; no label was changed here.
Phase 1 label changes: none listed (the only change vs the prior proposal
was confirmed_by, not label: rows 10 and 15 INFERRED -> SOURCE on the
fresh Utils print). Checked set: sample rows 1, 6, 11, 16, 21, 26, 31, 36
PLUS rows 10 and 15 (the confirmed_by-change rows).

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | DrawerExpandableAdapter.onBindChildViewHolder | REACHABLE / INFERRED | PASS | Body DrawerExpandableAdapter.java:105-124 (`holder.bind(group, item)` :115, click listener :116-123); adapter set on RecyclerView at MainActivity.java:255 and manager attached at :259; dispatch is library, hence INFERRED. |
| 6 | DrawerExpandableAdapter$GroupViewHolder.\<init\> | REACHABLE / SOURCE | PASS | Printed construction DrawerExpandableAdapter.java:80 `new GroupViewHolder(v)`; definition :196-201. |
| 10 | DrawerGroup.\<init\> | REACHABLE / SOURCE | PASS | Fresh Utils print verified: `getNavigationDrawerItems` at Utils.java:720; `new DrawerGroup(...)` at :726 (status), :732 (sorting), :739 (dateAdded); called from MainActivity.java:248. Definition DrawerGroup.java:39-44 (3-arg ctor). The INFERRED -> SOURCE upgrade stands. |
| 11 | DrawerGroup.getDefaultExpandState | REACHABLE / SOURCE | PASS | MainActivity.java:604 `if (group.getDefaultExpandState())`; definition DrawerGroup.java:65-68. |
| 15 | DrawerGroupItem.\<init\> | REACHABLE / SOURCE | PASS | Fresh Utils print verified: `status.items.add(new DrawerGroupItem(...))` at Utils.java:745 and sorting/dateAdded equivalents from :757 onward; called from MainActivity.java:248. Definition DrawerGroupItem.java:32-37 (3-arg ctor). The INFERRED -> SOURCE upgrade stands. |
| 16 | EmptyTagItem.\<init\> | REACHABLE / SOURCE | PASS | Printed constructions MainActivity.java:475, :498, :509 (implicit default ctor; EmptyTagItem.java declares no explicit ctor). |
| 21 | NoTagsItem.isSame | REACHABLE / SOURCE | PASS | Printed call TagsAdapter.java:308 `item.isSame(selectedItem)` in NoTagsItemViewHolder.bind; definition NoTagsItem.java:24-26. Also the DiffUtil route TagsAdapter.java:145. |
| 26 | drawer.TagsAdapter.\<init\> | REACHABLE / SOURCE | PASS | MainActivity.java:271 `new TagsAdapter(tagsClickListener)`; definition TagsAdapter.java:52-56 (`super(diffCallback)` :53). |
| 31 | drawer.TagsAdapter.setSelectedItem | REACHABLE / SOURCE | PASS | Printed calls MainActivity.java:334, :498, :501, :509, :519 and holder click lambdas TagsAdapter.java:193, :250, :296; definition TagsAdapter.java:117-124. |
| 36 | drawer.TagsAdapter$EmptyItemViewHolder.\<init\> | REACHABLE / SOURCE | PASS | Printed construction TagsAdapter.java:70 `new EmptyItemViewHolder(binding)`; definition :229-233. |

## Totals

- Checked: 10 rows. PASS: 10. FAIL: 0.
- Proposed corrections: none.

## Notes

- Build/sampler/C1: not run (not this task).
