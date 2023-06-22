
import csv
import datetime
import telegram


class DumpRewards:

    def __init__(self, tab):
        # Données du tableau
        tableau = [['StakeLab', 'ibc/0025F8A87464A471E66B234C4F93AEC5B4DA3D42D7986451A059273426290DD5', '2.641932694633278186'], ['StakeLab', 'uatom', '91632.829505824052887929'], ['cros-nest', 'ibc/0025F8A87464A471E66B234C4F93AEC5B4DA3D42D7986451A059273426290DD5', '2.725751250130960770'], ['cros-nest', 'uatom', '94631.012854503760552410'], ['Meria', 'ibc/0025F8A87464A471E66B234C4F93AEC5B4DA3D42D7986451A059273426290DD5', '0.233944841584373066'], ['Meria', 'uatom', '8108.824720607010400649'], ['SmartNodes', 'ibc/0025F8A87464A471E66B234C4F93AEC5B4DA3D42D7986451A059273426290DD5', '0.000000009893421567'], ['SmartNodes', 'ibc/B05539B66B72E2739B986B86391E5D08F12B8D5D2C2A7F8F8CF9ADF674DFA231', '0.000000000627177657'], ['SmartNodes', 'ibc/DEC41A02E47658D40FC71E5A35A9C807111F5A6662A3FB5DA84C4E6F53E616B3', '0.000000000013195562'], ['SmartNodes', 'uatom', '0.006639578852959659'], ['Stargaze', 'ibc/0025F8A87464A471E66B234C4F93AEC5B4DA3D42D7986451A059273426290DD5', '0.000000013166611195'], ['Stargaze', 'uatom', '0.000593762398103411']]

        # Nom du fichier CSV à créer
        nom_fichier = 'timestamp' + '_tableau.csv'

        # Écriture du tableau dans le fichier CSV
        with open(nom_fichier, 'w', newline='') as fichier:
            writer = csv.writer(fichier)
            writer.writerows(tab)

        token = '5885875594:AAETBQxIg4EQrKjAL2sdhrWNVKUM3v-J4QM'
        chat_id = '890885070'
        fichier = nom_fichier
        bot = telegram.Bot(token=token)
        bot.send_document(chat_id=chat_id, document=open(fichier, 'rb'))

        # Remplacez les valeurs suivantes par vos propres informations

