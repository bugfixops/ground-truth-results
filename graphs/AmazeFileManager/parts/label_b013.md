STATUS: RUNNING 21:41

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CompressedExplorerAdapter.<init> | REACHABLE | | Constructor called from CompressedExplorerFragment.createViews when fragment shows archive | SRC CompressedExplorerFragment.java:450-451 constructs adapter |
| CompressedExplorerAdapter.animate | REACHABLE | | Called from onBindViewHolder to animate items | SRC CompressedExplorerAdapter.java:191 calls animate(holder) |
| CompressedExplorerAdapter.generateZip | REACHABLE | | Called from CompressedExplorerFragment.createViews to update items | SRC CompressedExplorerFragment.java:454 calls generateZip |
| CompressedExplorerAdapter.getCheckedItemPositions | REACHABLE | | Called from action mode callback to get selected items | SRC CompressedExplorerFragment.java:297,309,324,326 calls getCheckedItemPositions |
| CompressedExplorerAdapter.getItemCount | REACHABLE | | RecyclerView.Adapter method called by RecyclerView framework | SRC CompressedExplorerAdapter.java:299 overrides framework method; androidx library INFERRED source not read |
| CompressedExplorerAdapter.getItemId | REACHABLE | | RecyclerView.Adapter method called by RecyclerView framework when stable IDs enabled | SRC CompressedExplorerAdapter.java:159 overrides framework method; androidx library INFERRED source not read |
| CompressedExplorerAdapter.getItemViewType | REACHABLE | | RecyclerView.Adapter method called by RecyclerView framework | SRC CompressedExplorerAdapter.java:164 overrides framework method; androidx library INFERRED source not read |
| CompressedExplorerAdapter.isPositionHeader | UNREACHABLE | no_trigger_in_app | Always returns false, never actually used for headers | SRC CompressedExplorerAdapter.java:327-328 returns false; TODO comment indicates incomplete |
| CompressedExplorerAdapter.lambda$onBindViewHolder$0 | REACHABLE | | Lambda for rl.setOnLongClickListener in onBindViewHolder | SRC CompressedExplorerAdapter.java:236 sets listener |
| CompressedExplorerAdapter.lambda$onBindViewHolder$1 | REACHABLE | | Lambda for genericIcon.setOnClickListener in onBindViewHolder | SRC CompressedExplorerAdapter.java:242 sets listener |
| CompressedExplorerAdapter.lambda$onBindViewHolder$2 | REACHABLE | | Lambda for rl.setOnClickListener in onBindViewHolder | SRC CompressedExplorerAdapter.java:262 sets listener |
| CompressedExplorerAdapter.onBindViewHolder | REACHABLE | | RecyclerView.Adapter method called by RecyclerView framework to bind data | SRC CompressedExplorerAdapter.java:189 overrides framework method; androidx library INFERRED source not read |
| CompressedExplorerAdapter.onCreateViewHolder | REACHABLE | | RecyclerView.Adapter method called by RecyclerView framework to create views | SRC CompressedExplorerAdapter.java:172 overrides framework method; androidx library INFERRED source not read |
| CompressedExplorerAdapter.onFailedToRecycleView | REACHABLE | | RecyclerView.Adapter method called by RecyclerView framework on recycle failure | SRC CompressedExplorerAdapter.java:321 overrides framework method; androidx library INFERRED source not read |
| CompressedExplorerAdapter.onViewAttachedToWindow | REACHABLE | | RecyclerView.Adapter method called by RecyclerView framework when view attached | SRC CompressedExplorerAdapter.java:311 overrides framework method; androidx library INFERRED source not read |
| CompressedExplorerAdapter.onViewDetachedFromWindow | REACHABLE | | RecyclerView.Adapter method called by RecyclerView framework when view detached | SRC CompressedExplorerAdapter.java:304 overrides framework method; androidx library INFERRED source not read |
| CompressedExplorerAdapter.toggleChecked | REACHABLE | | Called from action mode callback to toggle all items | SRC CompressedExplorerFragment.java:311,339 calls toggleChecked(boolean) |
| CompressedExplorerAdapter.toggleChecked | REACHABLE | | Called from lambda listeners and within adapter | SRC CompressedExplorerAdapter.java:238,244,267 calls toggleChecked(int,ImageView) |

STATUS: DONE 21:43
