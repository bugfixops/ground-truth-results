# G2-2 route check: AMApplication.getCurrentApplicationContext

- Method: AMApplication.getCurrentApplicationContext
- Label: REACHABLE
- Steps: 22; checked: 22 (every step read in the source)
- Verdict: WRONG (3 wrong steps: 11, 17, 20). The chain is an export chain that ends in an importer, which the code cannot do. The real route is the SuperMemo import through the Misc tab picker.

## Why the route is wrong
- Steps 11-19 run ConverterFragment, which is used only for the six EXPORT buttons (MiscTabFragment.java:290-337). Its converter class comes from the arguments set at those buttons (ConverterFragment.java:69). Every exporter has a non-"db" dest extension (CSVExporter "csv", MnemosyneXMLExporter "xml", QATxtExporter "txt", ZipExporter "zip", Mnemosyne2CardsExporter "cards").
- The import buttons never open ConverterFragment. importSupermemoButton calls launchImportConvert(SupermemoXMLImporter.class) (MiscTabFragment.java:269-270, 408-413), which opens the picker. The result comes back to onActivityResult (MiscTabFragment.java:425-427), then invokeImportConversion starts ConvertIntentService with the importer class and the picker's content:// URI (MiscTabFragment.java:466-478).

## Wrong steps

**Step 11. MiscTabFragment.onClick -> S_DLG_CONVERTER (ENTERS, needs_state=NEED_DECK)**
- The edge is a correct export edge (the six export buttons, MiscTabFragment.java:290-337; graph_def.py:1391). It is wrong as the first step of this route: the export dialog never leads to SuperMemo import. The import starts at importSupermemoButton (MiscTabFragment.java:269-270), then launchImportConvert (408-413), then the picker (graph_def.py:1387).
- Fix: no change on this edge. The route is wrong because the export chain reaches the importer class (step 20). After the step 17 and step 20 fixes, the build must pick the picker path (launchImportConvert -> S_EXT_PICKER -> MiscTabFragment.onActivityResult, graph_def.py:1405 -> invokeImportConversion -> ConvertIntentService.onCreate, graph_def.py:1078). The export edge at graph_def.py:1391 stays for the exporters.

**Step 17. ConverterFragment.startConversion -> ConverterFragment.invokeConverterService (CALL, "Direct call", no guard)**
- Source ConverterFragment.java:121-125: `} else { amFileUtil.deleteDbSafe(outputPath); invokeConverterService(inputPath, outputPath, null); }`, inside `if (converter.getDestExtension().equals("db"))` (line ~97) and `if (new File(outputPath).exists())` is false.
- Missing guard: `converter.getDestExtension() == "db"` AND the output file does not exist. Exporters (dest not db) never reach line 125: they go to the save picker (ConverterFragment.java:127-134) and call invokeConverterService from onActivityResult (line 142; graph_def.py:1073 has that edge).
- Fix (graph_def.py): add GATE entry for `('ConverterFragment.startConversion', 'ConverterFragment.invokeConverterService')` with guard `'destination extension is db and the output file does not exist (ConverterFragment.java:97-125); exporters use the save picker (127-142)'`. The auto edge itself is generated, so the GATE dict (graph_def.py:2769 onward) is the place. Note: the route builder ignores guards, so this text alone does not remove the path; see the step 20 fix.

**Step 20. ConvertIntentService.onHandleIntent -> SupermemoXMLImporter.convert (CALL, "Virtual/interface call", no guard)**
- Source ConvertIntentService.java:113-115: `Class<Converter> converterClass = (Class<Converter>) intent.getSerializableExtra(EXTRA_CONVERTER_CLASS); Converter converter = converterMap.get(converterClass);` then line 125 `converter.convert(finalInputFilePath, finalOutputFilePath);`. The callee is chosen by the intent extra, so this edge needs the class to be SupermemoXMLImporter. On the export path the class is an exporter (ConverterFragment.java:155).
- The route builder ignores guards, so a guard text does not stop the path. The fix is a split by caller, the recipe's pattern: `ConvertIntentService.onHandleIntent@IMPORT` (entered from MiscTabFragment.invokeImportConversion, graph_def.py:1078 and the onCreate -> onHandleIntent edge) and `onHandleIntent@EXPORT` (entered from ConverterFragment.invokeConverterService, graph_def.py:1079). Add `sup((ConvertIntentService.onHandleIntent, <each converter>.convert))` for the plain pairs; then one hand edge per variant to its own converter classes (importers from @IMPORT, exporters from @EXPORT). Guard text for the import variant: `EXTRA_CONVERTER_CLASS is a chained importer (MiscTabFragment.java:472)`.
- Data origin for the import variant: the picker gives a content:// URI (EXTRA_INPUT_URI); onHandleIntent copies it to a cache file (ConvertIntentService.java:88-98) and returns early if the copy fails (line 97). Add this as a guard on the import variant.

## Steps checked as OK (as edges)
1-8 same as G2-1 steps 1-8 (manifest, lifecycle, bottom-nav cold start, Misc tab tap; guard itemId == misc_tab_menu at AnyMemo.java:249-250 matches). 9 MiscTabFragment.onCreateView lifecycle (INFERRED FragmentManager). 10 onCreateView -> onClick (listeners set at MiscTabFragment.java:156-168). 12 S_DLG_CONVERTER -> ConverterFragment view (valid for an export). 13-14 row click at 514-519. 15 openFile@CONVERTER -> ConverterFragment$1 (FileBrowserFragment.java:412-414; listener set in ConverterFragment onCreate, line 68). 16 ConverterFragment$1 -> startConversion (74-76). 18 invokeConverterService -> ConvertIntentService.onCreate (startService, ConverterFragment.java:162). 19 onCreate -> onHandleIntent: FW-SRC `core/java/android/app/IntentService.java:76` (ServiceHandler calls onHandleIntent) and `:126-130` (onStart posts the message). The graph cites ActivityThread.java with no lines: the citation should name IntentService.java. 21 SupermemoXMLImporter.convert -> getHelper(String) at SupermemoXMLImporter.java:89 (no guard on the path). 22 getHelper(String) -> AMApplication.getCurrentApplicationContext at AnyMemoDBOpenHelperManager.java:46 (unconditional).

## Cold start / state
- AMApplication.onCreate sets the static context (AMApplication.java:65) before any activity or service runs in the process, so the getter is safe on every route that starts from the app entry. No extra STATE needed.

## Not checked
- The converterMap contents (Dagger map) and whether the auto edges from onHandleIntent go to every converter's convert (the route shows one).
- RxJava / SAX parser behaviour inside SupermemoXMLImporter.convert (INFERRED only as the parse call, not read in the framework).
