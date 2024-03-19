num = (int(input("enter a number: ")))
prime = 1
if num > 1:
    for x in range(2, num):
        if(num % x == 0):
            prime = 0;
    if prime == 1:
        print("prime")
    else:
        print("composite")
else:
    print("not prime")


for x in range (2, 101):
    prime = 1
    for i in range(2, x):
        if(x % i == 0):
            prime = 0       
    if (prime == 1):
        print(x)
        
#print all prime numbers between 1-100(2, 3, 5, 7)