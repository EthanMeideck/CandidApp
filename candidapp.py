import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "data.json")

class Candidapp:

    def __init__(self, title, status):
        self.title = title.title()
        self.status = status.title()

    def __str__(self):
        return f"{self.title} {self.status}"

    def _get_society(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_society(self, new_dict):
        with open(DATA_FILE, "w") as f:
            return json.dump(new_dict, f, indent=4)
        
    def add_society(self):
        society_dict = self._get_society()
        if self.title not in society_dict:
            society_dict[self.title] = self.status
            self._write_society(society_dict)
            return True
        else:
            logging.warning(" The society is already in the data base.")

    def remove_society(self, title):
        society_dict = self._get_society()
        if title in society_dict:
            del society_dict[title]
            self._write_society(society_dict)
            return True
        else:
            logging.warning(" The society is not in the data base.")

    def societys_sum(self):
        with open(DATA_FILE, "r") as f:
            society_dict = json.load(f)
        numbers = 0
        for _ in society_dict:
            numbers += 1
        return numbers

#Importer depuis un fichier word ou txt

if __name__ == "__main__":
    c = Candidapp("test", "en attente")
    # c.add_society()
    # c.remove_society()
    # c.societys_sum()
    # societys_sum()