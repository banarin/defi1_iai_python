from exercice_semaine_3.Employee import Employee

class Manager(Employee):
    
    def __init__(self,firstName,lastName,salary,employes=None):
        super().__init__(firstName,lastName,salary)
        if employes is None:
            self.employes = []
        else:
            self.employes = employes
            
            
    def add_emp():
        if emp not in self.employees:
            self.employees.append(emp)
            
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        print("", self.prenom, self.nom)
        for emp in self.employees:
            print(f"- {emp.prenom} {emp.nom}")