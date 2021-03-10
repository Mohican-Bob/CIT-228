class Employee:
    def __init__(self, employee_name, employee_last, salary):
        self.employee_name = employee_name
        self.employee_last = employee_last
        self.salary = salary

    def give_raise(self, bonus = 5000):
        self.salary += bonus      
        
    

        
    
