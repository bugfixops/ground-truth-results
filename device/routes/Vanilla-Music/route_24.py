"""Route route_24: SlidingTabStrip.blendColors.

Printed route source: graphs/Vanilla-Music/verification.csv path row
"SlidingTabStrip.blendColors" ("Steps read: library content inflates
VanillaTabLayout(Context,AttributeSet) ->
(Context,AttributeSet,int) -> super (SlidingTabLayout 3-arg ctor) ->
new SlidingTabStrip(context) -> onDraw -> blendColors") and
device/routes/Vanilla-Music/ROUTES.csv row route_24 (source:
VanillaTabLayout.java:37,41; SlidingTabLayout.java:100;
SlidingTabStrip.java:112).

Edge ids, in order:
  E47380ade, E0fd35a14, E4bc576b2, E6e95ad7a, E68f785e9, E4a8b2e51,
  Eeff96387, E05a156b0.

Permissions: none (ROUTES.csv permissions cell is empty).
Fixtures: none (STATE file gates: none).
Setup (done by run_app.sh before this script): push fixtures/Music +
media scan. This script therefore starts by launching the app; the
tab strip is drawn on ordinary launch when the library content
inflates.

UI facts used (read from layout XML / strings, never invented):
- library_content.xml includes the tab layout as
  android.support.iosched.tabs.VanillaTabLayout with
  android:id "@+id/sliding_tabs".
- The default library tab title is "Artists"
  (res/values/translatable.xml artists); waiting for it proves the
  tab strip has been inflated and drawn.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness.harness import Runner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    r = Runner(package=args.package, route="route_24", edge_ids=[
        "E47380ade", "E0fd35a14", "E4bc576b2", "E6e95ad7a", "E68f785e9",
        "E4a8b2e51", "Eeff96387", "E05a156b0",
    ], log_path=args.log, dry_run=args.dry_run, outdir=args.outdir)

    # E47380ade -- MAIN / LAUNCHER intent starts LibraryActivity.
    r.launch(args.package + "/.LibraryActivity", "E47380ade")

    # E0fd35a14 -- Activity lifecycle callback (LibraryActivity
    # onCreate). No user action.
    r.comment("lifecycle-onCreate-no-user-action", "E0fd35a14")

    # E4bc576b2 -- setContentView / inflate builds the view
    # <VanillaTabLayout> of library_content.xml (also
    # bottombar_controls.xml, controls.xml). Wait for the Artists
    # tab title so the inflated tab strip is on screen.
    r.wait_for("E4bc576b2", text="Artists")

    # E6e95ad7a -- Direct call: VanillaTabLayout(Context,AttributeSet)
    # -> (Context,AttributeSet,int).
    r.comment("direct-call-no-user-action", "E6e95ad7a")

    # E68f785e9 -- Direct call: VanillaTabLayout 3-arg ctor -> super
    # (SlidingTabLayout 3-arg ctor).
    r.comment("direct-call-no-user-action", "E68f785e9")

    # E4a8b2e51 -- Direct call: SlidingTabLayout 3-arg ctor -> new
    # SlidingTabStrip(context).
    r.comment("direct-call-no-user-action", "E4a8b2e51")

    # Eeff96387 -- the strip is drawn (framework calls onDraw).
    # No user action: drawing follows inflation automatically.
    r.comment("framework-onDraw-no-user-action", "Eeff96387")

    # E05a156b0 -- Direct call: SlidingTabStrip.onDraw ->
    # blendColors (target).
    r.comment("direct-call-target-reached", "E05a156b0")

    r.done()


if __name__ == "__main__":
    main()
