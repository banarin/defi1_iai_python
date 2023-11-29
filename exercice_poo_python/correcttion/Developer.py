import Employee
### Developer herite de Employee
class Developer(Employee):
    
    raise_amont = 0.1
    
    def __init__(self,firsName,lastName,salary,prog_lang):
        ### faire appel au 
        super().__init__(firsName,lastName,salary)
        self.prog_lang = prog_lang