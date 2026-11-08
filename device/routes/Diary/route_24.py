#!/usr/bin/env python3
"""Diary route_24: FileUtils.getExtension (first-start help-text path).

Method: FileUtils.getExtension
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea909ae66 Efd70ec06 Efaf4b20b
    E3a96a5f2 E0a8291a8 Eaddab195
Printed route: overnight/stream-D/Diary/scratch/route_steps.txt,
    section "FileUtils.getExtension" (verdict correct, SOURCE,
    FileUtils.java:218-219); path row 25 of graphs/Diary/verification.csv.
    Edge details: graphs/Diary/out/diary_trigger_graph.json.
Permissions (ROUTES.csv, merger-updated): WRITE_EXTERNAL_STORAGE (pre-launch SETUP grant for the help-copy gate).
Fixtures (ROUTES.csv): none.
Setup (ROUTES.csv): none.
FIRST-START REQUIREMENT: this route runs only from a cleared app.
    run_app.sh does pm clear before running this script, so Diary
    starts with no entries and an empty page: onResume copies the help
    text into the empty page (Diary.java:560-568), the text watcher
    sets changed (Diary.java:1084-1085), and markdown && changed calls
    loadMarkdown (Diary.java:567-568). Do NOT run this script against
    an app state that already holds entries: with entries present the
    help text is not copied, changed stays false, and this route is
    not reached. No typing or tapping is done here on purpose -- any
    user edit would change which text is rendered instead of the help
    text.
Route shape: launch Diary from the cleared state and let onResume run.
    loadMarkdown renders the help text (Diary.java:1353-1357, 1362,
    1376); mediaCheck finds the help text's image elements
    (Diary.java:1382-1390; assets/help.md:173-187) and calls
    FileUtils.getMimeType for each, which calls getExtension on the
    file name (FileUtils.java:216-225).
MERGER DECISION APPLIED: WRITE_EXTERNAL_STORAGE is granted pre-launch
    (see grant block below) and listed in ROUTES.csv. The help-copy gate
    at Diary.java:561-564 requires it on API 27 (the app targets SDK 28,
    build.gradle:34; the SDK < M branch does not apply on API 27); without
    it the help copy is skipped and this route is not reached.
"""

import argparse
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, _ROOT)

from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea909ae66", "Efd70ec06",
    "Efaf4b20b", "E3a96a5f2", "E0a8291a8", "Eaddab195",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Diary route_24 replay")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)

    r = Runner(args.package, "route_24", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)

    # Ee6b8aa80 -- Tap the Diary icon in the launcher
    # (MAIN/LAUNCHER intent filter, AndroidManifest.xml:52-59).
    # Realised as launching the Diary activity, the adb equivalent
    # of tapping the launcher icon. Must run from a cleared app
    # (run_app.sh pm clear) so the first-start help copy runs.
    # MERGER EDIT (pre-launch SETUP grant): the first-start help copy
    # runs during this launch's onResume and requires
    # WRITE_EXTERNAL_STORAGE on API 27 (Diary.java:561-564); granting
    # after launch would be too late. Logged under the launch edge.
    r.grant("android.permission.WRITE_EXTERNAL_STORAGE", "Ee6b8aa80")
    r.launch("org.billthefarmer.diary/.Diary", "Ee6b8aa80")

    # Edd0b9192 -- The system instantiates Diary, then onCreate
    # (Diary.java:441-443). Lifecycle edge, no user action.
    r.comment("Diary instantiated, onCreate runs", "Edd0b9192")

    # Ee63879c9 -- onStart -> onResume (Diary.java:539-541).
    # Lifecycle edge, no user action. onResume itself copies the help
    # text into the empty page (Diary.java:560-568) on this cleared
    # first start.
    r.comment("onStart to onResume; help text copied to empty page",
              "Ee63879c9")

    # Ea909ae66 -- markdown && changed: render the (help) text
    # (Diary.java:567-568). changed was set by the text watcher when
    # the help text was copied in (Diary.java:1084-1085). Internal
    # call, no user action.
    r.comment("markdown and changed, so loadMarkdown runs",
              "Ea909ae66")

    # Efd70ec06 -- loadMarkdown(textView.getText())
    # (Diary.java:1353-1357). Internal call, no user action.
    r.comment("loadMarkdown with the help text", "Efd70ec06")

    # Efaf4b20b -- markdownCheck(text) (Diary.java:1362).
    # Internal call, no user action.
    r.comment("loadMarkdown calls markdownCheck", "Efaf4b20b")

    # E3a96a5f2 -- ![..](geo:/audio/video) -> iframe/audio/video HTML
    # (Diary.java:1376). Internal call, no user action.
    r.comment("markdownCheck calls mediaCheck", "E3a96a5f2")

    # E0a8291a8 -- FileUtils.getMimeType(new File(path)) for each
    # ![title](path) (Diary.java:1382-1390; assets/help.md:173-187,
    # three image elements). Internal call, no user action.
    r.comment("mediaCheck calls getMimeType for help-text images",
              "E0a8291a8")

    # Eaddab195 -- getExtension(file.getName())
    # (FileUtils.java:216-225). Internal call, no user action.
    r.comment("getMimeType calls getExtension", "Eaddab195")

    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
