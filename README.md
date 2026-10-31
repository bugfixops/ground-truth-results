# ground-truth-results: full work (branch work-2026-10-31)

Full working copy for finishing the schema 2 trigger graphs of 13 Android apps (ICST 2027).

Start with handoff/MUSE_HANDOVER.md. It has the state of each app, the rules, and the work packages in order.

Included: graphs/<app>/ (graph_def.py, out/ final outputs, AGENT_NOTES.md, scratch/), final_java_only/ (app source and method lists, without APKs), fw_src/ (AOSP 8.1.0_r1 framework source for citations), tools/, handoff/.

Not included, on purpose: APK and zip files, build folders, Gradle caches, tool coverage reports (monkey, ape, combined), graph backups, archive/, local.properties files, one AmazeFileManager test file with a key block, and the run lock and stop files.

Rules: tool coverage is never evidence for a label. Do not push to any other repository without the user's instruction. Device replay (handoff/NEXT_DEVICE_REPLAY.md) starts only after the user says go.
