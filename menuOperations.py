print("addition:       1")
print("subtraction:    2")
print("multiplication: 3")
print("division:       4")

option = int(input("Choose option: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
output = 0;
if option == 1:
    output = num1 + num2
    print("output:", output)
elif option == 2:
    output = num1 - num2
    print("output:", output)
elif option == 3:
    output = num1 * num2
    print("output:", output)
elif option == 4:
    output = num1 / num2
    print("output:", output)


