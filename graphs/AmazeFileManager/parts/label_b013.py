# ---- Helper batch_013 label part (2026-10-27)
# CompressedExplorerAdapter - RecyclerView adapter for archive file browser

# Constructor - called when fragment creates adapter
e('CompressedExplorerFragment.createViews', 'CompressedExplorerAdapter.<init>', 'CONSTRUCTED',
  'Fragment creates adapter to display archive contents',
  evidence='SRC CompressedExplorerFragment.java:450-451 new CompressedExplorerAdapter(...)')

# Adapter set on RecyclerView
e('CompressedExplorerFragment.createViews', 'RecyclerView.setAdapter', 'CALL',
  'Fragment sets adapter on RecyclerView',
  evidence='SRC CompressedExplorerFragment.java:452 listView.setAdapter(compressedExplorerAdapter)')

# RecyclerView framework calls to adapter lifecycle methods
e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onCreateViewHolder', 'FRAMEWORK',
  'RecyclerView framework calls onCreateViewHolder to create view holders',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView framework calls onBindViewHolder to bind data to views',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.getItemCount', 'FRAMEWORK',
  'RecyclerView framework calls getItemCount to determine adapter size',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.getItemViewType', 'FRAMEWORK',
  'RecyclerView framework calls getItemViewType to determine view type',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.getItemId', 'FRAMEWORK',
  'RecyclerView framework calls getItemId when stable IDs enabled',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract with setHasStableIds(true), source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onViewAttachedToWindow', 'FRAMEWORK',
  'RecyclerView framework calls onViewAttachedToWindow when view attached',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter lifecycle, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onViewDetachedFromWindow', 'FRAMEWORK',
  'RecyclerView framework calls onViewDetachedFromWindow when view detached',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter lifecycle, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onFailedToRecycleView', 'FRAMEWORK',
  'RecyclerView framework calls onFailedToRecycleView on recycle failure',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter lifecycle, source not read')

# Adapter internal method calls
e('CompressedExplorerAdapter.onBindViewHolder', 'CompressedExplorerAdapter.animate', 'CALL',
  'onBindViewHolder animates view holder if animation not stopped',
  evidence='SRC CompressedExplorerAdapter.java:190-191 if (!stoppedAnimation) animate(holder)')

e('CompressedExplorerAdapter.getItemViewType', 'CompressedExplorerAdapter.isPositionHeader', 'CALL',
  'getItemViewType checks if position is header',
  evidence='SRC CompressedExplorerAdapter.java:164 if (isPositionHeader(position))')

# Lambda method routes - onBindViewHolder sets up click listeners
e('CompressedExplorerAdapter.onBindViewHolder', 'CompressedExplorerAdapter.lambda$onBindViewHolder$0', 'ASYNC',
  'onBindViewHolder sets long click listener on row layout',
  evidence='SRC CompressedExplorerAdapter.java:236 holder.rl.setOnLongClickListener(view -> {...})')

e('CompressedExplorerAdapter.lambda$onBindViewHolder$0', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Lambda calls toggleChecked(int,ImageView) on long press',
  evidence='SRC CompressedExplorerAdapter.java:238 toggleChecked(position, holder.checkImageView)')

e('CompressedExplorerAdapter.onBindViewHolder', 'CompressedExplorerAdapter.lambda$onBindViewHolder$1', 'ASYNC',
  'onBindViewHolder sets click listener on generic icon',
  evidence='SRC CompressedExplorerAdapter.java:242 holder.genericIcon.setOnClickListener(view -> {...})')

e('CompressedExplorerAdapter.lambda$onBindViewHolder$1', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Lambda calls toggleChecked(int,ImageView) when icon clicked',
  evidence='SRC CompressedExplorerAdapter.java:244 toggleChecked(position, holder.checkImageView)')

e('CompressedExplorerAdapter.onBindViewHolder', 'CompressedExplorerAdapter.lambda$onBindViewHolder$2', 'ASYNC',
  'onBindViewHolder sets click listener on row layout',
  evidence='SRC CompressedExplorerAdapter.java:262 holder.rl.setOnClickListener(p1 -> {...})')

e('CompressedExplorerAdapter.lambda$onBindViewHolder$2', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Lambda calls toggleChecked(int,ImageView) in selection mode',
  evidence='SRC CompressedExplorerAdapter.java:267 toggleChecked(position, holder.checkImageView)')

# Calls from fragment to adapter methods
e('CompressedExplorerFragment.createViews', 'CompressedExplorerAdapter.generateZip', 'CALL',
  'Fragment calls generateZip to update adapter items',
  evidence='SRC CompressedExplorerFragment.java:454 compressedExplorerAdapter.generateZip(items)')

e('CompressedExplorerFragment$1.onPrepareActionMode', 'CompressedExplorerAdapter.getCheckedItemPositions', 'CALL',
  'Action mode callback gets checked positions to update UI',
  evidence='SRC CompressedExplorerFragment.java:297 compressedExplorerAdapter.getCheckedItemPositions()')

e('CompressedExplorerFragment$1.onActionItemClicked', 'CompressedExplorerAdapter.getCheckedItemPositions', 'CALL',
  'Action mode callback gets checked positions for select all action',
  evidence='SRC CompressedExplorerFragment.java:309 compressedExplorerAdapter.getCheckedItemPositions()')

e('CompressedExplorerFragment$1.onActionItemClicked', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Action mode callback toggles selection state',
  evidence='SRC CompressedExplorerFragment.java:311 compressedExplorerAdapter.toggleChecked(shouldDeselectAll)')

e('CompressedExplorerFragment$1.onDestroyActionMode', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Action mode callback clears selection when action mode destroyed',
  evidence='SRC CompressedExplorerFragment.java:339 compressedExplorerAdapter.toggleChecked(false)')

# UNREACHABLE methods
UNREACHABLE['CompressedExplorerAdapter.isPositionHeader'] = (
    'no_trigger_in_app',
    'Always returns false with TODO comment, header functionality incomplete',
    'SRC CompressedExplorerAdapter.java:327-328 return false; // TODO:',
    'SOURCE'
)
