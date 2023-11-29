from Employee import Employee

class Manager(Employee):
    
    def __init__(self,firsName,lastName,salary,employees=None):
        super().__init__(firsName,lastName,salary)
        if employees != None:
            self.employees = employees
        else:
            self.employees = []
        
    def add_emp(self,employe):
        ## verifier voir si employe existe déjà
        if employe not in self.employees:
            self.employees.append(employe)
        else:
            print("employe existe déjà")
        
    def remove_emp(self,employe):
        if employe in self.employees:
            self.employees.remove(employe)
        else:
            print("employe n'existe déjà")    
    
    def print_emps(self):
        
        for employe in self.employees:
            print(employe.email)
            
if __name__ == '__main__':
    employe1 = Employee.from_string("jkqbe-otajkqbdwku-1002044000")
    employe2 = Employee.from_string("jk-qjhdbw-2044000")
    
    manager = Manager("john","doe","100000000",[employe1,employe2])
    manager.add_emp(employe2)
    manager.print_emps()