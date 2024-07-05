from PySide2 import QtWidgets
import os
import json

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "data.json")

class Candidapp:

    def __init__(self, title, status):
        self.title = title.title()
        self.status = status.title()

    def _get_society(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_society(self, society):
        with open(DATA_FILE, "w") as f:
            return json.dump(society, f, indent=4)

#Récupérer entreprise avec une majuscule a chaque mot
#Récupérer statut


#Ecrire dans un fichier json (dictionnaire ?)

#Retirer entreprise avec le statut associé

#Importer depuis un fichier word ou txt

if __name__ == "__main__":
    c = Candidapp("t", "t")
    c._get_society()
    c._write_society("test")