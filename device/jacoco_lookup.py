#!/usr/bin/env python3
"""Map a graph method to its JaCoCo XML coverage entry (brief D4).

Usage: python3 -I device/jacoco_lookup.py <method_list.json> <report.xml> <method>
Prints one line: reached | not_reached | absent
  reached     -- the method's INSTRUCTION counter has covered > 0
  not_reached -- the method exists in the report with covered == 0
  absent      -- no matching (class, name, descriptor) in the report

Method naming follows tools/build_graph.py method_names() exactly
(the tools/emu_compare.py pattern): base node name per method, with
overload/package disambiguation. Run with the tools dir importable:
this module inserts <repo>/tools into sys.path when given a repo root
via --tools, or when run from a staging root that has a tools sibling.
method_list.json rows carry class (slashed), name, desc; JaCoCo XML
uses the same slashed class names, method names, and descriptors.
"""

import json
import os
import sys
import xml.etree.ElementTree as ET


def load_method_names(method_list_path, tools_dir):
    sys.path.insert(0, tools_dir)
    import build_graph  # noqa: E402
    with open(method_list_path, encoding="utf-8") as f:
        rows = json.load(f)
    names, by_name = build_graph.method_names(rows)
    # by_name: node name -> method_list row (class slashed, name, desc).
    return {name: (r["class"], r["name"], r["desc"])
            for name, r in by_name.items()}


def lookup(report_path, target):
    """target = (class, name, desc); returns reached/not_reached/absent."""
    tree = ET.parse(report_path)
    cls, name, desc = target
    for package in tree.getroot().iter("package"):
        for klass in package.iter("class"):
            if klass.get("name") != cls:
                continue
            for method in klass.iter("method"):
                if method.get("name") == name and \
                        method.get("desc") == desc:
                    for counter in method.iter("counter"):
                        if counter.get("type") == "INSTRUCTION":
                            return ("reached"
                                    if int(counter.get("covered", "0")) > 0
                                    else "not_reached")
                    return "not_reached"
    return "absent"


def main(argv):
    if len(argv) < 3:
        sys.stderr.write(
            "usage: jacoco_lookup.py <method_list.json> <report.xml> <method> [--tools DIR]\n")
        return 2
    method_list, report, method = argv[0], argv[1], argv[2]
    tools_dir = None
    i = 3
    while i < len(argv):
        if argv[i] == "--tools" and i + 1 < len(argv):
            tools_dir = argv[i + 1]
            i += 1
        i += 1
    if tools_dir is None:
        # Guess: repo root is two levels above this file's dir.
        tools_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "tools")
    names = load_method_names(method_list, tools_dir)
    if method not in names:
        sys.stderr.write("method %s not in method_list naming\n" % method)
        return 2
    print(lookup(report, names[method]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
