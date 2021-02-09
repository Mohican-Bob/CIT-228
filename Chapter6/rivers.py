rivers = {
    "Nile":["Ethiopia", "South Sudan", "North Sudan", "Egypt"],
    "Rhine":["Switzerland", "France", "Germany", "Holland"],
    "Dneiper":["Russia", "Belarus", "Ukraine"]
}

print("---------------Rivers & Countries-------------")
for key, value in rivers.items():
    print(f"the {key.title()} river flows through {value}")


print("---------------Rivers-------------")
for key in rivers.keys():
    print(key.title())


print("---------------Countries-------------")
for value in rivers.values():
    print(value)

