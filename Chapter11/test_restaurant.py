import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):    
    
    def setUp(self):
        restaurant_name="Outback"
        cuisine_type="Chain"
        number_served=3
        self.restaurant = Restaurant(restaurant_name, cuisine_type, number_served)

    def test_number_served_int(self):
        number_served=5
        self.restaurant.set_number_served(number_served)
        self.assertEqual(self.restaurant.number_served,5)

    def test_number_served_string(self):
        number_served="5"
        self.restaurant.set_number_served(number_served)
        self.assertEqual(self.restaurant.number_served,5)    

    def test_increment_daily_sales_int(self):
        served=16
        self.restaurant.increment_number_served(served)
        self.assertEqual(self.restaurant.number_served,19)  

    def test_increment_daily_sales_string(self):
        served="8"
        self.restaurant.increment_number_served(served)
        self.assertEqual(self.restaurant.number_served,11)

if __name__ == '__main__':
    unittest.main()