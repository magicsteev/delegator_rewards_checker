from getrewards import GetRewards
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

# Définir les informations d'identification pour accéder à votre compte Google Sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('cosmosrewards-d891d19a5027.json', scope)
client = gspread.authorize(creds)

# Ouvrir la feuille de calcul
sheet = client.open('CosmosRewards').sheet1
data = [    {'Nom': 'Durand', 'Prénom': 'Jean', 'Âge': 42},    {'Nom': 'Dupont', 'Prénom': 'Marie', 'Âge': 28},    {'Nom': 'Martin', 'Prénom': 'Pierre', 'Âge': 35},]
sheet.insert_rows(data)


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
a=GetRewards("https://api-cosmoshub-ia.cosmosia.notional.ventures/", "cosmos1lpu6xj6qsu5aqxnserzxjteaq56j86lcl9hchy", "uatom")
r=a.get_pending_rewards()
print("new_rewards:", r)
