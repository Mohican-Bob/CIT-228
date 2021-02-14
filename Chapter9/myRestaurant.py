from restaurant import Restaurant
from icecream import IceCreamStand


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

flavors = []
flavor = ""
flavor = input("name your first flavor: ")
flavors.append(flavor)
flavor = input("name your second flavor: ")
flavors.append(flavor)
flavor = input("name your second flavor: ")
flavors.append(flavor)

stand = IceCreamStand("Cold n Creamy", "Desert", 0, flavors)

print(f"The restaurant is called {stand.restaurant_name} it serves {stand.cuisine_type}")

stand.displayFlavors()