﻿# Créé par guyard, le 28/11/2016 en Python 3.2

import os
import csv


base_chemin = "Q:\Espace d'échange\Mini projets ISN\mp1-4-annuaire"
os.chdir(base_chemin)

csv_chemin = "Annuaire.csv"

nom=input("Entrer le nom de la personne:")

# lire un fichier csv
with open(csv_chemin, mode='r', newline='') as csv_file :
    csv_reader = csv.reader(csv_file,delimiter=';')

    for line in csv_reader :
        if nom==line[0]:
            print(line)

