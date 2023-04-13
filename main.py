from time import sleep
from requests import get

class GetRewards:

    def __init__(self):

        self.rest_servers_prod = ['https://api-cosmoshub-ia.cosmosia.notional.ventures',
                             'https://cosmos-lcd.quickapi.com:443', 'https://lcd-cosmoshub.blockapsis.com',
                             'https://lcd.cosmos.dragonstake.io', 'https://api.cosmos.silknodes.io',
                             'https://cosmoshub-api.lavenderfive.com:443']

        self.wallet_address = "cosmos13w3uzqu8yjups2r4rgw7cy0jxe9nya5966j68g"
        self.denom = "uatom"

        self.rewards_url = f"/cosmos/distribution/v1beta1/delegators/{self.wallet_address}/rewards"

        #Telegram bot https://medium.com/codex/using-python-to-send-telegram-messages-in-3-simple-steps-419a8b5e5e2
        token = ""
        chat_id = 0000000
        self.url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text="

    def run(self):

        rewards = 0
        while True:
            new_rewards = self.get_pending_rewards()

            if new_rewards == rewards: #new_rewards can be lower if there was a withdrawal. No alert unless both values are identical.
                message = f"Warning: rewards aren't incrementing\n {self.wallet_address}: {rewards}{self.denom}"
                get(self.url+message) #send TG message

            rewards = new_rewards
            sleep(7200) #run every 2h?


    def get_pending_rewards(self):
        for i in self.rest_servers_prod:
            try:
                rewards = get(i + self.rewards_url, timeout=5).json()
                rewards = float([i['amount'] for i in rewards['total'] if i['denom'] == self.denom][0])
                return rewards
            except Exception as e:
                print(e)
                pass #Rest server down, probably. Try the next one.

        return 0



if __name__ == "__main__":
    GetRewards().run()