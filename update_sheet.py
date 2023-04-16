import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

class SheetRewards:

    def __init__(self, rewards):
        #endpoint cosmosHub
        self.rewards = json.dumps(rewards)
        # Définir les informations d'identification pour accéder à votre compte Google Sheet
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('cosmosrewards-d891d19a5027.json', scope)
        self.client = gspread.authorize(creds)


    def updtsheet(self):
      sheet = self.client.open('CosmosRewards').sheet1
      
      
      
      print(f"La première ligne vide est la ligne {first_empty_row}")
      
      #Remplir le tableau à partir de la première ligne disponible
      json_obj = json.loads(self.rewards)
      for reward in json_obj['rewards']:
        print("Validator address: ", reward['validator_address'])
        
        # Trouver la première ligne vide dans la première colonne
        cell = sheet.find("")
        sheet.update_cell(cell.row, 1, timestamp)
        sheet.update_cell(row_to_update.row, 2, reward['validator_address'])
        for reward in reward['validator_address']:
            sheet.update_cell(row_to_update.row, 3, reward['amount'])
            sheet.update_cell(row_to_update.row, 4, reward['amount'])
        
        
      sheet.update('A2:B3', [[1, 2], [3, 4]])
      print("sheetupdated:")
