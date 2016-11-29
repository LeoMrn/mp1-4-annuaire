# Créé par GUYARD, le 21/11/2016 en Python 3.2

import os
import csv

# on travaillera dans un dossier qu'on choisira
base_chemin = "Q:\Espace d'échange\Mini projets ISN\mp1-4-annuaire"
os.chdir(base_chemin)
# avec un fichier du nom suivant
csv_chemin = "Annuaire.csv"

# lire un fichier csv
with open(csv_chemin, mode='r', newline='') as csv_file :
    csv_reader = csv.reader(csv_file,delimiter=';')

    for ligne in csv_reader :
        print(ligne)
