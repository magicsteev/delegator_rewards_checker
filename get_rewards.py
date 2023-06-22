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
                rewards = get(self.rest_servers_prod + self.rewards_url, timeout=5).json()
                #rewards = float([i['amount'] for i in rewards['total'] if i['denom'] == self.denom][0])
                return jsonRewards_to_table(rewards)
        except Exception as e:
                print(e)
                pass #Rest server down, probably. Try the next one.

        return 0
        
def get_validator_name(self,valoper):
    try:
            url = self.rest_servers_prod + "/staking/v1beta1/validators" + valoper
            print ("calling : " + url)
            val = get(url, timeout=5).json()
            #rewards = float([i['amount'] for i in rewards['total'] if i['denom'] == self.denom][0])
            return val
    except Exception as e:
            print(e)
            pass #Rest server down, probably. Try the next one.

    return 0
        
def jsonRewards_to_table(data):
    table = []
    
    # Traitement des récompenses des validateurs
    rewards = data["rewards"]
    for reward in rewards:
        validator_address = reward["validator_address"]
        val = get_validator_name(validator_address)
        reward_data = reward["reward"]
    
        for entry in reward_data:
            denom = entry["denom"]
            amount = entry["amount"]
    
            table.append([val, denom, amount])
        
    return table
