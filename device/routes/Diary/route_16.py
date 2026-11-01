#!/usr/bin/env python3
"""Diary device route script: route_16.

Method: FileUtils.fileProviderPath
Edge ids in order:
    E43a85cbd E2e841378 E9be312f5 E1559572d E80301e27
Printed route file: graphs/Diary/scratch route print for
    FileUtils.fileProviderPath, in
    ~/workspace/overnight/stream-D/Diary/scratch/route_steps.txt
    (section "FileUtils.fileProviderPath", verdict REACHABLE) and
    route_judgements.txt line 16 (fixed, SOURCE, FileUtils.java:602-608).
Permissions (ROUTES.csv): none.
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none (Diary row of work-emulator ci/apps.csv has an
    empty setup cell).

Route summary (from the printed route and the trigger graph): another app
opens a text file with Diary's Editor via a VIEW/EDIT text/* intent
carrying a content:// URI with no _data column; Editor.onCreate calls
resolveContent, which calls FileUtils.getPath, which falls through to
fileProviderPath.

Mapping notes:
- The Editor intent filter (AndroidManifest.xml:85-98) declares scheme
  http with mime text/*, so a content:// URI would not match it through
  the resolver. The script therefore sends an explicit intent to the
  exported Editor component; explicit intents do not need a filter
  match. This is the adb equivalent of "another app opens a text file
  with Diary's Editor" (trigger-graph edge E43a85cbd, gui text).
- The URI is Diary's own FileProvider URI (authority
  org.billthefarmer.diary.fileprovider, AndroidManifest.xml:119-127;
  filepaths.xml maps external-path/cache-path/root-path). Its query
  returns only DISPLAY_NAME and SIZE (FileProvider.java:326, 433-460),
  never a _data column, so FileUtils.getDataColumn returns null
  (FileUtils.java:436-467) and getPath falls through to fileProviderPath
  (FileUtils.java:602-608, called at FileUtils.java:603-606 in the
  content-scheme branch).
- Path segments of the chosen URI are [external, Download, todo.txt];
  fileProviderPath's external-storage branch then builds
  <external-storage>/Download/todo.txt (FileUtils.java:602-608). The
  method itself is entered whether or not that file exists; a non-null
  return additionally needs the file to exist on the device. No fixture
  is listed for this route in ROUTES.csv, so the script pushes none;
  the device lead may add the file if a non-null return is wanted.
- The provider is Diary's own, so Diary reads it under its own UID and
  no cross-app URI-permission grant is needed.
- Lifecycle and CALL edges with no user action are logged with
  r.comment, per the D3 rules.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner

PKG = "org.billthefarmer.diary"
ROUTE = "route_16"
EDGES = ["E43a85cbd", "E2e841378", "E9be312f5", "E1559572d", "E80301e27"]
# Diary's own FileProvider URI, FileProvider-style segments, no _data column.
URI = "content://org.billthefarmer.diary.fileprovider/external/Download/todo.txt"
EDITOR = "org.billthefarmer.diary/org.billthefarmer.diary.Editor"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adb", default="adb")
    a = ap.parse_args()
    r = Runner(package=a.package, route=ROUTE, edge_ids=EDGES,
               log_path=a.log, dry_run=a.dry_run, adb=a.adb,
               outdir=a.outdir)
    try:
        # E43a85cbd -- Another app opens a text file with Diary's Editor
        # (VIEW/EDIT text/*). Trigger-graph gui: "In Files open a text
        # file with Open with -> Diary". Sent as an explicit adb intent
        # to the exported Editor component (see header note on the
        # http-scheme filter quirk).
        r.start_intent(edge="E43a85cbd", action="android.intent.action.VIEW",
                       data=URI, mime="text/plain", component=EDITOR)
        # E2e841378 -- The system instantiates Editor, then onCreate
        # (theme from pref_theme, Up arrow on). No user action.
        r.comment("system instantiates Editor, then onCreate",
                  edge="E2e841378")
        # E9be312f5 -- content:// URI: uri = resolveContent(uri); file
        # stays null if it cannot be mapped (Editor.java:114-126).
        # No user action; runs inside Editor.onCreate.
        r.comment("content URI: resolveContent maps it via FileUtils.getPath",
                  edge="E9be312f5")
        # E1559572d -- path = FileUtils.getPath(this, uri); file:// URI
        # from the path (Editor.java:315-325). No user action.
        r.comment("resolveContent calls FileUtils.getPath",
                  edge="E1559572d")
        # E80301e27 -- No _data column: rebuild a path from
        # FileProvider-style segments (FileUtils.java:602-608, 290-338).
        # No user action; this is the route target.
        r.comment("no _data column: getPath falls through to fileProviderPath",
                  edge="E80301e27")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
