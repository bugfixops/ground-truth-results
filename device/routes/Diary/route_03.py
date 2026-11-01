#!/usr/bin/env python3
"""Diary route_03: AboutPreference.<init>.

Method: AboutPreference.<init>
Edge ids in order:
    Ee6b8aa80 Edd0b9192 Ee63879c9 Ea885d6f1 E002e1746 E65bffa72
    E003e3f4e Eb04234de E614e3b2e E18bac421 Eccf994be
Printed route: the AboutPreference.<init> section of the Diary route
    print (overnight stream-D Diary scratch route_steps.txt), verdict
    REACHABLE / SOURCE_OK, ref res/xml/preferences.xml:172; path row of
    graphs/Diary/verification.csv.
Permissions: none (ROUTES.csv permissions column empty).
Fixtures: none. Setup: none (Diary row of work-emulator ci/apps.csv has
    an empty setup cell).
Standard configuration: run_app.sh starts from `pm clear` and grants
    only the ROUTES.csv permissions (none here).

Mapping notes (printed source):
  - Diary is the MAIN/LAUNCHER activity (AndroidManifest.xml:52-59).
  - Settings and Add time / Add media are overflow items: menu main.xml
    gives settings showAsAction="never" (main.xml:105-107) with title
    "Settings" (res/values/strings.xml:45), so the script opens the
    overflow menu (content-desc "More options" on AOSP) and taps the
    "Settings" text.
  - SettingsFragment.onCreate calls addPreferencesFromResource
    (SettingsFragment.java:52-53); the framework inflates the
    AboutPreference element at res/xml/preferences.xml:172-179, which
    constructs AboutPreference(Context, AttributeSet)
    (AboutPreference.java constructor). No user action drives that
    final edge, so it is logged with r.comment.
"""

import argparse
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402

EDGE_IDS = [
    "Ee6b8aa80", "Edd0b9192", "Ee63879c9", "Ea885d6f1", "E002e1746",
    "E65bffa72", "E003e3f4e", "Eb04234de", "E614e3b2e", "E18bac421",
    "Eccf994be",
]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Diary route_03")
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    r = Runner(args.package, "route_03", EDGE_IDS, args.log,
               dry_run=args.dry_run, adb=args.adb, outdir=args.outdir)
    # Ee6b8aa80 S_ENTRY -> Diary.<init>: Tap the Diary icon in the
    # launcher (MAIN/LAUNCHER intent filter).
    r.launch(args.package + "/.Diary", "Ee6b8aa80")
    # Edd0b9192 Diary.<init> -> Diary.onCreate: system instantiates
    # Diary, then onCreate. No user action.
    r.comment("system instantiates Diary, then onCreate", "Edd0b9192")
    # Ee63879c9 Diary.onCreate -> Diary.onResume: onStart -> onResume.
    # No user action.
    r.comment("onStart -> onResume", "Ee63879c9")
    # Ea885d6f1 Diary.onResume -> S_DIARY_VIEW: Diary visible with the
    # MarkdownView. No user action.
    r.comment("Diary visible with the MarkdownView", "Ea885d6f1")
    # E002e1746 S_DIARY_VIEW -> Diary.onOptionsItemSelected@VIEW: open
    # the action bar menu (More options overflow).
    r.tap("E002e1746", desc="More options")
    # E65bffa72 Diary.onOptionsItemSelected@VIEW -> Diary.settings:
    # switch case R.id.settings (Diary.java:714-715).
    r.tap("E65bffa72", text="Settings")
    # E003e3f4e Diary.settings -> Settings.<init>: startActivity(new
    # Intent(this, Settings.class)) (Diary.java:1976-1979). Automatic
    # after the tap; no further action.
    r.comment("startActivity Settings intent", "E003e3f4e")
    # Eb04234de Settings.<init> -> Settings.onCreate: system
    # instantiates Settings, then onCreate. No user action.
    r.comment("system instantiates Settings, then onCreate", "Eb04234de")
    # E614e3b2e Settings.onCreate -> SettingsFragment.<init>:
    # replace(android.R.id.content, new SettingsFragment()).commit()
    # (Settings.java:91-94). No user action.
    r.comment("fragment transaction commits SettingsFragment", "E614e3b2e")
    # E18bac421 SettingsFragment.<init> -> SettingsFragment.onCreate:
    # the committed transaction runs fragment onCreate. No user action.
    r.comment("fragment onCreate runs", "E18bac421")
    # Eccf994be SettingsFragment.onCreate -> AboutPreference.<init>:
    # addPreferencesFromResource(preferences.xml) inflates
    # AboutPreference(Context, AttributeSet) (preferences.xml:172-179).
    # Framework inflation; no user action. This is the target edge.
    r.comment("framework inflates AboutPreference from preferences.xml",
              "Eccf994be")
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
