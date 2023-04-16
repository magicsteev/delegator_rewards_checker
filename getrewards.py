from requests import get

class GetRewards:

    def __init__(self, endpoint, address, denom):
        #endpoint cosmosHub
        self.rest_servers_prod = endpoint
         #endpoint osmosis
        self.rest_servers_osmo = ['https://rest.cosmos.directory/osmosis']
        
        self.wallet_address = address
        self.denom = denom

        self.rewards_url = f"/cosmos/distribution/v1beta1/delegators/{self.wallet_address}/rewards"
        print("End Cons")
