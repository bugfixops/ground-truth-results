"""UI harness for device route replay (brief section 5.6, D2).

Python 3 standard library plus adb only. No third-party packages, no
network access, no emulator control beyond adb commands.

A route script drives one Runner:

    from device.harness import Runner
    r = Runner(package="org.example.app", route="route_01",
               edge_ids=["E0123...", ...], log_path="steps/route_01.log")
    r.launch("org.example.app/.MainActivity", edge="E0123...")
    r.tap(text="Settings", edge="E0456...")
    r.done()

Every action takes an edge id and logs exactly one line to the steps log:
    <UTC ISO time> <edge id> <action> <target> <result>
In dry-run mode (dry_run=True) no adb command is executed: the planned
commands are recorded and every action's edge id is checked against the
route's edge ids. In real mode the same calls execute adb commands.
Setup scripts (not route edges) pass edge_ids=None to skip edge checks.
"""

from .harness import (Runner, find_node, find_row_action, parse_bounds,
                      node_center)

__all__ = ["Runner", "find_node", "find_row_action", "parse_bounds",
           "node_center"]
