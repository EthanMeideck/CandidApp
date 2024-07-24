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
        with open(DATA_FILE, "w", encoding="utf-8") as f:
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
            raise ValueError

    def societys_sum(self):
        numbers = 0
        for _ in self._get_society():
            numbers += 1
        return numbers
    
    def import_society(self, file):
        society_dict = self._get_society()
        society_dict.clear()
        
        with open(file[0], "r", encoding="utf-8") as f:
            for lines in f:
                lines = lines.replace("\n", "")
                lines = lines.replace("\t", "")

                if "Refus" in lines:
                    part = lines.split("Refus")
                    society = part[0]
                    society_dict[society.title()] = "Refus"

                if not "Refus" in lines:
                    society_dict[lines] = "Waiting"

        self._write_society(society_dict)