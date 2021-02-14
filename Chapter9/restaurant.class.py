class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The Restaurant {self.restaurant_name} serves {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"The Restaurant {self.restaurant_name} is open")
    

print("---------------exercise 9-1------------")

restaurant = Restaurant("Outback Steakhouse", "American")
print("The restuarant name is ", restaurant.restaurant_name)
print("The Cuisine type is ", restaurant.cuisine_type)

restaurant.open_restaurant()
restaurant.describe_restaurant()

print("---------------exercise 9-2------------")

restaurant1 = Restaurant("Outback Steakhouse", "American")
restaurant2 = Restaurant("Blue Tracktor", "American")
restaurant3 = Restaurant("Fuji", "Japanese")

restaurant1.open_restaurant()
restaurant1.describe_restaurant()
restaurant2.open_restaurant()
restaurant2.describe_restaurant()
restaurant3.open_restaurant()
restaurant3.describe_restaurant()