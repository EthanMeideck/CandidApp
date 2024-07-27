import os, json, logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "data.json")

class Society:

    def __init__(self, title, status):
        self.title = title.title()
        self.status = status.title()

    def __str__(self):
        return f"{self.title} {self.status}"

    def get(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def write(self, new_dict):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            return json.dump(new_dict, f, indent=4)
        
    def add(self):
        society_dict = self.get()
        if self.title not in society_dict:
            society_dict[self.title] = self.status
            self.write(society_dict)
            return True
        else:
            logging.warning(" The society is already in the data base.")

    def remove(self, title):
        society_dict = self.get()
        if title in society_dict:
            del society_dict[title]
            self.write(society_dict)
            return True
        else:
            raise ValueError

    def sum_(self):
        try:
            for society in enumerate(self.get(), 1):
                numbers = society[0]
            return numbers
        except UnboundLocalError:
            return 0
    
    def import_(self, file):
        society_dict = self.get()
        society_dict.clear()
        
        with open(file[0], "r", encoding="utf-8") as f:
            for lines in f:
                lines = lines.replace("\n", "")
                lines = lines.replace("\t", "")

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
                    society_dict[lines] = "Waiting"

        self.write(society_dict)

if __name__ == "__main__":
    c = Society("t", "t")
    c.sum_()