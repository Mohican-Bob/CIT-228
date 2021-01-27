people = ["Bernie", "Franklin", "Stephen"]
print("----------3-4------------")
print("Hello", people[0], """ I know you've been everywhere lately, but I am
wondering if you could make it to my cookout?""")
print("dear Mr.", people[1], """, I know you're very busy fighting Fascism and
rebuilding from the great depression. I am hoping you could make it to my Cookout?""")
print("Hey", people[2], " I know you have a show to run but I want you at my Cookout.")
print("----------3-5------------")
print("Unfortunately Mr.", people[1], "Cannot make the cookout")
people.pop(1)
people.insert(1, "Sammi")
print("Hello", people[0], """ I know you've been everywhere lately, but I am
wondering if you could make it to my cookout?""")
print("So", people[1], "I uh, forgot to mention I'm having a cookout")
print("Hey", people[2], " I know you have a show to run but I want you at my Cookout.")
print("----------3-6------------")
print("Its not a real cookout without animals! lets bring 'em along!")
people.insert(0, "Zappa")
people.insert(2, "Ozzy")
people.append("Java")
print("Hello", people[1], """ I know you've been everywhere lately, but I am
wondering if you could make it to my cookout?""")
print("So", people[3], "I uh, forgot to mention I'm having a cookout")
print("Hey", people[4], " I know you have a show to run but I want you at my Cookout.")
print("Hey ", people[0], "miss ya boy, lets eat some chicken bones")
print("welcome to your first cookout", people[2])
print("I guess a cat can join... Come on", people[5])
print("----------3-9------------")
print("The Total Number of Guests are:", len(people))
