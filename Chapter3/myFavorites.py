favFoods = ["Spaghetti", "Ribeye", "Stir fry", "Pizza", "Stroganoff", "Ribs"]
favNumbers = [8, 6, 7, 5, 3, 0]
favMovies = ["Forest Gump", "Saving Private Ryan", "Oh Brother Where Art Thou"]
combo = ["Spaghetti", "Ribeye", 8, 6, "Forest Gump", "Saving Private Ryan"]
print("------------------------------------Hands on 1----------------------------")
print(favFoods)
print(favNumbers)
print(favMovies)

print(favFoods[-1])
print("Item 2:", favNumbers[1], "item 4:", favNumbers[3], "item 6:", favNumbers[5])
print("My top 3 favorite movies are: ", favMovies[0], " ", favMovies[1], " and ", favMovies[2])
print("first food, first number, first movie: ", combo[0], combo[2], combo[4])

print("------------------------------------Hands on 2----------------------------")

favMovies.append("Old School")
print("added a movie to: ", favMovies)
favNumbers.insert(3, 66)
print("added 66 in position 4: ", favNumbers)
favFoods.insert(5, "Reeses")
print("replaced food 6 to Reeses: ", favFoods)
del favFoods[4]
print("deleted favorite food 5: ", favFoods)
favNumbers.pop()
print("removed last item: ", favNumbers)
favNumbers.pop(2)
print("removed item three ", favNumbers)

print("------------------------------------Hands on 2----------------------------")

favMovies.sort()
print("Sorted Movies:", favMovies)
favFoods.sort()
print("Sorted Foods:", favFoods)
print("Temporary Sorted Numbers:", sorted(favNumbers))
print("Original list of Numbers:", favNumbers)
favMovies.reverse()
print("Reversed List of Movies: ", favMovies)




