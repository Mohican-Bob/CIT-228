import unittest
from employee import Employee

class TestEmployee(unittest.TestCase): 
    
    def setUp(self):
        employee_name="Joshua"
        employee_last="Paul"
        salary=25000        
        self.employee = Employee(employee_name, employee_last, salary)

    def test_give_default_raise(self):        
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,30000)

    def test_give_custom_raise(self):        
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary,35000)

if __name__ == '__main__':
    unittest.main()