mathOption = 0
def getInput():
    global mathOption
    while True:
        try:
            mathOption = int(input("What calculation would you like to perform? (1 - basic calculator, 2 - quadratic formula, 3 - tip calculator)"))
            break         
        except:
            print("That's not an int")
    Options()

def Options():
    if mathOption == 1:
        basicCal()
    elif mathOption == 2:
        quadratic()
    elif mathOption == 3:
        tip()
    else:
        my_name = input("What's your name ")
        name(my_name)

def basicCal():
    while True:
        try:
            x = int(input("What's your first number? "))
            y = int(input("What's your second number? "))
            choice = input("What would you like to do? (add, subtract, multiply, divide) ")
            if choice.lower() == "add":
                print(x + y)
            elif choice.lower() == "subtract":
                print(x - y)
            elif choice.lower() == "multiply":
                print(x * y)
            elif choice.lower() == "divide":
                print(x / y)
            else:
                basicCal()
            print("\n")
            closeGame()
            break
        except:
            print("That's not an int!!")

def quadratic():
    while True:
        try:
            probe1 = int(input("Is the value \'x\' known? (1 - yes, 0 - no) "))
            if probe1 == 1:
                x = int(input("What's the value of x? "))
                a = int(input("What's the value of a? If no value exist, enter 1. "))
                b = int(input("What's the value of b? If no value exist, enter 1. "))
                c = int(input("What's the value of c? If no value exist, enter 1. "))
                print( (a * (x**2) + (b * x) + c ))
                print("\n")
                closeGame()
            elif probe1 == 2:
                print("Nothing")
            else:
                quadratic()
            break
        except:
            print("That's not an int!!")
       
    
def tip():
     while True:
        try:
            total = float(input("Enter your total "))
            tip = float(input("How much would you like to tip? "))
            print("Your tip amount is... $" + str(total * (tip / 100.0)))
            print("\n")
            closeGame()            
            break
        except ValueError:
            print("You didn't input a float, try again!!")

def name(yourName):
    print("Are you ready to begin your pokemon adventure" + yourName + "?")

def closeGame():
    isDone = input("Would you like to exit? (Yes,No) ")
    if isDone.lower() == "no":
        print(getInput())
    elif isDone.lower() == "yes":
        print("See you later!")
    else:
        closeGame()

print(getInput())