# Créé par CLERCL, le 05/12/2016 en Python 3.2

from PIL import Image

nom=input("entrer le nom de la personne:").upper()
nom_image = Image.open("photo/" + nom + ".jpg")


nom_image.show()
