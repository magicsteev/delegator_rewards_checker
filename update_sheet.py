import gspread
import json

from oauth2client.service_account import ServiceAccountCredentials

class SheetRewards:

    def __init__(self, rewards, datetime):
        #endpoint cosmosHub
        self.rewards = json.dumps(rewards)
        # Définir les informations d'identification pour accéder à votre compte Google Sheet
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('cosmosrewards-d891d19a5027.json', scope)
        self.client = gspread.authorize(creds)
        self.dt = datetime
    def isok(self):

        spreadsheet = self.client.open('CosmosRewards')

        # Obtenir la liste des onglets
        sheets = spreadsheet.worksheets()
        for sheet in sheets:
            print(sheet.title)
    
    def updtsheet(self,rewards):
      sheet = self.client.open('CosmosRewards').sheet1
      str_list = list(filter(None, sheet.col_values(1)))
      cell=len(str_list)+1
      print("Cell : ", cell)
      
      #Remplir le tableau à partir de la première ligne disponible
      
      for reward in rewards:
        print("Validator address: ", reward[0])
        
        # Trouver la première ligne vide dans la première colonne
        #cell = sheet.find('')

        sheet.update_cell(cell, 1, self.dt)
        sheet.update_cell(cell, 2, reward[0])
        sheet.update_cell(cell, 3, reward[1])
        sheet.update_cell(cell, 4, reward[2])
        
        cell=cell+1
        
      #sheet.update('A2:B3', [[1, 2], [3, 4]])
      print("sheetupdated:")
