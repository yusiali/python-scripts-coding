

def fibonacci(x):
   if x <= 1:
       return x
   else:
       return(fibonacci(x-1) + fibonacci(x-2))

num = int(input("enter num: "))

if num <= 0:
   print("Plese enter a positive number")
else:
   print("Fibonacci sequence:")
   for i in range(num):
       print(fibonacci(i))

#ask for num, add to sum, go back to main code and ask if they want to continue, go back into method as desired
#fibbonachi sequence
