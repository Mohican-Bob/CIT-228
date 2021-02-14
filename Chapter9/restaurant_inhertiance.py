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
    
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0, flavors = []):
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = flavors
    
    def displayFlavors(self):
        print("~the following flavors are available~")
        for f in self.flavors:
            print(f.title())

print("---------------exercise 9-6------------")
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



