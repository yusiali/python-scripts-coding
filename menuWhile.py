continue1 = 'y'
while (continue1 == 'y'):
    print("addition 1")
    print("subtraction 2")
    print("multiplication 3")
    print("division 4")
    x = (float(input("Enter a number:")))
    y = (float(input("enter another number:")))
    a = (int(input("Enter an operation:")))
    if(a == 1):
        print("output: ", (x+y))
    elif(a == 2):
        print("output: ", (x-y))
    elif(a == 3):
        print("output: ", (x*y))
    elif(a == 4):
        print("output: ", (x/y))
    continue1 = input("Enter 'y' to continue:" )
    
    
    
    