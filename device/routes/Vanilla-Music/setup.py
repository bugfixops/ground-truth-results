"""Per-route setup for Vanilla-Music device replay (ROUTES.csv setup cell:
push fixtures/Music + media scan).

run_app.sh runs this once per route (after pm clear, before the route
script) when it exists as device/routes/Vanilla-Music/setup.py, with:
    python3 -I setup.py --package <PKG> --log <log> --outdir <outdir>
It pushes every file under $WEMU/fixtures/Music to /sdcard/Music/ and
then broadcasts MEDIA_SCANNER_SCAN_FILE for each file so the media
library picks them up. The route scripts wait_for library content
before proceeding, which covers scan completion; nothing here assumes
a particular track (the gates are "a song", not "that file").

$WEMU is the work-emulator checkout (CI provides it; locally it is
~/workspace/finish/work-emulator). If $WEMU is unset the script fails
with a clear message instead of silently running against an empty
library.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
from device.harness.harness import Runner  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    wemu = os.environ.get("WEMU")
    if not wemu:
        sys.stderr.write("setup.py: $WEMU is not set (work-emulator "
                         "checkout with fixtures/ is required)\n")
        return 2
    music = os.path.join(wemu, "fixtures", "Music")
    if not os.path.isdir(music):
        sys.stderr.write("setup.py: no fixtures/Music under $WEMU=%s\n"
                         % wemu)
        return 2
    r = Runner(package=a.package, route="setup", edge_ids=None,
               log_path=a.log, dry_run=a.dry_run, outdir=a.outdir)
    for name in sorted(os.listdir(music)):
        local = os.path.join(music, name)
        if not os.path.isfile(local):
            continue
        dest = "/sdcard/Music/" + name
        r.push_fixture(local, "setup", dest=dest)
        # broadcast() has no data parameter; the -d URI rides in
        # extras_args (appended verbatim to the am broadcast command).
        r.broadcast("setup",
                    action="android.intent.action.MEDIA_SCANNER_SCAN_FILE",
                    extras_args=["-d", "file://" + dest])
    r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
