def addition(num1, num2):
    ans = num1+num2
    return ans
def subtraction(num1, num2):
    ans = num1-num2
    return ans
def multiplication(num1, num2):
    ans = num1*num2
    return ans
def division(num1, num2):
    ans = num1/num2
    return ans

stop = "y"
while stop == "y":
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))
    print("addition:       1")
    print("subtraction:    2")
    print("multiplication: 3")
    print("division:       4")
    func = int(input("Enter number of operation: "))
    if func == 1:
        ans = addition(num1, num2)
    if func == 2:
        ans = subtraction(num1, num2)
    if func == 3:
        ans = multiplication(num1, num2)
    if func == 4:
        ans = division(num1, num2)
    print(ans)
    stop = input("do u want to continue?('y' or 'n'): ")
