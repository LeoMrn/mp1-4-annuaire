# Créé par guyard, le 12/12/2016 en Python 3.2
import os
import csv
from PIL import Image

def afficher_image(nom):
    im = Image.open("Q:\Espace d'échange\Mini projets ISN\mp1-4-annuaire\photo")
    im.show()


def ajouter_personne(annuaire, nom, prenom, tel):
    """Ajouter"""
    annuaire.append([nom, prenom, tel])

def retirer_personne(annuaire, nom, prenom, tel):
    """retirer une personne de l'annuaire"""
    annuaire.remove([nom, prenom, tel])

def lire_annuaire():
    """Lecture du fichier et renvoi de la structure Annuaire"""
    annuaire = []
    # lecture csv
    return annuaire

def ecrire_annuaire(annuaire):
    """Ecriture de la structure Annuaire sur le fichier"""
    # Ecriture csv

def cherche_personne(annuaire,nom):
    for line in annuaire:
        if nom==line[0]:
            return line
    return []
