# conflicts_001 (LABEL helper, AnkiDroid batch 001)

## Ownership convention used in this batch
- An edge is written by the part whose batch holds its source method.
- For an S_ENTRY, framework or library source with no app node, the part holding the destination writes the edge. This batch wrote three such edges (S_ENTRY -> AnkiDroidApp.<init>, S_ENTRY -> IntentHandler.<init>, S_ENTRY -> AnkiDroidApp.onConfigurationChanged). Not yet recorded in any shared file; the lead should confirm.
- Exception, directed by the coordinator: the edge IntentHandler$1.<init> -> IntentHandler$1.onPositive (FRAMEWORK) is written here even though its source is an app node. Its owner is unknown (see below).

## Edges written here outside the S_ENTRY convention
- IntentHandler$1.<init> -> IntentHandler$1.onPositive, kind FRAMEWORK. The first pass had kind REGISTER. The coordinator changed it to FRAMEWORK because the reachability builder does not follow REGISTER edges, so REGISTER would leave onPositive unreachable. The source IntentHandler$1.<init> is the anonymous ButtonCallback creation at IntentHandler.java:118. It is not listed in any scratch/batches/*.txt file (a grep for IntentHandler$1 matches only batch_001.txt, which lists onPositive). Owner unknown; the lead should confirm.

## Edges not written here
- Edges between methods of this batch other than the one above. Routes such as IntentHandler.onCreate -> DeckPicker and DeckPicker.sync -> Connection.sync pass through nodes owned by other batches. Those edges are written by the batches that hold their sources.

## Overlap with graph_def.py
- graph_def.py already has S_ENTRY -> IntentHandler.onCreate (ENTRY, lines 138 and 140) and S_ENTRY -> AnkiDroidApp.onCreate (ENTRY, line 142). This batch adds S_ENTRY -> IntentHandler.<init> and S_ENTRY -> AnkiDroidApp.<init> (FRAMEWORK), which give the constructors their only incoming edge. They do not duplicate the onCreate edges. The lead should confirm.

## Build type
- The dataset APK is the debug build (final_java_only/AnkiDroid/app/DATASET.txt, apk line). So BuildConfig.DEBUG is true, the debug-branch plant at line 157 runs, and the release-branch plant at AnkiDroidApp.java:166 never runs.
- The eight AnkiDroidApp$ProductionCrashReportingTree methods (createTag, e, formatString, i, w, with both overloads) are therefore UNREACHABLE, kind closed_by_configuration, confirmed_by SOURCE, with source SRC com/ichi2/anki/AnkiDroidApp.java:155-166. This replaces the earlier release-build reasoning.

## Missing gates
- System configuration change: the edge S_ENTRY -> AnkiDroidApp.onConfigurationChanged now uses env=ENV_CONFIG_CHANGE, with note "NEW CONST ENV_CONFIG_CHANGE". The coordinator adds the constant at merge.
- Other conditions named in row reasons without a gate constant: tablet layout (mFragmented, DeckPicker), malformed sentExceptionReports pref (state), storage permission and StorageAccessException (AnkiDroidApp.onCreate).

## Screens
- IntentHandler and NavigationDrawerActivity have no S_ page in graph_def.py SCREENS. Routes through them are written in reasons only.

## Coverage-file disclosure
- I printed the first 1500 bytes of graphs/AnkiDroid/scratch/build_001.txt by mistake while looking for conventions. It contains tool-coverage sanity-check lines. Those lines were not used as evidence for any row. No other coverage file was opened.
