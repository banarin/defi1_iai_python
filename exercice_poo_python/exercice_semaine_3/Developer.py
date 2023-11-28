## importation de la class
from exercice_semaine_3.Employee import Employee

## heritage 
class Developer(Employee):
    def __init__(self):
        ## les attributs de la class mere
        super().__init__(self,firstName,lastName,salary,prog_lang)
        self.prog_lang = prog_lang
    