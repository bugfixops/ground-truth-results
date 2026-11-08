"""Diary route_09: Diary$FindTask.lambda$onPostExecute$0.

Method: Diary$FindTask.lambda$onPostExecute$0
Edge ids, in route order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E1b4e3a4b
    E5f3770ba E0eebf4dd Eb360afa9 Edf2bd842 E129c3852 E1999f783
    E03d355a9
Printed route file: overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary$FindTask.lambda$onPostExecute$0", ref
    Diary.java:3302-3306).
Permissions (ROUTES.csv, merger-updated): WRITE_EXTERNAL_STORAGE;READ_EXTERNAL_STORAGE (SETUP grants for saving/reading entries).
Fixtures: none (ROUTES.csv fixtures column empty).
Setup: none from ROUTES.csv (setup column empty); the STATE data
    the route needs is established by this script itself (see below),
    not by a fixture: ROUTES.csv state_kinds is "data" with the gate
    "a saved entry contains the text that is searched for" (edge
    E1999f783, guard "at least one match").
STATE ESTABLISHED BY THIS SCRIPT: before searching, the script
    saves an entry whose only line is the search word "porcupine"
    (Edit button res/layout/main.xml @+id/edit, text field @+id/text,
    Accept button @+id/accept; accept saves, Diary.java:992-1010).
    The search then has exactly one match, so onPostExecute sets the
    result click handler (Diary.java:3285-3288) that the target
    lambda hangs off.
Standard configuration: run_app.sh clears the package before this
    script; no permissions are granted and no fixtures pushed.

Mapping notes:
- Launcher tap (Ee6b8aa80) is driven as am start via r.launch: the
  harness has no launcher-UI action, and starting the MAIN/LAUNCHER
  activity is the adb equivalent (AndroidManifest.xml:52-59).
- Setup actions are logged under the first edge (Ee6b8aa80) and
  marked STATE SETUP; they are not route steps, but every harness
  action needs an edge id of the route.
- The Search (magnifier) action-bar item is tapped by content
  description "Search...": the item is showAsAction="ifRoom" with a
  SearchView action view (res/menu/main.xml, Diary.java:637-638),
  so it is an icon, not overflow text. If the emulator's SearchView
  button description differs, this is the selector to adjust.
- "Find all..." is visible only while the SearchView is expanded
  (Diary.java:649-650), which is why the search is expanded before
  opening the overflow menu for it.
- The search text field is the SearchView's internal
  search_src_text view; the harness res_id matcher accepts the
  trailing segment, so res_id="search_src_text" matches it.
- The result row text is built by FindTask (Diary.java:3241-3265)
  as DateFormat.MEDIUM of the entry date + two spaces + the matched
  line. With the setup entry saved today and its single line
  "porcupine", the row is e.g. "1 November 2026  porcupine" under
  the AOSP default en-US locale; the script computes that string
  from the host clock, assuming the emulator clock and locale match
  it (the CI emulator default). If the locale differs, the date
  part is the step to adjust.
- The target lambda runs via searchView.postDelayed(..., 256 ms)
  (Diary.java:3302-3306). After tapping the result, the script
  takes a UI dump under the target edge: live, the dump gives the
  256 ms delay time to elapse before run_app.sh takes its coverage
  dump; in dry mode it is only a planned command.
"""

import argparse
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner

COMPONENT = "org.billthefarmer.diary/org.billthefarmer.diary.Diary"
SETUP_EDGE = "Ee6b8aa80"
SEARCH_WORD = "porcupine"

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
    "E1b4e3a4b", "E5f3770ba", "E0eebf4dd", "Eb360afa9", "Edf2bd842",
    "E129c3852", "E1999f783", "E03d355a9",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(args.package, "route_09", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    try:
        # Ee6b8aa80 -- Tap the Diary icon in the launcher
        # (MAIN/LAUNCHER intent filter). Driven as am start.
        r.launch(COMPONENT, "Ee6b8aa80")

        # MERGER EDIT (SETUP grants): Diary.save() returns early without
        # WRITE_EXTERNAL_STORAGE (Diary.java:2248-2265); entry reads on
        # shared storage need READ_EXTERNAL_STORAGE. Granted before any
        # setup save so the setup entries persist. Logged under Ee6b8aa80.
        r.grant("android.permission.WRITE_EXTERNAL_STORAGE", "Ee6b8aa80")
        r.grant("android.permission.READ_EXTERNAL_STORAGE", "Ee6b8aa80")

        # STATE SETUP (not a route step; logged under Ee6b8aa80):
        # save an entry containing the search word.
        r.tap(SETUP_EDGE, res_id="edit")
        r.tap(SETUP_EDGE, res_id="text")
        r.type_text(SEARCH_WORD, SETUP_EDGE)
        r.tap(SETUP_EDGE, res_id="accept")

        # Edd0b9192 -- The system instantiates Diary, then onCreate.
        # Lifecycle edge: no user action (already launched above).
        r.comment("system instantiates Diary, then onCreate", "Edd0b9192")

        # Ee63879c9 -- onStart -> onResume. Lifecycle edge: no action.
        r.comment("onStart -> onResume", "Ee63879c9")

        # Ea885d6f1 -- Diary visible with the MarkdownView.
        # Page arrival: wait for the MarkdownView (res/layout/main.xml
        # @+id/markdown).
        r.wait_for("Ea885d6f1", res_id="markdown")

        # E002e1746 -- Tap an action bar icon or an item under More
        # options. Here: the Search (magnifier) action-bar icon.
        r.tap("E002e1746", desc="Search\u2026")

        # E1b4e3a4b -- R.id.search falls to default (super returns
        # false); the menu then expands the SearchView in the action
        # bar (Diary.java:716-718; res/menu/main.xml:63-67). The
        # expansion follows from the previous tap; focus the search
        # field and type the query (findAll reads it, Diary.java:
        # 1778-1780).
        r.tap("E1b4e3a4b", res_id="search_src_text")
        r.type_text(SEARCH_WORD, "E1b4e3a4b")

        # E5f3770ba -- Tap an action bar icon or an item under More
        # options. Open the overflow menu (Find all lives there).
        r.tap("E5f3770ba", desc="More options")

        # E0eebf4dd -- switch case R.id.findAll (Diary.java:687-688).
        r.tap("E0eebf4dd", text="Find all\u2026")

        # Eb360afa9 -- execute -> doInBackground(query) on a worker
        # thread (Diary.java:1780). Async edge: no user action.
        r.comment("FindTask execute -> doInBackground(query)",
                  "Eb360afa9")

        # Edf2bd842 -- onPostExecute(matches) on the main thread
        # (Diary.java:3268). Async edge: no user action.
        r.comment("onPostExecute(matches) on main thread", "Edf2bd842")

        # E129c3852 -- builder.show(): result list (or an empty list)
        # with Cancel (Diary.java:3274-3316). Wait for the Cancel
        # button, which proves the dialog is shown.
        r.wait_for("E129c3852", text="Cancel")

        # E1999f783 -- Tap a result: go to that entry
        # (Diary.java:3288-3311). The row text is MEDIUM date + two
        # spaces + the matched line (Diary.java:3263-3265).
        today = date.today()
        result_text = "%s %d, %d  %s" % (
            today.strftime("%b"), today.day, today.year, SEARCH_WORD)
        r.tap("E1999f783", text=result_text)

        # E03d355a9 -- searchView.postDelayed(setQuery(search),
        # 256 ms) (Diary.java:3302-3306). Fires from the result tap's
        # handler; the UI dump below gives it time to elapse live.
        r.dump_ui("route_09_result", "E03d355a9")
        r.comment("searchView.postDelayed(setQuery(search), 256 ms)",
                  "E03d355a9")
    finally:
        r.done()


if __name__ == "__main__":
    main()
