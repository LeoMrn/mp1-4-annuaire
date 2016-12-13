# Créé par guyard, le 12/12/2016 en Python 3.2
import manipulationsAnnuaire

annuaire = lire_annuaire()

reponse = input("Que voulez vous faire ?")

while reponse != "quitter":
    if reponse=="ajouter":
        manipulationsAnnuaire.ajouter_personne(annuaire, nom, prenom, tel)
    elif reponse=="retirer":
        manipulationsAnnuaire.retirer_personne(annuaire, nom, prenom, tel)
    elif reponse=="rechercher":
        manipulationsAnnuaire.cherche_personne(annuaire, nom)
        manipulationsAnnuaire.afficher_image(nom)
    else:
        print("Veuillez choisir entre: ajouter, retirer, rechercher ou quitter si vous souhaitez annuler")

ecrire_annuaire(annuaire)