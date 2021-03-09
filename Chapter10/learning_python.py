filename = "Chapter10/learning_python.txt"
# 10 - 1 
with open(filename) as pythonFile:
    myFile = pythonFile.read()
print("----------Output from read()--------")
print(myFile)

print("----------Output from from for loop inside with...open--------")
with open(filename) as pythonFile:
    for line in pythonFile:
        print(line)

print("----------Output from readlines()--------")
with open(filename) as pythonFile:
    myFile = pythonFile.readlines()
#prints the original list
print("Original List=", myFile)
# processes each item (line) in the list
for line in myFile:
    print(line)

print("----------Output Python with C#--------")
with open(filename) as pythonFile:
    for line in pythonFile:
        print("Original: ", line)
        print("Modified: ", line.replace("Python", "C#"))