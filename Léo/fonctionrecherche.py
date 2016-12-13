# Créé par morin, le 12/12/2016 en Python 3.2

def cherche_personne(annuaire,nom):
    for line in annuaire:
        if nom==line[0]:
            return line
    return []

