TITLE = 'Omni-Notes generated (calibration run)'
USE_AUTO = True
PREFER_SETUP_OVER_ENV = True
AUTO_DEAD = 'No route found by the generator'
import sys
sys.path.insert(0, TOOLS)
import gen_edges
gen_edges.apply(globals(), GDIR, 'Omni-Notes', {})
