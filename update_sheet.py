import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SheetRewards:

    def __init__(self, rewards):
        #endpoint cosmosHub
        self.rewards = rewards
        # Définir les informations d'identification pour accéder à votre compte Google Sheet
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('cosmosrewards-d891d19a5027.json', scope)
        self.client = gspread.authorize(creds)


    def updtsheet(self):
      sheet = self.client.open('CosmosRewards').sheet1
      sheet.update('A2:B3', [[1, 2], [3, 4]])
      print("sheetupdated:")
