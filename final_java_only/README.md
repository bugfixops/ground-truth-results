# final_java_only: apps without any Kotlin source

Copied (not moved) from `../final_41`; `final_41` is unchanged. Each app folder is the full copy: `app/` (APK, instrumented source incl. JacocoInstrument, class dirs, class_files.json, DATASET.txt), `ape/`, `monkey/`, `combined/`.

**Selection rule:** no `*.kt` file anywhere under `<App>/app/` (JacocoInstrument harness excluded; build dirs excluded). Java library dependencies may still pull in Kotlin at run time; this is a statement about the app's own source only.

13 apps: Aegis, AmazeFileManager, AnkiDroid, AnyMemo, Currency, Diary, LibreTorrent, MMEX, Markor, Omni-Notes, Vanilla-Music, hash-checker, openlauncher

- in the 38-app tool run set (10): AmazeFileManager, AnyMemo, Currency, Diary, LibreTorrent, Markor, Omni-Notes, Vanilla-Music, hash-checker, openlauncher
- not in the 38-app run set (3): Aegis, AnkiDroid, MMEX (Aegis / MMEX need a manual setup, AnkiDroid needs a login; see final_41/README.md)
- near miss, NOT included: Vinyl-Music-Player (4 .kt files among 268 .java)

Tables are the final_41 tables filtered to these apps. `_fixtures/` is the full copy.
