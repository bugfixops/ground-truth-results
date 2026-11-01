"""Device replay preparation (brief section 5.6, D1-D9).

Subpackages: harness (D2), plus plan.py, run_app.sh, collect.py,
compare.py, drycheck.py, jacoco_lookup.py, route_info.py. Route
scripts live in device/routes/<App>/ and import device.harness via a
sys.path bootstrap from their own location (python3 -I ignores
PYTHONPATH).
"""
