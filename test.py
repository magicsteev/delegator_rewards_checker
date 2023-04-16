from getrewards import GetRewards
from update_sheet import SheetRewards
import csv

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
a=GetRewards("https://api-cosmoshub-ia.cosmosia.notional.ventures/", "cosmos1lpu6xj6qsu5aqxnserzxjteaq56j86lcl9hchy", "uatom")
r=a.get_pending_rewards()
print("new_rewards:", r)

b=SheetRewards(r)
t=b.updtsheet()
