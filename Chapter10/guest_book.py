"""
userName = input("What is you user name? (q to quit)")
with open("Chapter10/userName.txt", "a") as userFile:
    while userName != "q":
        userName += "\n"
        userFile.write(userName)
        input("What is you user name? (q to quit)")"""


import os
import random

filename = "Chapter10/guests.txt"
#deleting the file if it exists
if os.path.exists(filename):
    os.remove(filename)
#creating a new file
rooms = []
with open(filename,"w") as guestFile:
    guests = input("Please enter your name? (q to quit)")
    while guests != 'q':
        number=random.randint(1,30)
        while number in rooms:
            number=random.randint(1,30)
        print(f"{guests} you will sleep in room# {number}")
        rooms.append(number)
        guests+=", room# " + str(number) + "\n"
        guestFile.write(guests)
        guests = input("Please enter your name? (q to quit)")
#reading from the new file
with open(filename) as guestFile:
    print("----------------guest and room assigned-----------\n")
    for line in guestFile:
        print(line)



