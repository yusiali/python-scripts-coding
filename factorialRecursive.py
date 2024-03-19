def factorial(x):
    if(x > 0):
        return(x * factorial(x-1))

num = int(input("enter number: ")) 
print(factorial(num))