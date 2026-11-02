#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# Per-route setup for new setup_route_20. Run-time generation only; nothing here is
# committed as a binary. Interface: --package --log --outdir --gen-dir (GEN_DIR
# fallback). No real emulator/adb run, no CI request, no drycheck pass claimed.
"""Run-time generator for Aegis route_20's icon pack fixture.

Builds aegis_icon_pack.zip from text only (pack.json + one SVG
icon file) into the run's gen dir. Nothing binary is committed:
run_app.sh invokes this script with --gen-dir <outdir>/gen/
route_20 (GEN_DIR env as fallback) before pushing the zip to
/sdcard/aegis_icon_pack.zip for the route_20 picker step.

The pack satisfies IconPackManager.importPack's checks:
pack.json at the zip root; a UUID name and version 1, so the
installed dir is filesDir/icons/<uuid>/1/; one icon entry whose
filename exists in the zip. The icon file's bytes are never
parsed at import (they are only copied), so a minimal SVG
suffices. On the route_20 relaunch, rescanIconPacks requires
the pack UUID to equal the folder UUID and the version to
equal the version-dir name -- both hold by construction.

Usage (run_app.sh contract):
    python3 -I setup_route_20.py --package <pkg> --log <log>
        --outdir <outdir> --gen-dir <outdir>/gen/route_20
"""

import argparse
import json
import os
import sys
import zipfile

PACK_UUID = "12345678-1234-1234-1234-123456789abc"
PACK_NAME = "Draft pack"
PACK_VERSION = 1
ICON_FILENAME = "icon.svg"
ZIP_NAME = "aegis_icon_pack.zip"

SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'width="48" height="48"><rect width="48" height="48" '
    'fill="#808080"/></svg>\n'
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", default="")
    parser.add_argument("--log", default="")
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--gen-dir", default="")
    args = parser.parse_args()
    gen_dir = args.gen_dir or os.environ.get("GEN_DIR", "") or args.outdir
    os.makedirs(gen_dir, exist_ok=True)
    pack = {
        "uuid": PACK_UUID,
        "name": PACK_NAME,
        "version": PACK_VERSION,
        "icons": [
            {
                "filename": ICON_FILENAME,
                "name": "Draft",
                "category": None,
                "issuer": ["Draft"],
            }
        ],
    }
    out_path = os.path.join(gen_dir, ZIP_NAME)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("pack.json", json.dumps(pack))
        zf.writestr(ICON_FILENAME, SVG)
    sys.stdout.write("generated %s\n" % out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
