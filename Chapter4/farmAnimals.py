animals = ["horse", "cow", "pig", "chicken", "rooster", "goat"]
print("------------ Original List ----------------")
for ani in animals:
    print(ani)
newAnimals = animals[:]
newAnimals.append("cat")
newAnimals.append("dog")
newAnimals.append("llama")
newAnimals.append("mink")
print("------------ New List ----------------")
for new in newAnimals:
    print(new)

print("------------ 4-10 ----------------")
print("the first three items in the list are:", newAnimals[0:3])
print("three items in the middle of the list are:", newAnimals[4:7])
print("the last three items in the list are:", newAnimals[7:11])



