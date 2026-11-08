# AmazeFileManager Merge Status

## Current Build Stats (after label_b002, b004, c2-c4 + fixes)
- **Methods total**: 2981
- **REACHABLE**: 806 (27.0%)
- **UNREACHABLE**: 203 (6.8%)
- **UNRESOLVED**: 1972 (66.2%)
- **Edges**: 6548
- **Contradictions**: 0 ✓
- **Invalid edge kinds**: 0 ✓

## Parts Merged
✓ label_c1 (original)
✓ label_b001_norm
✓ label_b003_norm
✓ label_b005_norm
✓ label_b006_norm
✓ label_b007_norm
✓ label_b008_norm
✓ label_b009
✓ label_b010
✓ label_b011
✓ label_b012
✓ label_b002 (manual merge with dict conversion)
✓ label_b004 (manual merge)
✓ label_c2 (manual merge)
✓ label_c3 (manual merge)
✓ label_c4 (manual merge)

## Fixes Applied
✓ AppConfig contradictions resolved (11 methods: removed incorrect UNREACHABLE, added proper routes)
✓ Edge kind normalization (ENTRY_POINT→CALL, CALLS→CALL, FW→FRAMEWORK, UI→EXPLICIT)

## Remaining Work

### Unlabeled Methods: 1972 (66.2%)
Across **362 classes**

### Top 50 Unlabeled Classes:
1. GeneralDialogCreation: 69
2. MainActivity: 66
3. MainFragment: 54
4. FileUtils: 53
5. HybridFile: 50
6. SevenZArchiveEntry: 46
7. DataUtils: 44
8. Drawer: 37
9. SevenZOutputFile: 34
10. FtpServerFragment: 34
11. UtilsHandler: 33
12. MainActivityHelper: 28
13. RecyclerAdapter: 27
14. SevenZFile: 26
15. Indicator: 26
16. FileUtil: 25
17. HybridFileParcelable: 24
18. CompressedExplorerFragment: 23
19. TextEditorActivity: 21
20. SftpConnectDialog: 21
21. LoadFilesListTask: 18
22. RootHelper: 18
23. FastScroller: 18
24. CryptUtil: 18
25. CompressedExplorerAdapter: 17
26. ProgressHandler: 16
27. PrepareCopyTask: 15
28. SearchAsyncTask: 15
29. ExtractService: 15
30. RootUtils: 15
31. Utils: 15
32. FtpService: 14
33. CompressedHelper: 14
34. CopyService: 13
35. DecryptService: 13
36. SshClientUtils: 13
37. SshConnectionPool: 13
38. TabFragment: 13
39. FoldersPref: 13
40. PrefFrag: 13
41. PreferencesActivity: 12
42. EncryptService: 12
43. ZipService: 12
44. ProcessViewerFragment: 12
45. HiddenAdapter: 11
46. MediaStoreHack: 11
47. SmbConnectDialog: 11
48. GlideRequest: 10
49. PemToKeyPairTask: 10
50. ColorPreferenceHelper: 10

### Class Categories for Next Batches:
- **Core Activities** (152 methods): MainActivity(66), TextEditorActivity(21), PreferencesActivity(12), DatabaseViewerActivity(TBD)
- **Fragments** (120 methods): MainFragment(54), FtpServerFragment(34), CompressedExplorerFragment(23), TabFragment(13), ProcessViewerFragment(12)
- **Dialogs** (91 methods): GeneralDialogCreation(69), SftpConnectDialog(21), SmbConnectDialog(11)
- **File Operations** (153 methods): FileUtils(53), HybridFile(50), FileUtil(25), HybridFileParcelable(24)
- **Services** (67 methods): ExtractService(15), FtpService(14), CopyService(13), DecryptService(13), EncryptService(12), ZipService(12)
- **Adapters** (55 methods): RecyclerAdapter(27), CompressedExplorerAdapter(17), HiddenAdapter(11)
- **Utilities** (105 methods): DataUtils(44), UtilsHandler(33), MainActivityHelper(28)
- **7z Library** (106 methods): SevenZArchiveEntry(46), SevenZOutputFile(34), SevenZFile(26)
- **UI Components** (81 methods): Drawer(37), Indicator(26), FastScroller(18)

## Notes for Next Wave
- All merged parts passed C1 validation (syntax, build) except contradictions which are now fixed
- No STALE routes (route verification hasn't started - requires UNRESOLVED=0 first)
- Edge evidence mix: SRC(6387), INFERRED(121), FW-SRC(40)
- Label confirmation: INFERRED(2619), SOURCE(362)
- Path status: UNCHECKED(2778) - sample draw waits for UNRESOLVED=0 per C6

## Suggested Next Batches (for Haiku helpers)
1. **Batch 013**: GeneralDialogCreation + MainActivity methods (135 methods)
2. **Batch 014**: MainFragment + FileUtils (107 methods)
3. **Batch 015**: HybridFile + SevenZArchiveEntry (96 methods)
4. **Batch 016**: DataUtils + Drawer + FtpServerFragment (115 methods)
5. **Batch 017**: Services group (ExtractService, FtpService, CopyService, DecryptService) (55 methods)
6. **Batch 018**: SevenZOutputFile + SevenZFile + UtilsHandler (93 methods)
7. **Batch 019**: Adapters + UI components (RecyclerAdapter, CompressedExplorerAdapter, Indicator, FastScroller) (88 methods)
8. **Batch 020**: Remaining fragments + dialogs (TextEditorActivity, CompressedExplorerFragment, SftpConnectDialog) (65 methods)

Total in suggested batches: ~754 methods
Remaining after: ~1218 methods (would need ~6-8 more batch waves)
