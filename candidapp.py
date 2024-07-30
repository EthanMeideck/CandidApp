import json
import logging
import os

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "data.json")

class Society:

    def __init__(self, title, status):
        self.title = title.title()
        self.status = status.title()
        self.society_dict = self.get_society()

    def __str__(self):
        return f"{self.title} {self.status}"

    def get_society(self):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def write_society(self, new_dict):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            return json.dump(new_dict, f, indent=4)
        
    def add_society(self):
        if self.title not in self.society_dict:
            self.society_dict[self.title] = self.status
            self.write_society(self.society_dict)
            return True
        else:
            logging.warning(" The society is already in the data base.")

    def remove_society(self, title):
        society_dict = self.get_society()
        if title in society_dict:
            del society_dict[title]
            self.write_society(society_dict)
            return True

    def society_sum(self):
        try:
            for society in enumerate(self.get_society(), 1):
                numbers = society[0]
            return numbers
        except UnboundLocalError:
            return 0
    
    def import_society(self, file):
        society_dict = self.get_society()
        society_dict.clear()
        
        with open(file[0], "r", encoding="utf-8") as f:
            for lines in f:
                lines = lines.replace("\n", "").replace("\t", "")

                if "Refus" in lines:
                    part = lines.split("Refus")
                    society = part[0]
                    society_dict[society.title()] = "Refus"

                elif "Entretien" in lines:
                    part = lines.split("Entretien")
                    society = part[0]
                    society_dict[society.title()] = "Entretien"
                
                elif "Accepté" in lines:
                    part = lines.split("Accepté")
                    society = part[0]
                    society_dict[society.title()] = "Accepté"
                        
                else:
                    society_dict[lines.title()] = "Waiting"

        self.write_society(society_dict)