def addition():
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))
    print("Sum:", (num1+num2))
def subtraction():
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))
    print("Difference:", (num1-num2))
def multiplication():
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))
    print("Product:", (num1*num2))
def division():
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))
    print("Product:", (num1/num2))

stop = "y"
while stop == "y":
    print("addition:       1")
    print("subtraction:    2")
    print("multiplication: 3")
    print("division:       4")
    func = int(input("Enter number of operation: "))
    if func == 1:
        addition()
    if func == 2:
        subtraction()
    if func == 3:
        multiplication()
    if func == 4:
        division()
        
    stop = input("do u want to continue?('y' or 'n'): ")