from getrewards import GetRewards
from update_sheet import SheetRewards
import csv
import datetime

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

a=GetRewards("https://api-cosmoshub-ia.cosmosia.notional.ventures/", "cosmos1lpu6xj6qsu5aqxnserzxjteaq56j86lcl9hchy", "uatom")
r=a.get_pending_rewards()
print("new_rewards:", r)

b=SheetRewards(r, timestamp)
t=b.updtsheet()

a=GetRewards("https://rest.cosmos.directory/osmosis/", "osmo1lpu6xj6qsu5aqxnserzxjteaq56j86lch7ygpk", "uatom")
r=a.get_pending_rewards()
print("new_rewards:", r)

b=SheetRewards(r, timestamp)
t=b.updtsheet()
