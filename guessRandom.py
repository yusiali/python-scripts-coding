import random
def guess(num):
    a = 0
    while(a != num):
        a = int(input("guess the number: "))
        if(a<num):
            print("number is greater")
        elif(a>num):
            print("number is less")
    return("correct")
    

num = random.randint(1,10)
print(guess(num))