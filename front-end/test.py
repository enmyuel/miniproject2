import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import getDistance

a = getDistance.getStationData()
print(a)
