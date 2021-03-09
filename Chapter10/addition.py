import random
def add(a, b):
    return a+b

quit=""

while quit != "q": 
    try:
        a = input("what is the value of number one?")
        int(a)
        b = input("what is the value of number two?")
        int(b)
    except ValueError:
       print("You entered a non-number")        
    else:
        print(a, "+", b, "=", add(a,b))
    finally:
        print("Thanks for playing!")   
    
    quit=input("Would you like to continue, q to quit? ") 