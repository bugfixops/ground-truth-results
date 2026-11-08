# High-Value Class Coverage Tracking

## Top Priority Classes (mentioned by parent)
- **GeneralDialogCreation** (69 methods) - Dialogs utility, called from many UI contexts
- **MainActivity** (66 methods) - Core entry point, navigation hub
- **MainFragment** (54 methods) - Primary file browser fragment
- **FileUtils** (53 methods) - File operations utility
- **HybridFile** (50 methods) - Core file abstraction
- **SevenZArchiveEntry** (46 methods) - 7z library (likely heavy UNREACHABLE)
- **DataUtils** (44 methods) - Data management utility
- **Drawer** (37 methods) - Navigation drawer, makes downstream methods reachable

## Coverage Notes from Parent
- MainActivity/MainFragment/Drawer: "core entry/nav and will make many downstream methods reachable"
- SevenZArchiveEntry: "7z library class likely heavy UNREACHABLE-with-grep"

## Batch Assignment (when .py files arrive, check which classes each covers)
Batches 013-016 (Sonnet) - awaiting .py files
- label_b013.py: TBD
- label_b014.py: TBD (placeholder exists, RUNNING as of 21:39)
- label_b015.py: TBD
- label_b016.py: TBD (placeholder exists, RUNNING as of 21:39)

## Once Identified
Will report which batches cover the 8 high-priority classes so parent can prioritize next Sonnet waves.
