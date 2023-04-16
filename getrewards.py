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

    def get_pending_rewards(self):
        try:
                rewards = get(i + self.rewards_url, timeout=5).json()
                rewards = float([i['amount'] for i in rewards['total'] if i['denom'] == self.denom][0])
        except Exception as e:
                print(e)
                pass #Rest server down, probably. Try the next one.

        return rewards

