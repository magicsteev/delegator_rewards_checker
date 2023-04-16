import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SheetRewards:

    def __init__(self, rewards):
        #endpoint cosmosHub
        self.rewards = rewards
        # Définir les informations d'identification pour accéder à votre compte Google Sheet
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('cosmosrewards-d891d19a5027.json', scope)
        client = gspread.authorize(creds)


    def updtsheet(self):
      sheet = client.open('CosmosRewards').sheet1
      sheet.update('A1:B2', [[1, 2], [3, 4]])
      print("sheetupdated:")
