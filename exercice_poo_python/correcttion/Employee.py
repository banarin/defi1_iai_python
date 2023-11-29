import datetime

class Employee:
    raise_amount = 0.04
    nb_of_emps = 0
    ### constructor
    def __init__(self,firsName,lastName,salary):
        self.firsName = firsName
        self.lastName = lastName
        self.salary = salary
        Employee.nb_of_emps += 1 
        
    @property
    def fullname(self):
        return f"{self.firsName} {self.lastName}"
    
    @property
    def email(self):
        return f"{self.firsName}.{self.lastName}@company.org"
    
    def updateSalary(self):
        self.salary += self.salary * Employee.raise_amount 
    ### methode de la classe
    @classmethod
    def set_raise_amt(cls,new_raise_amount):
        cls.raise_amount = new_raise_amount
    ### methode de la classe
    @classmethod
    def from_string(cls,emp_str):
        first,second,salary_new = emp_str.split('-')
        conver_salary_new = float(salary_new)
        ### return Employee("first",second,conver_salary_new)
        return cls(first,second,conver_salary_new)
    
    @staticmethod
    def work_day(day):
        op =  day.weekday()
        
        if op < 5:
            return True
        else:
            return False

    def __add__(self, other):
        return self.salary + other.salary

### 
if __name__ == '__main__':
    ### creation de la classe
    employe = Employee.from_string("maxim-otaku-100000")
    employe1 = Employee.from_string("max-otaku-200000")
    
    print(employe+em)
    
    # print(employe.firsName)
    # print(employe.lastName)
    # print(employe.salary)
    
    # date_xampe = datetime.date(2023,11,29)
    # print(date_xampe)
    # print(employe.work_day(date_xampe))
    
        
