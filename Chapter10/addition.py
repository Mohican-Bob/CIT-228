import random
def add(a, b):
    return a+b

quit=""

while quit != "q": 
    try:
        a = int(input("what is the value of number one?"))        
        b = int(input("what is the value of number two?"))        
    except ValueError:
       print("You entered a non-number")        
    else:
        print(a, "+", b, "=", add(a,b))
    finally:
        print("Thanks for playing!")   
    
    quit=input("Would you like to continue, q to quit? ") 