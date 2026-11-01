"""Shared ROUTES.csv helpers for the device scripts (D1/D4).

Prefix map is the brief section 2.2 build-prefix table: the trigger
graph for an app is graphs/<App>/out/<prefix>_trigger_graph.json.

CLI (used by device/run_app.sh):
    route_info.py <App> [--scripted|--unscriptable|--all] [--root R]
prints one TSV line per route:
    route<TAB>method<TAB>edges<TAB>permissions<TAB>fixtures<TAB>setup<TAB>status
"""

import csv
import os
import sys

PREFIXES = {
    "Currency": "currency",
    "Diary": "diary",
    "hash-checker": "hash-checker",
    "Omni-Notes": "omni-notes",
    "openlauncher": "openlauncher",
    "Vanilla-Music": "vanilla",
    "Markor": "markor",
    "AnyMemo": "anymemo",
    "Aegis": "aegis",
    "AmazeFileManager": "amazefilemanager",
    "AnkiDroid": "ankidroid",
    "MMEX": "mmex",
    "LibreTorrent": "libretorrent",
}

COLUMNS = ["route", "method", "edges", "source", "env_kinds", "state_kinds",
           "permissions", "fixtures", "setup", "status"]


def repo_root(start=None):
    here = start or os.path.abspath(__file__)
    return os.path.dirname(os.path.dirname(here))


def load_routes(app, root):
    """All ROUTES.csv rows for an app, in file order."""
    path = os.path.join(root, "device", "routes", app, "ROUTES.csv")
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            raise ValueError("%s: bad header %r" % (path, reader.fieldnames))
        return list(reader)


def trigger_graph_path(app, root):
    return os.path.join(root, "graphs", app, "out",
                        "%s_trigger_graph.json" % PREFIXES[app])


def methods_csv_path(app, root):
    return os.path.join(root, "graphs", app, "out", "methods.csv")


def find_manifest(app, root):
    """The app's main manifest (prefers a src/main path)."""
    base = os.path.join(root, "final_java_only", app, "app")
    hits = []
    for dirpath, _dirs, files in os.walk(base):
        if "AndroidManifest.xml" in files:
            hits.append(os.path.join(dirpath, "AndroidManifest.xml"))
    hits.sort(key=lambda p: ("/src/main/" not in p, len(p)))
    return hits[0] if hits else None


def main(argv):
    if not argv:
        sys.stderr.write("usage: route_info.py <App> [--scripted|--unscriptable|--all] [--root R]\n")
        return 1
    app = argv[0]
    mode = "all"
    root = repo_root()
    i = 1
    while i < len(argv):
        if argv[i] in ("--scripted", "--unscriptable", "--all"):
            mode = argv[i][2:]
        elif argv[i] == "--root" and i + 1 < len(argv):
            root = argv[i + 1]
            i += 1
        else:
            sys.stderr.write("unknown argument: %s\n" % argv[i])
            return 1
        i += 1
    rows = load_routes(app, root)
    for row in rows:
        if mode == "scripted" and row["status"] != "scripted":
            continue
        if mode == "unscriptable" and not row["status"].startswith("unscriptable"):
            continue
        sys.stdout.write("\t".join([
            row["route"], row["method"], row["edges"], row["permissions"],
            row["fixtures"], row["setup"], row["status"]]) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
