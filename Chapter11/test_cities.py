import unittest
from cities_functions import cities_function
from cities_functions import cities_function2



class CitiesTestCase(unittest.TestCase):


    def test_cities(self):
        formatted_name = cities_function('Tokyo', 'Japan')
        self.assertEqual(formatted_name, 'Tokyo Japan')  
    def test_cities2(self):
        formatted_name = cities_function2('Tokyo', 'Japan', 200)
        self.assertEqual(formatted_name, 'Tokyo Japan population: 200')                

if __name__ == '__main__':
    unittest.main()  