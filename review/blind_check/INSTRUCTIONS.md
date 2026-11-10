# Classify methods from the source: instructions for a blind reader

You decide, from the SOURCE CODE ONLY, which class each Android method really has. You get no labels: classify every method
from scratch. Be strict and look for hidden gates: guards (if conditions, boolean fields set only by an earlier action,
settings, menu or preference visibility or enabled state, data that must exist, a collection that is empty in the baseline, an
early return, a reflection edge) on the call chain from the app launch to the method.

## What you may open
- The app source: /Users/darshan/Desktop/yang/final_java_only/<App>/app/<project folder>/ (Java sources, AndroidManifest.xml,
  res/ layouts, menus, xml, values). <App> is in the row.
- The Android 8.1 framework source: /Users/darshan/Desktop/yang/work/fw_src/android-8.1.0_r1/
- Your chunk file and this file.

## What you must NOT open (it would spoil the blind check)
- Anything under /Users/darshan/Desktop/yang/work/graphs/, any graphs/ folder, any methods.csv, verification.csv, audit_*.csv,
  sanity_check.csv, graph_def*.py, out/ folder, scratch/ folder, device/ folder, handoff/ folder, review/ folder (except this
  file), run_result/ folder, tools/ and tools_dev/ folders;
- /Users/darshan/Desktop/yang/handoff/, /Users/darshan/Downloads/ and /Users/darshan/Documents/;
- /Users/darshan/Desktop/yang/kiro_lt, kiro_scripts, and any git clone of this project;
- any output file of another reader (another reader works on the same rows independently; never read their file).
- The class_files.json and .apk files are not needed.

## Setting (the baseline; never counts as state)
The instrumented debug build on an Android 8.1 (API 27) emulator, started from a fresh install plus the first-run setup:
Aegis: onboarding passed, and a password vault with two entries (no entry has an icon). MMEX: a database with one checking
account and nothing else. AnkiDroid: a sample deck imported. AmazeFileManager and LibreTorrent: nothing to set up.
Anything the first-run setup creates is part of the baseline. Runtime-permission prompts are GUI actions.
Intent extras that the app's own screens set are NOT env (env only when the Intent comes from outside the app).
Long press, drag, text input and rotation are GUI actions.

## Class rule: the FIRST class that applies
- dead: nothing in this build can execute it: no caller, a framework that never calls the override, or a condition that can never hold.
- config: runs only in another build or on another API level.
- env: needs something outside the app: another app or the system (picker results, shares, widgets, broadcasts), network or
  servers (a real server answering), device (camera, biometrics, SD card), time, data left by an older app version, or limits of
  the API 27 image.
- state: reachable from the GUI, but only after in-app actions create state: stored data, a file or document, a non-default
  setting, a UI session (a selection, an open dialog, an unsaved form), or an account or vault.
- library: reachable only through an edge that a library or reflection creates (EventBus, Rx, data binding, a class inflated
  from XML, Class.newInstance, generated code the app does not call explicitly).
- gui: reachable with GUI actions alone.
Best-route rule: a gate counts only if no other route avoids it. Pick the route with the fewest env gates first, then the fewest state
gates. Do not count null checks or similar guards that always hold in normal use. A guard becomes a gate only if the baseline plus
ordinary GUI actions cannot satisfy it AND no other route avoids it. A state that in-app actions can create only after an env
action (a picked file, an installed icon pack, a real server) is env, not state.

## How to work on each row
1. Find the method: jvm_class is the class path (with $ for inner classes), method the name, desc the JVM descriptor (it tells
   overloads apart). Read the method.
2. Find every caller in the app (grep). If there is no caller, check overrides called by the framework, lifecycle callbacks, XML
   (onClick, layouts, menus, manifest components), reflection, EventBus/Rx. Check that the caller itself is reachable.
3. Walk the best route from app launch (launcher activity) to the method with the GUI actions a user takes. Note the guards on the
   route (if conditions, settings, data present, dialogs) and decide for each whether it is a gate, and of which kind.
4. Decide the class with the rule above. (jvm_class may be a build-time class path; the method column is "Class.method" in the app source.)

## Output
Write a CSV (UTF-8, comma separated, quote cells that contain commas) with this header, one row per input row, to the output
path you were given:
id,class_found,dialog_dependent,confidence,route,gates,evidence,reasoning
- class_found: the class the source supports: gui, state, env, library, dead or config. Always fill it; if you really cannot decide give your best guess and set confidence to low.
- dialog_dependent: yes if your class would change when a dialog, selection or other UI session that the SAME GUI sequence opens and
  closes (tap a row, the dialog opens, tap OK) did not count as state; otherwise no.
- confidence: high, medium or low.
- route: the in-app route in a few short steps joined by " > " (screen/action names), or "none" for dead.
- gates: the gates you counted, e.g. "state: backup file; env: network", or "none".
- evidence: file:line list (source file names relative to the app project folder, or framework path).
- reasoning: at most 300 characters.
When you are done, reply with a short final message: one line per row "id | class_found | dialog_dependent | confidence".
