import argparse
from openlase import Openlase_Driver

parser = argparse.ArgumentParser(description='This is a shitty work-around')

parser.add_argument('message', action="store", type=str)
parser.add_argument('time_display', action="store", type=float)

results = parser.parse_args()


print results.message
print results.time_display

od = Openlase_Driver.Openlase_Driver()
od.write_tweet(results.message, results.time_display)
