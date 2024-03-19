continue1 = 'y'
while (continue1 == 'y'):
    age = 16
    while (age >= 16):
        age = (int(input("enter age: ")))
        if(age < 16):
            print("You are not eligible for a diver's license.")
        else:
            name = input("enter your name: ")
            signal = input("Would you drive or stop on a red light? ")
            stop = input("Do you come to a 'rolling' or 'full' stop on a stop sign? ")
            limit = input("What is the speed limit in residential areas in miles? ")
            if((signal == "stop") and (stop == "full") and (limit == "30")):
                print(name, ", you are eligible for a driver's license.")
            else:
                print(name, ", you have failed the test.")
        print("\nnext candidate")      
    continue1 = input("enter 'y' to continue: ")