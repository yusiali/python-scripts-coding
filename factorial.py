def factorial(num):
    ans = num
    for x in range(num-1, 0, -1):
        ans *= x
    return ans

num = int(input("enter number of factorial: "))
ans = factorial(num)
print(ans)