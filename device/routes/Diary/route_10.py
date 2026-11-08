"""Diary route_10: Diary.dateCheck(CharSequence,String).

Method: Diary.dateCheck(CharSequence,String)
Edge ids, in route order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E65bffa72
    E003e3f4e Eb04234de E614e3b2e E18bac421 E70b5909f E7ada6d09
    E51866d90 Ee9b231d0 E128aa89d Eae35dc61 E59723e4b E11c6d202
    Ebb6ba654
Printed route file: overnight/stream-D/Diary/scratch/route_steps.txt
    (section "Diary.dateCheck(CharSequence,String)", ref
    Diary.java:2714).
Permissions (ROUTES.csv, merger-updated): WRITE_EXTERNAL_STORAGE;READ_EXTERNAL_STORAGE (SETUP grants for saving/reading entries).
Fixtures: none (ROUTES.csv fixtures column empty).
Setup: none from ROUTES.csv (setup column empty); the STATE data
    the route needs is established by this script itself (see below),
    not by a fixture: ROUTES.csv state_kinds is "data" with the gate
    "the shown day has no entry text yet (a day without an entry;
    the help text of the first start is not empty)".
STATE ESTABLISHED BY THIS SCRIPT, BETWEEN ROUTE EDGES 5 AND 6:
    the script first saves an entry for today (so the first-start
    help text is no longer copied on resume -- Diary.java:563-568
    copies it only when prevEntry and nextEntry are both null),
    then navigates to tomorrow, a day with no entry, via "Go to
    date..." and the DatePickerDialog (Diary.java:1721-1733).
    Setup must sit here, not before the route launch: after the
    Settings return (edges 15-16) Diary resumes on the same shown
    day (tomorrow), still empty, so the Edit tap (edge 17) reaches
    template() on an empty entry. A fresh relaunch would reset the
    shown day to today (Diary.java:500-512) and lose the empty day.
    Setup actions are logged under the first edge (Ee6b8aa80) and
    marked STATE SETUP; they are not route steps, but every harness
    action needs an edge id of the route.
Standard configuration: run_app.sh clears the package before this
    script; storage permissions are granted up front (see grant block) and no fixtures pushed.

Mapping notes:
- Launcher tap (Ee6b8aa80) is driven as am start via r.launch: the
  harness has no launcher-UI action, and starting the MAIN/LAUNCHER
  activity is the adb equivalent (AndroidManifest.xml:52-59).
- "Use template" defaults to false (res/xml/preferences.xml,
  CheckBoxPreference android:defaultValue="false"), so one tap on
  the "Use template" row enables it on a fresh install.
- Date navigation uses the standard DatePickerDialog; its day cells
  carry a content description of the form "2 November 2026" (day,
  full month name, year). The script computes tomorrow from the host
  clock, assuming the emulator clock matches it (the CI emulator
  default) and the locale gives English month names; if the locale
  differs, the month name is the step to adjust. Confirmed with "OK".
- template() (Diary.java:2689-2719) returns at once for a non-empty
  entry, which is why the shown day must be empty; it then calls
  dateCheck on the template page text (Diary.java:2714). The
  template page defaults to 2000-01-01 (DatePickerPreference
  DEFAULT_VALUE), which normally has no entry, but dateCheck is
  called on whatever text is read, even empty text, so no template
  content needs to be authored.
- The Edit button is res/layout/main.xml @+id/edit; template() is
  called from its listener when useTemplate is set
  (Diary.java:1033-1044).
"""

import argparse
import os
import sys
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner

COMPONENT = "org.billthefarmer.diary/org.billthefarmer.diary.Diary"
SETUP_EDGE = "Ee6b8aa80"

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
    "E65bffa72", "E003e3f4e", "Eb04234de", "E614e3b2e", "E18bac421",
    "E70b5909f", "E7ada6d09", "E51866d90", "Ee9b231d0", "E128aa89d",
    "Eae35dc61", "E59723e4b", "E11c6d202", "Ebb6ba654",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()

    r = Runner(args.package, "route_10", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    try:
        # Ee6b8aa80 -- Tap the Diary icon in the launcher
        # (MAIN/LAUNCHER intent filter). Driven as am start.
        r.launch(COMPONENT, "Ee6b8aa80")

        # Edd0b9192 -- The system instantiates Diary, then onCreate.
        # Lifecycle edge: no user action.
        r.comment("system instantiates Diary, then onCreate", "Edd0b9192")

        # Ee63879c9 -- onStart -> onResume. Lifecycle edge: no action.
        r.comment("onStart -> onResume", "Ee63879c9")

        # Ea885d6f1 -- Diary visible with the MarkdownView.
        # Page arrival: wait for the MarkdownView (res/layout/main.xml
        # @+id/markdown).
        r.wait_for("Ea885d6f1", res_id="markdown")

        # STATE SETUP (not route steps; logged under Ee6b8aa80).
        # It sits between route edges 4 and 5: see the header note.
        # save an entry for today, then move to tomorrow (empty).
        # MERGER EDIT (SETUP grants): Diary.save() returns early without
        # WRITE_EXTERNAL_STORAGE (Diary.java:2248-2265); entry reads on
        # shared storage need READ_EXTERNAL_STORAGE. Granted before the
        # setup save so the setup entry persists. Logged under SETUP_EDGE.
        r.grant("android.permission.WRITE_EXTERNAL_STORAGE", SETUP_EDGE)
        r.grant("android.permission.READ_EXTERNAL_STORAGE", SETUP_EDGE)
        r.tap(SETUP_EDGE, res_id="edit")
        r.tap(SETUP_EDGE, res_id="text")
        r.type_text("setup entry", SETUP_EDGE)
        r.tap(SETUP_EDGE, res_id="accept")
        tomorrow = date.today() + timedelta(days=1)
        r.tap(SETUP_EDGE, desc="More options")
        r.tap(SETUP_EDGE, text="Go to date\u2026")
        r.tap(SETUP_EDGE, desc="%d %s %d" % (
            tomorrow.day, tomorrow.strftime("%B"), tomorrow.year))
        r.tap(SETUP_EDGE, text="OK")

        # E002e1746 -- Tap an action bar icon or an item under More
        # options. Open the overflow menu for the Settings item.
        r.tap("E002e1746", desc="More options")

        # E65bffa72 -- switch case R.id.settings (Diary.java:714-715).
        r.tap("E65bffa72", text="Settings")

        # E003e3f4e -- startActivity(new Intent(this, Settings.class))
        # (Diary.java:1976-1979). Internal intent; no user action.
        r.comment("startActivity(Settings)", "E003e3f4e")

        # Eb04234de -- The system instantiates Settings, then
        # onCreate. Lifecycle edge: no user action.
        r.comment("system instantiates Settings, then onCreate",
                  "Eb04234de")

        # E614e3b2e -- replace(android.R.id.content, new
        # SettingsFragment()).commit() (Settings.java:91-94).
        # Internal call; no user action.
        r.comment("replace(content, SettingsFragment)", "E614e3b2e")

        # E18bac421 -- The fragment transaction commits: fragment
        # onCreate. Lifecycle edge: no user action.
        r.comment("fragment transaction commits, onCreate", "E18bac421")

        # E70b5909f -- The fragment resumes with the activity.
        # Lifecycle edge: no user action.
        r.comment("fragment resumes with activity", "E70b5909f")

        # E7ada6d09 -- Settings list shown (SettingsFragment.java:
        # 107-113). Wait for the "Use template" preference row.
        r.wait_for("E7ada6d09", text="Use template")

        # E51866d90 -- Tap the Use template checkbox row: the value
        # flips and the listener fires (res/xml/preferences.xml:
        # pref_use_template). Default false, so this tap enables it.
        r.tap("E51866d90", text="Use template")

        # Ee9b231d0 -- Settings stays shown with the new value
        # (Template page row enabled). Page arrival; no user action.
        r.comment("Settings stays shown, new value", "Ee9b231d0")

        # E128aa89d -- Back finishes Settings; Diary resumes.
        # Settings has no onBackPressed override (Settings.java:
        # 36-119), so Back finishes it.
        r.back("E128aa89d")

        # Eae35dc61 -- Back in Diary with the changed preference
        # (getPreferences in onResume) (Diary.java:539-571). Diary
        # resumes on the empty day established in setup; no action.
        r.comment("Diary resumes on empty day, new preference",
                  "Eae35dc61")

        # E59723e4b -- Tap the Edit button: switch to the EditText
        # (Diary.java:1033-1062; res/layout/main.xml:78-86). The
        # shown day (tomorrow) has no entry text.
        r.tap("E59723e4b", res_id="edit")

        # E11c6d202 -- useTemplate: template() fills an empty entry
        # from the template page (Diary.java:1042-1044). The Edit
        # listener calls template() because useTemplate is set;
        # template() proceeds because the entry is empty.
        r.comment("useTemplate: template() fills empty entry",
                  "E11c6d202")

        # Ebb6ba654 -- text = dateCheck(text, "EEEE d MMMM yyyy
        # HH:mm"): <<date>> patterns become now (Diary.java:2714).
        # Called synchronously by template(); no user action.
        r.comment("dateCheck(text, DATE_FORMAT) in template()",
                  "Ebb6ba654")
    finally:
        r.done()


if __name__ == "__main__":
    main()
