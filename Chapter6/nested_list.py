rivers = {
    "Nile":["Ethiopia", "South Sudan", "North Sudan", "Egypt"],
    "Rhine":["Switzerland", "France", "Germany", "Holland"],
    "Dneiper":["Russia", "Belarus", "Ukraine"]
}

print("--------------Rivers & Countries----------")
for key, value in rivers.items():
        print(f"The {key} river flows through:")
        for v in value:
            print("\t\t\t\t",v)


print("--------------Rivers----------")

for key in rivers.values():
    print(key)


print("--------------Countries----------")

for value in rivers.values():
    for v in value:
        print(v)

