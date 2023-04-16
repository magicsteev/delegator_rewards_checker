from requests import get

class GetRewards:

    def __init__(self):
        #endpoint cosmosHub
        self.rest_servers_prod = ['https://api-cosmoshub-ia.cosmosia.notional.ventures',
                             'https://cosmos-lcd.quickapi.com:443', 'https://lcd-cosmoshub.blockapsis.com',
                             'https://lcd.cosmos.dragonstake.io', 'https://api.cosmos.silknodes.io',
                             'https://cosmoshub-api.lavenderfive.com:443']
         #endpoint osmosis
        self.rest_servers_osmo = ['https://rest.cosmos.directory/osmosis']
        
        self.wallet_address = "cosmos13w3uzqu8yjups2r4rgw7cy0jxe9nya5966j68g"
        self.denom = "uatom"

        self.rewards_url = f"/cosmos/distribution/v1beta1/delegators/{self.wallet_address}/rewards"
