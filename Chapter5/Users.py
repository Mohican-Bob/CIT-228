print("----------5-8---------------------------")

users = ["admin", "John", "Josh", "Karey", "Stacey"]

for u in users:
    if u == "admin":
        print("hello", u, "would you like to see a status report?")
    else:
        print("hello", u, "thank you for logging in again")
print("----------5-9---------------------------")
users = []
if users == []:
    print("We need to find some users!")
for u in users:
    if u == "admin":
        print("hello", u, "would you like to see a status report?")
    else:
        print("hello", u, "thank you for logging in again")

users = ["admin", "John", "Josh", "Karey", "Stacey"]
newUsers = ["Toby", "Sam", "Josh", "karey", "Leo"]
print("----------5-10---------------------------")
for new in newUsers:
    for old in users:
        if new.lower() == old.lower():
            print("Sorry", new, "is taken")


