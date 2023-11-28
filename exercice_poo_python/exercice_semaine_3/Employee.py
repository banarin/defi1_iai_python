# 1
class Employee:
    ### variable de class
    
    raise_amount = 4
    nb_of_emps = 0
    ### constructor ###
    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName,
        self.lastName = lastName,
        self.salary = salary,
        self.email = f"{firstName}.{lastName}@company.org"
        ## incrementation a chaque create d'un employee
        nb_of_emps = nb_of_emps + 1
    
    ### methode fullName ###
    def fullname(self):
        return f"{self.firstName} {self.lastName}"
    
    ### methode pour MAJ le salaire ###
    def maj_salaire(self,new_salary):
        self.salary = new_salary
    ### méthodes de classe set_raise_amt 
    def set_raise_amt(new_raise_amount):
        raise_amount = new_raise_amount
        
    ### méthodes from_string
    def from_string(cls, emp_str):
        # Diviser la chaîne de caractères en utilisant les délimiteurs spécifiés ('-')
        prenom, nom, salaire_str = emp_str.split('-')
        nom, salaire_str = nom.split('-')
        
        # Convertir la partie salaire en nombre entier
        salaire = int(salaire_str)

        # Retourner une nouvelle instance de la classe Employee
        return cls(prenom, nom, salaire)
    @staticmethod
    def day_work(day):
        liste_day = ["lundi", "mardi","mercredie","jeudi","vendredi"]
        if(day in liste_day):
            return True
        else:
            return False