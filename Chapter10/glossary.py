import json
glossary ={
    "Dictionary":"Python data type that stores key value pairs",
    "Variable":"object that stores any data such as an int, double, or string",
    "Loop":"a continuous function that repeats until a certain event happens",
    "Print":"reveal data or type in the form of a string",
    "List":"A memory space where multiple items can be held, sorted, and iterated"
}

for item in glossary:
    print(item)
    print("\t", glossary[item])

def menu():
      selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
      while selection!=1 and selection !=2 and selection !=3 and selection !=4:
          print("You made and invalid selection, please try again")
          selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
      return selection


def create(object):
    overwrite = input("you are about to create a new file, existing data will be overwritten (q to quit) ")
    if overwrite != 'q':
        try:
            with open("Chapter10/glossary.json", "w") as write_file:
                json.dump(object, write_file, indent=4, sort_keys=True)
                print("glossary.json has been created")
        except TypeError:
            print("TypeError is happening")
        

def append(new_item):
    with open("Chapter10/glossary.json", "r+") as add_file:
        glossaryDictionary = json.load(add_file)
        glossaryDictionary.update(new_item)
        add_file.seek(0)
        json.dump(glossaryDictionary, add_file, indent=4, sort_keys=True)
        print("Data has been added to glossary.json")

def read():
    try:
        with open("Chapter10/glossary.json") as read_file:
            glossaryDictionary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesnt exist or cannot be found.")
        print("please make a different menu selection")
    else: 
        for key, value in glossaryDictionary.items():
            print("Element: ", key.title(), "Description: ", value.title())

def get_key():
    element= input("enter the python element you've learned: ")
    return element

def get_value():
    description = input("enter the element's description: ")
    return description

choice = menu()
while choice != 4:
    if choice == 1:
        create(glossary)
    elif choice == 2:
        read()
    elif choice == 3:
        key = get_key()
        value = get_value()
        new_glossary = {key:value}
        append(new_glossary)
    else:
        print("The option you selected is not available, please try again")
    choice = menu()

