from getrewards import GetRewards
from update_sheet import SheetRewards
import csv
import datetime

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Tu trouves les endpoints sur https://cosmos.directory/
print("Hello world")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#ATOM
a=GetRewards("https://api-cosmoshub-ia.cosmosia.notional.ventures/", "cosmos1lpu6xj6qsu5aqxnserzxjteaq56j86lcl9hchy", "uatom")
r=a.get_pending_rewards()
print("new_rewards:", r)

b=SheetRewards(r, timestamp)
t=b.updtsheet()
#OSMO
a=GetRewards("https://rest.cosmos.directory/osmosis/", "osmo1lpu6xj6qsu5aqxnserzxjteaq56j86lch7ygpk", "uosmo")
r=a.get_pending_rewards()
print("new_rewards:", r)

b=SheetRewards(r, timestamp)
t=b.updtsheet()


#EVMOS
a=GetRewards("https://rest.cosmos.directory/evmos", "evmos184ceng8y5n70wtegmmchefa4uynsssl2hgulld", "uevmos")
r=a.get_pending_rewards()
print("new_rewards:", r)

b=SheetRewards(r, timestamp)
t=b.updtsheet()

#SECRET
#https://rest.cosmos.directory/secretnetwork
#secret1q4x50wc7tjz8y6vchz54rxeahtv4v6srj5etrq

a=GetRewards("https://rest.cosmos.directory/secretnetwork", "secret1q4x50wc7tjz8y6vchz54rxeahtv4v6srj5etrq", "usecret")
r=a.get_pending_rewards()
print("new_rewards:", r)

b=SheetRewards(r, timestamp)
t=b.updtsheet()

#AKT
#https://rest.cosmos.directory/akash
#akash1lpu6xj6qsu5aqxnserzxjteaq56j86lcj76lw7

a=GetRewards("https://rest.cosmos.directory/akash", "akash1lpu6xj6qsu5aqxnserzxjteaq56j86lcj76lw7", "uakt")
r=a.get_pending_rewards()
print("new_rewards:", r)

b=SheetRewards(r, timestamp)
t=b.updtsheet()


#STARGAZE
#https://rest.cosmos.directory/stargaze
#
