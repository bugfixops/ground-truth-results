#!/usr/bin/env python3
"""AnyMemo per-route setup for route_18 (SettingsScreen$12.onClick).

Copies DejaVuSans.ttf at run time into the run's gen dir (see
--gen-dir), from a system font location on the runner. run_app.sh
pushes the copy to the picker's root
/sdcard/Android/data/org.liberty.android.fantastischmemo/files/anymemo/
(see the route's ROUTES.csv fixture cell, gen: form), where the file
picker lists it: the picker filters by extension only
(SettingsScreen.java:723-731), so any listed *.ttf row is tappable,
and route_18's script taps the row text "DejaVuSans.ttf".

WHY COPY, NOT GENERATE OR EMBED: embedding a base64 blob in this
script IS committing binary content, which is forbidden; generating
a synthetic minimal TTF named DejaVuSans.ttf would be misleading
(the real font is the faithful fixture, and content validity only
matters after the click, which the picker does not check). The
system-font copy is the honest run-time provisioning.

PREREQUISITE (runner image): the DejaVu fonts package installed
(apt: fonts-dejavu). If no system DejaVuSans.ttf is found this
script exits 1 with a provisioning error: the route then fails at
the setup step (setup_failed -> unclear, never wrong), which is a
provisioning signal, not a script defect. This script itself pushes
nothing to the device and the copied font is never committed — it
lives only under the run's out dir.

Usage (invoked by run_app.sh):
    setup_route_18.py --package <pkg> --log <log> --outdir <dir> \
        --gen-dir <dir>
"""

import argparse
import os
import shutil
import subprocess
import sys

FONT_NAME = "DejaVuSans.ttf"

CANDIDATE_PATHS = (
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/TTF/DejaVuSans.ttf",
    "/usr/local/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/local/share/fonts/TTF/DejaVuSans.ttf",
)


def find_system_font():
    """Return a system DejaVuSans.ttf path, or None if none is found."""
    for path in CANDIDATE_PATHS:
        if os.path.isfile(path):
            return path
    try:
        out = subprocess.run(["fc-list", "DejaVu Sans", "file"],
                             capture_output=True, text=True,
                             timeout=30, check=False).stdout
    except (OSError, subprocess.TimeoutExpired):
        out = ""
    for line in out.splitlines():
        path = line.split(":", 1)[0].strip()
        if os.path.basename(path) == FONT_NAME and os.path.isfile(path):
            return path
    return None


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="AnyMemo route_18 setup: copy DejaVuSans.ttf at run time")
    parser.add_argument("--package", default="")
    parser.add_argument("--log", default=None)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--gen-dir", default=None)
    args = parser.parse_args(argv)
    gen_dir = args.gen_dir or os.path.join(os.getcwd(), "gen")
    os.makedirs(gen_dir, exist_ok=True)
    src = find_system_font()
    if src is None:
        sys.stderr.write(
            "setup_route_18: no system DejaVuSans.ttf found. "
            "Provisioning prerequisite: install the DejaVu fonts on "
            "the runner (apt: fonts-dejavu). Route fails at setup "
            "(unclear, never wrong); this is a provisioning signal, "
            "not a script defect.\n")
        return 1
    dst = os.path.join(gen_dir, FONT_NAME)
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    line = "copied %s -> %s (%d bytes)\n" % (src, dst, size)
    if args.log:
        with open(args.log, "a", encoding="utf-8") as f:
            f.write(line)
    sys.stdout.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
