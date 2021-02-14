class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The Restaurant {self.restaurant_name} serves {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"The Restaurant {self.restaurant_name} is open")
    
    def set_number_served(self, served):
        self.number_served = int(served)

    def increment_number_served(self, served):
        self.number_served += int(served)
    

print("---------------exercise 9-4------------")

restaurant = Restaurant("Outback Steakhouse", "American", 4)
print("The restuarant name is ", restaurant.restaurant_name)
print("The Cuisine type is ", restaurant.cuisine_type)

restaurant.open_restaurant()
restaurant.describe_restaurant()
#print number served
print("The Number of customers served is ", restaurant.number_served)
#change number served
restaurant.number_served = 20
print("The new number of cusomters served is ", restaurant.number_served)
#asking how many have been served
served = input("how many customers have been served?")
restaurant.set_number_served(served)
print("The new number of cusomters served is ", restaurant.number_served)
#adding customers served using increment
served = input("How many additional customers have been served?")
restaurant.increment_number_served(served)
print("The total number of cusomters served is ", restaurant.number_served)

