color= "blue"
weather= "Rainy"
height= "short"
number = 2
days = ["friday", "saturday", "sunday", "monday", "tuesday"]
months = []

print("------------True Results----------------------------")
print("the color is blue", color == "blue")
print("the weather is rainy", weather == "Rainy")
print("the height is short", height == "short")
print("the number is greater that 1", number > 1)
for d in days:
    if d == "saturday":
        print("days include saturday")    
print("Rainy is lowercase", weather.lower() == "rainy")
if days:
    print("list of days exists")
if height == "short" and weather == "Rainy":
    print("im Short and its Rainy")











print("------------False Results----------------------------")
print("the color is green", color == "green")
print("the weather is sunny", weather == "sunny")
print("the height is tall", height == "tall")
print("the number is greater that 2", number > 2)
for d in days:
    if d == "wednesday":
        print("days include wednesday")  
if months == []:
    print("there is no months")


