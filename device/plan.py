#!/usr/bin/env python3
"""Print the device-replay matrix for apps that have route scripts.

Usage: python3 -I device/plan.py <apps...>
       python3 -I device/plan.py all

Prints exactly one line on stdout:
    matrix={"app": ["Currency", ...]}
listing the named apps (or, for `all`, the 13 apps in brief order)
that have at least one device/routes/<App>/route_*.py script.
Errors go to stderr; exit 1 with a message when no requested app has
route scripts, or when a named app is unknown.

The workflow feeds this line straight into GITHUB_OUTPUT, so stdout
must contain nothing else.
"""

import glob
import json
import os
import sys

APPS_13 = ["Currency", "Diary", "hash-checker", "Omni-Notes",
           "openlauncher", "Vanilla-Music", "Markor", "AnyMemo", "Aegis",
           "AmazeFileManager", "AnkiDroid", "MMEX", "LibreTorrent"]


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def apps_with_scripts(apps, root):
    out = []
    for app in apps:
        scripts = glob.glob(os.path.join(root, "device", "routes", app,
                                         "route_*.py"))
        if scripts:
            out.append(app)
    return out


def main(argv):
    if not argv:
        sys.stderr.write("usage: plan.py <apps...> | all\n")
        return 1
    root = repo_root()
    if argv == ["all"]:
        wanted = APPS_13
    else:
        unknown = [a for a in argv if a not in APPS_13]
        if unknown:
            sys.stderr.write("unknown app(s): %s\n" % ", ".join(unknown))
            return 1
        wanted = argv
    have = apps_with_scripts(wanted, root)
    if not have:
        sys.stderr.write("no requested app has device/routes/<App>/route_*.py\n")
        return 1
    sys.stdout.write("matrix=%s\n" % json.dumps({"app": have}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
