﻿# Créé par guyard, le 12/12/2016 en Python 3.2

import os
import csv
[
["nom", "prenom", "telephone", "adresse"]
, ["nom", "prenom", "telephone", "adresse"]
]

base_chemin = "Q:\Espace d'échange\Mini projets ISN\mp1-4-annuaire"
os.chdir(base_chemin)

csv_chemin = "Annuaire.csv"

nom=input("Entrer le nom de la personne:").upper()


with open(csv_chemin, mode='r', newline='') as csv_file :
    csv_reader = csv.reader(csv_file,delimiter=';')

    for nom in csv_reader:
        ligne = ligne.replace("nom","")

