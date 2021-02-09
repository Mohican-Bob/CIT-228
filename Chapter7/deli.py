sandwich_orders = ["Pastrami", "Meatball", "Pastrami", "Turkey", "Pastrami", "Ham", "Reuben", "Philly Steak"]
finished_sandwiches = []
counter = 0
print("sandwiches ordered:")
for sands in sandwich_orders:
    print(sands)
print("we are out of Pastrami")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
print("new Sandwich oders:")
for sands in sandwich_orders:
    print(sands)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("sandwiches made: ")
for sands in finished_sandwiches:
    print(sands)

